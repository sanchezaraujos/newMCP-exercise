from sqlalchemy import Column, String, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .db import Base
import datetime


class Activity(Base):
    __tablename__ = "activities"
    name = Column(String, primary_key=True, index=True)
    description = Column(Text, nullable=True)
    schedule = Column(String, nullable=True)
    max_participants = Column(Integer, nullable=True)
    # relationships
    participants = relationship("Enrollment", back_populates="activity", cascade="all, delete-orphan")


class Student(Base):
    __tablename__ = "students"
    email = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    grade = Column(String, nullable=True)
    admission_no = Column(String, nullable=True)
    photo = Column(String, nullable=True)
    enrollments = relationship("Enrollment", back_populates="student", cascade="all, delete-orphan")


class Enrollment(Base):
    __tablename__ = "enrollments"
    id = Column(Integer, primary_key=True, index=True)
    activity_name = Column(String, ForeignKey("activities.name"))
    student_email = Column(String, ForeignKey("students.email"))
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    activity = relationship("Activity", back_populates="participants")
    student = relationship("Student", back_populates="enrollments")
