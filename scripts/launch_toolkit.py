#!/usr/bin/env python3
"""
QubeX Model Toolkit - Launcher Script

This script launches the QubeX Model Toolkit from within Maya.
"""

import sys
import os
from pathlib import Path

# Add the src directory to Python path
# Handle both script execution and Maya console execution
try:
    # When run as script
    current_dir = Path(__file__).parent.parent
except NameError:
    # When run in Maya console, use the QubeX directory
    current_dir = Path(r"Q:\METAL\tools\pipeline\QubeX")

src_dir = current_dir / "src"
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))

try:
    from model_pipeline import show_model_toolkit_window
    show_model_toolkit_window()
    print("QubeX Model Toolkit launched successfully!")
except ImportError as e:
    print(f"Error: Could not import QubeX Model Toolkit: {e}")
    print("Make sure the toolkit is properly installed.")
except Exception as e:
    print(f"Error launching QubeX Model Toolkit: {e}")
