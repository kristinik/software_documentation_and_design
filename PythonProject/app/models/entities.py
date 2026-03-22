from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.config.db import Base


class UserProfile(Base):
    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)

    sensors = relationship("Sensor", back_populates="user")
    notifications = relationship("Notification", back_populates="user")


class Sensor(Base):
    __tablename__ = "sensors"

    id = Column(Integer, primary_key=True)
    sensor_type = Column(String, nullable=False)
    location = Column(String, nullable=False)
    status = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user_profiles.id"), nullable=False)

    user = relationship("UserProfile", back_populates="sensors")


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, autoincrement=True)
    message = Column(String, nullable=False)
    notif_type = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user_profiles.id"), nullable=False)

    user = relationship("UserProfile", back_populates="notifications")