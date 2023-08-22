CREATE TABLE Oseba (
    ID SERIAL PRIMARY KEY,
    Spol CHAR(1) CHECK (Spol IN ('Z', 'M')),
    PriimekInIme VARCHAR(100)
    -- Add more columns as needed
);


ALTER TABLE Oseba
ADD LR FLOAT,
ADD "3.3km" TIME WITHOUT TIME ZONE,
ADD "6.6km" TIME WITHOUT TIME ZONE,
ADD "10km" TIME WITHOUT TIME ZONE;

ALTER TABLE Oseba
ADD "3km" TIME WITHOUT TIME ZONE,
ADD kraj TEXT,
ADD leto INT,
ADD razdalja FLOAT;

INSERT INTO Oseba (spol, PriimekInIme, LR, "3.3km", "6.6km", "10km", kraj, leto, razdalja)
SELECT 'M', "Priimek in Ime", "LR", "K1"::TIME, "K2"::TIME,
       CASE WHEN "Rezultat" = 'DNF' THEN NULL ELSE "Rezultat"::TIME END,
       'kranj', '2019' , '10'
FROM "2019_kranj_10_M";

INSERT INTO Oseba (spol, PriimekInIme, LR, "3.3km", "6.6km", "10km", kraj, leto, razdalja)
SELECT 'Z', "Priimek in Ime", "LR",
       CASE WHEN "K1" = '&nbsp;' THEN NULL ELSE "K1"::TIME END,
       CASE WHEN "K2" = '&nbsp;' THEN NULL ELSE "K2"::TIME END,
       CASE WHEN "Rezultat" = 'DNF' THEN NULL ELSE "Rezultat"::TIME END,
       'kranj', '2019', '10'
FROM "2019_kranj_10_Z";

INSERT INTO Oseba (spol, PriimekInIme, LR, "3.3km", "6.6km", "10km", kraj, leto, razdalja)
SELECT 'M', "Priimek in Ime", "LR", "3.3km"::TIME, "6.6km"::TIME, "Rezultat"::TIME,
        'kranj', '2022', '10'
FROM "2022_kranj_10_M";

INSERT INTO Oseba (spol, PriimekInIme, LR, "3.3km", "6.6km", "10km", kraj, leto, razdalja)
SELECT 'Z', "Priimek in Ime", "LR", "3.3km"::TIME, "6.6km"::TIME, "Rezultat"::TIME,
'kranj', '2022', '10'
FROM "2022_kranj_10_Z";

INSERT INTO Oseba (spol, PriimekInIme, LR, "3km", kraj, leto, razdalja)
SELECT 'M', "Priimek in Ime", "LR",
        CASE WHEN "Rezultat" = 'DNF' THEN NULL ELSE "Rezultat"::TIME END,
        'kranj', '2019', '3'
FROM "2019_kranj_3_M";

INSERT INTO Oseba (spol, PriimekInIme, LR, "3km", kraj, leto, razdalja)
SELECT 'Z', "Priimek in Ime", "LR",
        CASE WHEN "Rezultat" = 'DNF' THEN NULL ELSE "Rezultat"::TIME END,
        'kranj', '2019', '3'
FROM "2019_kranj_3_Z";

ALTER TABLE Oseba
ADD "6km" TIME WITHOUT TIME ZONE;

INSERT INTO Oseba (spol, PriimekInIme, LR, "6km", "10km", kraj, leto, razdalja)
SELECT 'M', "Priimek in ime", "LR", 
        CASE WHEN "6km" = '&nbsp;' THEN NULL ELSE "6km"::TIME END,
        CASE WHEN "Rezultat" = 'DNF' THEN NULL ELSE "Rezultat"::TIME END,
        'kraski', '2019', '10'
FROM "2019_kraski_10_M";

ALTER TABLE Oseba
ADD "17km" TIME WITHOUT TIME ZONE,
ADD "21km" TIME WITHOUT TIME ZONE;

INSERT INTO Oseba (spol, PriimekInIme, LR, "10km", "17km", "21km", kraj, leto, razdalja)
SELECT 'M', "Priimek in ime", "LR", 
        CASE WHEN "10km" = '&nbsp;' THEN NULL ELSE "10km"::TIME END,
        CASE WHEN "17km" = '&nbsp;' THEN NULL ELSE "17km"::TIME END,
        CASE WHEN "Rezultat" = 'DNF' THEN NULL ELSE "Rezultat"::TIME END,
        'kraski', '2019', '21'
FROM "2019_kraski_21_M";

