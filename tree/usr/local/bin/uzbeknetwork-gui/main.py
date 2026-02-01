import sys
import subprocess
import threading
import time

from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt6.QtCore import Qt

from network import Ui_MainWindow


FIFO_IN = "/tmp/uzbeknetwork.fifo.in"
FIFO_OUT = "/tmp/uzbeknetwork.fifo.out"


class UzbekNetwork(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("UzbekНетворк")
        self.setFixedSize(self.size())

        self.sudo_password: str | None = None

        if not self.ask_sudo_password():
            sys.exit(1)

        self.setup_logic()
        self.update_ui_state()

    def ask_sudo_password(self) -> bool:
        from PyQt6.QtWidgets import QInputDialog, QLineEdit

        pwd, ok = QInputDialog.getText(
            self,
            "авторизация",
            "введи пароль root для UzbekNetwork:",
            QLineEdit.EchoMode.Password,
        )

        if not ok or not pwd:
            QMessageBox.critical(self, "error", "пароль не введён")
            return False

        if not self.check_password(pwd):
            QMessageBox.critical(self, "error", "неверный пароль")
            return False

        self.sudo_password = pwd
        return True

    def check_password(self, password: str) -> bool:
        try:
            p = subprocess.run(
                ["sudo", "-S", "-k", "true"],
                input=password + "\n",
                text=True,
                capture_output=True,
                timeout=5,
            )
            return p.returncode == 0
        except Exception:
            return False

    def fifo_command(self, command: str, timeout: int = 20) -> str:
        cmd = (
            f'printf "%s\\n" "{self.sudo_password}" | '
            f'sudo -S sh -c \'echo "{command}" > {FIFO_IN}\''
        )
    
        subprocess.run(
            cmd,
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=5,
        )
    
        start = time.time()
        while time.time() - start < timeout:
            try:
                with open(FIFO_OUT, "r") as f:
                    return f.read().strip()
            except FileNotFoundError:
                time.sleep(0.2)
    
        raise TimeoutError("timeout")
    

    def setup_logic(self):
        self.ui.radioButton.toggled.connect(self.update_ui_state)
        self.ui.radioButton_2.toggled.connect(self.update_ui_state)

        self.ui.radioButton.toggled.connect(self.load_interfaces)
        self.ui.radioButton_2.toggled.connect(self.load_interfaces)

        self.ui.comboBox_2.currentTextChanged.connect(self.scan_wifi)
        self.ui.pushButton.clicked.connect(self.connect)

    def update_ui_state(self):
        wired = self.ui.radioButton.isChecked()
        wifi = self.ui.radioButton_2.isChecked()

        self.ui.comboBox.setEnabled(wired)
        self.ui.comboBox_2.setEnabled(wifi)
        self.ui.comboBox_3.setEnabled(wifi)
        self.ui.lineEdit.setEnabled(wifi)

    def load_interfaces(self):
        try:
            out = self.fifo_command("list interfaces")
        except TimeoutError:
            QMessageBox.critical(self, "error", "таймаут")
            return

        interfaces = out.split()

        self.ui.comboBox.clear()
        self.ui.comboBox_2.clear()

        for iface in interfaces:
            if iface.startswith("e"):
                self.ui.comboBox.addItem(iface)
            elif iface.startswith("w"):
                self.ui.comboBox_2.addItem(iface)

    def scan_wifi(self):
        iface = self.ui.comboBox_2.currentText()
        if not iface:
            return

        try:
            out = self.fifo_command(f"interface scan {iface}")
        except TimeoutError:
            QMessageBox.critical(self, "error", "таймаут")
            return

        self.ui.comboBox_3.clear()
        for ssid in out.splitlines():
            self.ui.comboBox_3.addItem(ssid)

    def connect(self):
        if self.ui.radioButton.isChecked():
            iface = self.ui.comboBox.currentText()
            if not iface:
                QMessageBox.critical(self, "error", "интерфейс не выбран")
                return
            cmd = f"interface wake {iface}"
    
        else:
            iface = self.ui.comboBox_2.currentText()
            ssid = self.ui.comboBox_3.currentText()
            pwd = self.ui.lineEdit.text()
    
            if not iface or not ssid or not pwd:
                QMessageBox.critical(self, "error", "не всё заполнено")
                return
    
            cmd = f"interface wake {iface} {ssid} {pwd}"
    
        try:
            output = self.fifo_command(cmd)
            QMessageBox.information(self, "info", output if output else "успешно")
        except TimeoutError:
            QMessageBox.critical(self, "error", "таймаут")
    


def main():
    app = QApplication(sys.argv)
    win = UzbekNetwork()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
