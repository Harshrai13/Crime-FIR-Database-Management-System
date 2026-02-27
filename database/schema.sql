CREATE DATABASE crime_management;
USE crime_management;

CREATE TABLE Officers (
    officer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    rank VARCHAR(50),
    station VARCHAR(100)
);

CREATE TABLE Complainant (
    complainant_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(15),
    address TEXT
);

CREATE TABLE Crime_Category (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(100) NOT NULL
);

CREATE TABLE FIR (
    fir_id INT PRIMARY KEY AUTO_INCREMENT,
    complainant_id INT,
    officer_id INT,
    category_id INT,
    description TEXT,
    status VARCHAR(50) DEFAULT 'Pending',
    date_filed DATE,
    FOREIGN KEY (complainant_id) REFERENCES Complainant(complainant_id),
    FOREIGN KEY (officer_id) REFERENCES Officers(officer_id),
    FOREIGN KEY (category_id) REFERENCES Crime_Category(category_id)
);
