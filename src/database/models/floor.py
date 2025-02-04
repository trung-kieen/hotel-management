"""
Author: Hoang Le Thuy Hoa
"""
from sqlalchemy import DECIMAL, Boolean, CheckConstraint, Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import Relationship, backref, defaultload, relationship

from database.models.audit import  AuditCreation
from database.orm import Base
class Floor(Base):
    __tablename__ = "floors"
    id = Column(Integer ,  primary_key= True, autoincrement=True, nullable=False)
    hotel_id = Column(Integer, ForeignKey("hotels.id"))

    def __repr__(self):
        return f"<{self.__class__.__name__}(id={self.id}, hotel_id={self.hotel_id})>"
