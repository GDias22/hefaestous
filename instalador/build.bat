@echo off
rem Compila Instalar_HEFAESTOUS.exe e HEFAESTOUS.exe (PyInstaller, venv web\.venv313) e os coloca na RAIZ do projeto.
rem Depois disso a pasta inteira (sem web\.venv313, node_modules, sessions) e a distribuicao: zip ou git.
setlocal
cd /d "%~dp0.."
set "ROOT=%CD%"
set "PY=%ROOT%\web\.venv313\Scripts\python.exe"
if not exist "%PY%" (echo venv nao encontrado em %PY% & exit /b 1)
set "ICO=%ROOT%\web\frontend\img\hefaestous.ico"
if not exist "%ICO%" (echo icone nao encontrado em %ICO% & exit /b 1)
"%PY%" -m pip install --quiet --disable-pip-version-check pyinstaller || exit /b 1
echo [1/2] HEFAESTOUS.exe (lancador)
"%PY%" -m PyInstaller --noconfirm --clean --onefile --noconsole --icon "%ICO%" --name HEFAESTOUS ^
  --distpath "%ROOT%" --workpath "%ROOT%\instalador\build" --specpath "%ROOT%\instalador\build" "%ROOT%\instalador\launcher.py" || exit /b 1
echo [2/2] Instalar_HEFAESTOUS.exe
"%PY%" -m PyInstaller --noconfirm --clean --onefile --noconsole --icon "%ICO%" --name Instalar_HEFAESTOUS ^
  --distpath "%ROOT%" --workpath "%ROOT%\instalador\build" --specpath "%ROOT%\instalador\build" "%ROOT%\instalador\instalador.py" || exit /b 1
rmdir /s /q "%ROOT%\instalador\build" 2>nul
echo.
echo Pronto: HEFAESTOUS.exe e Instalar_HEFAESTOUS.exe na raiz do projeto.
