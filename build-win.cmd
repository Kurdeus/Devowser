@echo off
chcp 65001 > nul

:: Clean previous builds
if exist setup.spec del setup.spec
if exist dist rmdir /s /q dist
if exist build rmdir /s /q build

:: Set virtual environment command prefix
set VENV_CMD=.venv\Scripts\
if not exist .venv set VENV_CMD=

:: Build optimized executable
%VENV_CMD%pyi-makespec ^
  --onefile ^
  --icon=app.ico ^
  --name=Devowser ^
  --strip ^
  --noconsole ^
  --optimize 2 ^
  --hidden-import=win32gui,win32process,win32con ^
  --hidden-import=selenium,selenium.webdriver,selenium.webdriver.chrome.options ^
  app.py && ^
ren Devowser.spec setup.spec && ^
%VENV_CMD%pyinstaller --noconfirm --upx-dir=./upx --clean setup.spec