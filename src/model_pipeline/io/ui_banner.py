import os
from PySide2 import QtWidgets, QtCore, QtGui


class Banner(QtWidgets.QWidget):
    """Centralized banner widget for QubeX tools."""
    
    def __init__(self, title, icon_name=None, parent=None):
        super().__init__(parent)
        self.setFixedHeight(60)
        self.setStyleSheet("""
            QFrame {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #2b2d42, stop:0.5 #3d405b, stop:1 #4a4e69);
                border-radius: 8px;
            }
            QLabel {
                color: white;
                font-size: 18pt;
                font-weight: bold;
            }
            QLabel#icon {
                padding-left: 35px;
                background: transparent;
                padding-top: 10px;
            }
            QLabel#title {
                padding-right: 35px;
            }
        """)
        
        layout = QtWidgets.QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Add icon if provided
        if icon_name:
            icon_path = os.path.join(os.path.expanduser("~"), "Documents", "maya", "2024", "prefs", "icons", icon_name)
            if os.path.exists(icon_path):
                icon_label = QtWidgets.QLabel()
                icon_label.setObjectName("icon")
                icon_pixmap = QtGui.QPixmap(icon_path)
                icon_pixmap = icon_pixmap.scaled(40, 40, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
                icon_label.setPixmap(icon_pixmap)
                layout.addWidget(icon_label)
        
        # Add title
        title_label = QtWidgets.QLabel(title)
        title_label.setObjectName("title")
        title_label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(title_label)
        
        layout.addStretch()
