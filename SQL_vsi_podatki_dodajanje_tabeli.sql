INSERT INTO vsi_podatki (spol, priimek_ime, LR, km2, km3_3, km5, km6_6, km10, km17, km21, km21_1, km25, km30, km35, km40_1, km40_2, km42)
SELECT 'Z' AS spol, "Priimek in Ime" AS priimek_ime, "LR" AS LR, NULL AS km2, CAST("3.3km" AS TIME) AS km3_3, NULL AS km5, CAST("6.6km" AS TIME) km6_6, CAST("Rezultat" AS TIME) AS km10, NULL AS km17, NULL AS km21, NULL AS km21_1, NULL AS km25, NULL AS km30, NULL AS km35, NULL AS km40_1, NULL AS km40_2, NULL AS km42
FROM "2022_kranj_10_Z";

INSERT INTO vsi_podatki (spol, priimek_ime, LR, km2, km3_3, km5, km6_6, km10, km17, km21, km21_1, km25, km30, km35, km40_1, km40_2, km42)
SELECT 'Z' AS spol, "Priimek in Ime" AS priimek_ime, "LR" AS LR, NULL AS km2, CASE WHEN "K1" = 'DNF' THEN NULL WHEN "K1" = '&nbsp;' THEN NULL ELSE CAST("K1" AS TIME) END AS km3_3, NULL AS km5, CASE WHEN "K2" = 'DNF' THEN NULL WHEN "K2" = '&nbsp;' THEN NULL ELSE CAST("K2" AS TIME) END AS km6_6, CASE WHEN "Rezultat" = 'DNF' THEN NULL ELSE CAST("Rezultat" AS TIME) END AS km10, NULL AS km17, NULL AS km21, NULL AS km21_1, NULL AS km25, NULL AS km30, NULL AS km35, NULL AS km40_1, NULL AS km40_2, NULL AS km42
FROM "2019_kranj_10_Z";

INSERT INTO vsi_podatki (spol, priimek_ime, LR, km2, km3_3, km5, km6_6, km10, km17, km21, km21_1, km25, km30, km35, km40_1, km40_2, km42)
SELECT 'M' AS spol, "Priimek in Ime" AS priimek_ime, "LR" AS LR, NULL AS km2, CAST("3.3km" AS TIME) AS km3_3, NULL AS km5, CAST("6.6km" AS TIME) km6_6, CAST("Rezultat" AS TIME) AS km10, NULL AS km17, NULL AS km21, NULL AS km21_1, NULL AS km25, NULL AS km30, NULL AS km35, NULL AS km40_1, NULL AS km40_2, NULL AS km42
FROM "2022_kranj_10_M";

INSERT INTO vsi_podatki (spol, priimek_ime, LR, km2, km3_3, km5, km6_6, km10, km17, km21, km21_1, km25, km30, km35, km40_1, km40_2, km42)
SELECT 'M' AS spol, "Priimek in Ime" AS priimek_ime, "LR" AS LR, NULL AS km2, CAST("K1" AS TIME) AS km3_3, NULL AS km5, CAST("K2" AS TIME) km6_6, CASE WHEN "Rezultat" = 'DNF' THEN NULL ELSE CAST("Rezultat" AS TIME) END AS km10, NULL AS km17, NULL AS km21, NULL AS km21_1, NULL AS km25, NULL AS km30, NULL AS km35, NULL AS km40_1, NULL AS km40_2, NULL AS km42
FROM "2019_kranj_10_M";

INSERT INTO vsi_podatki (spol, priimek_ime, LR, km3)
SELECT 'M' AS spol, "Priimek in Ime" AS priimek_ime, "LR" AS LR, CASE WHEN "Rezultat" = 'DNF' THEN NULL ELSE CAST("Rezultat" AS TIME) END AS km3
FROM "2019_kranj_3_M";

INSERT INTO vsi_podatki (spol, priimek_ime, LR, km3)
SELECT 'Z' AS spol, "Priimek in Ime" AS priimek_ime, "LR" AS LR, CASE WHEN "Rezultat" = 'DNF' THEN NULL ELSE CAST("Rezultat" AS TIME) END AS km3
FROM "2019_kranj_3_Z";

