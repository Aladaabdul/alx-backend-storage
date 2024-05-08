-- Create table users

CREATE TABLE IF NOT EXISTS users(
	id INT AUTO_INCREMENT NOT NULL,
	email VARCHAR(255) NOT NULL,
	name VARCHAR(255),
	country SET('US', 'CO', 'TN') DEFAULT 'US'
	PRIMARY KEY (id),
	UNIQUE (email)
	);
