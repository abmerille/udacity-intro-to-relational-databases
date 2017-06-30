-- Adam Merille
-- Written for Udacity Intro To Relational Databases
-- Last Updated: June 30, 1017
-- Command line usage 'psql -f tournament.sql'

-- Clear out tournament database if it exists and create new one
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament

-- Create Players table
CREATE TABLE players (
  id SERIAL PRIMARY KEY,
  name TEXT
);

-- Create matches table, make sure winner_id and loser_id are never the same
CREATE TABLE matches (
  id SERIAL PRIMARY KEY,
  winner_id INTEGER REFERENCES players(id) ON DELETE CASCADE,
  loser_id INTEGER REFERENCES players(id) ON DELETE CASCADE,
  CHECK (winner_id <> loser_id)
);

-- Create winner_count view to generate number of wins per player
CREATE VIEW winner_count AS
  SELECT players.id, players.name, COUNT(matches.id) AS wins
  FROM players LEFT JOIN matches ON players.id = matches.winner_id
  GROUP BY players.id;

-- Create matches_count view to generate total matches played per player
CREATE VIEW matches_count AS
  SELECT players.id, players.name, COUNT(matches) AS total_matches
  FROM players LEFT JOIN matches
  ON players.id = matches.winner_id OR players.id = matches.loser_id
  GROUP BY players.id;

-- Create standings view to combine winner_count and matches_count
CREATE OR REPLACE VIEW standings AS
  SELECT winner_count.id, winner_count.name, winner_count.wins,
    matches_count.total_matches
  FROM winner_count JOIN matches_count ON winner_count.id = matches_count.id
  ORDER BY winner_count.wins DESC;
