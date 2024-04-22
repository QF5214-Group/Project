CREATE DATABASE IF NOT EXISTS `dwd`;

USE `dwd`;

CREATE TABLE IF NOT EXISTS `dwd_news_df` (
  `news_id` decimal(11,0) PRIMARY KEY,
  `date` date,
  `news_title` varchar(300) BINARY,
  `news_url` varchar(300) BINARY,
  `news_domain` varchar(100) BINARY,
  `news_language` varchar(100) BINARY,
  `news_country` varchar(100) BINARY,
  `news_title_emotion` double,
  `news_title_subjectivity` double
);

CREATE TABLE IF NOT EXISTS `dwd_market_df` (
  `date` date PRIMARY KEY,
  `btc_price` decimal(9,4),
  `btc_volume` decimal(16,4),
  `eth_price` decimal(9,4),
  `eth_volume` decimal(16,4),
  `cpi` decimal(6,3),
  `employment_nonfarm` int,
  `population` int,
  `employment_nonfarm_ratio` double,
  `ffr` decimal(5,4),
  `sofr` decimal(5,4)
);

CREATE TABLE IF NOT EXISTS `dwd_talk_comments_df` (
  `talk_comment_id` decimal(12,0) PRIMARY KEY,
  `date` date,
  `talk_subject_id` varchar(300) BINARY,
  `talk_user_id` varchar(100) BINARY,
  `talk_comment` text BINARY,
  `talk_comment_emotion` double
);

CREATE TABLE IF NOT EXISTS `dwd_talk_subjects_df` (
  `talk_subject_id` varchar(300) BINARY PRIMARY KEY,
  `date` date,
  `talk_subject_replies` int,
  `talk_subject_views` int,
  `talk_subject_emotion` double,
  `talk_subject_subjectivity` double
);

CREATE TABLE IF NOT EXISTS `dwd_talk_users_df` (
  `talk_user_id` varchar(100) BINARY PRIMARY KEY,
  `talk_user_activity` int,
  `talk_user_merit` int
);

ALTER TABLE `dwd_news_df` ADD FOREIGN KEY (`date`) REFERENCES `dwd_market_df` (`date`);

ALTER TABLE `dwd_talk_comments_df` ADD FOREIGN KEY (`date`) REFERENCES `dwd_market_df` (`date`);

ALTER TABLE `dwd_talk_subjects_df` ADD FOREIGN KEY (`date`) REFERENCES `dwd_market_df` (`date`);

ALTER TABLE `dwd_talk_comments_df` ADD FOREIGN KEY (`talk_subject_id`) REFERENCES `dwd_talk_subjects_df` (`talk_subject_id`);

ALTER TABLE `dwd_talk_comments_df` ADD FOREIGN KEY (`talk_user_id`) REFERENCES `dwd_talk_users_df` (`talk_user_id`);

