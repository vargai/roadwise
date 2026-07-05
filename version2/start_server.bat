@echo off
cd /d "%~dp0"
C:\Python313\python.exe server.py > server.out.log 2> server.err.log
