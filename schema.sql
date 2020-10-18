CREATE TABLE golf_clubs (
  club_name TEXT PRIMARY KEY,
  address TEXT
);
CREATE TABLE users (
  username TEXT PRIMARY KEY,
  real_name TEXT,
  password TEXT NOT NULL,
  club TEXT REFERENCES golf_clubs,
  admin BOOLEAN DEFAULT false
);
CREATE TABLE golf_courses (
  id SERIAL PRIMARY KEY,
  club TEXT REFERENCES golf_clubs,
  name TEXT NOT NULL,
  expired BOOLEAN DEFAULT false
);
CREATE TABLE holes (
  id SERIAL PRIMARY KEY,
  course_id INTEGER REFERENCES golf_courses,
  hole INTEGER NOT NULL,
  par INTEGER NOT NULL,
  length INTEGER NOT NULL
);
CREATE TABLE rounds (
  id SERIAL PRIMARY KEY,
  player TEXT REFERENCES users ON DELETE CASCADE,
  course INTEGER REFERENCES golf_courses ON DELETE CASCADE,
  handicap BOOLEAN NOT NULL,
  date_played DATE NOT NULL
);
CREATE TABLE scores (
  id SERIAL PRIMARY KEY,
  round_id INTEGER REFERENCES rounds ON DELETE CASCADE,
  hole_id INTEGER REFERENCES holes ON DELETE CASCADE,
  strokes INTEGER NOT NULL,
  putts INTEGER NOT NULL
);
CREATE TABLE friendships (
  id SERIAL PRIMARY KEY,
  user_id TEXT REFERENCES users ON DELETE CASCADE,
  friend_id TEXT REFERENCES users ON DELETE CASCADE
);
