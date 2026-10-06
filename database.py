from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///predictions.db", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Prediction(Base):
    __tablename__ = "predictions"
    id = Column(Integer, primary_key=True)
    text = Column(String)
    label = Column(String)
    confidence = Column(Float)

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("Table ban gayi!")