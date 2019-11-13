from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask_bcrypt import Bcrypt

# create_engine connect to xamrag model

# WARNING --- dialect+driver://username:password@host:port/database --- Warning, port is db, dont change it,
engine = create_engine('mysql+pymysql://newroot:528491@db/xamreg',
                       encoding='utf-8',
                       echo=True,
                       pool_size=5)
# echo is to set up SQLAlchemy logging


# Once base class is declared, any number of mapped classes can be defined in terms of it
Base = declarative_base()

# Session class is defined using sessionmaker()
Session = sessionmaker(bind=engine)
session = Session()

# User persistent class
class User(Base):
    __tablename__ = 'user'
    UserID = Column(String(45), primary_key=True)
    Username = Column(String(45), nullable=False, unique=True)
    Password = Column(String(240), nullable=False)
    Fullname = Column(String(45), nullable=False)
    Dob = Column(DateTime(45), nullable=False)
    Gender = Column(String(45), nullable=False)


    @classmethod
    def isExist(cls, name):
        session = Session()
        exists = session.query(User).filter_by(Username=name).scalar()
        if exists is not None:
            return exists
        return

    @classmethod
    def create(cls, userid, username, password, fullname, dob, email, gender):
        new_user = User(UserID=userid, Username=username, Password=password, Fullname=fullname, Dob=dob, Gender=gender)
        session.add(new_user)
        session.commit()
        return new_user

    @classmethod
    def check_register(cls, username, password):
        check = session.query(User).filter(User.Username == username).scalar()
        if check is not None:
            if Bcrypt().check_password_hash(check.Password, password) is True:
                return True
            else:
                return False
        return False

# User_Role persistent class
class User_Role(Base):
    __tablename__ = 'user_role'
    UserID = Column(String(45),
                    ForeignKey('user.UserID'),
                    primary_key=True, unique=True)
    Role_Type = Column(String(45), nullable=False)

    @classmethod
    def isExist(cls, UserID):
        exists = session.query(User_Role).filter_by(UserID=UserID).scalar()
        session.close()
        if exists is not None:
            return True
        return False

    @classmethod
    def create(cls, UserID, Role_Type):
        role = User_Role(UserID=UserID, Role_Type=Role_Type)
        session.add(role)
        session.commit()
        session.close()

# Student persistent class
class Student(Base):
    __tablename__ = 'student'
    StudentID = Column(String(45),
                       primary_key=True,
                       )
    CourseID = Column(String(45),
                      ForeignKey('course.CourseID'),
                      nullable=False)

# Subject persistent class
class Subject(Base):
    __tablename__ = 'subject'
    SubjectID = Column(String(45),
                       primary_key=True)
    SubjectTitle = Column(String(45),
                          nullable=False)


# Course persistent class
class Course(Base):
    __tablename__ = 'course'
    CourseID = Column(String(45),
                      primary_key=True)
    SubjectID = Column(String(45),
                       ForeignKey('subject.SubjectID'),
                       nullable=False)


# Exam_Room persistent class
class Exam_Room(Base):
    __tablename__ = 'exam_room'
    RoomID = Column(Integer,
                    primary_key=True,
                    autoincrement=True)
    RoomName = Column(String(45),
                      nullable=False)
    Computer_Number = Column(Integer,
                             nullable=False)


# Shift persistent class
class Shift(Base):
    __tablename__ = 'shift'
    ShiftID = Column(Integer,
                     primary_key=True,
                     autoincrement=True)
    SubjectID = Column(String(45),
                       ForeignKey('subject.SubjectID'),
                       nullable=False)
    Start_At = Column(DateTime,
                      nullable=False)
    Date_Start = Column(DateTime,
                        nullable=False)
    RoomID = Column(Integer,
                    ForeignKey('exam_room.RoomID'),
                    nullable=False)

# Semester Examination persistent class
class Semester_Examination(Base):
    __tablename__ = 'semester_examination'
    ExamID = Column(Integer,
                    primary_key=True,
                    autoincrement=True)
    ExamTitle = Column(String(45),
                       nullable=False)
    ShiftID = Column(Integer,
                     ForeignKey('shift.ShiftID'),
                     nullable=False)


Base.metadata.create_all(bind=engine)
