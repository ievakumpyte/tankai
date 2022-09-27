import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///highscores.db')
Base = declarative_base()

class Highscores(Base):
    __tablename__ = 'Highscores'
    id = Column(Integer, primary_key=True)
    name = Column("Vardas", String)
    surname = Column("Pavarde", String)
    taskai = Column("Taskai", Integer)
    created_date = Column("Zaide", DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name, surname, taskai):
        self.name = name
        self.surname = surname
        self.taskai = taskai

    def __repr__(self):
        return f"{self.name} {self.surname} - {self.taskai}"

Base.metadata.create_all(engine)