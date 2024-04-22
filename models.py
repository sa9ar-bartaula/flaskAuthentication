import hashlib

import sqlalchemy as db
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from werkzeug.security import generate_password_hash, check_password_hash

from constants.const import *
from secure.local import DATABASE_ENGINE, CREATE_DATABASE
Base = declarative_base()


class Group(Base):
    __tablename__ = "group"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    code  = db.Column(db.String(100))
    user = relationship("User", back_populates="group")
    

class User(Base):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(50), unique=True, nullable=False)
    first_name = db.Column(db.String(100), nullable=True)
    last_name = db.Column(db.String(100), nullable=True)
    _password = db.Column('password', db.String(255), nullable=False)
    is_active = db.Column(db.Boolean(), default=True)
    is_admin = db.Column(db.Boolean(), default=False)
    is_superadmin = db.Column(db.Boolean(), default=False)
    date_joined = db.Column(db.DateTime())
    last_login = db.Column(db.DateTime())
    group = relationship("Group", back_populates="user")
    
    def __repr__(self) -> str:
        return f"[User: {self.id!r}, {self.first_name!r} {self.last_name!r}]"
    
    @property
    def fullname(self):
        if self.first_name is not None and self.last_name is not None:
            return f"{self.first_name!r} {self.last_name!r}"
        return ""
    
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        # Hash the plaintext password before storing it
        self._password = generate_password_hash(password)
        
    # Verify password
    def check_password(self, password):
        return check_password_hash(self._password, password)
        
   
# Create an engine to connect to your database     
engine = db.create_engine(DATABASE_ENGINE)
SessionMaker = sessionmaker(bind=engine)
session = SessionMaker()

# Generate SQL schema
if CREATE_DATABASE:
    print('<= Starting database creation...')
    Base.metadata.create_all(engine)
    print('<= Database Successfully Created.')