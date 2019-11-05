from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

# create_engine connect to xamrag db
engine = create_engine('mysql+mysqldb://newroot:528491@localhost:3306/xamreg',
                       encoding='utf-8',
                       echo=True,
                       pool_size=5)
# echo is to set up SQLAlchemy logging
# dialect+driver://username:password@host:port/database

# Once base class is declared, any number of mapped classes can be defined in terms of it
Base = declarative_base()


# User persistent class
class User(Base):
    __tablename__ = 'user'
    UserID = Column(Integer, autoincrement=True, primary_key=True)
    Username = Column(String(45), nullable=False, unique=True)
    Password = Column(String(240), nullable=False)
    Fullname = Column(String(45), nullable=False)
    Dob = Column(DateTime(45), nullable=False)
    Email = Column(String(45), nullable=False)
    Gender = Column(String(45), nullable=False)
    Profile_Picture = Column(String(100), nullable=True)


# User_Role persistent class
class User_Role(Base):
    __tablename__ = 'user_role'
    UserID = Column(Integer,
                    ForeignKey('user.UserID'),
                    primary_key=True)
    RoleID = Column(Integer,
                    ForeignKey('role.RoleID'))


# Role persistent class
class Role(Base):
    __tablename__ = 'role'
    RoleID = Column(Integer,
                    primary_key=True,
                    autoincrement=True)
    RoleTitle = Column(String(45),
                       nullable=False)

# Admin persistent class
class Admin(Base):
    __tablename__ = 'admin'
    AdminID = Column(Integer,
                     primary_key=True,
                     autoincrement=True)
    UserID = Column(Integer,
                    ForeignKey('user.UserID'),
                    nullable=False)

# Student persistent class
class Student(Base):
    __tablename__ = 'student'
    StudentID = Column(Integer,
                       primary_key=True,
                       autoincrement=True)
    UserID = Column(Integer,
                    ForeignKey('user.UserID'),
                    nullable=False)
    CourseID = Column(Integer,
                      ForeignKey('subject.SubjectID'),
                      nullable=False)

# Subject persistent class
class Subject(Base):
    __tablename__ = 'subject'
    SubjectID = Column(Integer,
                       primary_key=True,
                       autoincrement=True)
    SubjectTitle = Column(String(45),
                          nullable=False)


# Course persistent class
class Course(Base):
    __tablename__ = 'course'
    CourseID = Column(Integer,
                      primary_key=True,
                      autoincrement=True)
    CourseTitle = Column(String(45),
                         nullable=False)
    SubjectID = Column(Integer,
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
    SubjectID = Column(Integer,
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
