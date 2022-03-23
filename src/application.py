import os

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from src.storage.controllers import new_file
from PyQt5 import uic


class MainApplication(QApplication):
    def __init__(self, main_window_ui_path, icons_path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.main_window_ui_path = main_window_ui_path
        self.setWindowIcon(QIcon(os.path.join(icons_path, "icon.ico")))

    def run(self):
        Form, Window = uic.loadUiType(self.main_window_ui_path)

        window = Window()
        form = Form()
        form.setupUi(window)
        form.actionSave.triggered.connect(new_file)
        window.show()
        self.exec_()