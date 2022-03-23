from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QPushButton, QWidget
from PyQt5.QtGui import QIcon
import sys, os

from dependency_injector import containers, providers
from dependency_injector.wiring import inject, Provide

from src.storage.controllers import new_file
from src.time_period.controller import TimePeriodController

BASE_DIR = os.path.dirname(__file__)
MAIN_WINDOW_UI_PATH = os.path.join(BASE_DIR, './uic/main_window.ui')

try:
    from ctypes import windll  # Only exists on Windows.
    myappid = 'mycompany.myproduct.subproduct.version'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

Form, Window = uic.loadUiType(MAIN_WINDOW_UI_PATH)


class MainApplication(QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowIcon(QIcon(os.path.join(BASE_DIR, "icons", "icon.ico")))

    def run(self):
        window = Window()
        form = Form()
        form.setupUi(window)
        form.actionSave.triggered.connect(new_file)
        window.show()
        self.exec_()


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    main_application = providers.Singleton(MainApplication, [config.app_args])
    time_period_controller = providers.Factory(
        TimePeriodController,
    )


def add_button():
    print('close')
    return False


@inject
def main(main_app: MainApplication = Provide[Container.main_application]):
    main_app.run()


if __name__ == '__main__':
    container = Container()
    container.app_args = sys.argv
    container.wire(modules=[__name__])

    main()
