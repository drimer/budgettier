from dependency_injector import containers, providers

from src.application import MainApplication
from src.time_period.controller import TimePeriodController


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    main_application = providers.Singleton(
        MainApplication,
        config.main_window_ui_path,
        config.icons_path,
        config.app_args,
    )
    time_period_controller = providers.Factory(
        TimePeriodController,
    )