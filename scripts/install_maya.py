#!/usr/bin/env python3
"""
QubeX Model Toolkit - Maya Installation Script

This script installs the QubeX Model Toolkit into Maya's user preferences.
"""

import os
import sys
import shutil
from pathlib import Path

def get_maya_versions():
    """Get available Maya versions on the system."""
    maya_versions = []
    maya_dir = Path.home() / "Documents" / "maya"
    
    if maya_dir.exists():
        for item in maya_dir.iterdir():
            if item.is_dir() and item.name.isdigit():
                maya_versions.append(item.name)
    
    return sorted(maya_versions, reverse=True)

def install_to_maya(version, toolkit_path):
    """Install the toolkit to a specific Maya version."""
    maya_dir = Path.home() / "Documents" / "maya" / version
    scripts_dir = maya_dir / "scripts"
    prefs_dir = maya_dir / "prefs"
    icons_dir = prefs_dir / "icons"
    
    # Create directories if they don't exist
    scripts_dir.mkdir(parents=True, exist_ok=True)
    icons_dir.mkdir(parents=True, exist_ok=True)
    
    # Copy the toolkit to scripts directory
    toolkit_dest = scripts_dir / "model_pipeline"
    if toolkit_dest.exists():
        shutil.rmtree(toolkit_dest)
    shutil.copytree(toolkit_path, toolkit_dest)
    
    # Create userSetup.py if it doesn't exist
    user_setup = scripts_dir / "userSetup.py"
    setup_content = f'''
# QubeX Model Toolkit Auto-import
import sys
import os

# Add toolkit to Python path
toolkit_path = r"{toolkit_dest}"
if toolkit_path not in sys.path:
    sys.path.insert(0, toolkit_path)

# Import and make available
try:
    import model_pipeline
    print("QubeX Model Toolkit loaded successfully")
except ImportError as e:
    print(f"Failed to load QubeX Model Toolkit: {{e}}")
'''
    
    # Append to existing userSetup.py or create new one
    if user_setup.exists():
        with open(user_setup, 'r') as f:
            existing_content = f.read()
        if "model_pipeline" not in existing_content:
            with open(user_setup, 'a') as f:
                f.write(setup_content)
    else:
        with open(user_setup, 'w') as f:
            f.write(setup_content)
    
    print(f"✓ Installed to Maya {version}")
    return True

def main():
    print("QubeX Model Toolkit - Maya Installation")
    print("=" * 40)
    
    # Get current script directory (should be in the toolkit root)
    current_dir = Path(__file__).parent.parent
    toolkit_path = current_dir / "src" / "model_pipeline"
    
    if not toolkit_path.exists():
        print(f"Error: Toolkit not found at {toolkit_path}")
        return False
    
    # Get available Maya versions
    maya_versions = get_maya_versions()
    
    if not maya_versions:
        print("No Maya installations found in Documents/maya/")
        return False
    
    print(f"Found Maya versions: {', '.join(maya_versions)}")
    
    # Install to all versions or let user choose
    install_all = input("Install to all versions? (y/n): ").lower().startswith('y')
    
    if install_all:
        for version in maya_versions:
            install_to_maya(version, toolkit_path)
    else:
        print("Available versions:")
        for i, version in enumerate(maya_versions, 1):
            print(f"  {i}. Maya {version}")
        
        try:
            choice = int(input("Select version (number): ")) - 1
            if 0 <= choice < len(maya_versions):
                install_to_maya(maya_versions[choice], toolkit_path)
            else:
                print("Invalid selection")
                return False
        except ValueError:
            print("Invalid input")
            return False
    
    print("\nInstallation complete!")
    print("Restart Maya to use the QubeX Model Toolkit.")
    print("\nTo launch the toolkit, run:")
    print("  from model_pipeline import show_model_toolkit_window")
    print("  show_model_toolkit_window()")
    
    return True

if __name__ == "__main__":
    main()
