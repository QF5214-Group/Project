CREATE DATABASE IF NOT EXISTS `dws`;

USE `dws`;

CREATE TABLE IF NOT EXISTS `dws_news_300d` (
  `date` date PRIMARY KEY,
  `news_id_daily_count` int,
  `news_title_emotion` double,
  `news_title_subjectivity` double
);

CREATE TABLE IF NOT EXISTS `dws_market_300d` (
  `date` date PRIMARY KEY,
  `btc_price` decimal(9,4),
  `btc_volume` decimal(16,4),
  `eth_price` decimal(9,4),
  `cpi` decimal(6,3),
  `employment_nonfarm_ratio` double,
  `ffr` decimal(5,4)
);

CREATE TABLE IF NOT EXISTS `dws_talk_comments_300d` (
  `date` date PRIMARY KEY,
  `talk_comment_id_daily_count` int,  
  `talk_comment_emotion_daily_mean` double,
  `talk_comment_emotion_daily_std` double
);

CREATE TABLE IF NOT EXISTS `dws_talk_subjects_300d` (
  `date` date PRIMARY KEY,
  `talk_subject_id_daily_count` int,
  `talk_subject_emotion_daily_mean` double,
  `talk_subject_subjectivity_daily_mean` double
);

