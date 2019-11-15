from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *
from flask_bcrypt import generate_password_hash, check_password_hash

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
    def isExist(cls, name):
        session = Session()
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
            if check_password_hash(check.Password, password) is True:
                return True
            else:
                return False
        return False


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


# Unqualified student class
class Unqualified_Student(Base):
    __tablename__ = 'unqualified_student'

    UnqualifiedID = Column(Integer,
                           primary_key=True,
                           autoincrement=True)
    StudentID = Column(String(45),
                       ForeignKey('user.ID'),
                       nullable=False)
    SubjectID = Column(String(45),
                       ForeignKey('subject.SubjectID'),
                       nullable=False)
    User = relationship('User',
                        back_populates='unqualified_student')
    Subject = relationship('Subject',
                           back_populates='unqualified_student')

    @classmethod
    def create(cls, studentID, subjectID):
        if session.query(Unqualified_Student).filter(Unqualified_Student.StudentID == studentID,
                                                     Unqualified_Student.SubjectID == subjectID).scalar() is None:
            new_unqualified_user = Unqualified_Student(StudentID=studentID,
                                                       SubjectID=subjectID)
            session.add(new_unqualified_user)
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

User.unqualified_student = relationship('Unqualified_Student',
                                        order_by=Unqualified_Student.StudentID,
                                        back_populates='User')
Subject.unqualified_student = relationship('Unqualified_Student',
                                           order_by=Unqualified_Student.SubjectID,
                                           back_populates='Subject')


# Unqualified student class
class Qualified_Student(Base):
    __tablename__ = 'qualified_student'

    QualifiedID = Column(Integer,
                         primary_key=True,
                         autoincrement=True)
    StudentID = Column(String(45),
                       ForeignKey('user.ID'),
                       nullable=False)
    SubjectID = Column(String(45),
                       ForeignKey('subject.SubjectID'),
                       nullable=False)
    User = relationship('User',
                        back_populates='qualified_student')
    Subject = relationship('Subject',
                           back_populates='qualified_student')

    @classmethod
    def create(cls, studentID, subjectID):
        if session.query(Qualified_Student).filter(Qualified_Student.StudentID == studentID,
                                                   Qualified_Student.SubjectID == subjectID).scalar() is None:
            new_qualified_user = Qualified_Student(StudentID=studentID,
                                                   SubjectID=subjectID)
            session.add(new_qualified_user)
            session.commit()
            session.close()
            return True
        else:
            return False


User.qualified_student = relationship('Qualified_Student',
                                      order_by=Qualified_Student.StudentID,
                                      back_populates="User")
Subject.qualified_student = relationship('Qualified_Student',
                                         order_by=Qualified_Student.SubjectID,
                                         back_populates="Subject")

# Each Table object is a member of larger collection known as MetaData
# This object is available using the .metadata attribute of declarative base class.
# The metadata.create_all() method is passing in our Engine as a source of database connectivity.
#  For all tables that haven’t been created yet, it issues CREATE TABLE statements to the database.
Base.metadata.create_all(bind=engine)
