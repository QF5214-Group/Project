DROP DATABASE IF EXISTS `ods`;

CREATE DATABASE IF NOT EXISTS `ods`;

USE `ods`;

CREATE TABLE IF NOT EXISTS `ods_news_delta` (
  `news_id` int PRIMARY KEY,
  `date` date,
  `news_title` varchar(300) BINARY,
  `news_url` varchar(300) BINARY,
  `news_domain` varchar(100) BINARY,
  `news_language` varchar(100) BINARY,
  `news_country` varchar(100) BINARY,
  `news_title_emotion` double,
  `news_title_subjectivity` double
);

CREATE TABLE IF NOT EXISTS `ods_market_btc_delta` (
  `date` date PRIMARY KEY,
  `btc_price` decimal(9,4),
  `btc_volume` decimal(16,4)
);


CREATE TABLE IF NOT EXISTS `ods_market_eth_delta` (
  `date` date PRIMARY KEY,
  `eth_price` decimal(9,4),
  `eth_volume` decimal(16,4)
);


CREATE TABLE IF NOT EXISTS `ods_market_cpi_delta` (
  `date` date PRIMARY KEY,
  `cpi` decimal(6,3)
);

CREATE TABLE IF NOT EXISTS `ods_market_employment_delta` (
  `date` date PRIMARY KEY,
  `employment_nonfarm` int,
  `population` int
);

CREATE TABLE IF NOT EXISTS `ods_market_ffr_delta` (
  `date` date PRIMARY KEY,
  `ffr` decimal(5,4)
);

CREATE TABLE IF NOT EXISTS `ods_market_sofr_delta` (
  `date` date PRIMARY KEY,
  `sofr` decimal(5,4)
);

CREATE TABLE IF NOT EXISTS `ods_talk_comments_delta` (
  `talk_comment_id` int PRIMARY KEY,
  `date` date,
  `talk_subject_id` varchar(300) BINARY,
  `talk_user_id` varchar(100) BINARY,
  `talk_comment` text,
  `talk_comment_emotion` double
);

CREATE TABLE IF NOT EXISTS `ods_talk_subjects_delta` (
  `talk_subject_id` varchar(300) BINARY PRIMARY KEY,
  `date` date,
  `talk_subject_replies` int,
  `talk_subject_views` int,
  `talk_subject_emotion` double,
  `talk_subject_subjectivity` double
);

CREATE TABLE IF NOT EXISTS `ods_talk_users_delta` (
  `talk_user_id` varchar(100) BINARY PRIMARY KEY,
  `talk_user_activity` int,
  `talk_user_merit` int
);