create table if not exists exam_room
(
    RoomID          int auto_increment
        primary key,
    Roomname        varchar(45) not null,
    Computer_number int         not null,
    constraint exam_room_Roomname_uindex
        unique (Roomname)
);

create table if not exists role
(
    RoleID    int auto_increment
        primary key,
    RoleTitle varchar(45) not null
);

create table if not exists subject
(
    SubjectID    int auto_increment
        primary key,
    SubjectTitle varchar(60) not null
);

create table if not exists course
(
    CourseID    int auto_increment
        primary key,
    CourseTitle varchar(70) not null,
    SubjectID   int         not null,
    constraint course_SubjectID_uindex
        unique (SubjectID),
    constraint course_subject_SubjectID_fk
        foreign key (SubjectID) references subject (SubjectID)
            on update cascade on delete cascade
);

create table if not exists shift
(
    ShiftID    int auto_increment
        primary key,
    SubjectID  int       not null,
    Start_At   timestamp not null on update CURRENT_TIMESTAMP,
    End_At     timestamp not null,
    Date_Start date      not null,
    RoomID     int       not null,
    constraint shift_exam_room_RoomID_fk
        foreign key (RoomID) references exam_room (RoomID)
            on update cascade on delete cascade,
    constraint shift_subject_SubjectID_fk
        foreign key (SubjectID) references subject (SubjectID)
            on update cascade on delete cascade
);

create table if not exists semester_examination
(
    ExamID    int auto_increment
        primary key,
    ExamTitle varchar(45) not null,
    ShiftID   int         not null,
    constraint semester_examination_shift_ExamShiftID_fk
        foreign key (ShiftID) references shift (ShiftID)
            on update cascade on delete cascade
);

create table if not exists user
(
    UserID          int auto_increment
        primary key,
    Username        varchar(45)  not null,
    Password        varchar(100) not null,
    Fullname        varchar(100) not null,
    Dob             datetime     not null,
    Email           varchar(100) not null,
    Gender          varchar(45)  not null,
    Profile_Picture varchar(100) not null,
    constraint user_AccountName_uindex
        unique (Username)
);

create table if not exists admin
(
    AdminID int auto_increment
        primary key,
    UserID  int not null,
    constraint admin_UserID_uindex
        unique (UserID),
    constraint admin_user_UserID_fk
        foreign key (UserID) references user (UserID)
            on update cascade on delete cascade
);

create table if not exists student
(
    StudentID varchar(45) not null,
    UserID    int         not null,
    CourseID  int         not null,
    constraint student_StudentID_uindex
        unique (StudentID),
    constraint student_course_CourseID_fk
        foreign key (CourseID) references course (CourseID)
            on update cascade on delete cascade,
    constraint student_user_UserID_fk
        foreign key (UserID) references user (UserID)
            on update cascade on delete cascade
);

alter table student
    add primary key (StudentID);

create table if not exists user_role
(
    UserID int not null
        primary key,
    RoleID int not null,
    constraint user_role_role_RoleID_fk
        foreign key (RoleID) references role (RoleID)
            on update cascade on delete cascade,
    constraint user_role_user_UserID_fk
        foreign key (UserID) references user (UserID)
            on update cascade on delete cascade
);


