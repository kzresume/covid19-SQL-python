CREATE DATABASE COVID_19;

CREATE TABLE covid19 (
    id bigserial NOT NULL PRIMARY KEY,
    date_value DATE NOT NULL,
    country_code VARCHAR(10) NOT NULL,
    confirmed int ,
    deaths int );
    
CREATE TABLE codes (
    id bigserial NOT NULL PRIMARY KEY,
    country_code VARCHAR(10) NOT NULL,
    polish_title VARCHAR(50) NOT NULL );
