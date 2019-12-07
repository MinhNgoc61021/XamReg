from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *
from flask_bcrypt import generate_password_hash, check_password_hash
from marshmallow_sqlalchemy import ModelSchema

# create_engine connect to examrag model

# WARNING --- dialect+driver://username:password@host:port/database --- Warning, port is db, dont change it,
from sqlalchemy_filters import apply_pagination

engine = create_engine('mysql+mysqldb://newroot:528491@db/xamreg?charset=utf8mb4',
                       echo=True,
                       pool_size=5)
# echo is to set up SQLAlchemy logging


# Once base class is declared, any number of mapped classes can be defined in terms of it
# Any class below is mapped, contains the table names, columns in the database
Base = declarative_base()

# Session class is defined using sessionmaker()
Session = scoped_session(sessionmaker())
Session.configure(bind=engine)


# User persistent class
class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    ID = Column(String(45), primary_key=True)
    Username = Column(String(45), nullable=False, unique=True)
    Password = Column(String(240), nullable=False)
    Fullname = Column(String(45), nullable=False)
    Dob = Column(Date, nullable=False)
    Gender = Column(String(45), nullable=False)
    CourseID = Column(String(45), nullable=False)
    Role_Type = Column(String(45), nullable=False)

    # unqualified_student = relationship("unqualified_student", cascade="all, delete, delete-orphan", passive_deletes=True)
    # qualified_student = relationship("qualified_student", cascade="all, delete, delete-orphan", passive_deletes=True)

    @classmethod
    def getUser(cls, username):
        sess = Session()
        try:
            user = sess.query(User).filter_by(Username=username).scalar()
            return user_schema.dump(user)
        except:
            sess.rollback()
            raise
        finally:
            sess.close()

    @classmethod
    def searchStudentRecord(cls, studentID):
        sess = Session()
        try:
            user = sess.query(User).filter(User.ID.like(studentID+'%'))
            return user_schema.dump(user, many=True)
        except:
            sess.rollback()
            raise
        finally:
            sess.close()

    @classmethod
    def getRecord(cls, page_index, per_page, sort_field, sort_order):
        sess = Session()
        try:
            record_query = sess.query(User).filter(text('Role_Type = :type')).params(type='Student').order_by(getattr(
                getattr(User, sort_field), sort_order)())

            # user_query is the user object and get_record_pagination is the index data
            record_query, get_record_pagination = apply_pagination(record_query, page_number=int(page_index),
                                                                   page_size=int(per_page))

            # many=True if user_query is a collection of many results, so that record will be serialized to a list.
            return user_schema.dump(record_query, many=True), get_record_pagination
        except:
            sess.rollback()
            raise
        finally:
            sess.close()

    @classmethod
    def updateRecord(cls, currentStudentID, newStudentID, newUsername, newFullname, newCourseID, newDob, newGender):
        sess = Session()
        try:
            # A dictionary of key - values with key being the attribute to be updated, and value being the new
            # contents of attribute
            sess.query(User).filter_by(ID=currentStudentID).update(
                {User.ID: newStudentID, User.Username: newUsername, User.Fullname: newFullname,
                 User.CourseID: newCourseID, User.Dob: newDob, User.Gender: newGender})
            print('OK3', flush=True)
            sess.commit()
            print('OK4', flush=True)
        except:
            sess.rollback()
            raise
        finally:
            sess.close()

    @classmethod
    def delRecord(cls, studentID):
        sess = Session()
        try:
            user = sess.query(User).filter_by(ID=studentID).one()
            sess.delete(user)
            sess.commit()
        except:
            sess.rollback()
            raise
        finally:
            sess.close()

    @classmethod
    def isExist(cls, id):
        sess = Session()
        try:
            exist = sess.query(User).filter_by(ID=id).scalar()
            if exist is None:
                return False
            else:
                return True
        except:
            sess.rollback()
            raise
        finally:
            sess.close()

    # create a new user
    @classmethod
    def create(cls, id, username, password, fullname, dob, gender, courseID, role_type):
        sess = Session()
        try:
            if sess.query(User).filter(User.Username == username).scalar() is None:
                new_user = User(ID=id,
                                Username=username,
                                Password=generate_password_hash(password),
                                Fullname=fullname,
                                Dob=dob,
                                Gender=gender,
                                CourseID=courseID,
                                Role_Type=role_type)
                sess.add(new_user)
                sess.commit()
                return True
            else:
                return False
        except:
            sess.rollback()
            raise
        finally:
            sess.close()

    @classmethod
    def check_register(cls, username, password):
        sess = Session()
        try:
            check = sess.query(User).filter(User.Username == username).scalar()
            if check is not None:
                if check_password_hash(check.Password, str(password)) is True:
                    if check.Role_Type == 'Admin':
                        return 'Admin'
                    else:
                        return 'Student'
            else:
                return 'Not found'
        except:
            sess.rollback()
            raise
        finally:
            sess.close()


# Subject persistent class
class Subject(Base):
    __tablename__ = 'subject'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    SubjectID = Column(String(45),
                       primary_key=True)
    SubjectTitle = Column(String(45),
                          nullable=False)

    @classmethod
    def create(cls, subjectID, subjectTitle):
        sess = Session()
        try:
            if sess.query(Subject).filter(Subject.SubjectID == subjectID).scalar() is None:
                new_subject = Subject(SubjectID=subjectID,
                                      SubjectTitle=subjectTitle)
                sess.add(new_subject)
                sess.commit()
                return True
            else:
                return False
        except:
            sess.rollback()
            raise
        finally:
            sess.close()

    @classmethod
    def getRecord(cls, studentID, status_type, page_index, per_page, sort_field, sort_order):
        sess = Session()
        try:
            record_query = sess.query(Subject).join(
                Student_Status).filter(Student_Status.StudentID == studentID,
                                       Student_Status.Status == status_type).order_by(
                getattr(
                    getattr(Subject, sort_field), sort_order)())

            # record_query is the user object and get_record_pagination is the index data
            record_query, get_record_pagination = apply_pagination(record_query, page_number=int(page_index),
                                                                   page_size=int(per_page))
            # many=True if user_query is a collection of many results, so that record will be serialized to a list.
            return subject_schema.dump(record_query, many=True), get_record_pagination
        except:
            sess.rollback()
            raise
        finally:
            sess.close()


