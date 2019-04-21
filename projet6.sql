-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le :  ven. 19 avr. 2019 à 15:31
-- Version du serveur :  5.7.24
-- Version de PHP :  7.2.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `projet6`
--

-- --------------------------------------------------------

--
-- Structure de la table `datafromusers`
--

DROP TABLE IF EXISTS `datafromusers`;
CREATE TABLE IF NOT EXISTS `datafromusers` (
  `entryID` int(10) NOT NULL AUTO_INCREMENT,
  `warning` varchar(3) NOT NULL DEFAULT 'NO',
  `usersConcerned` varchar(20) NOT NULL,
  `sizeExceeded` varchar(30) NOT NULL,
  `Date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`entryID`)
) ENGINE=MyISAM AUTO_INCREMENT=36 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `datafromusers`
--

INSERT INTO `datafromusers` (`entryID`, `warning`, `usersConcerned`, `sizeExceeded`, `Date`) VALUES
(1, 'YES', 'TestUser', '143 Mo', '2019-02-27 15:33:18'),
(2, 'YES', 'Franz', '157 Mo', '2019-02-27 15:33:18'),
(3, 'YES', 'TestUser', '143 Mo', '2019-02-27 15:36:12'),
(4, 'YES', 'Franz', '157 Mo', '2019-02-27 15:36:12'),
(5, 'YES', 'TestUser', '143 Mo', '2019-02-27 16:55:09'),
(6, 'YES', 'Franz', '157 Mo', '2019-02-27 16:55:09'),
(7, 'YES', 'TestUser', '143 Mo', '2019-02-28 11:40:24'),
(8, 'YES', 'Franz', '157 Mo', '2019-02-28 11:40:24'),
(9, 'YES', 'TestUser', '143 Mo', '2019-02-28 11:48:15'),
(10, 'YES', 'Franz', '157 Mo', '2019-02-28 11:48:15'),
(11, 'YES', 'TestUser', '143 Mo', '2019-02-28 12:03:55'),
(12, 'YES', 'Franz', '157 Mo', '2019-02-28 12:03:55'),
(13, 'YES', 'TestUser', '143 Mo', '2019-02-28 12:10:02'),
(14, 'YES', 'Franz', '157 Mo', '2019-02-28 12:10:02'),
(15, 'YES', 'TestUser', '143 Mo', '2019-02-28 12:12:56'),
(16, 'YES', 'Franz', '157 Mo', '2019-02-28 12:12:56'),
(17, 'YES', 'TestUser', '143 Mo', '2019-02-28 12:13:44'),
(18, 'YES', 'Franz', '157 Mo', '2019-02-28 12:13:44'),
(19, 'YES', 'TestUser', '143 Mo', '2019-02-28 12:36:52'),
(20, 'YES', 'Franz', '157 Mo', '2019-02-28 12:36:52'),
(21, 'YES', 'TestUser', '143 Mo', '2019-02-28 12:36:56'),
(22, 'YES', 'Franz', '157 Mo', '2019-02-28 12:36:56'),
(23, 'YES', 'TestUser', '143 Mo', '2019-03-04 16:58:03'),
(24, 'YES', 'Franz', '157 Mo', '2019-03-04 16:58:03'),
(25, 'YES', 'TestUser', '143 Mo', '2019-03-04 16:58:07'),
(26, 'YES', 'Franz', '157 Mo', '2019-03-04 16:58:07'),
(27, 'YES', 'TestUser', '143 Mo', '2019-03-08 16:06:54'),
(28, 'YES', 'Franz', '157 Mo', '2019-03-08 16:06:54'),
(29, 'YES', 'TestUser', '143 Mo', '2019-03-08 16:07:25'),
(30, 'YES', 'Franz', '143 Mo', '2019-03-08 16:07:25'),
(31, 'YES', 'TestUser', '143 Mo', '2019-03-08 16:21:47'),
(32, 'YES', 'Franz', '143 Mo', '2019-03-08 16:21:47'),
(33, 'YES', 'TestUser', '143 Mo', '2019-03-08 16:22:03'),
(34, 'YES', 'Franz', '143 Mo', '2019-03-08 16:22:03'),
(35, 'YES', 'Franz', '3700 Mo', '2019-04-19 14:22:22');

-- --------------------------------------------------------

--
-- Structure de la table `sizesharedfolder`
--

DROP TABLE IF EXISTS `sizesharedfolder`;
CREATE TABLE IF NOT EXISTS `sizesharedfolder` (
  `ID` int(10) NOT NULL AUTO_INCREMENT,
  `Date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Size` varchar(30) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `sizesharedfolder`
--

INSERT INTO `sizesharedfolder` (`ID`, `Date`, `Size`) VALUES
(1, '2019-02-27 15:33:18', '2.30'),
(2, '2019-02-27 15:36:12', '2.30 Go'),
(3, '2019-02-27 16:55:09', '2.30 Go'),
(4, '2019-02-28 11:40:24', '2.30 Go'),
(5, '2019-02-28 11:48:15', '2.30 Go'),
(6, '2019-02-28 12:03:55', '2.30 Gb'),
(7, '2019-02-28 12:10:02', '2.30 Go'),
(8, '2019-02-28 12:12:56', '2.30 Go'),
(9, '2019-02-28 12:13:44', '2.30 Gb'),
(10, '2019-02-28 12:36:52', '2.30 Gb'),
(11, '2019-02-28 12:36:56', '2.30 Go'),
(12, '2019-03-04 16:58:03', '2.30 Go'),
(13, '2019-03-04 16:58:07', '2.30 Gb'),
(14, '2019-03-08 16:07:25', '2.29 Go'),
(15, '2019-03-08 16:21:47', '2.29 Go'),
(16, '2019-03-08 16:22:03', '2.29 Gb'),
(17, '2019-04-19 14:07:46', '0.00 Go'),
(18, '2019-04-19 14:07:51', '0.00 Gb'),
(19, '2019-04-19 14:20:46', '0.04 Go'),
(20, '2019-04-19 14:22:22', '4.70 Go'),
(21, '2019-04-19 15:08:30', '0.63 Go'),
(22, '2019-04-19 15:13:35', '0.63 Go'),
(23, '2019-04-19 15:15:28', '0.63 Go');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
