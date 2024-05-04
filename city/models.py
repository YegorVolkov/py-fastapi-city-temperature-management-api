from sqlalchemy import Column, String, Integer

from engine import Base


class DBCity(Base):
    __tablename__ = "city"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    additional_info = Column(String, nullable=False)



