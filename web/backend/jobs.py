# -*- coding: utf-8 -*-
"""Tarefas em segundo plano (thread) com progresso e cancelamento."""
import threading
import time
import traceback
import uuid

_jobs = {}
_lock = threading.Lock()


class Job:
    def __init__(self, nome):
        self.id = uuid.uuid4().hex[:10]
        self.nome = nome
        self.status = "pendente"      # pendente | rodando | concluido | cancelado | erro
        self.progresso = 0.0
        self.mensagem = ""
        self.resultado = None
        self.erro = None
        self.inicio = time.time()
        self.fim = None
        self.cancel = threading.Event()
        self.contagem = 0

    def info(self):
        return {"job_id": self.id, "nome": self.nome, "status": self.status, "progresso": round(self.progresso, 1),
                "mensagem": self.mensagem, "encontrados": self.contagem, "erro": self.erro,
                "tempo_s": round((self.fim or time.time()) - self.inicio, 1)}


MAX_JOBS = 20


def iniciar(nome, fn, *args, **kwargs):
    """fn(job, *args, **kwargs) -> resultado. Deve consultar job.cancel.is_set() e atualizar job.progresso."""
    job = Job(nome)
    with _lock:
        # mantém só os MAX_JOBS mais recentes já terminados (resultados de busca podem ter centenas de kB)
        terminados = [j for j in _jobs.values() if j.status in ("concluido", "cancelado", "erro")]
        for j in sorted(terminados, key=lambda j: j.inicio)[: max(0, len(terminados) - MAX_JOBS + 1)]:
            _jobs.pop(j.id, None)
        _jobs[job.id] = job

    def run():
        job.status = "rodando"
        try:
            job.resultado = fn(job, *args, **kwargs)
            job.status = "cancelado" if job.cancel.is_set() else "concluido"
            job.progresso = 100.0
        except Exception as ex:  # noqa: BLE001
            job.status = "erro"
            job.erro = f"{ex}\n{traceback.format_exc()[-1500:]}"
        finally:
            job.fim = time.time()

    threading.Thread(target=run, daemon=True).start()
    return job


def obter(job_id):
    with _lock:
        return _jobs.get(job_id)


def cancelar(job_id):
    j = obter(job_id)
    if j:
        j.cancel.set()
    return j
