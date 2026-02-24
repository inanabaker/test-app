CREATE EXTENSION IF NOT EXISTS postgis;

CREATE TABLE IF NOT EXISTS inanas_data (
    id SERIAL PRIMARY KEY,
    text text,
    geom geometry(Point,25833)
);

CREATE INDEX IF NOT EXISTS idx_messages_geometry ON inanas_data USING gist (geom);