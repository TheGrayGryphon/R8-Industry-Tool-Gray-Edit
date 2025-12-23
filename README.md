# Run8 Industry Tool

A GUI application for viewing and editing Run8 Train Simulator industry configuration files (.ind).

## Features

- View and edit industry configurations
- Search and replace functionality for tags, local names, and symbols
- Track-level editing and management
- Producer configuration (car types, hours, capacity, outbound tags)
- Visual indicators for unsaved changes
- Export configurations to new files

## Requirements

- Python 3.8+
- PySide6 6.10.1

## Installation

1. Clone this repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

```bash
python r8it.py
```

## Building an Executable

See [BUILD_README.md](BUILD_README.md) for instructions on creating a standalone executable using PyInstaller.

## Usage

1. **Open a File**: File → Open, navigate to your Run8 region directory (e.g., `\Content\V3Routes\Regions\SouthernCA`), and select `Config.ind`
2. **Edit Industries**: Double-click any industry row to open the detail dialog
3. **Search/Replace**: Use the "Find..." button to search and replace tags, symbols, or local names
4. **Save Changes**: File → Save (or Save As...)

See [instructions.md](instructions.md) for detailed usage instructions.

## File Structure

- `r8it.py` - Main application entry point
- `r8lib.py` - Core data structures for Run8 file format
- `mainTable.py` - Table model with dirty row tracking
- `industryDetailDialog.py` - Industry detail editor
- `findReplaceDialog.py` - Main window find/replace functionality
- `industryFindReplaceDialog.py` - Industry-specific tag find/replace
- `*.ui` files - Qt Designer UI definitions
- `r8CarTypes.csv` - Car type reference data

## License

[Add your license here]

## Contributing

[Add contribution guidelines if applicable]
