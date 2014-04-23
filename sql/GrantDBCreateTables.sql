CREATE DATABASE IF NOT EXISTS grants;
USE grants;

CREATE TABLE `PI` (
	PI_id INTEGER PRIMARY KEY,
	first_name VARCHAR(30),
	last_name VARCHAR(50) ) ENGINE = INNODB;
	
CREATE TABLE City (
	city_id INTEGER PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(30) ) ENGINE = INNODB;
	
CREATE TABLE Country (
	country_id INTEGER PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(30) ) ENGINE = INNODB;
	
CREATE TABLE State (
	state_id INTEGER PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(30) ) ENGINE = INNODB;
	
CREATE TABLE Term (
	term_id INTEGER PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(50) ) ENGINE = INNODB;
	
CREATE TABLE Organization (
	organization_id INTEGER PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(50),
	city_id INTEGER,
	country_id INTEGER,
	state_id INTEGER,
	district_id INTEGER,
	duns INTEGER,
  zip INTEGER,
  FOREIGN KEY city_id REFERENCE City (city_id),
  FOREIGN KEY country_id REFERENCE Country (country_id),
  FOREIGN KEY state_id REFERENCE State (state_id)
	) ENGINE = INNODB;
  
CREATE TABLE Department (
	department_id INTEGER PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(50) ) ENGINE = INNODB;
  
CREATE TABLE IC (
	ic_id INTEGER PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(50) ) ENGINE = INNODB;
	
CREATE TABLE Institution (
  organization_id integer,
  department_id integer,
  PRIMARY KEY (organization_id, department_id),
  FOREIGN KEY organization_id REFERENCES Organization (organization_id),
  FOREIGN KEY department_id REFERENCES Department (department_id) ) ENGINE = INNODB;
	
CREATE TABLE `Grant` (
	grant_id INTEGER PRIMARY KEY,
	project_id INTEGER,
	project_title VARCHAR(200),
	activity VARCHAR(10),
	award INTEGER,
	support_year INTEGER,
	suffix VARCHAR(10),
	foa_num VARCHAR(20),
	project_start DATE,
	project_end DATE,
	budget_start DATE,
	budget_end DATE,
	app_type INTEGER,
	cfda_code INTEGER,
	study_section VARCHAR(10) ) ENGINE = INNODB;
	
CREATE TABLE Grant_Institution (
	grant_id INTEGER,
	organization_id INTEGER,
	department_id INTEGER,
  PRIMARY KEY (grant_id, organization_id, department_id),
	FOREIGN KEY (grant_id) REFERENCES `Grant`(grant_id),
	FOREIGN KEY (department_id) REFERENCES `Department`(department_id),
	FOREIGN KEY (organization_id) REFERENCES Organization(organization_id) ) ENGINE = INNODB;
	
CREATE TABLE Grant_Project_Term (
	grant_id INTEGER,
	term_id INTEGER,
  PRIMARY KEY (grant_id, term_id),
	FOREIGN KEY (grant_id) REFERENCES `Grant`(grant_id),
	FOREIGN KEY (term_id) REFERENCES Term (term_id) ) ENGINE = INNODB;
	
CREATE TABLE Grant_Abstract_Term (
	grant_id INTEGER,
	term_id INTEGER,
  PRIMARY KEY (grant_id, term_id),
	FOREIGN KEY (grant_id) REFERENCES `Grant`(grant_id),
	FOREIGN KEY (term_id) REFERENCES Term (term_id) ) ENGINE = INNODB;
	
CREATE TABLE Grant_PHR_Term (
	grant_id INTEGER,
	term_id INTEGER,
  PRIMARY KEY (grant_id, term_id),
	FOREIGN KEY (grant_id) REFERENCES `Grant`(grant_id),
	FOREIGN KEY (term_id) REFERENCES Term (term_id) ) ENGINE = INNODB;	
  
CREATE TABLE Funding_IC (
	ic_id INTEGER,
	grant_id INTEGER,
  amount integer,
  PRIMARY KEY (ic_id, grant_id),
	FOREIGN KEY (grant_id) REFERENCES `Grant`(grant_id),
	FOREIGN KEY (ic_id) REFERENCES IC (ic_id) ) ENGINE = INNODB;
  
CREATE TABLE Admin_IC (
	ic_id INTEGER,
	grant_id INTEGER,
  PRIMARY KEY (ic_id, grant_id),
	FOREIGN KEY (grant_id) REFERENCES `Grant`(grant_id),
	FOREIGN KEY (ic_id) REFERENCES IC (ic_id) ) ENGINE = INNODB;
	
CREATE TABLE PI_Grant (
	grant_id INTEGER,
	pi_id INTEGER,
  PRIMARY KEY (grant_id, pi_id),
	FOREIGN KEY (grant_id) REFERENCES `Grant`(grant_id),
	FOREIGN KEY (pi_id) REFERENCES `PI` (pi_id) ) ENGINE = INNODB;