CREATE DATABASE IF NOT EXISTS `ads`;

USE `ads`;

CREATE TABLE IF NOT EXISTS `ads_news_300d` (
  `date` date PRIMARY KEY,
  `news_id_daily_count_quantile` int,
  `news_title_emotion_quantile` double,
  `news_title_subjectivity_quantile` double
);

CREATE TABLE IF NOT EXISTS `ads_market_300d` (
  `date` date PRIMARY KEY,
  `btc_price_quantile` decimal(9,4),
  `btc_volume_quantile` decimal(16,4),
  `eth_price_quantile` decimal(9,4),
  `cpi_quantile` decimal(6,3),
  `employment_nonfarm_ratio_quantile` double,
  `ffr_quantile` decimal(5,4)
);

CREATE TABLE IF NOT EXISTS `ads_talk_comments_300d` (
  `date` date PRIMARY KEY,
  `talk_comment_id_daily_count_quantile` int,  
  `talk_comment_emotion_daily_mean_quantile` double,
  `talk_comment_emotion_daily_std_quantile` double
);

CREATE TABLE IF NOT EXISTS `ads_talk_subjects_300d` (
  `date` date PRIMARY KEY,
  `talk_subject_id_daily_count_quantile` int,
  `talk_subject_emotion_daily_mean_quantile` double,
  `talk_subject_subjectivity_daily_mean_quantile` double
);

