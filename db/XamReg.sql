create table if not exists exam_room
(
    RoomID          int auto_increment
        primary key,
    RoomName        varchar(45) not null,
    Computer_Number int         not null
);

create table if not exists subject
(
    SubjectID    int auto_increment
        primary key,
    SubjectTitle varchar(45) not null
);

create table if not exists shift
(
    ShiftID    int auto_increment
        primary key,
    SubjectID  int      not null,
    Start_At   datetime not null,
    Date_Start datetime not null,
    RoomID     int      not null,
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

create table if not exists user
(
    UserID          int auto_increment
        primary key,
    Username        varchar(45)  not null,
    Password        varchar(240) not null,
    Fullname        varchar(45)  not null,
    Dob             datetime     null,
    Email           varchar(45)  null,
    Gender          varchar(45)  null,
    Profile_Picture varchar(100) null,
    constraint Username
        unique (Username)
);

create table if not exists admin
(
    AdminID int auto_increment
        primary key,
    UserID  int not null,
    constraint admin_ibfk_1
        foreign key (UserID) references user (UserID)
);

create index UserID
    on admin (UserID);

create table if not exists student
(
    StudentID int auto_increment
        primary key,
    UserID    int not null,
    SubjectID int not null,
    constraint student_ibfk_1
        foreign key (UserID) references user (UserID),
    constraint student_ibfk_2
        foreign key (SubjectID) references subject (SubjectID)
);

create index CourseID
    on student (SubjectID);

create index UserID
    on student (UserID);

create table if not exists user_role
(
    UserID    int         not null,
    Role_Type varchar(45) not null,
    constraint user_role_UserID_uindex
        unique (UserID),
    constraint user_role_ibfk_1
        foreign key (UserID) references user (UserID)
);

create index RoleID
    on user_role (Role_Type);

alter table user_role
    add primary key (UserID);

