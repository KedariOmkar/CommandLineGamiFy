CREATE DATABASE  IF NOT EXISTS `gbm` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `gbm`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: gbm
-- ------------------------------------------------------
-- Server version	8.0.37

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `character_habit`
--

DROP TABLE IF EXISTS `character_habit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `character_habit` (
  `cur_date` text,
  `a` int DEFAULT NULL,
  `b` int DEFAULT NULL,
  `c` int DEFAULT NULL,
  `d` int DEFAULT NULL,
  `e` int DEFAULT NULL,
  `f` int DEFAULT NULL,
  `g` int DEFAULT NULL,
  `h` int DEFAULT NULL,
  `i` int DEFAULT NULL,
  `j` int DEFAULT NULL,
  `k` int DEFAULT NULL,
  `l` int DEFAULT NULL,
  `m` int DEFAULT NULL,
  `n` int DEFAULT NULL,
  `o` int DEFAULT NULL,
  `p` int DEFAULT NULL,
  `q` int DEFAULT NULL,
  `r` int DEFAULT NULL,
  `s` int DEFAULT NULL,
  `t` int DEFAULT NULL,
  `u` int DEFAULT NULL,
  `v` int DEFAULT NULL,
  `x` int DEFAULT NULL,
  `y` int DEFAULT NULL,
  `z` int DEFAULT NULL,
  `total_habit` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `character_habit`
--

LOCK TABLES `character_habit` WRITE;
/*!40000 ALTER TABLE `character_habit` DISABLE KEYS */;
INSERT INTO `character_habit` VALUES ('2024-05-31',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
/*!40000 ALTER TABLE `character_habit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `character_physiqe_sharp`
--

DROP TABLE IF EXISTS `character_physiqe_sharp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `character_physiqe_sharp` (
  `cur_date` varchar(30) NOT NULL,
  `punch` int DEFAULT NULL,
  `strike` int DEFAULT NULL,
  `kick` int DEFAULT NULL,
  `defense` int DEFAULT NULL,
  `attack` int DEFAULT NULL,
  `total_workout` int DEFAULT NULL,
  PRIMARY KEY (`cur_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `character_physiqe_sharp`
--

