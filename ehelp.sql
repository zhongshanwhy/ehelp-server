/*
DROP TABLE IF EXISTS `alluser`;
CREATE TABLE `alluser` (
  `user_id` varchar(45) NOT NULL,
  `password` varchar(45) DEFAULT NULL,
  `phone` varchar(45) DEFAULT NULL,
  `job` varchar(45) DEFAULT NULL,
  `age` int(11) DEFAULT 0,
  `gender` varchar(10) DEFAULT NULL,
  `health_state` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
)


CREATE TABLE `question` (
  `question_id` varchar(45) NOT NULL,
  `question_content` text(500) DEFAULT NULL,
  `question_type` int(11) NOT NULL,
  `question_time` datetime DEFAULT NULL,
  PRIMARY KEY (`question_id`)
)


CREATE TABLE answer (
  `answer_id` varchar(45) NOT NULL,
  `question_id` varchar(45) NOT NULL,
  `answer_content` text(500) DEFAULT NULL,
  `answer_type` int(11) NOT NULL,
  `answer_time` datetime DEFAULT NULL,
  PRIMARY KEY (`question_id`),
  CONSTRAINT `question_answer_tuple_fk` FOREIGN KEY (`question_id`) REFERENCES `question` (`question_id`) ON DELETE CASCADE ON UPDATE CASCADE
)
*/

CREATE TABLE `friendlist` (
  `host_name` varchar(45) NOT NULL,
  `guest_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`host_name`),
  CONSTRAINT friend_host_fk FOREIGN KEY (`host_name`) REFERENCES alluser (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT friend_guest_fk FOREIGN KEY (`guest_name`) REFERENCES alluser (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
)
/**/

CREATE TABLE `bank` (
  `bank_id` int(11) NOT NULL AUTO_INCREMENT,
  `bank_name` varchar(45) NOT NULL,
  `grade` int(11) DEFAULT NULL,
  `coin` int(11) DEFAULT 20,
  PRIMARY KEY (`bank_id`)
  CONSTRAINT bank_name_fk FOREIGN KEY (`bank_name`) REFERENCES alluser (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
)

CREATE TABLE `sign` (
  `sign_id` int(11) NOT NULL AUTO_INCREMENT,
  `sign_name` varchar(45) NOT NULL,
  `sign_history` int(11) DEFAULT 0,
  `sign_time` date DEFAULT NULL,
  PRIMARY KEY (`sign_id`),
  CONSTRAINT sign_name_fk FOREIGN KEY (`sign_name`) REFERENCES alluser (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
)