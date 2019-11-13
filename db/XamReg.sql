create table if not exists subject
(
    subjectID    varchar(45) not null,
    subjectTitle varchar(45) not null,
    constraint subject_subjectID_uindex
        unique (subjectID),
    constraint subject_subjectTitle_uindex
        unique (subjectTitle)
);

alter table subject
    add primary key (subjectID);

create table if not exists user
(
    userID    varchar(45)  not null,
    username  varchar(45)  not null,
    password  varchar(200) not null,
    fullname  varchar(45)  not null,
    dob       datetime     not null on update CURRENT_TIMESTAMP,
    gender    varchar(20)  not null,
    courseID  varchar(45)  not null,
    role_type varchar(45)  not null,
    constraint user_userID_uindex
        unique (userID),
    constraint user_username_uindex
        unique (username)
);

alter table user
    add primary key (userID);

create table if not exists qualified_student
(
    quaIifiedD int auto_increment
        primary key,
    userID     varchar(45) not null,
    subjectID  varchar(45) not null,
    constraint qualified_student_subject_subjectID_fk
        foreign key (subjectID) references subject (subjectID)
            on update cascade on delete cascade,
    constraint qualified_student_user_userID_fk
        foreign key (userID) references user (userID)
            on update cascade on delete cascade
);

create table if not exists unqualified_student
(
    unqualifiedID int auto_increment
        primary key,
    userID        varchar(45) not null,
    subjectID     varchar(45) not null,
    constraint student_status_user_userID_fk
        foreign key (userID) references user (userID)
            on update cascade on delete cascade,
    constraint unqualified_student_subject_subjectID_fk
        foreign key (subjectID) references subject (subjectID)
            on update cascade on delete cascade
);


