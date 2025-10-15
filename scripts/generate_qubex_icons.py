#!/usr/bin/env python3
"""
Generate basic icons for qubeX shelf tools.

This script creates simple colored icons for the qubeX shelf buttons.
"""

import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import sys

def create_icon(name, color, size=(64, 64)):
    """Create a simple colored icon with text."""
    # Create image with transparent background
    img = Image.new('RGBA', size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Draw colored circle
    margin = 8
    draw.ellipse([margin, margin, size[0]-margin, size[1]-margin], fill=color)
    
    # Add text (simplified - just use a basic approach)
    try:
        # Try to use a system font
        font_size = 12
        font = ImageFont.load_default()
        
        # Get text dimensions
        bbox = draw.textbbox((0, 0), name, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        # Center the text
        x = (size[0] - text_width) // 2
        y = (size[1] - text_height) // 2
        
        # Draw text with white color
        draw.text((x, y), name, fill='white', font=font)
    except:
        # If font fails, just draw a simple pattern
        draw.rectangle([20, 20, 44, 44], fill='white')
    
    return img

def main():
    """Generate all qubeX icons."""
    print("🎨 Generating qubeX Icons")
    print("=" * 30)
    
    # Define icons to create
    icons = [
        ("qubeX_icon_git.png", "Reload", (100, 100, 100)),      # Gray
        ("qubeX_icon_toolkit.png", "Toolkit", (70, 130, 180)),  # Blue
        ("qubeX_icon_rename.png", "Rename", (180, 100, 70)),    # Orange
        ("qubeX_icon_hierarchy.png", "Hierarchy", (100, 180, 70)), # Green
        ("qubeX_icon_cleanup.png", "Cleanup", (180, 70, 100)),  # Pink
    ]
    
    # Get the icons directory
    script_dir = Path(__file__).parent
    icons_dir = script_dir.parent / "config" / "icons"
    icons_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        for filename, name, color in icons:
            icon_path = icons_dir / filename
            img = create_icon(name, color)
            img.save(icon_path, 'PNG')
            print(f"✅ Created: {filename}")
        
        print(f"\n🎉 All icons created in: {icons_dir}")
        print("📁 Icons are ready for the qubeX shelf!")
        
    except ImportError:
        print("❌ PIL (Pillow) not installed. Installing...")
        os.system("pip install Pillow")
        print("✅ Please run this script again.")
    except Exception as e:
        print(f"❌ Error creating icons: {e}")
        print("💡 You can manually create 64x64 PNG icons or use the existing rigX icons.")

if __name__ == "__main__":
    main()
