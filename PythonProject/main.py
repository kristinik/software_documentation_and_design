from app.config.db import engine, Base
from app.dao.repository import UserRepository
from app.dao.csv_reader import CSVReader
from app.services.service import UserService


def main():
    Base.metadata.create_all(bind=engine)

    repository = UserRepository()
    csv_reader = CSVReader()
    service = UserService(repository, csv_reader)

    service.process_csv("data/security_data.csv")


if __name__ == "__main__":
    main()