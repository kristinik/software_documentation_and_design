import csv
import random
import os


class CSVGenerator:
    def generate(self, file_path: str, count: int = 1000):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow([
                "sensor_id",
                "name",
                "email",
                "phone",
                "sensor_type",
                "location",
                "status",
                "message",
                "notif_type"
            ])

            sensor_types = ["MotionSensor", "DoorSensor", "SmokeSensor"]
            statuses = ["active", "inactive"]
            notif_types = ["warning", "alarm", "info"]

            for i in range(1, count + 1):
                writer.writerow([
                    i,
                    f"User {i}",
                    f"user{i}@mail.com",
                    f"+38099111{i:04d}",
                    random.choice(sensor_types),
                    f"Room {random.randint(1, 50)}",
                    random.choice(statuses),
                    f"Notification message {i}",
                    random.choice(notif_types)
                ])


if __name__ == "__main__":
    generator = CSVGenerator()
    generator.generate("data/security_data.csv", 1000)
    print("CSV файл створено.")