INSERT INTO vsi_podatki (spol, priimek_ime, LR, km3)
SELECT 'M' AS spol, "Priimek in Ime" AS priimek_ime, "LR" AS LR, CASE WHEN "Rezultat" = 'DNF' THEN NULL ELSE CAST("Rezultat" AS TIME) END AS km3
FROM "2022_kranj_3_M";

INSERT INTO vsi_podatki (spol, priimek_ime, LR, km3)
SELECT 'Z' AS spol, "Priimek in Ime" AS priimek_ime, "LR" AS LR, CASE WHEN "Rezultat" = 'DNF' THEN NULL ELSE CAST("Rezultat" AS TIME) END AS km3
FROM "2022_kranj_3_Z";

ALTER TABLE "vsi_podatki"
ADD "km6" TIME;

INSERT INTO vsi_podatki (spol, priimek_ime, LR, km6, km10)
SELECT 'M' AS spol, "Priimek in ime" AS priimek_ime, "LR" AS LR, CASE WHEN "6km" = 'DNF' THEN NULL WHEN "6km" = '&nbsp;' THEN NULL ELSE CAST("6km" AS TIME) END AS km6, CASE WHEN "Rezultat" = 'DNF' THEN NULL WHEN "Rezultat" = '&nbsp;' THEN NULL ELSE CAST("Rezultat" AS TIME) END AS km10
FROM "2019_kraski_10_M";


INSERT INTO vsi_podatki (spol, priimek_ime, LR, km6, km10)
SELECT 'M' AS spol, "Priimek in ime" AS priimek_ime, "LR" AS LR, CASE WHEN "6km" = 'DNF' THEN NULL WHEN "6km" = '&nbsp;' THEN NULL ELSE CAST("6km" AS TIME) END AS km6, CASE WHEN "Rezultat" = 'DNF' THEN NULL WHEN "Rezultat" = '&nbsp;' THEN NULL ELSE CAST("Rezultat" AS TIME) END AS km10
FROM "2022_kraski_10_Z";

INSERT INTO vsi_podatki (spol, priimek_ime, LR, km10, km17, km21)
SELECT 'M' AS spol, "Priimek in ime" AS priimek_ime, "LR" AS LR, CASE WHEN "10km" = 'DNF' THEN NULL WHEN "10km" = '&nbsp;' THEN NULL ELSE CAST("10km" AS TIME) END AS km10, CASE WHEN "17km" = 'DNF' THEN NULL WHEN "17km" = '&nbsp;' THEN NULL ELSE CAST("17km" AS TIME) END AS km17, CASE WHEN "Rezultat" = 'DNF' THEN NULL WHEN "Rezultat" = '&nbsp;' THEN NULL ELSE CAST("Rezultat" AS TIME) END AS km21
FROM "2019_kraski_21_M";

INSERT INTO vsi_podatki (spol, priimek_ime, LR, km10, km17, km21)
SELECT 'M' AS spol, "Priimek in ime" AS priimek_ime, "LR" AS LR, CASE WHEN "10km" = 'DNF' THEN NULL WHEN "10km" = '&nbsp;' THEN NULL ELSE CAST("10km" AS TIME) END AS km10, CASE WHEN "17km" = 'DNF' THEN NULL WHEN "17km" = '&nbsp;' THEN NULL ELSE CAST("17km" AS TIME) END AS km17, CASE WHEN "Rezultat" = 'DNF' THEN NULL WHEN "Rezultat" = '&nbsp;' THEN NULL ELSE CAST("Rezultat" AS TIME) END AS km21
FROM "2022_kraski_21_M";

INSERT INTO vsi_podatki (spol, priimek_ime, LR, km10, km17, km21)
SELECT 'Z' AS spol, "Priimek in ime" AS priimek_ime, "LR" AS LR, CASE WHEN "10km" = 'DNF' THEN NULL WHEN "10km" = '&nbsp;' THEN NULL ELSE CAST("10km" AS TIME) END AS km10, CASE WHEN "17km" = 'DNF' THEN NULL WHEN "17km" = '&nbsp;' THEN NULL ELSE CAST("17km" AS TIME) END AS km17, CASE WHEN "Rezultat" = 'DNF' THEN NULL WHEN "Rezultat" = '&nbsp;' THEN NULL ELSE CAST("Rezultat" AS TIME) END AS km21
FROM "2022_kraski_21_Z";

