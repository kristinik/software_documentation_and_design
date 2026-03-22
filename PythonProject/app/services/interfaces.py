from abc import ABC, abstractmethod


class IUserService(ABC):
    @abstractmethod
    def process_csv(self, file_path: str):
        pass