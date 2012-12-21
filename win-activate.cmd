@echo off

:: Absolute path this script is in
SET TOP_PATH=%~dp0

SET mg="%TOP_PATH%ENV\Scripts\python" "%TOP_PATH%sites\manage.py"

IF NOT DEFINED VIRTUAL_ENV (GOTO no_exist_virtual_env) ELSE (GOTO exist_virtual_env)

:no_exist_virtual_env
IF EXIST "%TOP_PATH%ENV\Scripts\activate.bat" (GOTO exist_activate) ELSE (GOTO no_exist_activate)

:exist_activate
ECHO Found "ENV\Scripts\activate.bat" script, activating current ENV ...
%TOP_PATH%ENV\Scripts\activate.bat & ECHO DONE

IF [%1]==[] (GOTO end_label) ELSE (GOTO exist_virtual_env)

:no_exist_activate
:: 参数为空，且未设置 VIRTUAL_ENV
IF [%1]==[] python %TOP_PATH%scripts\bootstrap.py --init & %TOP_PATH%ENV\Scripts\activate.bat & GOTO end_label

:exist_virtual_env
:: VIRTUAL_ENV 环境变量已设置，须执行 deactivate
deactivate.bat & python %TOP_PATH%scripts\bootstrap.py %* & %TOP_PATH%ENV\Scripts\activate.bat

:end_label
