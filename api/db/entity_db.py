from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *
from flask_bcrypt import generate_password_hash, check_password_hash
from marshmallow_sqlalchemy import ModelSchema

# create_engine connect to examrag model

# WARNING --- dialect+driver://username:password@host:port/database --- Warning, port is db, dont change it,
engine = create_engine('mysql+mysqldb://root:120399@db/xamreg?charset=utf8mb4',
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
    Password = Column(String(50), nullable=False)
    Fullname = Column(String(100), nullable=False)
    Dob = Column(Date, nullable=False)
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
    def isExist(cls, id):
        exist = session.query(User).filter_by(ID=id).scalar()
        if exist is None:
            return False
        else:
            return True


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
                          nullable=False)

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
# Semester Examination persistent class
class Semester_Examination(Base):
    __tablename__ = 'semester_examination'
    SemID = Column(Integer,
                   primary_key=True,
                   autoincrement=True)
    SemTitle = Column(String(200),
                      nullable=False)

    @classmethod
    def create(cls, semid, semtitle):
        if session.query(Semester_Examination).filter(Semester_Examination.SemID == semid).scalar() is None:
            new_semester = Semester_Examination(SemID=semid,
                                                SemTitle=semtitle)
            session.add(new_semester)
            session.commit()
            session.close()
            return True
        else:
            return False


# Shift persistent class
class Shift(Base):
    __tablename__ = 'shift'
    ShiftID = Column(Integer,
                     primary_key=True,
                     autoincrement=True)
    Date_Start = Column(Date,
                        nullable=False)
    Start_At = Column(Time,
                        nullable=False)
    SubjectID = Column(String(45),
                       ForeignKey('subject.SubjectID'),
                       nullable=False)
    Subject = relationship("Subject",
                           back_populates="shift")
    SemID = Column(Integer,
                   ForeignKey('semester_examination.SemID'),
                   nullable=False)
    Semester_Examination = relationship("Semester_Examination",
                                        back_populates="shift")

    @classmethod
    def create(cls, shiftid, subjectid, semid, start_at, date_start):
        if session.query(Shift).filter(Shift.ShiftID == shiftid,
                                       Shift.SubjectID == subjectid,
                                       Shift.SemID == semid).scalar() is None:
            new_shift = Shift(ShiftID=shiftid,
                              SubjectID=subjectid,
                              Start_At=start_at,
                              SemID=semid,
                              Date_Start=date_start)
            session.add(new_shift)
            session.commit()
            session.close()
            return True
        else:
            return False


########Relationship###########
Semester_Examination.shift = relationship("Shift",
                                          back_populates="Semester_Examination")
Subject.shift = relationship("Shift",
                             back_populates="Subject")


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
    ShiftID = Column(Integer,
                     ForeignKey('shift.ShiftID'),
                     nullable=False)
    Shift = relationship("Shift", back_populates="exam_room")

    @classmethod
    def create(cls, roomid, shiftid, room_name, computer_number):
        if session.query(Exam_Room).filter(Exam_Room.ShiftID == shiftid,
                                           Exam_Room.RoomID == roomid).scalar() is None:
            new_room = Exam_Room(RoomID=roomid,
                                 ShiftID=shiftid,
                                 RoomName=room_name,
                                 Computer_Number=computer_number)
            session.add(new_room)
            session.commit()
            session.close()
            return True
        else:
            return False

###############Relationship######################
Shift.exam_room = relationship("Exam_Room", back_populates="Shift")

###Create Database##########
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


class ExamRoomSchema(ModelSchema):
    class Meta:
        model = Exam_Room
        # optionally attach a Session
        # to use for deserialization
        sqla_session = session


class ShiftSchema(ModelSchema):
    class Meta:
        model = Shift
        # optionally attach a Session
        # to use for deserialization
        sqla_session = session


class SemesterExaminationSchema(ModelSchema):
    class Meta:
        model = Semester_Examination
        # optionally attach a Session
        # to use for deserialization
        sqla_session = session


user_schema = UserSchema()
