-- Create table users

DROP TABLE IF NOT EXISTS users;
CREATE TABLE users (
	id INT AUTO_INCREMENT NOT NULL,
	email VARCHAR(255) NOT NULL,
	name VARCHAR(255),
	country CHAR(2) NOT NULL DEFAULT 'US' CHECK (country IN ('US', 'CO', 'TN'))
	PRIMARY KEY (id),
	UNIQUE (email)
	);
