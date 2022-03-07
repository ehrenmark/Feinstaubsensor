CREATE TABLE IF NOT EXISTS SDS011 (
	id INT NOT NULL PRIMARY KEY,
    sensor_id INT NOT NULL,
    location INT,
    lon DECIMAL(10, 3),
    lat DECIMAL(10, 3),
    p1 DECIMAL(10, 2),
    dur_p1 DECIMAL,
    ratio_p1 DECIMAL,
    p2 DECIMAL(10, 2),
    dur_p2 DECIMAL,
    ratio_p2 DECIMAL,
    messzeitpunkt DATETIME
);

CREATE TABLE IF NOT EXISTS DHT22 (
	id INT NOT NULL PRIMARY KEY,
    sensor_id INT,
    location INT,
    lon DECIMAL(10, 3),
    lat DECIMAL(10, 3),
    humidity DECIMAL(10, 2),
    temperature DECIMAL(10, 2),
    messzeitpunkt DATETIME
);