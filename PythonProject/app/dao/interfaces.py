from abc import ABC, abstractmethod


class IUserRepository(ABC):
    @abstractmethod
    def get_sensor_by_id(self, sensor_id: int):
        pass

    @abstractmethod
    def save_user(self, user):
        pass

    @abstractmethod
    def save_sensor(self, sensor):
        pass

    @abstractmethod
    def save_notification(self, notification):
        pass