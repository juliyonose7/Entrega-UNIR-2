@echo off
title Servidor Local - Laboratorio JavaScript y AJAX (React)
color 0B
echo ===================================================================
echo     INICIANDO SERVIDOR LOCAL PARA LABORATORIO JAVASCRIPT Y AJAX
echo ===================================================================
echo.
echo Abriendo aplicacion React en su navegador predeterminado...
echo URL: http://localhost:8000/index.html
echo.
python servidor.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [AVISO] No se pudo ejecutar 'python servidor.py'.
    echo Intentando abrir index.html directamente en el navegador...
    start index.html
    pause
)

