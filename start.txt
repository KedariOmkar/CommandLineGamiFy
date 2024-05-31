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


cd faces
start cmd /k "title SUPERHUMAN & python superhuman.py"
start cmd /k "title TECHGENIUS & python techgenius.py"
start cmd /k "title ENTREPRENEUR & python entrepreneur.py"

