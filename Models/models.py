from Database.database import Base
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship



class Messages(Base):
    """
    A test class for database automation
    """
    __tablename__ = "Messages"
    
    ID = Column(Integer, index=True, primary_key=True)
    imei = Column(String, nullable=False)
    micro_op = Column(String, nullable=False)
    time_stamp = Column(DateTime, default=func.now())