from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *
from flask_bcrypt import generate_password_hash, check_password_hash
from marshmallow_sqlalchemy import *
from marshmallow_sqlalchemy.fields import Nested

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

    ID = Column(String(45),
                primary_key=True)
    Username = Column(String(45),
                      nullable=False,
                      unique=True)
    Password = Column(String(240),
                      nullable=False)
    Fullname = Column(String(45),
                      nullable=False)
    Dob = Column(Date,
                 nullable=False)
    Gender = Column(String(45),
                    nullable=False)
    CourseID = Column(String(45),
                      nullable=False)
    Role_Type = Column(String(45),
                       nullable=False)

    # unqualified_student = relationship("unqualified_student", cascade="all, delete, delete-orphan", passive_deletes=True)
    # qualified_student = relationship("qualified_student", cascade="all, delete, delete-orphan", passive_deletes=True)

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
            check = sess.query(User).filter(User.Username == str(username)).scalar()
            if check is not None:
                if check_password_hash(check.Password, str(password)) is True:
                    if check.Role_Type == 'Admin':
                        return user_schema.dump(check), 'Admin'
                    elif check.Role_Type == 'Student':
                        return user_schema.dump(check), 'Student'
                else:
                    return 'Not found'
            else:
                return 'Not found'
        except:
            sess.rollback()
            raise
        finally:
            sess.close()

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
            user = sess.query(User).filter(User.ID.like(studentID + '%'))
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
            if str(currentStudentID) == str(newStudentID):
                sess.query(User).filter_by(ID=currentStudentID).update(
                    {
                        User.Fullname: newFullname,
                        User.CourseID: newCourseID,
                        User.Dob: newDob,
                        User.Gender: newGender
                    })
                sess.commit()
                return True
            elif sess.query(User).filter(User.ID == newStudentID, User.ID != currentStudentID).scalar() is None:
                sess.query(User).filter_by(ID=currentStudentID).update(
                    {User.ID: newStudentID,
                     User.Password: generate_password_hash(newStudentID),
                     User.Username: newUsername,
                     User.Fullname: newFullname,
                     User.CourseID: newCourseID,
                     User.Dob: newDob,
                     User.Gender: newGender})
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

    @classmethod
    def updatePassword(cls, currentUserID, newPassword):
        sess = Session()
        try:
            sess.query(User).filter_by(ID=currentUserID).update(
                {User.Password: generate_password_hash(newPassword)})
            sess.commit()
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
    def getSubjectRecord(cls, page_index, per_page, sort_field, sort_order):
        sess = Session()
        try:
            record_query = sess.query(Subject).order_by(
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

    @classmethod
    def getSubjectStatusRecord(cls, studentID, status_type, page_index, per_page, sort_field, sort_order):
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

    @classmethod
    def delRecord(cls, subjectID):
        sess = Session()
        try:
            subject = sess.query(Subject).filter_by(SubjectID=subjectID).one()
            sess.delete(subject)
            sess.commit()
        except:
            sess.rollback()
            raise
        finally:
            sess.close()

    @classmethod
    def updateRecord(cls, currentSubjectID, newSubjectID, newSubjectTitle):
        sess = Session()
        try:
            # A dictionary of key - values with key being the attribute to be updated, and value being the new
            # contents of attribute
            if sess.query(Subject).filter(
                    or_(Subject.SubjectID == newSubjectID, Subject.SubjectTitle == newSubjectTitle),
                    Subject.SubjectID != currentSubjectID).scalar() is None:
                sess.query(Subject).filter_by(SubjectID=currentSubjectID).update(
                    {Subject.SubjectID: newSubjectID, Subject.SubjectTitle: newSubjectTitle})
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
    def searchSubjectRecord(cls, SubjectID):
        sess = Session()
        try:
            subject = sess.query(Subject).filter(Subject.SubjectID.like(SubjectID + '%'))
            return subject_schema.dump(subject, many=True)
        except:
            sess.rollback()
            raise
        finally:
            sess.close()


# Student_Status persistent class
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
                       ForeignKey('subject.SubjectID', onupdate="cascade"),
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
                if str(status).lower() == 'đủ điều kiện':
                    student_status = Student_Status(StudentID=studentID,
                                                    SubjectID=subjectID, Status='Qualified')
                    sess.add(student_status)
                    sess.commit()
                    return True
                elif str(status).lower() == 'không đủ điều kiện':
                    student_status = Student_Status(StudentID=studentID,
                                                    SubjectID=subjectID, Status='Unqualified')
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
            status = sess.query(Student_Status).filter(Student_Status.StudentID == studentID,
                                                       Student_Status.SubjectID == subjectID).one()
            sess.delete(status)
            sess.commit()
        except:
            sess.rollback()
            raise
        finally:
            sess.close()


# Semester_Examination persistent class
class Semester_Examination(Base):
    __tablename__ = 'semester_examination'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    SemID = Column(Integer,
                   primary_key=True)
    SemTitle = Column(String(200),
                      nullable=False)
    Status = Column(Boolean,
                    nullable=False, default=False)  # true là đang mở đăng kí, false là không mở đăng ký

    @classmethod
    def searchSemesterRecord(cls, SemTitle):
        sess = Session()
        try:
            semester = sess.query(Semester_Examination).filter(Semester_Examination.SemTitle.like(SemTitle + '%'),
                                                               Semester_Examination.Status == True)
            return semester_examination_schema.dump(semester, many=True)
        except:
            sess.rollback()
            raise
        finally:
            sess.close()

    @classmethod
    def create(cls, newSemesterTitle):
        sess = Session()
        try:
            if sess.query(Semester_Examination).filter(
                    Semester_Examination.SemTitle == newSemesterTitle).scalar() is None:
                new_semester = Semester_Examination(SemTitle=newSemesterTitle)
                sess.add(new_semester)
                sess.commit()
                sess.close()
                return True
            else:
                return False
        except:
            sess.rollback()
            raise
        finally:
            sess.close()

    @classmethod
    def getRecord(cls):
        sess = Session()
        try:
            semester_list = sess.query(Semester_Examination)
            return semester_examination_schema.dump(semester_list, many=True)
        except:
            sess.rollback()
            raise
        finally:
            sess.close()

    @classmethod
    def getRegisterRecord(cls):
        sess = Session()
        try:
            semester_list = sess.query(Semester_Examination).filter(Semester_Examination.Status == True)
            return semester_examination_schema.dump(semester_list, many=True)
        except:
            sess.rollback()
            raise
        finally:
            sess.close()

    @classmethod
    def delRecord(cls, semID, semTitle):
        sess = Session()
        try:
            semester = sess.query(Semester_Examination).filter_by(SemID=semID, SemTitle=semTitle).one()
            sess.delete(semester)
            sess.commit()
        except:
            sess.rollback()
            raise
        finally:
            sess.close()

    @classmethod
    def updateRecord(cls, currentSemID, new_semTitle, new_Status):
        sess = Session()
        try:
            # A dictionary of key - values with key being the attribute to be updated, and value being the new
            # contents of attribute
            if sess.query(Semester_Examination).filter(Semester_Examination.SemID != currentSemID,
                                                       Semester_Examination.SemTitle == new_semTitle).scalar() is None:
                sess.query(Semester_Examination).filter(Semester_Examination.SemID == currentSemID).update(
                    {Semester_Examination.SemTitle: new_semTitle, Semester_Examination.Status: new_Status})
                sess.commit()
                return True
            else:
                return False
        except:
            sess.rollback()
            raise
        finally:
            sess.close()


# Shift persistent class
# (khi tạo ky thi thì nhập vào ca thi(SemID, SubjectID))
class Shift(Base):
    __tablename__ = 'shift'

    ShiftID = Column(Integer,
                     primary_key=True)
    SubjectID = Column(String(45),
                       ForeignKey('subject.SubjectID', onupdate="cascade"),
                       nullable=False)
    SemID = Column(Integer,
                   ForeignKey('semester_examination.SemID', onupdate="cascade"),
                   nullable=False)
    Date_Start = Column(Date,
                        nullable=False)
    Start_At = Column(Time,
                      nullable=False)
    End_At = Column(Time,
                    nullable=False)
    Subject = relationship('Subject',
                           back_populates='shift')
    Semester_Examination = relationship('Semester_Examination',
                                        back_populates='shift')

    @classmethod
    def create(cls, subjectID, semID, date_start, start_at, end_at):
        sess = Session()
        try:
            if sess.query(Shift).filter(Shift.SubjectID == subjectID, Shift.SemID == semID).scalar() is None:
                newShift = Shift(SubjectID=subjectID,
                                 SemID=semID,
                                 Date_Start=date_start,
                                 Start_At=start_at,
                                 End_At=end_at)
                sess.add(newShift)
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
    def getRecord(cls, semID, page_index, per_page, sort_field, sort_order):
        sess = Session()
        try:
            record_query = sess.query(Shift).options(joinedload('Subject')).filter(Shift.SemID == semID).order_by(
                getattr(
                    getattr(Shift, sort_field), sort_order)())

            # record_query is the user object and get_record_pagination is the index data
            record_query, get_record_pagination = apply_pagination(record_query, page_number=int(page_index),
                                                                   page_size=int(per_page))

            # many=True if user_query is a collection of many results, so that record will be serialized to a list.
            return shift_schema.dump(record_query, many=True), get_record_pagination
        except:
            sess.rollback()
            raise
        finally:
            sess.close()

    @classmethod
    def getQualifiedShiftRecord(cls, semID, studentID, page_index, per_page, sort_field, sort_order):
        sess = Session()
        try:
            record_query = sess.query(Shift).filter(Shift.SemID == semID, Shift.SubjectID == Student_Status.SubjectID,
                                                    Student_Status.StudentID == studentID,
                                                    Student_Status.Status == 'Qualified'
                                                    ).order_by(
                getattr(
                    getattr(Shift, sort_field), sort_order)())

            # record_query is the user object and get_record_pagination is the index data
            record_query, get_record_pagination = apply_pagination(record_query, page_number=int(page_index),
                                                                   page_size=int(per_page))

            # many=True if user_query is a collection of many results, so that record will be serialized to a list.
            return shift_schema.dump(record_query, many=True), get_record_pagination
        except:
            sess.rollback()
            raise
        finally:
            sess.close()

    @classmethod
    def searchShiftRecord(cls, SubjectID):
        sess = Session()
        try:
            subject = sess.query(Shift).filter(Shift.SubjectID.like(SubjectID + '%'),
                                               Student_Status.Status.like('Qualified' + '%'),
                                               Student_Status.SubjectID == Shift.SubjectID)
            return shift_schema.dump(subject, many=True)
        except:
            sess.rollback()
            raise
        finally:
            sess.close()

    @classmethod
    def delRecord(cls, shiftID):
        sess = Session()
        try:
            shift = sess.query(Shift).filter(Shift.ShiftID == shiftID).one()
            sess.delete(shift)
            sess.commit()
        except:
            sess.rollback()
            raise
        finally:
            sess.close()

    @classmethod
    def updateRecord(cls, ShiftID, SemID, newSubjectID, new_date_start, new_start_at, new_end_at):
        sess = Session()
        try:
            # A dictionary of key - values with key being the attribute to be updated, and value being the new
            # contents of attribute
            if sess.query(Shift).filter(Shift.SubjectID == newSubjectID, Shift.SemID == SemID,
                                        Shift.ShiftID != ShiftID).scalar() is None:
                sess.query(Shift).filter(Shift.ShiftID == ShiftID).update(
                    {Shift.SubjectID: newSubjectID,
                     Shift.Date_Start: new_date_start,
                     Shift.Start_At: new_start_at,
                     Shift.End_At: new_end_at})
                sess.commit()
                return True
            else:
                return False
        except:
            sess.rollback()
            raise
        finally:
            sess.close()


# Room_Shift persistent class (khi tạo ca thi thì thêm phòng thi vào)
class Room_Shift(Base):
    __tablename__ = 'room_shift'

    Room_ShiftID = Column(Integer,
                          primary_key=True)
    RoomID = Column(Integer, ForeignKey('exam_room.RoomID', onupdate='cascade'),
                    nullable=False)
    ShiftID = Column(Integer, ForeignKey('shift.ShiftID', onupdate='cascade'),
                     nullable=False)
    Exam_Room = relationship('Exam_Room',
                             back_populates='room_shift')
    Shift = relationship('Shift',
                         back_populates='room_shift')
    Student_Shift = relationship('Student_Shift',
                                 back_populates='room_shift')

    @classmethod
    def create(cls, roomID, shiftID):
        sess = Session()
        try:
            if sess.query(Room_Shift).filter(Room_Shift.RoomID == roomID,
                                             Room_Shift.ShiftID == shiftID).scalar() is None:

                newShift = Room_Shift(RoomID=roomID, ShiftID=shiftID)
                sess.add(newShift)
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
    def getRecord(cls, shiftID, page_index, per_page, sort_field, sort_order):
        sess = Session()
        try:
            record_query = sess.query(Exam_Room).filter(Exam_Room.RoomID == Room_Shift.RoomID,
                                                        Room_Shift.ShiftID == shiftID).order_by(
                getattr(
                    getattr(Exam_Room, sort_field), sort_order)())

            # record_query is the user object and get_record_pagination is the index data
            record_query, get_record_pagination = apply_pagination(record_query, page_number=int(page_index),
                                                                   page_size=int(per_page))

            # many=True if user_query is a collection of many results, so that record will be serialized to a list.
            return examroom_schema.dump(record_query, many=True), get_record_pagination
        except:
            sess.rollback()
            raise
        finally:
            sess.close()

    # lấy các phòng cho phép đăng ký theo ca
    @classmethod
    def getRegisterRoom(cls, shiftID, page_index, per_page, sort_field, sort_order):
        sess = Session()
        try:
            record_query = sess.query(Room_Shift).options(
                joinedload('Exam_Room')).filter(
                Room_Shift.ShiftID == shiftID).order_by(
                getattr(
                    getattr(Room_Shift, sort_field), sort_order)())

            # to count current student register (đếm số sinh viên đã đăng ký)
            # record_query is the user object and get_record_pagination is the index data
            record_query, get_record_pagination = apply_pagination(record_query, page_number=int(page_index),
                                                                   page_size=int(per_page))

            # many=True if user_query is a collection of many results, so that record will be serialized to a list.
            return roomshift_schema.dump(record_query, many=True), get_record_pagination
        except:
            sess.rollback()
            raise
        finally:
            sess.close()

    # lấy các phòng cho phép đăng ký theo ca
    @classmethod
    def getExportRecord(cls, shiftID, page_index, per_page, sort_field, sort_order):
        sess = Session()
        try:
            record_query = sess.query(Room_Shift).options(
                joinedload('Exam_Room')).options(
                joinedload('Student_Shift')).filter(
                Room_Shift.ShiftID == shiftID).order_by(
                getattr(
                    getattr(Room_Shift, sort_field), sort_order)())

            # to count current student register (đếm số sinh viên đã đăng ký)
            # record_query is the user object and get_record_pagination is the index data
            record_query, get_record_pagination = apply_pagination(record_query, page_number=int(page_index),
                                                                   page_size=int(per_page))

            # many=True if user_query is a collection of many results, so that record will be serialized to a list.
            return roomshift_schema.dump(record_query, many=True), get_record_pagination
        except:
            sess.rollback()
            raise
        finally:
            sess.close()

    @classmethod
    def delRecord(cls, roomID, shiftID):
        sess = Session()
        try:
            room_shift = sess.query(Room_Shift).filter(Room_Shift.RoomID == roomID, Room_Shift.ShiftID == shiftID).one()
            sess.delete(room_shift)
            sess.commit()
        except:
            sess.rollback()
            raise
        finally:
            sess.close()

    @classmethod
    def getTicketExportData(cls, studentID):
        sess = Session()
        try:
            record_query = sess.query(Room_Shift).options(
                joinedload('Exam_Room')
            ).options(joinedload('Student_Shift')
                      ).options(joinedload('Shift')
                                ).filter(Student_Shift.StudentID == studentID, Student_Shift.Room_ShiftID == Room_Shift.Room_ShiftID)

            return roomshift_schema.dump(record_query, many=True)
        except:
            sess.rollback()
            raise
        finally:
            sess.close()


# Student_Shift persistent class
# dùng bảng này đăng ký nhé
class Student_Shift(Base):
    __tablename__ = 'student_shift'

    RegisterID = Column(Integer,
                        primary_key=True)
    StudentID = Column(String(45),
                       ForeignKey('user.ID', onupdate="cascade"),
                       nullable=False)
    Room_ShiftID = Column(Integer,
                          ForeignKey('room_shift.Room_ShiftID', onupdate="cascade"),
                          nullable=False)
    User = relationship('User',
                        back_populates='student_shift')
    Room_Shift = relationship('Room_Shift',
                              back_populates='student_shift')

    @classmethod
    def create(cls, room_shiftID, studentID):
        sess = Session()
        try:
            registerTotalbyRoom_Shift = sess.query(Student_Shift).filter(Student_Shift.Room_ShiftID == room_shiftID).count()
            getMaxcapacity = sess.query(Exam_Room).join(Room_Shift).filter(
                Room_Shift.Room_ShiftID == room_shiftID).first()
            print(registerTotalbyRoom_Shift, flush=True)
            print(getMaxcapacity.Maxcapacity, flush=True)
            print('OK1', flush=True)
            if int(registerTotalbyRoom_Shift) < int(getMaxcapacity.Maxcapacity):
                if sess.query(Student_Shift).filter(Student_Shift.Room_ShiftID == room_shiftID,
                                                    Student_Shift.StudentID == studentID).scalar() is None:
                    newShift = Student_Shift(Room_ShiftID=room_shiftID, StudentID=str(studentID))
                    sess.add(newShift)
                    sess.commit()
                    return 'success'
                else:
                    return 'already-registered'
            else:
                return 'out of capacity'
        except:
            sess.rollback()
            raise
        finally:
            sess.close()

    @classmethod
    def delRecord(cls, StudentID, Room_ShiftID):
        sess = Session()
        try:
            room = sess.query(Student_Shift).filter(Student_Shift.StudentID == StudentID,
                                                    Student_Shift.Room_ShiftID == Room_ShiftID).one()
            sess.delete(room)
            sess.commit()
        except:
            sess.rollback()
            raise
        finally:
            sess.close()

    @classmethod
    def getRecord(cls, Room_ShiftID, sort_field, sort_order):
        sess = Session()
        try:
            record_query = sess.query(User).join(Student_Shift).filter(Student_Shift.StudentID == User.ID,
                                                                       Student_Shift.Room_ShiftID == Room_ShiftID).order_by(
                getattr(
                    getattr(User, sort_field), sort_order)())
            count_record_query = record_query.statement.with_only_columns([func.count()]).order_by(None)
            count = record_query.session.execute(count_record_query).scalar()
            # many=True if user_query is a collection of many results, so that record will be serialized to a list.
            return user_schema.dump(record_query, many=True), count
        except:
            sess.rollback()
            raise
        finally:
            sess.close()

    @classmethod
    def getRegisteredRoom_Shift(cls, StudentID):
        sess = Session()
        try:
            record_query = sess.query(User).join(Student_Shift).filter(Student_Shift.StudentID == StudentID)

            # many=True if user_query is a collection of many results, so that record will be serialized to a list.
            return user_schema.dump(record_query, many=True)
        except:
            sess.rollback()
            raise
        finally:
            sess.close()

    @classmethod
    def delTicketExportData(cls, registerID):
        sess = Session()
        try:
            ticket_row = sess.query(Student_Shift).filter(Student_Shift.RegisterID == registerID).one()
            sess.delete(ticket_row)
            sess.commit()
        except:
            sess.rollback()
            raise
        finally:
            sess.close()


# Exam Room persistent class
class Exam_Room(Base):
    __tablename__ = 'exam_room'
    __table_args__ = {'mysql_engine': 'InnoDB'}
    RoomID = Column(Integer,
                    primary_key=True)
    RoomName = Column(String(45),
                      nullable=False)
    Maxcapacity = Column(Integer,
                         nullable=False)
    Room_Shift = relationship('Room_Shift',
                              back_populates='exam_room')
    @classmethod
    def create(cls, room_name, maxcapacity):
        sess = Session()
        try:
            if sess.query(Exam_Room).filter(Exam_Room.RoomName == room_name).scalar() is None:
                new_room = Exam_Room(
                    RoomName=room_name,
                    Maxcapacity=maxcapacity)
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

    @classmethod
    def getRecord(cls, page_index, per_page, sort_field, sort_order):
        sess = Session()
        try:
            record_query = sess.query(Exam_Room).order_by(getattr(
                getattr(Exam_Room, sort_field), sort_order)())

            # user_query is the user object and get_record_pagination is the index data
            record_query, get_record_pagination = apply_pagination(record_query, page_number=int(page_index),
                                                                   page_size=int(per_page))

            # many=True if user_query is a collection of many results, so that record will be serialized to a list.
            return room_schema.dump(record_query, many=True), get_record_pagination
        except:
            sess.rollback()
            raise
        finally:
            sess.close()

    @classmethod
    def updateRecord(cls, currentRoomID, newRoomName, newMaxcapacity):
        sess = Session()
        try:
            # A dictionary of key - values with key being the attribute to be updated, and value being the new
            # contents of attribute
            if sess.query(Exam_Room).filter(Exam_Room.RoomID != currentRoomID,
                                            Exam_Room.RoomName == newRoomName).scalar() is None:
                sess.query(Exam_Room).filter_by(RoomID=currentRoomID).update(
                    {Exam_Room.RoomName: newRoomName, Exam_Room.Maxcapacity: newMaxcapacity})
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
    def delRecord(cls, roomID):
        sess = Session()
        try:
            room = sess.query(Exam_Room).filter(Exam_Room.RoomID == roomID).one()
            sess.delete(room)
            sess.commit()
        except:
            sess.rollback()
            raise
        finally:
            sess.close()

    @classmethod
    def searchRoomRecord(cls, roomName):
        sess = Session()
        try:
            room = sess.query(Exam_Room).filter(Exam_Room.RoomName.like(roomName + '%'))
            return room_schema.dump(room, many=True)
        except:
            sess.rollback()
            raise
        finally:
            sess.close()


class Log(Base):
    __tablename__ = 'log'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    LogID = Column(Integer,
                   primary_key=True)
    UserID = Column(String(45),
                    ForeignKey('user.ID'),
                    nullable=False,
                    onupdate="cascade")
    Action = Column(String(200),
                    nullable=False)
    Created_At = Column(DateTime,
                        nullable=False)
    User = relationship("User",
                        back_populates="log")

    @classmethod
    def create(cls, userID, action, created_at):
        sess = Session()
        try:
            newLog = Log(UserID=userID,
                         Action=action,
                         Created_At=created_at)
            sess.add(newLog)
            sess.commit()
        except:
            sess.rollback()
            raise
        finally:
            sess.close()

    @classmethod
    def getLog(cls, page_index, per_page, sort_field, sort_order):
        sess = Session()
        try:
            log_query = sess.query(Log).order_by(getattr(
                getattr(Log, sort_field), sort_order)())

            # user_query is the user object and get_record_pagination is the index data
            log_query, get_record_pagination = apply_pagination(log_query, page_number=int(page_index),
                                                                page_size=int(per_page))
            print('OK3', flush=True)
            # many=True if user_query is a collection of many results, so that record will be serialized to a list.
            return log_schema.dump(log_query, many=True), get_record_pagination
        except:
            sess.rollback()
            raise
        finally:
            sess.close()


# ------------ Relationship ----------- #
# relationship() uses the foreign key relationships between the two tables to determine the nature of this linkage
# Determining that it is many to one.
# This corresponds to a parent-child or associative table relationship.
# back_populates parameter is used to establish a bidirectional relationship in one-to-many.
# where the “reverse” side is a many to one.

User.student_status = relationship('Student_Status',
                                   order_by=Student_Status.StudentID,
                                   back_populates='User',
                                   cascade='all, delete, delete-orphan')

Subject.student_status = relationship('Student_Status',
                                      order_by=Student_Status.SubjectID,
                                      back_populates='Subject',
                                      cascade='all, delete, delete-orphan')

User.log = relationship('Log',
                        order_by=Log.UserID,
                        back_populates='User',
                        cascade='all, delete, delete-orphan')

Subject.shift = relationship('Shift',
                             order_by=Shift.SubjectID,
                             back_populates='Subject',
                             cascade='all, delete, delete-orphan')

User.student_shift = relationship('Student_Shift',
                                  order_by=Student_Shift.StudentID,
                                  back_populates='User',
                                  cascade='all, delete, delete-orphan')

Room_Shift.student_shift = relationship('Student_Shift',
                                        order_by=Student_Shift.Room_ShiftID,
                                        back_populates='Room_Shift',
                                        cascade='all, delete, delete-orphan')
Room_Shift.exam_room = relationship('Exam_Room',
                                    order_by=Exam_Room.RoomID,
                                    back_populates='Room_Shift')

Student_Shift.room_shift = relationship('Room_Shift',
                                        order_by=Room_Shift.Room_ShiftID,
                                        back_populates='Student_Shift')

Exam_Room.room_shift = relationship('Room_Shift',
                                    order_by=Room_Shift.RoomID,
                                    back_populates='Exam_Room',
                                    cascade='all, delete, delete-orphan')

Shift.room_shift = relationship('Room_Shift',
                                order_by=Room_Shift.ShiftID,
                                back_populates='Shift',
                                cascade='all, delete, delete-orphan')

Semester_Examination.shift = relationship('Shift',
                                          order_by=Shift.SemID,
                                          back_populates='Semester_Examination',
                                          cascade='all, delete, delete-orphan')

# Each Table object is a member of larger collection known as MetaData
# This object is available using the .metadata attribute of declarative base class.
# The metadata.create_all() method is passing in our Engine as a source of database connectivity.
#  For all tables that haven’t been created yet, it issues CREATE TABLE statements to the database.
Base.metadata.create_all(bind=engine)


# marshmallow for each entity for JSON deserialize
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
        # sqla_session = scoped_session


class ShiftSchema(ModelSchema):
    Subject = Nested(SubjectSchema)

    class Meta:
        model = Shift
        # optionally attach a Session
        # to use for deserialization
        # sqla_session = scoped_session


class StudentShiftSchema(ModelSchema):
    class Meta:
        model = Student_Shift


class ExamRoomSchema(ModelSchema):
    class Meta:
        model = Exam_Room
        # optionally attach a Session
        # to use for deserialization
        # sqla_session = session


class RoomShiftSchema(ModelSchema):
    Exam_Room = Nested(ExamRoomSchema)
    Student_Shift = Nested(StudentShiftSchema, many=True, only=['RegisterID'])
    Subject = Nested(SubjectSchema)
    Shift = Nested(ShiftSchema)

    class Meta:
        model = Room_Shift


class SemesterExaminationSchema(ModelSchema):
    class Meta:
        model = Semester_Examination
        # optionally attach a Session
        # to use for deserialization
        # sqla_session = session


class LogSchema(ModelSchema):
    class Meta:
        model = Log
        # optionally attach a Session
        # to use for deserialization
        # sqla_session = session


# only=[] takes specific columns
user_schema = UserSchema(only=['ID', 'Username', 'Fullname', 'Dob', 'Gender', 'CourseID', 'Role_Type'])

subject_schema = SubjectSchema()

student_status_schema = StudentStatusSchema()

semester_examination_schema = SemesterExaminationSchema()

shift_schema = ShiftSchema()

examroom_schema = ExamRoomSchema()

roomshift_schema = RoomShiftSchema()

log_schema = LogSchema()

room_schema = ExamRoomSchema()