# student status class
class Student_Status(Base):
    __tablename__ = 'student_status'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    StatusID = Column(Integer,
                      primary_key=True,
                      autoincrement=True)
    StudentID = Column(String(45),
                       ForeignKey('user.ID', onupdate="cascade"),
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
        sess = Session()
        try:
            if sess.query(Student_Status).filter(Student_Status.StudentID == studentID,
                                                 Student_Status.SubjectID == subjectID).scalar() is None:
                student_status = Student_Status(StudentID=studentID,
                                                SubjectID=subjectID, Status=status)
                sess.add(student_status)
                sess.commit()
                return True
            else:
                return False
        except:
            sess.rollback()
            raise
        finally:
            sess.close()

    @classmethod
    def delRecord(cls, studentID, subjectID):
        sess = Session()
        try:
            status = sess.query(Student_Status).filter(Student_Status.StudentID == studentID, Student_Status.SubjectID == subjectID).one()
            sess.delete(status)
            sess.commit()
        except:
            sess.rollback()
            raise
        finally:
            sess.close()


class Semester_Examination(Base):
    __tablename__ = 'semester_examination'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    SemID = Column(Integer,
                   primary_key=True,
                   autoincrement=True)
    SemTitle = Column(String(200),
                      nullable=False)

    @classmethod
    def create(cls, semid, semtitle):
        sess = Session()
        if sess.query(Semester_Examination).filter(Semester_Examination.SemID == semid).scalar() is None:
            new_semester = Semester_Examination(SemID=semid,
                                                SemTitle=semtitle)
            sess.add(new_semester)
            sess.commit()
            sess.close()
            return True
        else:
            return False


# Shift persistent class
class Shift(Base):
    __tablename__ = 'shift'
    __table_args__ = {'mysql_engine': 'InnoDB'}

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
        sess = Session()
        try:
            if sess.query(Shift).filter(Shift.ShiftID == shiftid,
                                        Shift.SubjectID == subjectid,
                                        Shift.SemID == semid).scalar() is None:
                new_shift = Shift(ShiftID=shiftid,
                                  SubjectID=subjectid,
                                  Start_At=start_at,
                                  SemID=semid,
                                  Date_Start=date_start)
                sess.add(new_shift)
                sess.commit()
                return True
            else:
                return False
        except:
            sess.rollback()
            raise
        finally:
            sess.close()


# Exam_Room persistent class
class Exam_Room(Base):
    __tablename__ = 'exam_room'
    __table_args__ = {'mysql_engine': 'InnoDB'}

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
        sess = Session()
        try:
            if sess.query(Exam_Room).filter(Exam_Room.ShiftID == shiftid,
                                            Exam_Room.RoomID == roomid).scalar() is None:
                new_room = Exam_Room(RoomID=roomid,
                                     ShiftID=shiftid,
                                     RoomName=room_name,
                                     Computer_Number=computer_number)
                sess.add(new_room)
                sess.commit()
                return True
            else:
                return False
        except:
            sess.rollback()
            raise
        finally:
            sess.close()


############### Relationship ######################
# relationship() uses the foreign key relationships between the two tables to determine the nature of this linkage
# Determining that it is many to one.
# This corresponds to a parent-child or associative table relationship.
# back_populates parameter is used to establish a bidirectional relationship in one-to-many.
# where the “reverse” side is a many to one.

User.student_status = relationship('Student_Status',
                                   order_by=Student_Status.StudentID,
                                   back_populates='User', cascade="all, delete, delete-orphan")

Subject.student_status = relationship('Student_Status',
                                      order_by=Student_Status.SubjectID,
                                      back_populates='Subject', cascade="all, delete, delete-orphan")

Shift.exam_room = relationship("Exam_Room", back_populates="Shift", cascade="all, delete, delete-orphan")

Semester_Examination.shift = relationship("Shift",
                                          back_populates="Semester_Examination", cascade="all, delete, delete-orphan")

Subject.shift = relationship("Shift",
                             back_populates="Subject", cascade="all, delete, delete-orphan")

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
        sqla_session = scoped_session


class StudentStatusSchema(ModelSchema):
    class Meta:
        model = Student_Status
        # optionally attach a Session
        # to use for deserialization
        sqla_session = scoped_session


class ExamRoomSchema(ModelSchema):
    class Meta:
        model = Exam_Room
        # optionally attach a Session
        # to use for deserialization
        # sqla_session = session


class ShiftSchema(ModelSchema):
    class Meta:
        model = Shift
        # optionally attach a Session
        # to use for deserialization
        # sqla_session = session


class SemesterExaminationSchema(ModelSchema):
    class Meta:
        model = Semester_Examination
        # optionally attach a Session
        # to use for deserialization
        # sqla_session = session


# only=[] takes specific columns
user_schema = UserSchema(only=['ID', 'Username', 'Fullname', 'Dob', 'Gender', 'CourseID', 'Role_Type'])

subject_schema = SubjectSchema()

student_status_schema = StudentStatusSchema()
