from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *
from flask_bcrypt import generate_password_hash, check_password_hash
from marshmallow_sqlalchemy import ModelSchema

# create_engine connect to examrag model

# WARNING --- dialect+driver://username:password@host:port/database --- Warning, port is db, dont change it,
engine = create_engine('mysql+mysqldb://newroot:528491@db/xamreg?charset=utf8mb4',
                       echo=True,
                       pool_size=5)
# echo is to set up SQLAlchemy logging


# Once base class is declared, any number of mapped classes can be defined in terms of it
# Any class below is mapped, contains the table names, columns in the database
Base = declarative_base()

# Session class is defined using sessionmaker()
Session = sessionmaker(bind=engine)

# A session object is the handle to database
session = Session()


# User persistent class
class User(Base):
    __tablename__ = 'user'

    ID = Column(String(45), primary_key=True)
    Username = Column(String(45), nullable=False, unique=True)
    Password = Column(String(240), nullable=False)
    Fullname = Column(String(45), nullable=False)
    Dob = Column(DateTime, nullable=False)
    Gender = Column(String(45), nullable=False)
    CourseID = Column(String(45), nullable=False)
    Role_Type = Column(String(45), nullable=False)

    # unqualified_student = relationship("unqualified_student", cascade="all, delete, delete-orphan", passive_deletes=True)
    # qualified_student = relationship("qualified_student", cascade="all, delete, delete-orphan", passive_deletes=True)

    @classmethod
    def getUser(cls, username):
        user = session.query(User).filter_by(Username=username).scalar()
        return user_schema.dump(user)

    @classmethod
    def isExist(cls, name):
        exists = session.query(User).filter_by(Username=name).scalar()
        if exists is not None:
            return exists
        return

    # create a new user
    @classmethod
    def create(cls, id, username, password, fullname, dob, gender, courseID, role_type):
        if session.query(User).filter(User.Username == username).scalar() is None:
            new_user = User(ID=id,
                            Username=username,
                            Password=generate_password_hash(password),
                            Fullname=fullname,
                            Dob=dob,
                            Gender=gender,
                            CourseID=courseID,
                            Role_Type=role_type)
            session.add(new_user)
            session.commit()
            session.close()
            return True
        else:
            return False

    @classmethod
    def check_register(cls, username, password):
        check = session.query(User).filter(User.Username == username).scalar()
        if check is not None:
            if check_password_hash(check.Password, str(password)) is True:
                if check.Role_Type == 'Admin':
                    session.close()
                    return 'Admin'
                else:
                    session.close()
                    return 'Student'
        session.close()
        return 'Not found'


# Subject persistent class
class Subject(Base):
    __tablename__ = 'subject'
    SubjectID = Column(String(45),
                       primary_key=True)
    SubjectTitle = Column(String(45),
                          nullable=False,
                          unique=True)

    @classmethod
    def create(cls, subjectID, subjectTitle):
        if session.query(Subject).filter(Subject.SubjectID == subjectID).scalar() is None:
            new_subject = Subject(SubjectID=subjectID,
                                  SubjectTitle=subjectTitle)
            session.add(new_subject)
            session.commit()
            session.close()
            return True
        else:
            return False


# student status class
class Student_Status(Base):
    __tablename__ = 'student_status'

    StatusID = Column(Integer,
                      primary_key=True,
                      autoincrement=True)
    StudentID = Column(String(45),
                       ForeignKey('user.ID'),
                       nullable=False)
    SubjectID = Column(String(45),
                       ForeignKey('subject.SubjectID'),
                       nullable=False)
    Status = Column(String(45),
                    nullable=False)

    User = relationship('User',
                        back_populates='student_status')
    Subject = relationship('Subject',
                           back_populates='student_status')

    @classmethod
    def create(cls, studentID, subjectID, status):
        if session.query(Student_Status).filter(Student_Status.StudentID == studentID,
                                                Student_Status.SubjectID == subjectID).scalar() is None:
            student_status = Student_Status(StudentID=studentID,
                                            SubjectID=subjectID, Status=status)
            session.add(student_status)
            session.commit()
            session.close()
            return True
        else:
            return False


# relationship() uses the foreign key relationships between the two tables to determine the nature of this linkage
# Determining that it is many to one.
# This corresponds to a parent-child or associative table relationship.
# back_populates parameter is used to establish a bidirectional relationship in one-to-many.
# where the “reverse” side is a many to one.

User.student_status = relationship('Student_Status',
                                   order_by=Student_Status.StudentID,
                                   back_populates='User')
Subject.student_status = relationship('Student_Status',
                                      order_by=Student_Status.SubjectID,
                                      back_populates='Subject')

# Each Table object is a member of larger collection known as MetaData
# This object is available using the .metadata attribute of declarative base class.
# The metadata.create_all() method is passing in our Engine as a source of database connectivity.
#  For all tables that haven’t been created yet, it issues CREATE TABLE statements to the database.
Base.metadata.create_all(bind=engine)


# marshmallow for entity


class UserSchema(ModelSchema):
    class Meta:
        model = User


class SubjectSchema(ModelSchema):
    class Meta:
        model = Subject
        # optionally attach a Session
        # to use for deserialization
        sqla_session = session


class StudentStatusSchema(ModelSchema):
    class Meta:
        model = Student_Status
        # optionally attach a Session
        # to use for deserialization
        sqla_session = session


user_schema = UserSchema()
