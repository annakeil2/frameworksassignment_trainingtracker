CREATE DATABASE training_tracker;

SET TIME ZONE 'UTC';

CREATE TABLE training (
    id SERIAL PRIMARY KEY,
    create_date TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_date TIMESTAMP WITH TIME ZONE DEFAULT NULL,
    user_id integer,
    training_name TEXT,
    training_type integer, 
    trainer_name TEXT,
    trainer_email citext,
    start_date TIMESTAMP WITH TIME ZONE,
    end_date TIMESTAMP WITH TIME ZONE DEFAULT NULL,
    training_hours integer,
    organiser TEXT,
    training_setting integer,
    training_status integer
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    create_date TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    updated_date TIMESTAMP WITH TIME ZONE DEFAULT NULL
    login_password TEXT,
    user_email citext,
    user_full_name TEXT,
    role_id integer
);

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    sender_user_id integer,
    receiver_user_id integer,
    create_date TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    updated_date TIMESTAMP WITH TIME ZONE DEFAULT NULL
    message_status integer,
    message_subject TEXT,
    message_body TEXT
);
