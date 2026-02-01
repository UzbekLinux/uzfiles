import sys
import time
from pathlib import Path
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt6.QtGui import QIcon
from network import Ui_MainWindow

FIFO_IN = "/tmp/uzbeknetwork.fifo.in"
FIFO_OUT = "/tmp/uzbeknetwork.fifo.out"

class UzbekNetwork(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("UzbekНетворк")
        self.setFixedSize(627, 507)
        self.setWindowIcon(QIcon("/usr/local/bin/uzbeknetwork-gui/2705.png"))

        self.ui.pushButton.clicked.connect(self.connect)
        self.update_ui_state()
        self.ui.radioButton.toggled.connect(self.update_ui_state)
        self.ui.radioButton_2.toggled.connect(self.update_ui_state)

    def update_ui_state(self):
        wired = self.ui.radioButton.isChecked()
        wifi = self.ui.radioButton_2.isChecked()
        self.ui.comboBox.setEnabled(wired)
        self.ui.lineEdit.setEnabled(wifi)
        self.ui.lineEdit_2.setEnabled(wifi)
        if wired:
            self.update_interfaces()
    

    def update_interfaces(self):
        try:
            output = self.run_command("list interfaces")
            interfaces = [i for i in output.split() if i.startswith("e")]
            self.ui.comboBox.clear()
            self.ui.comboBox.addItems(interfaces)
        except Exception as e:
            QMessageBox.critical(self, "error", f"не удалось получить интерфейсы:\n{e}")
    
    
    def run_command(self, command: str, timeout: int = 20) -> str:
        fifo_in = Path(FIFO_IN)
        fifo_out = Path(FIFO_OUT)

        if not fifo_in.exists() or not fifo_out.exists():
            raise FileNotFoundError("у тебя точно есть UzbekNetwork?")

        fifo_in.write_text(command + "\n")

        start = time.time()
        while time.time() - start < timeout:
            try:
                result = fifo_out.read_text().strip()
                if result:
                    return result
            except Exception:
                pass
            time.sleep(0.2)

        raise TimeoutError("timeout выполнения команды UzbekNetwork")

    def connect(self):
        if self.ui.radioButton.isChecked():
            iface = self.ui.comboBox.currentText()
            if not iface:
                QMessageBox.critical(self, "error", "интерфейс не выбран")
                return
            cmd = f"interface wake {iface}"
        else:
            iface = self.ui.comboBox.currentText()
            ssid = self.ui.lineEdit_2.text()
            pwd = self.ui.lineEdit.text()
            if not ssid or not pwd:
                QMessageBox.critical(self, "error", "не всё заполнено")
                return
            cmd = f"interface wake {iface} {ssid} {pwd}" if iface else f"interface wake {ssid} {pwd}"

        try:
            output = self.run_command(cmd)
            QMessageBox.information(self, "info", output if output else "успешно")
        except Exception as e:
            QMessageBox.critical(self, "error", str(e))


def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("/usr/local/bin/uzbeknetwork-gui/2705.png"))
    window = UzbekNetwork()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
