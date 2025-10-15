"""
QubeX Model Pipeline Bootstrap Module

This module provides reload functionality for the qubeX model pipeline.
"""

import sys
import importlib
from pathlib import Path


def reload_all():
    """Reload all qubeX model pipeline modules."""
    print("🔄 Reloading qubeX Model Pipeline...")
    
    # Get the model_pipeline module path
    current_module = sys.modules.get('model_pipeline')
    if current_module:
        module_path = Path(current_module.__file__).parent
    else:
        # Fallback to current directory
        module_path = Path(__file__).parent
    
    # List of modules to reload
    modules_to_reload = [
        'model_pipeline',
        'model_pipeline.ui.model_toolkit_ui',
        'model_pipeline.ui.rename_tool_ui',
        'model_pipeline.utils.hierarchy_utils',
        'model_pipeline.utils.name_utils',
        'model_pipeline.utils.cleanup_utils',
    ]
    
    reloaded_count = 0
    
    for module_name in modules_to_reload:
        try:
            if module_name in sys.modules:
                importlib.reload(sys.modules[module_name])
                print(f"✅ Reloaded: {module_name}")
                reloaded_count += 1
            else:
                print(f"⚠️ Module not loaded: {module_name}")
        except Exception as e:
            print(f"❌ Failed to reload {module_name}: {e}")
    
    print(f"🎉 Reloaded {reloaded_count} modules successfully!")
    print("🚀 qubeX Model Pipeline is ready to use!")


def get_version():
    """Get the version of qubeX model pipeline."""
    try:
        version_file = Path(__file__).parent / "version.py"
        if version_file.exists():
            with open(version_file, 'r') as f:
                for line in f:
                    if line.startswith('__version__'):
                        return line.split('=')[1].strip().strip('"\'')
    except:
        pass
    return "1.0.0"


if __name__ == "__main__":
    reload_all()
