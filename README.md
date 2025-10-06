# QubeX Model Toolkit

A lightweight, standalone model utility toolkit for Maya that provides essential tools for model hierarchy creation and object renaming.

## Features

- **Hierarchy Creation**: Automatically create standardized model hierarchies based on asset type (character, prop, vehicle)
- **Object Renaming**: Search and replace functionality for selected objects
- **Advanced Rename Tool**: Full-featured rename tool with prefix/suffix, case conversion, and utilities
- **Maya-Native UI**: Clean, professional interface that matches Maya's look and feel

## Installation

### Automatic Installation

1. Download or clone this repository
2. Run the installation script:
   ```bash
   python scripts/install_maya.py
   ```
3. Follow the prompts to install to your desired Maya version(s)
4. Restart Maya

### Manual Installation

1. Copy the `src/qubex_model_toolkit` folder to your Maya scripts directory:
   - Windows: `Documents/maya/[version]/scripts/`
   - macOS: `~/Library/Preferences/Autodesk/maya/[version]/scripts/`
   - Linux: `~/maya/[version]/scripts/`

2. Add the following to your `userSetup.py` file in the scripts directory:
   ```python
   import sys
   import os
   
   # Add toolkit to Python path
   toolkit_path = r"[path_to_qubex_model_toolkit]"
   if toolkit_path not in sys.path:
       sys.path.insert(0, toolkit_path)
   
   # Import and make available
   try:
       import qubex_model_toolkit
       print("QubeX Model Toolkit loaded successfully")
   except ImportError as e:
       print(f"Failed to load QubeX Model Toolkit: {e}")
   ```

## Usage

### Launching the Toolkit

From Maya's Script Editor or command line:
```python
from qubex_model_toolkit import show_model_toolkit_window
show_model_toolkit_window()
```

Or run the launcher script:
```python
exec(open("scripts/launch_toolkit.py").read())
```

### Hierarchy Creation

1. Enter your asset name (e.g., "charZebuHuman")
2. Enter the variant name (e.g., "zebuHumanA")
3. Click "Create Hierarchy"

The toolkit will automatically detect the asset type based on the prefix:
- `char*` → Character hierarchy
- `prop*` → Prop hierarchy  
- `vhcl*` → Vehicle hierarchy
- Other → Character hierarchy (default)

### Object Renaming

1. Select objects in the viewport
2. Enter search pattern and replacement text
3. Click "Rename Selected"

### Advanced Rename Tool

Click "Open Rename Tool" for advanced renaming features:
- Batch renaming with numbering
- Prefix/suffix addition
- Case conversion
- Search and replace
- Duplicate fixing
- Shape name fixing
- Namespace cleanup

## Requirements

- Maya 2018 or later
- Python 2.7 (Maya 2018-2022) or Python 3 (Maya 2023+)
- PySide2 (included with Maya)

## Project Structure

```
qubex_model_toolkit/
├── src/
│   └── qubex_model_toolkit/
│       ├── __init__.py
│       ├── io/
│       │   ├── __init__.py
│       │   ├── theme.py
│       │   └── ui_banner.py
│       ├── ui/
│       │   ├── __init__.py
│       │   ├── model_toolkit_ui.py
│       │   └── rename_tool_ui.py
│       └── utils/
│           ├── __init__.py
│           ├── hierarchy_utils.py
│           ├── name_utils.py
│           └── cleanup_utils.py
├── scripts/
│   ├── install_maya.py
│   └── launch_toolkit.py
├── config/
└── README.md
```

## Development

### Adding New Features

1. Add utility functions to the appropriate module in `utils/`
2. Add UI components to modules in `ui/`
3. Update the main toolkit UI in `ui/model_toolkit_ui.py`
4. Test thoroughly in Maya

### Customizing Hierarchies

Edit the hierarchy presets in `utils/hierarchy_utils.py`:
- `CHAR_HIERARCHY_PRESET`: Character asset structure
- `PROP_HIERARCHY_PRESET`: Prop asset structure
- `VHCL_HIERARCHY_PRESET`: Vehicle asset structure

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues, questions, or contributions, please contact the QubeX development team.

## Changelog

### Version 1.0.0
- Initial release
- Hierarchy creation with asset type detection
- Basic and advanced renaming tools
- Maya-native UI styling
- Standalone installation system
