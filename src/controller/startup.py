from view.main_window import MainWindow
from model.db.database_factory import DatabaseFactory, DatabaseFactoryEnum


def start_view():
    conn = DatabaseFactory.new_connection(env=DatabaseFactoryEnum.PROD)
    DatabaseFactory.migrate(conn=conn)
    main = MainWindow()
    main.mainloop()
