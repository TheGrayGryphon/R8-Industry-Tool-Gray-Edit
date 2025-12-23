@echo off
echo ========================================
echo Building Run8 Industry Tool Executable
echo ========================================
echo.

REM Check if pyinstaller is installed
python -c "import PyInstaller" 2>nul
if errorlevel 1 (
    echo PyInstaller not found. Installing...
    pip install pyinstaller
    echo.
)

REM Update build date in version.py
echo Updating build date...
python update_version.py
echo.

REM Clean previous builds
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist

REM Build the executable with selective PySide6 imports (reduces file size)
echo Building executable...
python -m PyInstaller --onefile --windowed --name "Run8IndustryTool" --icon=app_icon.ico --add-data "r8CarTypes.csv;." --add-data "app_icon.ico;." --add-data "instructions.md;." --hidden-import=PySide6.QtCore --hidden-import=PySide6.QtGui --hidden-import=PySide6.QtWidgets r8it.py

echo.
if exist "dist\Run8IndustryTool.exe" (
    echo ========================================
    echo Build successful!
    echo ========================================
    echo.
    echo Executable location: dist\Run8IndustryTool.exe
    echo.
    echo You can distribute the entire 'dist' folder
    echo or just the Run8IndustryTool.exe file.
    echo.
) else (
    echo ========================================
    echo Build failed!
    echo ========================================
    echo Please check the output above for errors.
)

pause
