-- MySQL dump 10.13  Distrib 5.6.13, for Linux (x86_64)
--
-- Host: localhost    Database: Grants
-- ------------------------------------------------------
-- Server version	5.6.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Admin_IC`
--

DROP TABLE IF EXISTS `Admin_IC`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Admin_IC` (
  `ic_id` int(11) NOT NULL DEFAULT '0',
  `grant_id` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`ic_id`,`grant_id`),
  KEY `grant_id` (`grant_id`),
  CONSTRAINT `Admin_IC_ibfk_1` FOREIGN KEY (`grant_id`) REFERENCES `Grants` (`grant_id`),
  CONSTRAINT `Admin_IC_ibfk_2` FOREIGN KEY (`ic_id`) REFERENCES `IC` (`ic_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `City`
--

DROP TABLE IF EXISTS `City`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `City` (
  `city_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`city_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4097 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Country`
--

DROP TABLE IF EXISTS `Country`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Country` (
  `country_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`country_id`)
) ENGINE=InnoDB AUTO_INCREMENT=129 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `CountyCode`
--

DROP TABLE IF EXISTS `CountyCode`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CountyCode` (
  `state` varchar(10) DEFAULT NULL,
  `state_code` varchar(10) DEFAULT NULL,
  `county_code` varchar(20) DEFAULT NULL,
  `county_name` varchar(100) DEFAULT NULL,
  `ansi_cl` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Department`
--

