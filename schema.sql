CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    name TEXT,
    password TEXT,
    golf_club INTEGER REFERENCES golf_clubs,
);
CREATE TABLE golf_clubs (
    id SERIAL PRIMARY KEY,
    name TEXT,
    address TEXT,
);
CREATE TABLE rounds (
    id SERIAL PRIMARY KEY,
    shots INTEGER,
    player INTEGER REFERENCES users
);
