from sqlalchemy import Column, String, Integer, Date, Float, ForeignKey
# from sqlalchemy.orm import relationship

from engine import Base


class DBCity(Base):
    __tablename__ = "city"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    additional_info = Column(String, nullable=False)


# class DBTemperature(Base):
#     __tablename__ = "temperature"
#
#     id = Column(Integer, primary_key=True, index=True)
#     city_id = Column(Integer, ForeignKey("city.id"))
#     date_time = Column(Date)
#     temperature = Column(Float, nullable=False)
#
#     city = relationship(DBCity)

