from model.db.database_factory import DatabaseFactory, DatabaseFactoryEnum
from model.service.connections_service import ConnectionService
from model.dao.connection_dao import ConnectionDAO


class ConnectionController:
    @staticmethod
    def connection_service() -> ConnectionService:
        conn = DatabaseFactory.new_connection(env=DatabaseFactoryEnum.PROD)
        return ConnectionService(conn=conn)

    @staticmethod
    def submit_new_connection(name: str = None, url: str = None, company: str = None) -> ConnectionDAO:
        service = ConnectionController.connection_service()
        dao = service.save_connection(name=name, url=url, company=company)
        return dao

    @staticmethod
    def get_connections() -> list[ConnectionDAO]:
        service = ConnectionController.connection_service()
        data = service.get_all()
        return data

    @staticmethod
    def update_connection(dao: ConnectionDAO, field: str, value: str) -> ConnectionDAO:
        service = ConnectionController.connection_service()
        dao.set(field, value)
        service.edit_by_id(dao.id, dao)
        connection = service.get_by_id(dao.id)
        return connection
