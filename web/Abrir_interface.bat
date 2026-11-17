@echo off
cd /d "%~dp0"
if exist .venv313\Scripts\python.exe (
  .venv313\Scripts\python.exe app.py %*
) else (
  echo Venv nao encontrado. Crie com:
  echo   "C:\Users\gdias\AppData\Local\Programs\Python\Python313\python.exe" -m venv .venv313
  echo   .venv313\Scripts\python.exe -m pip install -r requirements.txt
  pause
)
