CREATE EXTENSION IF NOT EXISTS postgis;

CREATE TABLE IF NOT EXISTS inanas_data (
    id SERIAL PRIMARY KEY,
    text text,
    geom geometry(Point,25833)
);

CREATE INDEX IF NOT EXISTS idx_messages_geometry ON inanas_data USING gist (geom);

INSERT INTO inanas_data (text, geom)
VALUES (
  'Test data',
  ST_SetSRID(ST_GeomFromText('POINT(0 0)'), 25833)
);
