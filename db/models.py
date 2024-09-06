from sqlalchemy import String, DateTime, BigInteger, Column
from datetime import datetime
from db import Base

class Users(Base):
    __tablename__ = 'users'
    
    chatid = Column(BigInteger, primary_key=True)
    username = Column(String, nullable=True)
    first_started_at = Column(DateTime, default=datetime.utcnow)
    last_online_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Users(chatid={self.chatid}, username={self.username})>"

class Documents(Base):
    __tablename__ = 'documents'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    title = Column(String, nullable=True)
    description = Column(String, nullable=True)
    tags = Column(String, nullable=True)
    link = Column(String, nullable=False)
    owner_chatid = Column(BigInteger, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Documents(id={self.id}, title={self.title})>"