INSERT INTO vsi_podatki (spol, priimek_ime, km5, km10)
SELECT 'M' AS spol, "Priimek in ime" AS priimek_ime, CASE WHEN "5km" = 'DNF' THEN NULL WHEN "5km" = '&nbsp;' THEN NULL ELSE CAST("5km" AS TIME) END AS km5, CASE WHEN "Rezultat" = 'DNF' THEN NULL WHEN "Rezultat" = '&nbsp;' THEN NULL ELSE CAST("Rezultat" AS TIME) END AS km10
FROM "2021_ljubljanski_10_M";

ALTER TABLE "vsi_podatki"
ADD "km15" TIME;

ALTER TABLE "vsi_podatki"
ADD "km20" TIME;

INSERT INTO vsi_podatki (spol, priimek_ime, km5, km10, km15, km20, km21)
SELECT 'M' AS spol, "Priimek in ime" AS priimek_ime, CASE WHEN "5km" = 'DNF' THEN NULL WHEN "5km" = '&nbsp;' THEN NULL ELSE CAST("5km" AS TIME) END AS km5, CASE WHEN "10km" = 'DNF' THEN NULL WHEN "10km" = '&nbsp;' THEN NULL ELSE CAST("10km" AS TIME) END AS km10, CASE WHEN "15km" = 'DNF' THEN NULL WHEN "15km" = '&nbsp;' THEN NULL ELSE CAST("15km" AS TIME) END AS km15, CASE WHEN "20km" = 'DNF' THEN NULL WHEN "20km" = '&nbsp;' THEN NULL ELSE CAST("20km" AS TIME) END AS km20, CASE WHEN "Rezultat" = 'DNF' THEN NULL WHEN "Rezultat" = '&nbsp;' THEN NULL ELSE CAST("Rezultat" AS TIME) END AS km21
FROM "2021_ljubljanski_21_M";

INSERT INTO vsi_podatki (spol, priimek_ime, km5, km10, km15, km20, km21)
SELECT 'Z' AS spol, "Priimek in ime" AS priimek_ime, CASE WHEN "5km" = 'DNF' THEN NULL WHEN "5km" = '&nbsp;' THEN NULL ELSE CAST("5km" AS TIME) END AS km5, CASE WHEN "10km" = 'DNF' THEN NULL WHEN "10km" = '&nbsp;' THEN NULL ELSE CAST("10km" AS TIME) END AS km10, CASE WHEN "15km" = 'DNF' THEN NULL WHEN "15km" = '&nbsp;' THEN NULL ELSE CAST("15km" AS TIME) END AS km15, CASE WHEN "20km" = 'DNF' THEN NULL WHEN "20km" = '&nbsp;' THEN NULL ELSE CAST("20km" AS TIME) END AS km20, CASE WHEN "Rezultat" = 'DNF' THEN NULL WHEN "Rezultat" = '&nbsp;' THEN NULL ELSE CAST("Rezultat" AS TIME) END AS km21
FROM "2021_ljubljanski_21_Z";

ALTER TABLE "vsi_podatki"
ADD "km40" TIME;

INSERT INTO vsi_podatki (spol, priimek_ime, km5, km10, km15, km20, km21_1, km25, km30, km35, km40, km42)
SELECT 'M' AS spol, "Priimek in ime" AS priimek_ime, CASE WHEN "5km" = 'DNF' THEN NULL WHEN "5km" = '&nbsp;' THEN NULL ELSE CAST("5km" AS TIME) END AS km5, CASE WHEN "10km" = 'DNF' THEN NULL WHEN "10km" = '&nbsp;' THEN NULL ELSE CAST("10km" AS TIME) END AS km10, CASE WHEN "15km" = 'DNF' THEN NULL WHEN "15km" = '&nbsp;' THEN NULL ELSE CAST("15km" AS TIME) END AS km15, CASE WHEN "20km" = 'DNF' THEN NULL WHEN "20km" = '&nbsp;' THEN NULL ELSE CAST("20km" AS TIME) END AS km20, CASE WHEN "21.1km" = 'DNF' THEN NULL WHEN "21.1km" = '&nbsp;' THEN NULL ELSE CAST("21.1km" AS TIME) END AS km21_1, CASE WHEN "25km" = 'DNF' THEN NULL WHEN "25km" = '&nbsp;' THEN NULL ELSE CAST("25km" AS TIME) END AS km25, CASE WHEN "30km" = 'DNF' THEN NULL WHEN "30km" = '&nbsp;' THEN NULL ELSE CAST("30km" AS TIME) END AS km30, CASE WHEN "35km" = 'DNF' THEN NULL WHEN "35km" = '&nbsp;' THEN NULL ELSE CAST("35km" AS TIME) END AS km35, CASE WHEN "40km" = 'DNF' THEN NULL WHEN "40km" = '&nbsp;' THEN NULL ELSE CAST("40km" AS TIME) END AS km40, CASE WHEN "Rezultat" = 'DNF' THEN NULL WHEN "Rezultat" = '&nbsp;' THEN NULL ELSE CAST("Rezultat" AS TIME) END AS km42
FROM "2021_ljubljanski_42_M";

