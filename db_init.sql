DROP TABLE IF EXISTS diseasetype CASCADE;
DROP TABLE IF EXISTS country CASCADE;
DROP TABLE IF EXISTS disease CASCADE;
DROP TABLE IF EXISTS discover CASCADE;
DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS publicservant CASCADE;
DROP TABLE IF EXISTS doctor CASCADE;
DROP TABLE IF EXISTS specialize CASCADE;
DROP TABLE IF EXISTS record CASCADE;

CREATE TABLE diseasetype (
	id             integer PRIMARY KEY,
	description    varchar(140) NOT NULL
);

CREATE TABLE country (
	cname          varchar(50) PRIMARY KEY,
	population     bigint NOT NULL
);

CREATE TABLE disease (
	disease_code   varchar(50) PRIMARY KEY,
	pathogen       varchar(20) NOT NULL,
	description    varchar(140) NOT NULL,
	id             integer REFERENCES diseaseType(id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE discover (
	cname          varchar(50) REFERENCES country(cname) ON DELETE CASCADE,
	disease_code   varchar(50) REFERENCES disease(disease_code) ON DELETE CASCADE,
	first_enc_date date NOT NULL,
	PRIMARY KEY (cname, disease_code)
);

CREATE TABLE users (
	email          varchar(60) PRIMARY KEY,
	name           varchar(30) NOT NULL,
	surname        varchar(40) NOT NULL,
	salary         integer NOT NULL,
	phone          varchar(20) UNIQUE NOT NULL,
	cname          varchar(50) REFERENCES country(cname) ON DELETE CASCADE
);

CREATE TABLE publicservant (
	email          varchar(60) PRIMARY KEY REFERENCES users(email) ON DELETE CASCADE,
	department     varchar(50) NOT NULL
);

CREATE TABLE doctor (
	email          varchar(60) PRIMARY KEY REFERENCES users(email) ON DELETE CASCADE,
	degree         varchar(20) NOT NULL
);

CREATE TABLE specialize (
	id             integer REFERENCES diseasetype(id) ON DELETE CASCADE ON UPDATE CASCADE,
	email          varchar(60) REFERENCES doctor(email) ON DELETE CASCADE,
	PRIMARY KEY (id, email)
);

CREATE TABLE record (
	email          varchar(60) REFERENCES publicservant(email) ON DELETE CASCADE,
	cname          varchar(50) REFERENCES country(cname)  ON DELETE CASCADE,
	disease_code   varchar(50) REFERENCES disease(disease_code) ON DELETE CASCADE,
	total_deaths   integer NOT NULL,
	total_patients integer NOT NULL,
	PRIMARY KEY (email, cname, disease_code)
);