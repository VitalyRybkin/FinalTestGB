-- MySQL dump 10.13  Distrib 8.0.33, for macos11.7 (x86_64)
--
-- Host: localhost    Database: HumanFriends
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `animal_commands`
--

DROP TABLE IF EXISTS `animal_commands`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `animal_commands` (
  `id` tinyint unsigned NOT NULL AUTO_INCREMENT,
  `animal_id` tinyint unsigned NOT NULL,
  `animal_command_id` tinyint unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `animal_commands_id_index` (`id`),
  KEY `animal_commands_animal_command_id_foreign` (`animal_command_id`),
  KEY `animal_commands_animal_id_foreign` (`animal_id`),
  CONSTRAINT `animal_commands_animal_command_id_foreign` FOREIGN KEY (`animal_command_id`) REFERENCES `animal_commands_list` (`id`),
  CONSTRAINT `animal_commands_animal_id_foreign` FOREIGN KEY (`animal_id`) REFERENCES `animals` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `animal_commands`
--

LOCK TABLES `animal_commands` WRITE;
/*!40000 ALTER TABLE `animal_commands` DISABLE KEYS */;
INSERT INTO `animal_commands` VALUES (1,1,5),(2,2,5),(4,5,4),(5,6,1),(6,6,2),(7,6,3),(8,6,4),(9,6,5);
/*!40000 ALTER TABLE `animal_commands` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `animal_commands_list`
--

DROP TABLE IF EXISTS `animal_commands_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `animal_commands_list` (
  `id` tinyint unsigned NOT NULL AUTO_INCREMENT,
  `command_name` varchar(15) NOT NULL,
  `command_description` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `animal_commands_list_id_index` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `animal_commands_list`
--

LOCK TABLES `animal_commands_list` WRITE;
/*!40000 ALTER TABLE `animal_commands_list` DISABLE KEYS */;
INSERT INTO `animal_commands_list` VALUES (1,'sit!','animal sits by the owner'),(2,'down!','animal lay down by the owner'),(3,'searech!','animal starts search something'),(4,'voice!','animal makes its nature noise'),(5,'place!','animal gets to its place');
/*!40000 ALTER TABLE `animal_commands_list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `animal_group`
--

DROP TABLE IF EXISTS `animal_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `animal_group` (
  `id` tinyint unsigned NOT NULL AUTO_INCREMENT,
  `animal_group_name` varchar(15) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `animal_group_id_index` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `animal_group`
--

LOCK TABLES `animal_group` WRITE;
/*!40000 ALTER TABLE `animal_group` DISABLE KEYS */;
INSERT INTO `animal_group` VALUES (1,'pet'),(2,'packanimal'),(3,'wild');
/*!40000 ALTER TABLE `animal_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `animal_type`
--

DROP TABLE IF EXISTS `animal_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `animal_type` (
  `id` tinyint unsigned NOT NULL AUTO_INCREMENT,
  `animal_type_name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `animal_type_id_index` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `animal_type`
--

LOCK TABLES `animal_type` WRITE;
/*!40000 ALTER TABLE `animal_type` DISABLE KEYS */;
INSERT INTO `animal_type` VALUES (1,'horse'),(2,'camel'),(3,'donkey'),(4,'cat'),(5,'dog'),(6,'hamster');
/*!40000 ALTER TABLE `animal_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `animals`
--

DROP TABLE IF EXISTS `animals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `animals` (
  `id` tinyint unsigned NOT NULL AUTO_INCREMENT,
  `animal_type_id` tinyint unsigned NOT NULL,
  `animal_name` varchar(20) NOT NULL,
  `birthdate` date NOT NULL,
  `animal_group_id` tinyint unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `animals_id_index` (`id`),
  KEY `animals_animal_type_id_foreign` (`animal_type_id`),
  KEY `animals_animal_group_id_foreign` (`animal_group_id`),
  CONSTRAINT `animals_animal_group_id_foreign` FOREIGN KEY (`animal_group_id`) REFERENCES `animal_group` (`id`),
  CONSTRAINT `animals_animal_type_id_foreign` FOREIGN KEY (`animal_type_id`) REFERENCES `animal_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `animals`
--

LOCK TABLES `animals` WRITE;
/*!40000 ALTER TABLE `animals` DISABLE KEYS */;
INSERT INTO `animals` VALUES (1,1,'Johnny','2022-03-04',2),(2,1,'Benny','2022-03-04',2),(4,3,'Stupi-Do','2017-11-22',2),(5,4,'Meaw','2021-01-12',1),(6,5,'Snoopy','2021-06-30',1),(7,6,'Puffy','2022-03-31',1);
/*!40000 ALTER TABLE `animals` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `young_animals`
--

DROP TABLE IF EXISTS `young_animals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `young_animals` (
  `id` tinyint unsigned NOT NULL DEFAULT '0',
  `animal_name` varchar(20) NOT NULL,
  `birthdate` date NOT NULL,
  `age` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `young_animals`
--

LOCK TABLES `young_animals` WRITE;
/*!40000 ALTER TABLE `young_animals` DISABLE KEYS */;
INSERT INTO `young_animals` VALUES (1,'Johnny','2022-03-04',18),(2,'Benny','2022-03-04',18),(5,'Meaw','2021-01-12',32),(6,'Snoopy','2021-06-30',26),(7,'Puffy','2022-03-31',17);
/*!40000 ALTER TABLE `young_animals` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-29  9:01:07
