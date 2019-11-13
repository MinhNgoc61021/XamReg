create table if not exists exam_room
(
    RoomID          int auto_increment
        primary key,
    RoomName        varchar(45) not null,
    Computer_Number int         not null
);

create table if not exists subject
(
    SubjectID    varchar(45) not null
        primary key,
    SubjectTitle varchar(45) not null
);

create table if not exists course
(
    CourseID  varchar(45) not null
        primary key,
    SubjectID varchar(45) not null,
    constraint course_ibfk_1
        foreign key (SubjectID) references subject (SubjectID)
);

create index SubjectID
    on course (SubjectID);

create table if not exists shift
(
    ShiftID    int auto_increment
        primary key,
    SubjectID  varchar(45) not null,
    Start_At   datetime    not null,
    Date_Start datetime    not null,
    RoomID     int         not null,
    constraint shift_ibfk_1
        foreign key (SubjectID) references subject (SubjectID),
    constraint shift_ibfk_2
        foreign key (RoomID) references exam_room (RoomID)
);

create table if not exists semester_examination
(
    ExamID    int auto_increment
        primary key,
    ExamTitle varchar(45) not null,
    ShiftID   int         not null,
    constraint semester_examination_ibfk_1
        foreign key (ShiftID) references shift (ShiftID)
);

create index ShiftID
    on semester_examination (ShiftID);

create index RoomID
    on shift (RoomID);

create index SubjectID
    on shift (SubjectID);

create table if not exists student
(
    StudentID varchar(45) not null
        primary key,
    CourseID  varchar(45) not null,
    constraint student_ibfk_1
        foreign key (CourseID) references course (CourseID)
);

create index CourseID
    on student (CourseID);

create table if not exists user
(
    UserID   varchar(45)  not null
        primary key,
    Username varchar(45)  not null,
    Password varchar(240) not null,
    Fullname varchar(45)  not null,
    Dob      datetime     not null,
    Gender   varchar(45)  not null,
    constraint Username
        unique (Username)
);

create table if not exists user_role
(
    UserID    varchar(45) not null,
    Role_Type varchar(45) not null,
    constraint UserID
        unique (UserID),
    constraint user_role_ibfk_1
        foreign key (UserID) references user (UserID)
);

alter table user_role
    add primary key (UserID);

