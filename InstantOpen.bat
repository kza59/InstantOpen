@echo off
setlocal enabledelayedexpansion

set CONFIG_DIR=configs

set MAIN_SCRIPT=main.py

if not exist "%CONFIG_DIR%" (
    echo Config directory %CONFIG_DIR% does not exist.
    exit /b 1
)

for %%f in (%CONFIG_DIR%\*.txt) do (
    set "BASE_NAME=%%~nf"
    
    powershell -Command "(gc %MAIN_SCRIPT%) -replace 'configFile = .+', 'configFile = \"%CONFIG_DIR%\\%%~nxf\"' | Out-File %MAIN_SCRIPT% -Encoding ASCII"
    
    pyinstaller -F "%MAIN_SCRIPT%"
    
    ren "dist\main.exe" "!BASE_NAME!.exe"
    
)

echo Compilation complete.
endlocal
