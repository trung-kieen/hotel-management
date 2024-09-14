

from sqlalchemy import DECIMAL, Boolean, CheckConstraint, Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import Relationship, backref, defaultload, relationship

from database.models.audit import  AuditCreation
from database.orm import Base
"""
Author: Dang Xuan Lam
"""
class BedType(Base):
    __tablename__ = "bed_types"
    id = Column(Integer ,  primary_key= True)
    # TODO

    def __repr__(self):
        return f"{self.__class__.__name__}"
