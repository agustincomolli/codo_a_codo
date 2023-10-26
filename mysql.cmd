@echo off
setlocal

rem Verifica si se proporcionó un parámetro
if "%~1"=="" (
  echo Uso: %0 ^<start^|stop^>
  goto :eof
)

rem Verifica si el parámetro es "start"
if "%~1"=="start" (
  rem Inicia MySQL
  net start MySQL80

rem Verifica si el parámetro es "stop"
) else if "%~1"=="stop" (
  rem Detiene MySQL
  net stop MySQL80

) else (
  rem Si el parámetro no es válido
  echo Uso: %0 ^<start^|stop^>
  goto :eof
)

:end

