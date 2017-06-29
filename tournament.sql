-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

players_table = """create table players (
                    id serial PRIMARY KEY,
                    name text
                  );"""

matches_table = """create table matches (
                    id serial PRIMARY KEY,
                    winner_id integer references players,
                    loser_id integer references players
                  );"""

total_wins = """create view win_table as
                select players.id, count(matches.id) as wins
                from players left join matches on players.id = matches.winner_id
                group by players.id;"""
