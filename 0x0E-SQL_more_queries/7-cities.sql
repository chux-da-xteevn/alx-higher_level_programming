-- this query to create the DB called hbtn_0d_usa and table called cities with unique attributes and not null
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;

USE `hbtn_0d_usa`

CREATE TABLE IF NOT EXISTS `cities`(
    `id` INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `state_id`INT NOT NULL,
    `name` VARCHAR(256) NOT NULL,
    FOREIGN KEY(state_id) REFERENCES states(id)
);

DROP Table cities;