LOCK TABLES `character_physiqe_sharp` WRITE;
/*!40000 ALTER TABLE `character_physiqe_sharp` DISABLE KEYS */;
INSERT INTO `character_physiqe_sharp` VALUES ('2024-05-31',0,0,0,0,0,0);
/*!40000 ALTER TABLE `character_physiqe_sharp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `character_physiqe_shield`
--

DROP TABLE IF EXISTS `character_physiqe_shield`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `character_physiqe_shield` (
  `cur_date` varchar(30) NOT NULL,
  `chest` int DEFAULT NULL,
  `back` int DEFAULT NULL,
  `shoulder` int DEFAULT NULL,
  `abs` int DEFAULT NULL,
  `leg` int DEFAULT NULL,
  `bicep` int DEFAULT NULL,
  `tricep` int DEFAULT NULL,
  `forearm` int DEFAULT NULL,
  `total_workout` int DEFAULT NULL,
  PRIMARY KEY (`cur_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `character_physiqe_shield`
--

LOCK TABLES `character_physiqe_shield` WRITE;
/*!40000 ALTER TABLE `character_physiqe_shield` DISABLE KEYS */;
INSERT INTO `character_physiqe_shield` VALUES ('2024-05-31',0,0,0,0,0,0,0,0,0);
/*!40000 ALTER TABLE `character_physiqe_shield` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `character_physiqe_silent`
--

DROP TABLE IF EXISTS `character_physiqe_silent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `character_physiqe_silent` (
  `cur_date` varchar(30) NOT NULL,
  `focus` int DEFAULT NULL,
  `breath` int DEFAULT NULL,
  `power` int DEFAULT NULL,
  `total_workout` int DEFAULT NULL,
  PRIMARY KEY (`cur_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `character_physiqe_silent`
--

LOCK TABLES `character_physiqe_silent` WRITE;
/*!40000 ALTER TABLE `character_physiqe_silent` DISABLE KEYS */;
INSERT INTO `character_physiqe_silent` VALUES ('2024-05-31',0,0,0,0);
/*!40000 ALTER TABLE `character_physiqe_silent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `character_routine`
--

DROP TABLE IF EXISTS `character_routine`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `character_routine` (
  `cur_date` varchar(30) NOT NULL,
  `a` int DEFAULT NULL,
  `b` int DEFAULT NULL,
  `c` int DEFAULT NULL,
  `d` int DEFAULT NULL,
  `e` int DEFAULT NULL,
  `f` int DEFAULT NULL,
  `g` int DEFAULT NULL,
  `h` int DEFAULT NULL,
  `i` int DEFAULT NULL,
  `j` int DEFAULT NULL,
  `k` int DEFAULT NULL,
  `l` int DEFAULT NULL,
  `m` int DEFAULT NULL,
  `n` int DEFAULT NULL,
  `o` int DEFAULT NULL,
  `p` int DEFAULT NULL,
  `q` int DEFAULT NULL,
  `r` int DEFAULT NULL,
  `s` int DEFAULT NULL,
  `t` int DEFAULT NULL,
  `u` int DEFAULT NULL,
  `v` int DEFAULT NULL,
  `x` int DEFAULT NULL,
  `y` int DEFAULT NULL,
  `z` int DEFAULT NULL,
  `total_routine` int DEFAULT NULL,
  PRIMARY KEY (`cur_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `character_routine`
--

LOCK TABLES `character_routine` WRITE;
/*!40000 ALTER TABLE `character_routine` DISABLE KEYS */;
INSERT INTO `character_routine` VALUES ('2024-05-31',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
/*!40000 ALTER TABLE `character_routine` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `game_bank`
--

DROP TABLE IF EXISTS `game_bank`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `game_bank` (
  `account_id` varchar(20) NOT NULL,
  `earned` bigint DEFAULT NULL,
  `lost` bigint DEFAULT NULL,
  `fine` bigint DEFAULT NULL,
  PRIMARY KEY (`account_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game_bank`
--

LOCK TABLES `game_bank` WRITE;
/*!40000 ALTER TABLE `game_bank` DISABLE KEYS */;
INSERT INTO `game_bank` VALUES ('ONK',0,0,0);
/*!40000 ALTER TABLE `game_bank` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `game_bank_transaction`
--

DROP TABLE IF EXISTS `game_bank_transaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `game_bank_transaction` (
  `transaction_id` int NOT NULL AUTO_INCREMENT,
  `transaction_date` varchar(30) DEFAULT NULL,
  `item_name` varchar(30) DEFAULT NULL,
  `item_price` bigint DEFAULT NULL,
  `item_category` varchar(30) DEFAULT NULL,
  `item_sub_category` varchar(30) DEFAULT NULL,
  `balance_available` bigint DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`transaction_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game_bank_transaction`
--

LOCK TABLES `game_bank_transaction` WRITE;
/*!40000 ALTER TABLE `game_bank_transaction` DISABLE KEYS */;
/*!40000 ALTER TABLE `game_bank_transaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `game_competition`
--

DROP TABLE IF EXISTS `game_competition`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `game_competition` (
  `cur_date` varchar(20) DEFAULT NULL,
  `total_time` int DEFAULT NULL,
  `total_mission` int DEFAULT NULL,
  `total_routine` int DEFAULT NULL,
  `total_tasks` int DEFAULT NULL,
  `total_money` bigint DEFAULT NULL,
  `total_kill` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game_competition`
--

LOCK TABLES `game_competition` WRITE;
/*!40000 ALTER TABLE `game_competition` DISABLE KEYS */;
INSERT INTO `game_competition` VALUES ('2024-04-21',807,1615,17,240,29270000000,248),('2024-04-21',0,0,0,0,0,0),('2024-04-22',0,0,0,0,0,0),('2024-04-23',0,0,0,0,0,0),('2024-04-28',0,0,0,0,0,0),('2024-05-01',0,0,0,0,0,0),('2024-05-01',0,0,0,0,0,0),('2024-05-02',0,0,0,0,0,0),('2024-05-03',0,0,0,0,0,0),('2024-05-31',963,1786,21,188,31810000000,223);
/*!40000 ALTER TABLE `game_competition` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `game_elite_billionaie`
--

DROP TABLE IF EXISTS `game_elite_billionaie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `game_elite_billionaie` (
  `name` varchar(50) DEFAULT NULL,
  `wealth` bigint DEFAULT NULL,
  `country` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game_elite_billionaie`
--

LOCK TABLES `game_elite_billionaie` WRITE;
/*!40000 ALTER TABLE `game_elite_billionaie` DISABLE KEYS */;
INSERT INTO `game_elite_billionaie` VALUES ('Elon Musk',229,'United States'),('Bernard Arnault',179,'France'),('Jeff Bezos',177,'United States'),('Bill Gates',141,'United States'),('Steve Ballmer',131,'United States'),('Mark Zuckerberg',128,'United States'),('Larry Page',126,'United States'),('Larry Ellison',123,'United States'),('Sergey Brin',120,'United States'),('Warren Buffett',120,'United States'),('Carlos Slim',105,'Mexico'),('Francoise Bettencourt Meyers',100,'France'),('Mukesh Ambani',96,'India'),('Amancio Ortega',88,'Spain'),('Gautam Adani',84,'India'),('Michael Dell',78,'United States'),('Jim Walton',73,'United States'),('Rob Walton',71,'United States'),('Alice Walton',70,'United States'),('Zhong Shanshan',68,'China'),('Julia Flesher Koch & family',67,'United States'),('Charles Koch',62,'United States'),('Colin Huang',52,'China'),('Alain Wertheimer',47,'France'),('Gerard Wertheimer',47,'France'),('Jacqueline Badger Mars',47,'United States'),('John Mars',47,'United States'),('Klaus-Michael Kuehne',44,'Germany'),('Jensen Huang',44,'United States'),('Phil Knight & family',43,'United States'),('Stephen Schwarzman',42,'United States'),('Zhang Yiming',42,'China'),('Len Blavatnik',41,'United States'),('Tadashi Yanai',38,'Japan'),('Abigail Johnson',37,'United States'),('Ken Griffin',37,'United States'),('German Larrea',36,'Mexico'),('MacKenzie Scott',36,'United States'),('Francois Pinault',35,'France'),('Shapoor Mistry',35,'India'),('Ma Huateng',35,'China'),('Changpeng Zhao',34,'Canada'),('Miriam Adelson',34,'United States'),('Shiv Nadar',34,'India'),('Giovanni Ferrero & family',34,'Italy'),('Dieter Schwarz',34,'Germany'),('Vladimir Potanin',31,'Russian Federation'),('Prajogo Pangestu',31,'Indonesia'),('Jack Ma',30,'China'),('Andrew Forrest',30,'Australia'),('Dan Gilbert',30,'United States'),('James Simons',30,'United States'),('Jeff Yass',29,'United States'),('William Ding',29,'China'),('Susanne Klatten',29,'Germany'),('Li Ka-shing',29,'Hong Kong'),('Iris Fontbona & family',28,'Chile'),('Low Tuck Kwong',28,'Indonesia'),('Eric Schmidt',28,'United States'),('Leonid Mikhelson',28,'Russian Federation'),('Gina Rinehart',27,'Australia'),('Azim Premji',26,'India'),('Reinhold Wuerth',26,'Germany'),('Thomas Peterffy',26,'United States'),('Lukas Walton',26,'United States'),('Takemitsu Takizaki',25,'Japan'),('Ernesto Bertarelli & family',25,'Switzerland'),('Savitri Jindal',25,'India'),('Vagit Alekperov',25,'Russian Federation'),('Thomas Frist',25,'United States'),('Elaine Marshall',25,'United States'),('Stefan Quandt',25,'Germany'),('Zeng Yuqun',24,'Hong Kong'),('He Xiangjian',24,'China'),('Vladimir Lisin',24,'Russian Federation'),('Jorge Paulo Lemann',24,'Brazil'),('Budi Hartono',23,'Indonesia'),('Eyal Ofer',23,'Monaco'),('Mark Mateschitz',22,'Austria'),('Rodolphe Saade & family',22,'France'),('Henry Cheng',22,'Hong Kong'),('Michael Hartono',22,'Indonesia'),('Xu Yangtian',22,'China'),('Lee Shau Kee',22,'Hong Kong'),('Alisher Usmanov',21,'Russian Federation'),('Alexey Mordashov',21,'Russian Federation'),('Dilip Shanghvi',21,'India'),('John Menard',21,'United States'),('Lakshmi Mittal',21,'India'),('Gianluigi Aponte',21,'Switzerland'),('Vicky Safra',20,'Greece'),('Stefan Persson',20,'Sweden'),('Idan Ofer',20,'Israel'),('Dustin Moskovitz',20,'United States'),('James Dyson',20,'United Kingdom'),('Leonard Lauder',20,'United States'),('Liu Yongxing',20,'China'),('Radhakishan Damani',20,'India'),('Jim Ratcliffe',20,'United Kingdom'),('Eduardo Saverin',19,'Brazil'),('Andrey Melnichenko',19,'Russian Federation'),('Kumar Birla',19,'India'),('Hasso Plattner',18,'Germany'),('Cyrus Poonawalla',18,'India'),('Sherry Brydson',18,'Canada'),('Stan Kroenke',18,'United States'),('David Tepper',18,'United States'),('Jeffery Hildebrand',18,'United States'),('Robert Kuok',17,'Malaysia'),('Donald Bren',17,'United States'),('Ray Dalio',17,'United States'),('Dave Duffield',17,'United States'),('Harold Hamm',16,'United States'),('Peter Woo',16,'Hong Kong'),('K P Singh',16,'India'),('Donald Newhouse',16,'United States'),('Charlene de Carvalho-Heineken',16,'Netherlands'),('Sunil Mittal',16,'India'),('Harry Triguboff',16,'Australia'),('Mikhail Prokhorov',16,'Russian Federation'),('Philip Anschutz',16,'United States'),('Li Xiting',16,'Singapore'),('Karl Albrecht Jr',16,'Germany'),('Beate Heister',16,'Germany'),('David Sun',16,'United States'),('John Tu',16,'United States'),('Wang Chuan-Fu',15,'China'),('Aliko Dangote',15,'Nigeria'),('Paolo Rocca & family',15,'Italy'),('Lui Che-Woo',15,'Hong Kong'),('Sammy Lee',15,'Hong Kong'),('Jan Koum',15,'United States'),('Andy Bechtolsheim',15,'Germany'),('Alwaleed Bin Talal',15,'Saudi Arabia'),('Qin Yinglin',15,'China'),('Uday Kotak',15,'India'),('Ricardo Salinas',15,'Mexico'),('Lei Jun',14,'China'),('Ravi Jaipuria',14,'India'),('Mike Cannon-Brookes',14,'Australia'),('Scott Farquhar',14,'Australia'),('Gennady Timchenko',14,'Russian Federation'),('Steve Cohen',14,'United States'),('George Kaiser',14,'United States'),('Zhang Bo',14,'China'),('Zhang Zhidong',14,'China'),('Alejandro Santo Domingo & family',13,'Colombia'),('Judy Love',13,'United States'),('George Roberts',13,'United States'),('Jay Chaudhry',13,'United States'),('Jiang Rensheng',13,'China'),('Michael Platt',13,'United Kingdom'),('Andreas Struengmann',13,'Germany'),('Thomas Struengmann',13,'Germany'),('Micky Arison',13,'United States'),('Henry Kravis',13,'United States'),('Martin Viessmann & family',13,'Germany'),('Xu Hang',13,'Hong Kong'),('Hugh Grosvenor',13,'United Kingdom'),('Jerry Jones',13,'United States'),('Leon Black',13,'United States'),('Johann Rupert & family',12,'South Africa'),('Henry Samueli',12,'United States'),('Mikhail Fridman',12,'Russian Federation'),('Andy Beal',12,'United States'),('Melinda French Gates',12,'United States'),('Elizabeth Johnson',12,'United States'),('Ned Johnson IV',12,'United States'),('Charoen Sirivadhanabhakdi',12,'Thailand'),('Charles Schwab',12,'United States'),('Renata Kellnerova',12,'Czech Republic'),('Laurence Graff',12,'United Kingdom'),('John Fredriksen',12,'Cyprus'),('Goh Cheng Liang',12,'Singapore'),('Raymond Kwok',12,'Hong Kong'),('Marijke Mars',12,'United States'),('Victoria Mars',12,'United States'),('Pamela Mars-Wright',12,'United States'),('Valerie Mars',12,'United States'),('Melker Schorling',12,'Sweden'),('Dmitry Rybolovlev',12,'Russian Federation'),('Izzy Englander',12,'United States'),('Robert Smith',11,'United States'),('Huang Shilin',11,'China'),('Masayoshi Son',11,'Japan'),('Christy Walton',11,'United States'),('Tom Gores',11,'United States'),('Thomas Kwok',11,'Hong Kong'),('Barry Lam',11,'Taiwan'),('Tilman Fertitta',11,'United States'),('Gong Hongjia',11,'China'),('Brian Chesky',11,'United States'),('Taylor Thomson',11,'Canada'),('Peter Thomson',11,'Canada'),('David Thomson',11,'Canada'),('Les Wexner',11,'United States'),('Wei Jianjun',11,'China'),('Marcel Telles',11,'Brazil'),('Diane Hendricks',11,'United States'),('Sarath Ratanavadi',11,'Thailand'),('Hansjoerg Wyss',11,'Switzerland'),('Steven Rales',11,'United States'),('Wang Wei',11,'China'),('Charles Butt & family',11,'United States'),('Wee Cho Yaw',11,'Singapore'),('Dietmar Hopp',11,'Germany'),('Pham Nhat Vuong',11,'Viet Nam'),('Antonia Axson Johnson',11,'Sweden'),('Carl Cook',11,'United States'),('Leo Koguan',11,'United States'),('Patrick Soon-Shiong',11,'United States'),('Terry Pegula',10,'United States'),('Graeme Hart',10,'New Zealand'),('Pierre Omidyar',10,'United States'),('Sun Piaoyang',10,'China'),('John Albert Sobrato',10,'United States'),('Ralph Sonnenberg',10,'Netherlands'),('Laurene Powell Jobs',10,'United States'),('Sandra Ortega Mera',10,'Spain'),('Lv Xiang-yang',10,'China'),('Laurent Dassault',10,'France'),('Marie-Helene Habert-Dassault',10,'France'),('Thierry Dassault',10,'France'),('Anthoni Salim',10,'Indonesia'),('Alex Gerko',10,'United Kingdom'),('Nusli Wadia',10,'India'),('Andre Esteves',10,'Brazil'),('Tony Ressler',10,'United States'),('Michael Rubin',10,'United States'),('Jay Y. Lee',10,'Korea, Republic of'),('Stan Druckenmiller',10,'United States'),('Nicky Oppenheimer',10,'South Africa'),('Karel Komarek',10,'Czech Republic'),('Prince Hans-Adam II',10,'Liechtenstein'),('Victor Rashnikov',10,'Russian Federation'),('Li Shu Fu',10,'China'),('Leonid Fedun',10,'Russian Federation'),('Andrey Guryev',10,'Russian Federation'),('Dang Yanbao',10,'China'),('Michael Kadoorie',10,'Hong Kong'),('Anthony Pratt',10,'Australia'),('Theo Albrecht Jr',10,'Germany'),('Jim Goodnight',10,'United States'),('Gabe Newell',10,'United States'),('Marc Benioff',10,'United States'),('David Shaw',10,'United States'),('David Steward',10,'United States'),('Pang Kang',10,'China'),('Richard Kinder',9,'United States'),('Vincent Bollore',9,'France'),('Ma Jianrong',9,'China'),('Josh Harris',9,'United States'),('Mangal Prabhat Lodha',9,'India'),('Blair Parry-Okeden',9,'United States'),('Jim Kennedy',9,'United States'),('Peter Thiel',9,'United States'),('Ralph Lauren',9,'United States'),('Manuel Villar',9,'Philippines'),('Nathan Blecharczyk',9,'United States'),('David Geffen',9,'United States'),('Zhong Huijuan',9,'China'),('Mohammed Al Amoudi',9,'Saudi Arabia'),('Suleiman Kerimov',9,'Russian Federation'),('Carlos Sicupira',9,'Brazil'),('Dan Friedkin',9,'United States'),('Robin Li',9,'China'),('John Malone',9,'United States'),('Ivan Glasenberg',9,'Australia'),('Rupert Murdoch',9,'United States'),('Chip Wilson',9,'Canada'),('Ronda Stryker',9,'United States'),('John Grayken',9,'Ireland'),('Randa Williams',9,'United States'),('Stephen Ross',9,'United States'),('Dannine Avara',9,'United States'),('Scott Duncan',9,'United States'),('Milane Frantz',9,'United States'),('Tammy Gustavson',9,'United States'),('Chen Bang',9,'China'),('Anthony Bamford & family',9,'United Kingdom'),('Linda Campbell',9,'Canada'),('Gaye Farncombe',9,'Canada'),('Jude Reyes',9,'United States'),('Chris Reyes',9,'United States'),('Magdalena Martullo',8,'Switzerland'),('Shahid Khan',8,'United States'),('Bob Rich',8,'United States'),('Nassef Sawiris',8,'Egypt'),('Steven Spielberg',8,'United States'),('Stef Wertheimer',8,'Israel'),('Joe Gebbia',8,'United States'),('Frank Lowy',8,'Australia'),('Arthur Irving',8,'Canada'),('German Khan',8,'Russian Federation'),('David Velez',8,'Colombia'),('Patrick Ryan',8,'United States'),('Carl Bennet',8,'Sweden'),('Richard Liu',8,'China'),('Robert Kraft',8,'United States'),('Stefano Pessina',8,'Monaco'),('Rahel Blocher',8,'Switzerland'),('Heinrich Deichmann & family',8,'Germany'),('Roman Abramovich',8,'Russian Federation'),('Rocco Commisso',8,'United States'),('Daniel Kretinsky',8,'Czech Republic'),('Benu Bangur',8,'India'),('Nancy Laurie',8,'United States'),('Jimmy Haslam',8,''),('Lin Shu-Hong',8,'Taiwan'),('Woody Johnson',8,'United States'),('Zhang Congyuan',8,'Taiwan'),('Georg Schaeffler',8,'Germany'),('Jorge Moll & family',8,'Brazil'),('Joe Lewis',8,'United Kingdom'),('Marc Rowan',8,'United States'),('Vikram Lal',8,'India'),('Andrey Skoch',8,'Russian Federation'),('Ray Hunt',8,'United States'),('Thomas Schmidheiny',8,'Switzerland'),('Gwendolyn Sontheim Meyer',8,'United States'),('Pauline Keinath',8,'United States'),('Natie Kirsh',8,'South Africa'),('Shari Arison',8,'Israel'),('Alain Bouchard',8,'Canada'),('Tito Beveridge',8,'United States'),('Wu Jianshu',8,'Hong Kong'),('Xu Shihui',8,'China'),('Wang Xing',8,'China'),('Terry Gou',8,'Taiwan'),('Lynn Schusterman',8,'United States'),('Ludwig Merckle',7,'Germany'),('David Cheriton',7,'Canada'),('Sri Prakash Lohia',7,'Indonesia'),('Alexander Abramov',7,'Russian Federation'),('Pedro Moreira Salles',7,'Brazil'),('Wang Liping',7,'China'),('Qi Shi',7,'China'),('Simon Reuben',7,'United Kingdom'),('David Reuben',7,'United Kingdom'),('Robert Pera',7,'United States'),('Juan Beckmann Vidal & family',7,'Mexico'),('Jon Gray',7,'United States'),('Ernie Garcia',7,'United States'),('Mitchell Rales',7,'United States'),('Dan Cathy',7,'United States'),('Bubba Cathy',7,'United States'),('Fernando Moreira Salles',7,'Brazil'),('Viktor Vekselberg',7,'Russian Federation'),('Liu Hanyuan',7,'China'),('Eric Smidt',7,'United States'),('Enrique Razon',7,'Philippines'),('Brian Armstrong',7,'United States'),('Takahisa Takahara',7,'Japan'),('George Soros',7,'United States'),('Vladimir Kim',7,'Kazakhstan'),('Tom Morris',7,'United Kingdom'),('Wang Wenyin',7,'China'),('Piero Ferrari',7,'Italy'),('Marcos Galperin',7,'Argentina'),('Todd Graves',7,'United States'),('Reinhold Schmieding',7,'United States'),('Liu Yonghao',7,'China'),('Niels Louis-Hansen',7,'Denmark'),('Henry Laufer',7,'United States'),('Yu Yong',7,'China'),('Dennis Washington',7,'United States'),('Yeung Kin-Man',7,'Hong Kong'),('Ann Kroenke',7,'United States'),('Li Shuirong',7,'China'),('Pat Stryker',7,'United States'),('Anders Holch Povlsen & family',7,'Denmark'),('James Pattison',7,'Canada'),('J K Irving',7,'Canada'),('Liz Mohn',7,'Germany'),('Giorgio Armani',7,'Italy'),('Mark Cuban',7,'United States'),('Alejandro Bailleres',7,'Mexico'),('Murali Divi',7,'India'),('Luis Sarmiento',7,'Colombia'),('George Lucas',7,'United States'),('Tobi Lutke',7,'Canada'),('Clive Calder',7,'United Kingdom'),('Todd Boehly',7,'United States'),('John Doerr',7,'United States'),('Geoffrey Kwok',7,'Hong Kong'),('Cen Junda',7,'China'),('Alain Merieux',7,'France'),('Frederik Paulsen',7,'Sweden'),('Pankaj Patel',7,'India'),('Rafael Del Pino',7,'Spain'),('Jeff Skoll',7,'United States'),('Scott Cook',7,'United States'),('Pei Zhenhua',7,'China'),('Abdullah Al Ghurair',7,'United Arab Emirates'),('Edward Roski',7,'United States'),('Andre Hoffmann',7,'Switzerland'),('Zhou Qunfei',7,'China'),('Samuel Yin',7,'Taiwan'),('Mat Ishbia',7,'United States'),('Bidzina Ivanishvili',7,'Georgia'),('Mahendra Choksi & family',7,'India'),('Ding Shizhong',7,'China'),('Li Xiang',7,'China'),('Edward Cadogan',7,'United Kingdom'),('Joe Ricketts',7,'United States'),('Mark Shoen',7,'United States'),('Fredrik Lundberg',6,'Sweden'),('Naguib Sawiris',6,'Egypt'),('Bernie Marcus',6,'United States'),('John Brown',6,'United States'),('Wang Jianlin',6,'China'),('Leonard Stern',6,'United States'),('Lu Weiding',6,'China'),('Rahul Bhatia',6,'India'),('Gary Rollins',6,'United States'),('Kenneth Dart',6,'Cayman Islands'),('Ding Shijia',6,'China'),('Chris Hohn',6,'United Kingdom'),('Thomas Pritzker',6,'United States'),('Ronald McAulay',6,'Hong Kong'),('Richard White',6,'Australia'),('Michael Smith',6,'United States'),('Trevor Rees-Jones',6,'United States'),('Jason Chang',6,'Singapore'),('Vyacheslav Kantor',6,'Russian Federation'),('Tim Sweeney',6,'United States'),('Walther Moreira Salles Jr',6,'Brazil'),('Joao Moreira Salles',6,'Brazil'),('David Siegel',6,'United States'),('Marian Ilitch',6,'United States'),('John Overdeck',6,'United States'),('Margaretta Taylor',6,'United States'),('James Cox Chambers',6,'United States'),('Katharine Rayner',6,'United States'),('Kelcy Warren',6,'United States'),('David Filo',6,'United States'),('Charles Johnson',6,'United States'),('Alexey Kuzmichev',6,'Russian Federation'),('Xavier Niel',6,'France'),('Kjeld Kirk Kristiansen',6,'Denmark'),('Lin Bin',6,'United States'),('M A Yusuff Ali',6,'United Arab Emirates'),('Rudolf Maag',6,'Switzerland'),('Margot Perot & family',6,'United States'),('Joe Mansueto',6,'United States'),('Andrew Currie',6,'United Kingdom'),('Tsai Eng-Meng',6,'Taiwan'),('Vera Michalski-Hoffmann',6,'Switzerland'),('Maja Hoffmann',6,'Switzerland'),('Richard LeFrak',6,'United States'),('Ruan Liping',6,'China'),('John Reece',6,'United Kingdom'),('Petr Aven',6,'Russian Federation'),('Wu Yajun',6,'China'),('Yasumitsu Shigeta',6,'Japan'),('Ruan Xueping',6,'China'),('Autry Stephens',6,'United States'),('Agnete Kirk Thinggaard',6,'Denmark'),('Thomas Kirk Kristiansen',6,'Denmark'),('Tony James',6,'United States'),('Charles Dolan & family',6,'United States'),('Wang Laisheng',6,'China'),('Johann Graf',6,'Austria'),('Tomasz Biernacki',6,'Poland'),('Ira Rennert',6,'United States'),('Joseph Lau',6,'Hong Kong'),('Reed Hastings',6,'United States'),('Rinat Akhmetov',6,'Ukraine'),('Mark Scheinberg',6,'Isle of Man'),('Sophie Bellon',6,'France'),('Francis Choi',6,'Hong Kong'),('Brian Acton',6,'United States'),('Gordon Getty',6,'United States'),('Theo Mueller',6,'Germany'),('Peter-Alexander Wacker & family',6,'Germany'),('Richard Tsai',6,'Taiwan'),('David Green',6,'United States'),('Lin Muqin',6,'China'),('Sergey Galitskiy',6,'Russian Federation'),('Bertil Hult',6,'Sweden'),('Sofie Kirk Kristiansen',6,'Denmark'),('Miuccia Prada',6,'Italy'),('Zhang Lei',6,'China'),('Joseph Tsai',6,'Canada'),('Maria Angelicoussis',6,'Greece'),('Thai Lee',6,'United States'),('Dagmar Dolby',6,'United States'),('Li Ge',6,'United States'),('Patrizio Bertelli',6,'Italy'),('Daniel Tsai',6,'Taiwan'),('Jorn Rausing',6,'Sweden'),('Mary Malone',6,'United States'),('Frits Goldschmeding',6,'Netherlands'),('Red Emmerson',6,'United States'),('Rupert Johnson',6,'United States'),('Guillaume Pousaz',6,'Switzerland'),('Sergei Popov',6,'Russian Federation'),('Michael Ashley',6,'United Kingdom'),('Thomas Straumann',6,'Switzerland'),('Omkar Kedari',0,'India');
/*!40000 ALTER TABLE `game_elite_billionaie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `game_matrix_agents`
--

DROP TABLE IF EXISTS `game_matrix_agents`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `game_matrix_agents` (
  `cur_date` varchar(20) NOT NULL,
  `pornstars` int DEFAULT NULL,
  `actors` int DEFAULT NULL,
  `celebs` int DEFAULT NULL,
  `speakers` int DEFAULT NULL,
  `singers` int DEFAULT NULL,
  `girlfriends` int DEFAULT NULL,
  `relatives` int DEFAULT NULL,
  `elites` int DEFAULT NULL,
  `comedians` int DEFAULT NULL,
  `influencers` int DEFAULT NULL,
  `youtubers` int DEFAULT NULL,
  `total_agents_killed` int DEFAULT NULL,
  `time_saved` int DEFAULT NULL,
  `total_agents_assult` int DEFAULT NULL,
  `time_wasted` int DEFAULT NULL,
  PRIMARY KEY (`cur_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game_matrix_agents`
--

LOCK TABLES `game_matrix_agents` WRITE;
/*!40000 ALTER TABLE `game_matrix_agents` DISABLE KEYS */;
INSERT INTO `game_matrix_agents` VALUES ('2024-05-31',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
/*!40000 ALTER TABLE `game_matrix_agents` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `game_setting`
--

DROP TABLE IF EXISTS `game_setting`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `game_setting` (
  `game_option` varchar(100) NOT NULL,
  `game_value` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`game_option`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game_setting`
--

LOCK TABLES `game_setting` WRITE;
/*!40000 ALTER TABLE `game_setting` DISABLE KEYS */;
INSERT INTO `game_setting` VALUES ('enddate','2024-08-25'),('startdate','2024-06-01');
/*!40000 ALTER TABLE `game_setting` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `game_store`
--

DROP TABLE IF EXISTS `game_store`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `game_store` (
  `name` varchar(100) DEFAULT NULL,
  `category` varchar(100) DEFAULT NULL,
  `field` varchar(100) DEFAULT NULL,
  `level` bigint DEFAULT NULL,
  `price` bigint DEFAULT NULL,
  `status` varchar(30) DEFAULT NULL,
  `bought_date` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game_store`
--

LOCK TABLES `game_store` WRITE;
/*!40000 ALTER TABLE `game_store` DISABLE KEYS */;
INSERT INTO `game_store` VALUES ('x5','lavish','car',80,2,'not owned','na'),('brentwood','lavish','house',80,2,'not owned','na'),('angela white','LAVISH','social',530,230,'not owned',NULL),('mia melano','LAVISH','social',320,230,'not owned',NULL),('wife','LIFE','relation',3000000000,2000000000,'not owned',NULL),('reagan foxx','LAVISH','social',500000000,300000000,'owned','2024-01-03'),('adria rae','LAVISH','social',1000000000,900000000,'not owned',NULL);
/*!40000 ALTER TABLE `game_store` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `objectives`
--

DROP TABLE IF EXISTS `objectives`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `objectives` (
  `ob_id` int NOT NULL AUTO_INCREMENT,
  `ob_name` varchar(100) DEFAULT NULL,
  `ob_cat` varchar(50) DEFAULT NULL,
  `ob_sub_cat` varchar(50) DEFAULT NULL,
  `ob_field` varchar(50) DEFAULT NULL,
  `ob_price` bigint DEFAULT NULL,
  `ob_achieved_date` varchar(20) DEFAULT NULL,
  `ob_age` int DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ob_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `objectives`
--

LOCK TABLES `objectives` WRITE;
/*!40000 ALTER TABLE `objectives` DISABLE KEYS */;
INSERT INTO `objectives` VALUES (5,'abigail mac','hoe','babe','lavish',20,'null',0,'lock'),(6,'leah gotti','hoe','babe','lavish',20,'null',0,'lock'),(7,'adria rae','hoe','teen','lavish',20,'null',0,'lock'),(8,'manasa varanasi','relations','model','personal',250,'null',0,'lock'),(9,'sreelela','relations','actress','personal',250,'null',0,'lock'),(10,'brentwood oiasis','mansions','primary','lavish',350,'null',0,'lock');
/*!40000 ALTER TABLE `objectives` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `report_mission_learn`
--

DROP TABLE IF EXISTS `report_mission_learn`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `report_mission_learn` (
  `cur_date` varchar(20) NOT NULL,
  `atma` varchar(30) DEFAULT NULL,
  `brain` varchar(30) DEFAULT NULL,
  `body` varchar(30) DEFAULT NULL,
  `lang` int DEFAULT NULL,
  `dsa` int DEFAULT NULL,
  `sub` int DEFAULT NULL,
  `tech` int DEFAULT NULL,
  `tools` int DEFAULT NULL,
  `build` int DEFAULT NULL,
  `softs` int DEFAULT NULL,
  `busi` int DEFAULT NULL,
  `total_mission` int DEFAULT NULL,
  PRIMARY KEY (`cur_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `report_mission_learn`
--

LOCK TABLES `report_mission_learn` WRITE;
/*!40000 ALTER TABLE `report_mission_learn` DISABLE KEYS */;
INSERT INTO `report_mission_learn` VALUES ('2024-05-31','0','0','0',0,0,0,0,0,0,0,0,0);
/*!40000 ALTER TABLE `report_mission_learn` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `report_mission_recall`
--

DROP TABLE IF EXISTS `report_mission_recall`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `report_mission_recall` (
  `cur_date` varchar(20) NOT NULL,
  `atma` varchar(30) DEFAULT NULL,
  `brain` varchar(30) DEFAULT NULL,
  `body` varchar(30) DEFAULT NULL,
  `lang` int DEFAULT NULL,
  `dsa` int DEFAULT NULL,
  `sub` int DEFAULT NULL,
  `tech` int DEFAULT NULL,
  `tools` int DEFAULT NULL,
  `build` int DEFAULT NULL,
  `softs` int DEFAULT NULL,
  `busi` int DEFAULT NULL,
  `total_mission` int DEFAULT NULL,
  PRIMARY KEY (`cur_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `report_mission_recall`
--

LOCK TABLES `report_mission_recall` WRITE;
/*!40000 ALTER TABLE `report_mission_recall` DISABLE KEYS */;
INSERT INTO `report_mission_recall` VALUES ('2024-05-31','0','0','0',0,0,0,0,0,0,0,0,0);
/*!40000 ALTER TABLE `report_mission_recall` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `report_mission_test`
--

DROP TABLE IF EXISTS `report_mission_test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `report_mission_test` (
  `cur_date` varchar(20) NOT NULL,
  `atma` varchar(30) DEFAULT NULL,
  `brain` varchar(30) DEFAULT NULL,
  `body` varchar(30) DEFAULT NULL,
  `lang` int DEFAULT NULL,
  `dsa` int DEFAULT NULL,
  `sub` int DEFAULT NULL,
  `tech` int DEFAULT NULL,
  `tools` int DEFAULT NULL,
  `build` int DEFAULT NULL,
  `softs` int DEFAULT NULL,
  `busi` int DEFAULT NULL,
  `total_mission` int DEFAULT NULL,
  PRIMARY KEY (`cur_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `report_mission_test`
--

LOCK TABLES `report_mission_test` WRITE;
/*!40000 ALTER TABLE `report_mission_test` DISABLE KEYS */;
INSERT INTO `report_mission_test` VALUES ('2024-05-31','0','0','0',0,0,0,0,0,0,0,0,0);
/*!40000 ALTER TABLE `report_mission_test` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `report_money`
--

DROP TABLE IF EXISTS `report_money`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `report_money` (
  `cur_date` varchar(20) DEFAULT NULL,
  `times` bigint DEFAULT NULL,
  `mission` bigint DEFAULT NULL,
  `lifestyle` bigint DEFAULT NULL,
  `matrix` bigint DEFAULT NULL,
  `tasks` bigint DEFAULT NULL,
  `total_money` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `report_money`
--

LOCK TABLES `report_money` WRITE;
/*!40000 ALTER TABLE `report_money` DISABLE KEYS */;
INSERT INTO `report_money` VALUES ('2024-05-31',0,0,0,0,0,0);
/*!40000 ALTER TABLE `report_money` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `report_session`
--

DROP TABLE IF EXISTS `report_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `report_session` (
  `cur_date` varchar(30) NOT NULL,
  `atma` int DEFAULT NULL,
  `brain` int DEFAULT NULL,
  `body` int DEFAULT NULL,
  `lang` int DEFAULT NULL,
  `dsa` int DEFAULT NULL,
  `sub` int DEFAULT NULL,
  `tech` int DEFAULT NULL,
  `tools` int DEFAULT NULL,
  `build` int DEFAULT NULL,
  `softs` int DEFAULT NULL,
  `busi` int DEFAULT NULL,
  `total_session` int DEFAULT NULL,
  PRIMARY KEY (`cur_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `report_session`
--

LOCK TABLES `report_session` WRITE;
/*!40000 ALTER TABLE `report_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `report_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `report_tasks`
--

DROP TABLE IF EXISTS `report_tasks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `report_tasks` (
  `task_id` int DEFAULT NULL,
  `task_name` varchar(400) DEFAULT NULL,
  `task_time` int DEFAULT NULL,
  `task_status` varchar(100) DEFAULT NULL,
  `task_level` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `report_tasks`
--

LOCK TABLES `report_tasks` WRITE;
/*!40000 ALTER TABLE `report_tasks` DISABLE KEYS */;
INSERT INTO `report_tasks` VALUES (1,'write the clear goals',20,'UNCHECKED','hig'),(2,'Update the Matrix ',20,'UNCHECKED','hig'),(3,'Identify the Obstacles',10,'UNCHECKED','hig'),(4,'create a main goal',10,'UNCHECKED','1'),(5,'create a main goal',5,'UNCHECKED','high'),(6,'write the top 25 skills for each face',20,'UNCHECKED','hig'),(7,'identify the boosters for hyper growth',20,'UNCHECKED','hig'),(8,'create routine , habits , protocols',20,'UNCHECKED','hig'),(9,'clean the obstacles ',10,'UNCHECKED','hig');
/*!40000 ALTER TABLE `report_tasks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `report_tasks_total`
--

DROP TABLE IF EXISTS `report_tasks_total`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `report_tasks_total` (
  `total_tasks_created` int NOT NULL DEFAULT '0',
  `total_tasks_done` int NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `report_tasks_total`
--

LOCK TABLES `report_tasks_total` WRITE;
/*!40000 ALTER TABLE `report_tasks_total` DISABLE KEYS */;
INSERT INTO `report_tasks_total` VALUES (0,0);
/*!40000 ALTER TABLE `report_tasks_total` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `report_time_learn`
--

DROP TABLE IF EXISTS `report_time_learn`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `report_time_learn` (
  `cur_date` varchar(20) NOT NULL,
  `atma` varchar(30) DEFAULT NULL,
  `brain` varchar(30) DEFAULT NULL,
  `body` varchar(30) DEFAULT NULL,
  `lang` int DEFAULT NULL,
  `dsa` int DEFAULT NULL,
  `sub` int DEFAULT NULL,
  `tech` int DEFAULT NULL,
  `tools` int DEFAULT NULL,
  `build` int DEFAULT NULL,
  `softs` int DEFAULT NULL,
  `busi` int DEFAULT NULL,
  `total_time` int DEFAULT NULL,
  PRIMARY KEY (`cur_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `report_time_learn`
--

LOCK TABLES `report_time_learn` WRITE;
/*!40000 ALTER TABLE `report_time_learn` DISABLE KEYS */;
INSERT INTO `report_time_learn` VALUES ('2024-05-31','0','0','0',0,0,0,0,0,0,0,0,0);
/*!40000 ALTER TABLE `report_time_learn` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `report_time_recall`
--

DROP TABLE IF EXISTS `report_time_recall`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `report_time_recall` (
  `cur_date` varchar(20) NOT NULL,
  `atma` varchar(30) DEFAULT NULL,
  `brain` varchar(30) DEFAULT NULL,
  `body` varchar(30) DEFAULT NULL,
  `lang` int DEFAULT NULL,
  `dsa` int DEFAULT NULL,
  `sub` int DEFAULT NULL,
  `tech` int DEFAULT NULL,
  `tools` int DEFAULT NULL,
  `build` int DEFAULT NULL,
  `softs` int DEFAULT NULL,
  `busi` int DEFAULT NULL,
  `total_time` int DEFAULT NULL,
  PRIMARY KEY (`cur_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `report_time_recall`
--

LOCK TABLES `report_time_recall` WRITE;
/*!40000 ALTER TABLE `report_time_recall` DISABLE KEYS */;
INSERT INTO `report_time_recall` VALUES ('2024-05-31','0','0','0',0,0,0,0,0,0,0,0,0);
/*!40000 ALTER TABLE `report_time_recall` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `report_time_test`
--

DROP TABLE IF EXISTS `report_time_test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `report_time_test` (
  `cur_date` varchar(20) NOT NULL,
  `atma` varchar(30) DEFAULT NULL,
  `brain` varchar(30) DEFAULT NULL,
  `body` varchar(30) DEFAULT NULL,
  `lang` int DEFAULT NULL,
  `dsa` int DEFAULT NULL,
  `sub` int DEFAULT NULL,
  `tech` int DEFAULT NULL,
  `tools` int DEFAULT NULL,
  `build` int DEFAULT NULL,
  `softs` int DEFAULT NULL,
  `busi` int DEFAULT NULL,
  `total_time` int DEFAULT NULL,
  PRIMARY KEY (`cur_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `report_time_test`
--

LOCK TABLES `report_time_test` WRITE;
/*!40000 ALTER TABLE `report_time_test` DISABLE KEYS */;
INSERT INTO `report_time_test` VALUES ('2024-05-31','0','0','0',0,0,0,0,0,0,0,0,0);
/*!40000 ALTER TABLE `report_time_test` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `routines`
--

DROP TABLE IF EXISTS `routines`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `routines` (
  `id` int NOT NULL AUTO_INCREMENT,
  `routine_name` varchar(255) NOT NULL,
  `habit_count` int DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `routines`
--

LOCK TABLES `routines` WRITE;
/*!40000 ALTER TABLE `routines` DISABLE KEYS */;
/*!40000 ALTER TABLE `routines` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `skill_en`
--

DROP TABLE IF EXISTS `skill_en`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `skill_en` (
  `id` int NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `field` varchar(45) DEFAULT NULL,
  `level` varchar(45) DEFAULT NULL,
  `time_learn` int DEFAULT NULL,
  `time_recall` int DEFAULT NULL,
  `time_test` int DEFAULT NULL,
  `mission_learn` int DEFAULT NULL,
  `mission_recall` int DEFAULT NULL,
  `mission_test` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `skill_en`
--

LOCK TABLES `skill_en` WRITE;
/*!40000 ALTER TABLE `skill_en` DISABLE KEYS */;
INSERT INTO `skill_en` VALUES (101,'communication','softs','average',0,0,0,0,0,0),(102,'delegation','softs','average',0,0,0,0,0,0),(103,'public','softs','average',0,0,0,0,0,0),(104,'sales','softs','average',0,0,0,0,0,0),(201,'commerce','busi','average',0,0,0,0,0,0);
/*!40000 ALTER TABLE `skill_en` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `skill_sh`
--

DROP TABLE IF EXISTS `skill_sh`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `skill_sh` (
  `id` int NOT NULL,
  `name` varchar(30) DEFAULT NULL,
  `field` varchar(30) DEFAULT NULL,
  `level` varchar(30) DEFAULT NULL,
  `time_learn` int DEFAULT NULL,
  `time_recall` int DEFAULT NULL,
  `time_test` int DEFAULT NULL,
  `mission_learn` int DEFAULT NULL,
  `mission_recall` int DEFAULT NULL,
  `mission_test` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `skill_sh`
--

LOCK TABLES `skill_sh` WRITE;
/*!40000 ALTER TABLE `skill_sh` DISABLE KEYS */;
INSERT INTO `skill_sh` VALUES (102,'pooja','atma','average',0,0,0,0,0,0),(103,'improvement','atma','average',0,0,0,0,0,0),(302,'shield','body','average',0,0,0,0,0,0);
/*!40000 ALTER TABLE `skill_sh` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `skill_tg`
--

DROP TABLE IF EXISTS `skill_tg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `skill_tg` (
  `id` int NOT NULL,
  `name` varchar(30) DEFAULT NULL,
  `field` varchar(30) DEFAULT NULL,
  `level` varchar(30) DEFAULT NULL,
  `time_learn` int DEFAULT NULL,
  `time_recall` int DEFAULT NULL,
  `time_test` int DEFAULT NULL,
  `mission_learn` int DEFAULT NULL,
  `mission_recall` int DEFAULT NULL,
  `mission_test` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `skill_tg`
--

LOCK TABLES `skill_tg` WRITE;
/*!40000 ALTER TABLE `skill_tg` DISABLE KEYS */;
INSERT INTO `skill_tg` VALUES (102,'python','lang','average',0,0,0,0,0,0),(103,'java','lang','average',0,0,0,0,0,0),(104,'javascript','lang','average',0,0,0,0,0,0),(105,'html','lang','average',0,0,0,0,0,0),(106,'css','lang','average',0,0,0,0,0,0),(107,'php','lang','average',0,0,0,0,0,0),(108,'ruby','lang','average',0,0,0,0,0,0),(109,'c++','lang','average',0,0,0,0,0,0),(110,'dart','lang','average',0,0,0,0,0,0),(111,'c#','lang','average',0,0,0,0,0,0),(112,'rust','lang','average',0,0,0,0,0,0),(202,'algorithms','dsa','average',0,0,0,0,0,0),(203,'data structures','dsa','average',0,0,0,0,0,0),(302,'computer systems','sub','average',0,0,0,0,0,0),(303,'embedded systems','sub','average',0,0,0,0,0,0),(304,'computer networks','sub','average',0,0,0,0,0,0),(305,'operating systems','sub','average',0,0,0,0,0,0),(306,'database systems','sub','average',0,0,0,0,0,0),(307,'software principles','sub','average',0,0,0,0,0,0),(308,'computer graphics','sub','average',0,0,0,0,0,0),(309,'1','sub','average',0,0,0,0,0,0),(310,'computer cryptography','sub','average',0,0,0,0,0,0),(311,'system design','sub','average',0,0,0,0,0,0),(402,'linux os','tech','average',0,0,0,0,0,0),(403,'cloud computing','tech','average',0,0,0,0,0,0),(404,'artificial intelligence','tech','average',0,0,0,0,0,0),(405,'blockchain','tech','average',0,0,0,0,0,0),(406,'iot','tech','average',0,0,0,0,0,0),(407,'data science','tech','average',0,0,0,0,0,0),(408,'visual reality','tech','average',0,0,0,0,0,0),(409,'nosql db','tech','average',0,0,0,0,0,0),(410,'sql db','tech','average',0,0,0,0,0,0),(502,'cloud tools','tools','average',0,0,0,0,0,0),(503,'ide','tools','average',0,0,0,0,0,0),(504,'version control','tools','average',0,0,0,0,0,0),(505,'build tools','tools','average',0,0,0,0,0,0),(506,'ci cd tools','tools','average',0,0,0,0,0,0),(507,'container tools','tools','average',0,0,0,0,0,0),(508,'orchestration tools','tools','average',0,0,0,0,0,0),(509,'text editor','tools','average',0,0,0,0,0,0),(510,'collaboration tools','tools','average',0,0,0,0,0,0),(511,'project management tools','tools','average',0,0,0,0,0,0),(512,'documentation tools','tools','average',0,0,0,0,0,0),(513,'monitoring tools','tools','average',0,0,0,0,0,0),(514,'testing tools','tools','average',0,0,0,0,0,0),(515,'designing tools','tools','average',0,0,0,0,0,0),(602,'apps','build','average',0,0,0,0,0,0),(603,'web','build','average',0,0,0,0,0,0),(604,'software','build','average',0,0,0,0,0,0);
/*!40000 ALTER TABLE `skill_tg` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-31 22:29:34
