/*
    Title: whatabook.init.sql
    Author: Professor Krasso
    Date: 16 July 2020
    Description: WhatABook database initialization script.
*/

-- drop test user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- drop contstraints if they exist
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop tables if they exist
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

/*
    Create table(s)
*/

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

/*
    insert store record 
*/
INSERT INTO store(locale)
    VALUES('1000 Galvin Rd S, Bellevue, NE 68005');
/*
    insert book records 
*/
INSERT INTO book(book_name, author, details)
    VALUES('The History of Tom Jones, a Foundling', 'Henry Fielding', 'A classic novel that tells the story of a young man seeking his identity and love in 18th century England');

INSERT INTO book(book_name, author, details)
    VALUES('Pride and Prejudice', 'Jane Austen', 'A romantic novel that portrays the Bennet sisters search for love and happiness in early 19th-century England');

INSERT INTO book(book_name, author, details)
    VALUES('The Red and the Black', 'Stendhal', 'A landmark novel of French literature that follows Julien Sorels rise to power in post-revolutionary France, with psychological depth and social criticism.');

INSERT INTO book(book_name, author, details)
    VALUES('Le Père Goriot', 'Honoré de Balzac', 'French literature that tells the story of a father who sacrifices everything for his ungrateful daughters and a young man in love with one of them, with realistic portrayal of Parisian society.');

INSERT INTO book(book_name, author, details)
    VALUES('David Copperfield', 'Charles Dickens', 'A novel that follows a young mans struggles to overcome obstacles and find love in 19th-century England');

INSERT INTO book(book_name, author, details)
    VALUES("Madame Bovary", 'Gustave Flaubert', 'French literature that portrays Emma Bovarys dissatisfaction with life and escape in romantic fantasies and extramarital affairs, with psychological insight and satirical commentary on bourgeois life.');

INSERT INTO book(book_name, author, details)
    VALUES('Moby-Dick', 'Herman Melville', 'A classic American novel that follows a sailors quest to hunt and kill the white whale Moby Dick, with complex characters and philosophical themes.');

INSERT INTO book(book_name, author, details)
    VALUES('Wuthering Heights', 'Emily Brontë', 'A Gothic novel that portrays the doomed love between Heathcliff and Catherine Earnshaw, with supernatural elements and passionate characters.');

INSERT INTO book(book_name, author, details)
    VALUES('The Brothers Karamazov', 'Dostoevsky', 'A masterpiece of Russian literature that follows three brothers and their fathers search for truth, justice, and faith in 19th-century Russia, with psychological depth and philosophical themes.');

/*
    insert users
*/ 
INSERT INTO user(first_name, last_name) 
    VALUES('Thomas', 'Morris');

INSERT INTO user(first_name, last_name)
    VALUES('Garry', 'Rice');

INSERT INTO user(first_name, last_name)
    VALUES('Bob', 'Frost');

/*
    insert wishlist records 
*/
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Thomas'), 
        (SELECT book_id FROM book WHERE book_name = 'The Brothers Karamazov')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Garry'),
        (SELECT book_id FROM book WHERE book_name = 'Wuthering Heights')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Bob'),
        (SELECT book_id FROM book WHERE book_name = 'The History of Tom Jones, a Foundling')
        );