INSERT INTO vsi_podatki (spol, priimek_ime, km5, km10, km15, km20, km21_1, km25, km30, km35, km40, km42)
SELECT 'Z' AS spol, "Priimek in ime" AS priimek_ime, CASE WHEN "5km" = 'DNF' THEN NULL WHEN "5km" = '&nbsp;' THEN NULL ELSE CAST("5km" AS TIME) END AS km5, CASE WHEN "10km" = 'DNF' THEN NULL WHEN "10km" = '&nbsp;' THEN NULL ELSE CAST("10km" AS TIME) END AS km10, CASE WHEN "15km" = 'DNF' THEN NULL WHEN "15km" = '&nbsp;' THEN NULL ELSE CAST("15km" AS TIME) END AS km15, CASE WHEN "20km" = 'DNF' THEN NULL WHEN "20km" = '&nbsp;' THEN NULL ELSE CAST("20km" AS TIME) END AS km20, CASE WHEN "21.1km" = 'DNF' THEN NULL WHEN "21.1km" = '&nbsp;' THEN NULL ELSE CAST("21.1km" AS TIME) END AS km21_1, CASE WHEN "25km" = 'DNF' THEN NULL WHEN "25km" = '&nbsp;' THEN NULL ELSE CAST("25km" AS TIME) END AS km25, CASE WHEN "30km" = 'DNF' THEN NULL WHEN "30km" = '&nbsp;' THEN NULL ELSE CAST("30km" AS TIME) END AS km30, CASE WHEN "35km" = 'DNF' THEN NULL WHEN "35km" = '&nbsp;' THEN NULL ELSE CAST("35km" AS TIME) END AS km35, CASE WHEN "40km" = 'DNF' THEN NULL WHEN "40km" = '&nbsp;' THEN NULL ELSE CAST("40km" AS TIME) END AS km40, CASE WHEN "Rezultat" = 'DNF' THEN NULL WHEN "Rezultat" = '&nbsp;' THEN NULL ELSE CAST("Rezultat" AS TIME) END AS km42
FROM "2021_ljubljanski_42_Z";

INSERT INTO vsi_podatki (spol, priimek_ime, LR, km2, km5)
SELECT 'M' AS spol, "Priimek in ime" AS priimek_ime, "LR" AS LR, CASE WHEN "2km" = 'DNF' THEN NULL WHEN "2km" = '&nbsp;' THEN NULL ELSE CAST("2km" AS TIME) END AS km2, CASE WHEN "Rezultat" = 'DNF' THEN NULL WHEN "Rezultat" = '&nbsp;' THEN NULL ELSE CAST("Rezultat" AS TIME) END AS km5
FROM "2022_kraski_5_M";

INSERT INTO vsi_podatki (spol, priimek_ime, LR, km2, km5)
SELECT 'Z' AS spol, "Priimek in ime" AS priimek_ime, "LR" AS LR, CASE WHEN "2km" = 'DNF' THEN NULL WHEN "2km" = '&nbsp;' THEN NULL ELSE CAST("2km" AS TIME) END AS km2, CASE WHEN "Rezultat" = 'DNF' THEN NULL WHEN "Rezultat" = '&nbsp;' THEN NULL ELSE CAST("Rezultat" AS TIME) END AS km5
FROM "2022_kraski_5_Z";

ALTER TABLE "vsi_podatki"
DROP "km40_1";

ALTER TABLE "vsi_podatki"
DROP "km40_2";

DELETE FROM vsi_podatki;

SELECT column_name
FROM information_schema.columns
WHERE table_name = '2019_kraski_10_M';

SELECT COLUMN_NAME, DATA_TYPE 
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE TABLE_NAME = '2019_kranj_10_Z'