ALTER TABLE Oseba
ADD "5km" TIME WITHOUT TIME ZONE;

INSERT INTO Oseba (spol, PriimekInIme,"5km", "10km", kraj, leto, razdalja)
SELECT 'M', "Priimek in ime", 
        CASE WHEN "5km" = '&nbsp;' THEN NULL ELSE "5km"::TIME END,
        CASE WHEN "Rezultat" = 'DNF' THEN NULL ELSE "Rezultat"::TIME END,
        'ljubljanski', '2021', '10'
FROM "2021_ljubljanski_10_M";

ALTER TABLE Oseba
ADD "15km" TIME WITHOUT TIME ZONE,
ADD "20km" TIME WITHOUT TIME ZONE;

INSERT INTO Oseba (spol, PriimekInIme,"5km", "10km", "15km", "20km", "21km", kraj, leto, razdalja)
SELECT 'M', "Priimek in ime", 
        CASE WHEN "5km" = '&nbsp;' THEN NULL ELSE "5km"::TIME END,
        CASE WHEN "10km" = '&nbsp;' THEN NULL ELSE "10km"::TIME END,
        CASE WHEN "15km" = '&nbsp;' THEN NULL ELSE "15km"::TIME END,
        CASE WHEN "20km" = '&nbsp;' THEN NULL ELSE "20km"::TIME END,
        CASE WHEN "Rezultat" = 'DNF' THEN NULL ELSE "Rezultat"::TIME END,
        'ljubljanski', '2021', '21'
FROM "2021_ljubljanski_21_M";

INSERT INTO Oseba (spol, PriimekInIme,"5km", "10km", "15km", "20km", "21km", kraj, leto, razdalja)
SELECT 'Z', "Priimek in ime", 
        CASE WHEN "5km" = '&nbsp;' THEN NULL ELSE "5km"::TIME END,
        CASE WHEN "10km" = '&nbsp;' THEN NULL ELSE "10km"::TIME END,
        CASE WHEN "15km" = '&nbsp;' THEN NULL ELSE "15km"::TIME END,
        CASE WHEN "20km" = '&nbsp;' THEN NULL ELSE "20km"::TIME END,
        CASE WHEN "Rezultat" = 'DNF' THEN NULL ELSE "Rezultat"::TIME END,
        'ljubljanski', '2021', '21'
FROM "2021_ljubljanski_21_Z";

ALTER TABLE Oseba
ADD "21.1km" TIME WITHOUT TIME ZONE,
ADD "25km" TIME WITHOUT TIME ZONE,
ADD "30km" TIME WITHOUT TIME ZONE,
ADD "35km" TIME WITHOUT TIME ZONE,
ADD "40km" TIME WITHOUT TIME ZONE,
ADD "42km" TIME WITHOUT TIME ZONE;

INSERT INTO Oseba (spol, PriimekInIme,"5km", "10km", "15km", "20km", "21.1km", "25km", "30km", "35km", "40km", "42km", kraj, leto, razdalja)
SELECT 'M', "Priimek in ime", 
        CASE WHEN "5km" = '&nbsp;' THEN NULL ELSE "5km"::TIME END,
        CASE WHEN "10km" = '&nbsp;' THEN NULL ELSE "10km"::TIME END,
        CASE WHEN "15km" = '&nbsp;' THEN NULL ELSE "15km"::TIME END,
        CASE WHEN "20km" = '&nbsp;' THEN NULL ELSE "20km"::TIME END,
        CASE WHEN "21.1km" = '&nbsp;' THEN NULL ELSE "21.1km"::TIME END,
        CASE WHEN "25km" = '&nbsp;' THEN NULL ELSE "25km"::TIME END,
        CASE WHEN "30km" = '&nbsp;' THEN NULL ELSE "30km"::TIME END,
        CASE WHEN "35km" = '&nbsp;' THEN NULL ELSE "35km"::TIME END,
        CASE WHEN "40km" = '&nbsp;' THEN NULL ELSE "40km"::TIME END,
        CASE WHEN "Rezultat" = 'DNF' THEN NULL ELSE "Rezultat"::TIME END,
        'ljubljanski', '2021', '42'
FROM "2021_ljubljanski_42_M";

