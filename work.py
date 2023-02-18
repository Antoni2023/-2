from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

engine = create_engine('sqlite:///queue_statuses.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)


class QueueStatus(Base):
    tablename = 'queue_statuses'

    id = Column(Integer, primary_key=True)
    s_name = Column(String(512))
    c_name = Column(String(512))
    c_id = Column(String(32))
    a_type = Column(String(128))
    direction = Column(String(32))
    activation = Column(String(32))
    c_state = Column(String(32))
    control = Column(String(32))
    created_at = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return f"<QueueStatus(id={self.id}, s_name={self.s_name}, c_name={self.c_name}, c_id={self.c_id}, a_type={self.a_type}, direction={self.direction}, activation={self.activation}, c_state={self.c_state}, control={self.control}, created_at={self.created_at})>"


def create_tables():
    Base.metadata.create_all(engine)


def save_data(s_name, c_name, c_id, a_type, direction, activation, c_state, control):
    session = Session()
    queue_status = QueueStatus(s_name=s_name, c_name=c_name, c_id=c_id, a_type=a_type, direction=direction, activation=activation, c_state=c_state, control=control)
    session.add(queue_status)
    session.commit()
    session.close()
