from .ui_BrushBoxGUI import Ui_BrushBoxGUI
from PySide6.QtWidgets import QApplication, QDialog
from PySide6.QtCore import QCoreApplication
import sys

class BrushBoxGUI(QDialog, Ui_BrushBoxGUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BrushBoxGUI()
    window.show()
    sys.exit(app.exec())