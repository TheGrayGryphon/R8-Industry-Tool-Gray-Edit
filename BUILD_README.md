# Building Run8 Industry Tool Executable

This guide explains how to create a standalone executable for the Run8 Industry Tool.

## Prerequisites

- Python 3.x installed
- All project dependencies installed (`pip install -r requirements.txt` if you have one)
- PyInstaller will be installed automatically by the build script

## Building the Executable

### Option 1: Using the Build Script (Recommended)

Simply double-click `build.bat` or run it from the command line:

```bash
build.bat
```

The script will:
1. Check if PyInstaller is installed (installs it if needed)
2. Clean any previous builds
3. Build the executable using the spec file
4. Report success/failure

### Option 2: Manual Build

If you prefer to build manually:

```bash
pyinstaller build.spec
```

## Output

After a successful build, you'll find:

- **dist/Run8IndustryTool.exe** - The standalone executable
- **build/** - Temporary build files (can be deleted)

## Distribution

You can distribute either:
- Just the `Run8IndustryTool.exe` file (recommended - everything is bundled)
- Or the entire `dist` folder

Users do **not** need Python or any other dependencies installed!

## Executable Size

The .exe file will be approximately 100-200 MB because it includes:
- Python interpreter
- PySide6/Qt libraries
- All application code and resources

## Testing

Before distributing:
1. Test the .exe on your development machine
2. Test on a clean Windows machine without Python installed
3. Verify all features work (open, save, edit industries)

## Troubleshooting

### "Module not found" errors
- Make sure all dependencies are listed in the spec file's `hiddenimports`
- Run: `pyinstaller --onefile --windowed r8it.py` to regenerate dependencies

### Missing data files
- Check that `r8CarTypes.csv` is in the `datas` section of build.spec
- Verify the file exists in the gui folder

### Antivirus warnings
- Some antivirus software flags PyInstaller executables as suspicious
- This is a false positive - you may need to whitelist the .exe

## Adding an Icon

To add a custom icon:
1. Create or obtain a .ico file (e.g., `app_icon.ico`)
2. Place it in the gui folder
3. Edit `build.spec` and change `icon=None` to `icon='app_icon.ico'`
4. Rebuild

## Customization

Edit `build.spec` to customize:
- Executable name: Change `name='Run8IndustryTool'`
- Icon: Set `icon='your_icon.ico'`
- Console visibility: Change `console=False` to `console=True` for debugging
- Additional data files: Add to the `datas` list
