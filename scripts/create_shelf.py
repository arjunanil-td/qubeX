#!/usr/bin/env python3
"""
Automatic Maya shelf creation script for qubeX.

This script attempts to automatically create the qubeX shelf in Maya
if Maya is running, or provides instructions if not.
"""

import os
import sys
from pathlib import Path


def create_shelf_in_maya():
    """Try to create the shelf directly in Maya if it's running."""
    try:
        import maya.cmds as cmds
        
        # Get the qubeX root directory
        script_dir = Path(__file__).parent
        qubex_root = script_dir.parent
        shelf_file = qubex_root / "config" / "shelves" / "shelf_QubeX.mel"
        
        if shelf_file.exists():
            # Source the shelf file
            cmds.evalDeferred(f'source "{shelf_file}";')
            print("✅ qubeX shelf created successfully in Maya!")
            print("🎉 You should now see the qubeX shelf with all tools!")
            return True
        else:
            print(f"❌ Shelf file not found: {shelf_file}")
            return False
            
    except ImportError:
        print("❌ Maya is not running or not accessible")
        return False
    except Exception as e:
        print(f"❌ Error creating shelf: {e}")
        return False


def main():
    """Main function."""
    print("🎨 qubeX Shelf Creation")
    print("=" * 40)
    
    # Try to create shelf automatically
    if create_shelf_in_maya():
        print("\n🎉 Success! The qubeX shelf is now available in Maya.")
        print("   You can find it in the shelf area with all your tools.")
    else:
        print("\n📋 Manual Setup Required:")
        print("1. Open Maya")
        print("2. Go to Window → General Editors → Script Editor")
        print("3. In the MEL tab, copy and paste this command:")
        print()
        
        # Get the current directory
        current_dir = Path.cwd()
        shelf_path = current_dir / "config" / "shelves" / "shelf_QubeX.mel"
        
        print("=" * 50)
        print(f'source "{shelf_path}";')
        print("=" * 50)
        print()
        print("4. Press Enter to execute")
        print("5. The qubeX shelf will appear with all tools!")
    
    print("\n📚 For more help, see README.md")
    print("🚀 Happy modeling!")


if __name__ == "__main__":
    main()
