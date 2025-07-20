from .ui_BrushBoxGUI import Ui_BrushBoxGUI
from PySide6.QtWidgets import QApplication, QDialog,QMessageBox
from PySide6.QtCore import QCoreApplication
from .TokenExcecpion import TokenException
import brushbox
import sys

class BrushBoxGUI(QDialog, Ui_BrushBoxGUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_dojob.clicked.connect(self.do_job)
    def do_job(self):
        self.btn_dojob.setEnabled(False)
        token = self.pte_token.toPlainText().strip()
        content = self.pte_content.toPlainText().strip()
        group_id = self.le_group_id.text().strip()
        try:
            times = int(self.sb_count.value())
            for i in range(times):
                brushbox.send_message(token, content, group_id)
                self.pb_process.setValue((i + 1) * 100 // times)
        except TokenException:
            print("[Error] Token过期")
            QMessageBox.critical(self, "Error", "Token 过期")
        except Exception as e:
            print(f"[Error] {e}")
            QMessageBox.critical(self, "Error", f"发生错误: {e}")
        self.btn_dojob.setEnabled(True)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BrushBoxGUI()
    window.show()
    sys.exit(app.exec())