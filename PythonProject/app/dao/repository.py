from app.dao.interfaces import IUserRepository
from app.config.db import SessionLocal
from app.models.entities import Sensor


class UserRepository(IUserRepository):
    def get_sensor_by_id(self, sensor_id: int):
        session = SessionLocal()
        try:
            return session.query(Sensor).filter_by(id=sensor_id).first()
        finally:
            session.close()

    def save_user(self, user):
        session = SessionLocal()
        try:
            session.add(user)
            session.commit()
            session.refresh(user)
            return user
        finally:
            session.close()

    def save_sensor(self, sensor):
        session = SessionLocal()
        try:
            session.add(sensor)
            session.commit()
            session.refresh(sensor)
            return sensor
        finally:
            session.close()

    def save_notification(self, notification):
        session = SessionLocal()
        try:
            session.add(notification)
            session.commit()
            session.refresh(notification)
            return notification
        finally:
            session.close()