@echo off
REM Activate the virtual environment
call .venv\Scripts\activate

cd src
cd screen


start cmd /k " title HOME & python home.py"
start cmd /k "title STATS & python stats.py"
start cmd /k "title TASKS & python tasks.py"
start cmd /k "title CHARACTER & python character.py"
start cmd /k "title MATRIX & python matrix.py"
start cmd /k "title STORE & python store.py"
start cmd /k "title SETTING & python setting.py"
start cmd /k "title TIME & python minute.py"


