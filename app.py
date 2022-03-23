import sys, os

from dependency_injector.wiring import inject, Provide

from src.application import MainApplication
from src.dependency_injection import Container


try:
    from ctypes import windll  # Only exists on Windows.
    myappid = 'mycompany.myproduct.subproduct.version'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass


@inject
def main(main_app: MainApplication = Provide[Container.main_application]):
    main_app.run()


if __name__ == '__main__':
    container = Container()
    container.config.app_args.update(sys.argv)
    base_dir = os.path.dirname(__file__)
    container.config.base_dir.update(base_dir)
    container.config.icons_path.update(os.path.join(base_dir, 'icons'))
    container.config.main_window_ui_path.update(os.path.join(base_dir, './uic/main_window.ui'))
    container.wire(modules=[__name__])

    main()
