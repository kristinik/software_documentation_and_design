from app.services.interfaces import IUserService
from app.models.entities import UserProfile, Sensor, Notification


class UserService(IUserService):
    def __init__(self, repository, csv_reader):
        self.repository = repository
        self.csv_reader = csv_reader

    def process_csv(self, file_path: str):
        rows = self.csv_reader.read(file_path)

        for row in rows:
            sensor_id = int(row["sensor_id"])
            existing_sensor = self.repository.get_sensor_by_id(sensor_id)

            if existing_sensor:
                print(f"Датчик {sensor_id} вже існує, пропускаємо.")
                continue

            user = UserProfile(
                name=row["name"],
                email=row["email"],
                phone=row["phone"]
            )
            saved_user = self.repository.save_user(user)

            sensor = Sensor(
                id=sensor_id,
                sensor_type=row["sensor_type"],
                location=row["location"],
                status=row["status"],
                user_id=saved_user.id
            )
            self.repository.save_sensor(sensor)

            notification = Notification(
                message=row["message"],
                notif_type=row["notif_type"],
                user_id=saved_user.id
            )
            self.repository.save_notification(notification)

        print("Дані успішно завантажено в базу.")