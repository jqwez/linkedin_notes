from model.db.database_factory import DatabaseFactory, DatabaseFactoryEnum
from model.service.connections_service import ConnectionService
from model.dao.connection_dao import ConnectionDAO


class ConnectionController:
    @staticmethod
    def connection_service() -> ConnectionService:
        conn = DatabaseFactory.new_connection(env=DatabaseFactoryEnum.PROD)
        return ConnectionService(conn=conn)

    @staticmethod
    def submit_new_connection(name: str = None, url: str = None, company: str = None):
        service = ConnectionController.connection_service()
        dao = service.save_connection(name=name, url=url, company=company)

    @staticmethod
    def get_connections() -> list[ConnectionDAO]:
        service = ConnectionController.connection_service()
        data = service.get_all()
        return data