DROP TABLE IF EXISTS `Department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Department` (
  `department_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`department_id`)
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `FrequentTerms`
--

DROP TABLE IF EXISTS `FrequentTerms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `FrequentTerms` (
  `term_id` int(11) DEFAULT NULL,
  `frequency` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Funding_IC`
--

DROP TABLE IF EXISTS `Funding_IC`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Funding_IC` (
  `ic_id` int(11) NOT NULL DEFAULT '0',
  `grant_id` int(11) NOT NULL DEFAULT '0',
  `amount` int(11) DEFAULT NULL,
  PRIMARY KEY (`ic_id`,`grant_id`),
  KEY `grant_id` (`grant_id`),
  CONSTRAINT `Funding_IC_ibfk_1` FOREIGN KEY (`grant_id`) REFERENCES `Grants` (`grant_id`),
  CONSTRAINT `Funding_IC_ibfk_2` FOREIGN KEY (`ic_id`) REFERENCES `IC` (`ic_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Grant_Abstract_Term`
--

DROP TABLE IF EXISTS `Grant_Abstract_Term`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Grant_Abstract_Term` (
  `grant_id` int(11) NOT NULL DEFAULT '0',
  `term_id` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`grant_id`,`term_id`),
  KEY `term_id` (`term_id`),
  CONSTRAINT `Grant_Abstract_Term_ibfk_1` FOREIGN KEY (`grant_id`) REFERENCES `Grants` (`grant_id`),
  CONSTRAINT `Grant_Abstract_Term_ibfk_2` FOREIGN KEY (`term_id`) REFERENCES `Term` (`term_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Grant_Institution`
--

DROP TABLE IF EXISTS `Grant_Institution`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Grant_Institution` (
  `grant_id` int(11) NOT NULL DEFAULT '0',
  `organization_id` int(11) NOT NULL DEFAULT '0',
  `department_id` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`grant_id`,`organization_id`,`department_id`),
  KEY `department_id` (`department_id`),
  KEY `organization_id` (`organization_id`),
  CONSTRAINT `Grant_Institution_ibfk_1` FOREIGN KEY (`grant_id`) REFERENCES `Grants` (`grant_id`),
  CONSTRAINT `Grant_Institution_ibfk_2` FOREIGN KEY (`department_id`) REFERENCES `Department` (`department_id`),
  CONSTRAINT `Grant_Institution_ibfk_3` FOREIGN KEY (`organization_id`) REFERENCES `Organization` (`organization_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Grant_PHR_Term`
--

DROP TABLE IF EXISTS `Grant_PHR_Term`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Grant_PHR_Term` (
  `grant_id` int(11) NOT NULL DEFAULT '0',
  `term_id` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`grant_id`,`term_id`),
  KEY `term_id` (`term_id`),
  CONSTRAINT `Grant_PHR_Term_ibfk_1` FOREIGN KEY (`grant_id`) REFERENCES `Grants` (`grant_id`),
  CONSTRAINT `Grant_PHR_Term_ibfk_2` FOREIGN KEY (`term_id`) REFERENCES `Term` (`term_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Grant_Project_Term`
--

DROP TABLE IF EXISTS `Grant_Project_Term`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Grant_Project_Term` (
  `grant_id` int(11) NOT NULL DEFAULT '0',
  `term_id` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`grant_id`,`term_id`),
  KEY `term_id` (`term_id`),
  CONSTRAINT `Grant_Project_Term_ibfk_1` FOREIGN KEY (`grant_id`) REFERENCES `Grants` (`grant_id`),
  CONSTRAINT `Grant_Project_Term_ibfk_2` FOREIGN KEY (`term_id`) REFERENCES `Term` (`term_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Grants`
--

DROP TABLE IF EXISTS `Grants`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Grants` (
  `grant_id` int(11) NOT NULL,
  `project_id` int(11) DEFAULT NULL,
  `project_title` varchar(200) DEFAULT NULL,
  `activity` varchar(10) DEFAULT NULL,
  `support_year` int(11) DEFAULT NULL,
  `suffix` varchar(10) DEFAULT NULL,
  `foa_num` varchar(20) DEFAULT NULL,
  `project_start` date DEFAULT NULL,
  `project_end` date DEFAULT NULL,
  `budget_start` date DEFAULT NULL,
  `budget_end` date DEFAULT NULL,
  `app_type` int(11) DEFAULT NULL,
  `cfda_code` int(11) DEFAULT NULL,
  `study_section` varchar(10) DEFAULT NULL,
  `total_cost` int(11) DEFAULT NULL,
  `total_cost_sub_project` int(11) DEFAULT NULL,
  `award` int(11) DEFAULT NULL,
  PRIMARY KEY (`grant_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `HeatMapInfo`
--

DROP TABLE IF EXISTS `HeatMapInfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `HeatMapInfo` (
  `zip` varchar(50) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `state` varchar(100) DEFAULT NULL,
  `county_name` varchar(100) DEFAULT NULL,
  `county_code` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `IC`
--

DROP TABLE IF EXISTS `IC`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `IC` (
  `ic_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ic_id`)
) ENGINE=InnoDB AUTO_INCREMENT=256 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Institution`
--

DROP TABLE IF EXISTS `Institution`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Institution` (
  `organization_id` int(11) NOT NULL DEFAULT '0',
  `department_id` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`organization_id`,`department_id`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `Institution_ibfk_1` FOREIGN KEY (`organization_id`) REFERENCES `Organization` (`organization_id`),
  CONSTRAINT `Institution_ibfk_2` FOREIGN KEY (`department_id`) REFERENCES `Department` (`department_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Organization`
--

DROP TABLE IF EXISTS `Organization`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Organization` (
  `organization_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `city_id` int(11) DEFAULT NULL,
  `country_id` int(11) DEFAULT NULL,
  `state_id` int(11) DEFAULT NULL,
  `district_id` int(11) DEFAULT NULL,
  `duns` int(11) DEFAULT NULL,
  `zip` int(11) DEFAULT NULL,
  PRIMARY KEY (`organization_id`),
  KEY `city_id` (`city_id`),
  KEY `country_id` (`country_id`),
  KEY `state_id` (`state_id`),
  CONSTRAINT `Organization_ibfk_1` FOREIGN KEY (`city_id`) REFERENCES `City` (`city_id`),
  CONSTRAINT `Organization_ibfk_2` FOREIGN KEY (`country_id`) REFERENCES `Country` (`country_id`),
  CONSTRAINT `Organization_ibfk_3` FOREIGN KEY (`state_id`) REFERENCES `State` (`state_id`)
) ENGINE=InnoDB AUTO_INCREMENT=49500 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `PI`
--

DROP TABLE IF EXISTS `PI`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PI` (
  `PI_id` int(11) NOT NULL,
  `first_name` varchar(30) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`PI_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `PI_Grant`
--

DROP TABLE IF EXISTS `PI_Grant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PI_Grant` (
  `grant_id` int(11) NOT NULL DEFAULT '0',
  `pi_id` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`grant_id`,`pi_id`),
  KEY `pi_id` (`pi_id`),
  CONSTRAINT `PI_Grant_ibfk_1` FOREIGN KEY (`grant_id`) REFERENCES `Grants` (`grant_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `State`
--

DROP TABLE IF EXISTS `State`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `State` (
  `state_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`state_id`)
) ENGINE=InnoDB AUTO_INCREMENT=256 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Term`
--

DROP TABLE IF EXISTS `Term`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Term` (
  `term_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`term_id`)
) ENGINE=InnoDB AUTO_INCREMENT=131071 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ZipCode`
--

DROP TABLE IF EXISTS `ZipCode`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ZipCode` (
  `zip` varchar(100) DEFAULT NULL,
  `latitude` varchar(50) DEFAULT NULL,
  `longitude` varchar(50) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `state` varchar(100) DEFAULT NULL,
  `county` varchar(200) DEFAULT NULL,
  `zip_class` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tempCity`
--

DROP TABLE IF EXISTS `tempCity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tempCity` (
  `city_id` int(11) NOT NULL DEFAULT '0',
  `name` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-05-04 22:55:58
