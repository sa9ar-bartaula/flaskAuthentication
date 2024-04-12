from datetime import datetime
import hashlib

import sqlalchemy as db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.ext.hybrid import hybrid_property

from constants.const import *

from secure.local import DATABASE_ENGINE
Base = declarative_base()
print('<= Starting database creation...')

class User(Base):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    user_type = db.Column(db.Enum(UserType), nullable=False)
    fullname = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(50), unique=True, nullable=False)
    _password = db.Column('password', db.String(255), nullable=False)
    date_joined = db.Column(db.DateTime(), default=datetime.utcnow())
    is_active = db.Column(db.Boolean(), default=True)
    is_superadmin = db.Column(db.Boolean(), default=False)
    
    
    def __repr__(self) -> str:
        return f"[User: {self.id!r}, {self.fullname!r}]"
    
    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, plaintext_password):
        # Hash the plaintext password before storing it
        self._password = hashlib.sha256(plaintext_password.encode()).hexdigest()
        
        
class TeacherInfo(Base):
    __tablename__ = "teacher_info"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    teaching_level = db.Column(db.Enum(EducationLevel), nullable=False)
    teaching_subject = db.Column(db.Enum(SubjectList), nullable=False)
    institute_type = db.Column(db.Enum(InstitutionType), nullable=False)
    institute_name = db.Column(db.String(100), unique=True, nullable=False)
    institute_website = db.Column(db.String(100), unique=True, nullable=False)
    institute_contact = db.Column(db.String(50), unique=True, nullable=False)
    institute_address = db.Column(db.String(255), unique=True, nullable=False)
    user = relationship("User", back_populates="teacher_info")
    
    def __repr__(self) -> str:
        return f"[TeacherInfo: {self.id!r}]"


class StudentInfo(Base):
    __tablename__ = "student_info"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    study_level = db.Column(db.Enum(EducationLevel), nullable=False)
    study_grade = db.Column(db.Enum(ClassList), nullable=False)
    institute_type = db.Column(db.Enum(InstitutionType), nullable=False)
    institute_name = db.Column(db.String(100), unique=True, nullable=False)
    institute_website = db.Column(db.String(100), unique=True, nullable=False)
    institute_contact = db.Column(db.String(50), unique=True, nullable=False)
    institute_address = db.Column(db.String(255), unique=True, nullable=False)
    user = relationship("User", back_populates="student_info")
    
    def __repr__(self) -> str:
        return f"[StudentInfo: {self.id!r}]"
        
   
# Create an engine to connect to your database     
engine = db.create_engine(DATABASE_ENGINE)

# Generate the SQL schema for the User model
metadata = db.MetaData()
Base.metadata.create_all(engine)
print('<= Database Successfully Created.')