INSERT INTO Oseba (spol, PriimekInIme,"5km", "10km", "15km", "20km", "21.1km", "25km", "30km", "35km", "40km", "42km", kraj, leto, razdalja)
SELECT 'Z', "Priimek in ime", 
        CASE WHEN "5km" = '&nbsp;' THEN NULL ELSE "5km"::TIME END,
        CASE WHEN "10km" = '&nbsp;' THEN NULL ELSE "10km"::TIME END,
        CASE WHEN "15km" = '&nbsp;' THEN NULL ELSE "15km"::TIME END,
        CASE WHEN "20km" = '&nbsp;' THEN NULL ELSE "20km"::TIME END,
        CASE WHEN "21.1km" = '&nbsp;' THEN NULL ELSE "21.1km"::TIME END,
        CASE WHEN "25km" = '&nbsp;' THEN NULL ELSE "25km"::TIME END,
        CASE WHEN "30km" = '&nbsp;' THEN NULL ELSE "30km"::TIME END,
        CASE WHEN "35km" = '&nbsp;' THEN NULL ELSE "35km"::TIME END,
        CASE WHEN "40km" = '&nbsp;' THEN NULL ELSE "40km"::TIME END,
        CASE WHEN "Rezultat" = 'DNF' THEN NULL ELSE "Rezultat"::TIME END,
        'ljubljanski', '2021', '42'
FROM "2021_ljubljanski_42_Z";

INSERT INTO Oseba (spol, PriimekInIme, LR, "3km", kraj, leto, razdalja)
SELECT 'M', "Priimek in Ime", "LR",
        CASE WHEN "Rezultat" = 'DNF' THEN NULL ELSE "Rezultat"::TIME END,
        'kranj', '2022', '3'
FROM "2022_kranj_3_M";

INSERT INTO Oseba (spol, PriimekInIme, LR, "3km", kraj, leto, razdalja)
SELECT 'Z', "Priimek in Ime", "LR",
        CASE WHEN "Rezultat" = 'DNF' THEN NULL ELSE "Rezultat"::TIME END,
        'kranj', '2022', '3'
FROM "2022_kranj_3_Z";

INSERT INTO Oseba (spol, PriimekInIme, LR, "6km", "10km", kraj, leto, razdalja)
SELECT 'Z', "Priimek in ime", "LR", 
        CASE WHEN "6km" = '&nbsp;' THEN NULL ELSE "6km"::TIME END,
        CASE WHEN "Rezultat" = 'DNF' THEN NULL ELSE "Rezultat"::TIME END,
        'kraski', '2022', '10'
FROM "2022_kraski_10_Z";

INSERT INTO Oseba (spol, PriimekInIme, LR, "10km", "17km", "21km", kraj, leto, razdalja)
SELECT 'M', "Priimek in ime", "LR", 
        CASE WHEN "10km" = '&nbsp;' THEN NULL ELSE "10km"::TIME END,
        CASE WHEN "17km" = '&nbsp;' THEN NULL ELSE "17km"::TIME END,
        CASE WHEN "Rezultat" = 'DNF' THEN NULL ELSE "Rezultat"::TIME END,
        'kraski', '2022', '21'
FROM "2022_kraski_21_M";

INSERT INTO Oseba (spol, PriimekInIme, LR, "10km", "17km", "21km", kraj, leto, razdalja)
SELECT 'Z', "Priimek in ime", "LR", 
        CASE WHEN "10km" = '&nbsp;' THEN NULL ELSE "10km"::TIME END,
        CASE WHEN "17km" = '&nbsp;' THEN NULL ELSE "17km"::TIME END,
        CASE WHEN "Rezultat" = 'DNF' THEN NULL ELSE "Rezultat"::TIME END,
        'kraski', '2022', '21'
FROM "2022_kraski_21_Z";

ALTER TABLE Oseba
ADD "2km" TIME WITHOUT TIME ZONE;

INSERT INTO Oseba (spol, PriimekInIme, LR, "2km", "5km", kraj, leto, razdalja)
SELECT 'M', "Priimek in ime", "LR", 
        CASE WHEN "2km" = '&nbsp;' THEN NULL ELSE "2km"::TIME END,
        CASE WHEN "Rezultat" = 'DNF' THEN NULL ELSE "Rezultat"::TIME END,
        'kraski', '2022', '5'
FROM "2022_kraski_5_M";

INSERT INTO Oseba (spol, PriimekInIme, LR, "2km", "5km", kraj, leto, razdalja)
SELECT 'Z', "Priimek in ime", "LR", 
        CASE WHEN "2km" = '&nbsp;' THEN NULL ELSE "2km"::TIME END,
        CASE WHEN "Rezultat" = 'DNF' THEN NULL ELSE "Rezultat"::TIME END,
        'kraski', '2022', '5'
FROM "2022_kraski_5_Z";

GRANT all
    ON oseba
    TO matejg;
 GRANT all
    ON utezi
    TO matejg;