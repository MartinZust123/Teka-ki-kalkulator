CREATE TABLE Uporabnik (
    ID SERIAL PRIMARY KEY,
    Spol CHAR(1) CHECK (Spol IN ('Z', 'M')),
    username VARCHAR(100) UNIQUE,
    ImeInPriimek VARCHAR(100),
    starost INT,
    geslo TEXT
);

INSERT INTO Uporabnik (Spol, username, ImeInPriimek, starost, geslo)
VALUES
    ('Z', 'jane_doe', 'Jane Doe', 25, 'hashed_password_1'),
    ('M', 'john_smith', 'John Smith', 30, 'hashed_password_2'),
    ('Z', 'alice_wonderland', 'Alice Wonderland', 28, 'hashed_password_3');


GRANT all
    ON Uporabnik
    TO matejg;
 GRANT all
    ON Uporabnik
    TO matejg;