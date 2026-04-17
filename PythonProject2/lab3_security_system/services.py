from models import db, UserProfile, Sensor, Notification


class UserService:
    @staticmethod
    def get_all():
        return UserProfile.query.all()

    @staticmethod
    def get_by_id(user_id):
        return UserProfile.query.get(user_id)

    @staticmethod
    def add(name, email, phone):
        user = UserProfile(name=name, email=email, phone=phone)
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def update(user_id, name, email, phone):
        user = UserProfile.query.get(user_id)
        if user:
            user.name = name
            user.email = email
            user.phone = phone
            db.session.commit()

    @staticmethod
    def delete(user_id):
        user = UserProfile.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()


class SensorService:
    @staticmethod
    def get_all():
        return Sensor.query.all()

    @staticmethod
    def get_by_id(sensor_id):
        return Sensor.query.get(sensor_id)

    @staticmethod
    def add(sensor_type, location, status, user_name):
        user = UserProfile.query.filter_by(name=user_name).first()
        if user:
            sensor = Sensor(
                sensor_type=sensor_type,
                location=location,
                status=status,
                user_id=user.id
            )
            db.session.add(sensor)
            db.session.commit()

    @staticmethod
    def update(sensor_id, sensor_type, location, status, user_name):
        sensor = Sensor.query.get(sensor_id)
        user = UserProfile.query.filter_by(name=user_name).first()
        if sensor and user:
            sensor.sensor_type = sensor_type
            sensor.location = location
            sensor.status = status
            sensor.user_id = user.id
            db.session.commit()

    @staticmethod
    def delete(sensor_id):
        sensor = Sensor.query.get(sensor_id)
        if sensor:
            db.session.delete(sensor)
            db.session.commit()


class NotificationService:
    @staticmethod
    def get_all():
        return Notification.query.all()

    @staticmethod
    def get_by_id(notification_id):
        return Notification.query.get(notification_id)

    @staticmethod
    def add(message, notif_type, user_name):
        user = UserProfile.query.filter_by(name=user_name).first()
        if user:
            notification = Notification(
                message=message,
                notif_type=notif_type,
                user_id=user.id
            )
            db.session.add(notification)
            db.session.commit()

    @staticmethod
    def update(notification_id, message, notif_type, user_name):
        notification = Notification.query.get(notification_id)
        user = UserProfile.query.filter_by(name=user_name).first()
        if notification and user:
            notification.message = message
            notification.notif_type = notif_type
            notification.user_id = user.id
            db.session.commit()

    @staticmethod
    def delete(notification_id):
        notification = Notification.query.get(notification_id)
        if notification:
            db.session.delete(notification)
            db.session.commit()