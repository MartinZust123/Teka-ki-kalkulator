CREATE TABLE Teki (
    ID SERIAL PRIMARY KEY,
    user_username VARCHAR(100),
    FOREIGN KEY (user_username) REFERENCES Uporabnik(username),
    ImeInPriimek VARCHAR(100),
    Razdalja INT,
    Cas INT
);

INSERT INTO Teki (user_username, ImeInPriimek, Razdalja, Cas)
VALUES
    ('jane_doe','Jane Doe', 10, 40),
    ('john_smith', 'John Smith', 15, 60),
    ('alice_wonderland', 'Alice Wonderland', 8, 35);

GRANT all
    ON Uporabnik
    TO matejg;
 GRANT all
    ON Uporabnik
    TO matejg;