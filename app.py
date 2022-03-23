from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QPushButton, QWidget
from PyQt5.QtGui import QIcon
import sys, os

from src.storage.controllers import new_file

BASE_DIR = os.path.dirname(__file__)
MAIN_WINDOW_UI_PATH = os.path.join(BASE_DIR, './uic/main_window.ui')

try:
    from ctypes import windll  # Only exists on Windows.
    myappid = 'mycompany.myproduct.subproduct.version'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

Form, Window = uic.loadUiType(MAIN_WINDOW_UI_PATH)


def add_button():
    print('close')
    return False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(os.path.join(BASE_DIR, "icons", "icon.ico")))
    window = Window()
    form = Form()
    form.setupUi(window)
    form.actionSave.triggered.connect(new_file)
    window.show()
    app.exec_()
