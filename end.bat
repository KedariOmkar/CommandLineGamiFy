@echo off
REM Kill all running Python processes
taskkill /F /IM python.exe /T

REM Optionally, you can also kill Python processes running with pythonw.exe
taskkill /F /IM pythonw.exe /T
