# Adam Merille
# Written for Udacity Intro To Relational Databases, tournament project
# Last Updated: June 30, 1017

import psycopg2
import bleach


def connect(database_name="tournament"):
    """
    Connect to the PostgreSQL database.
    Returns a database connection and cursor.
    """
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("Could not connect to database.")


def deleteMatches():
    """Remove all the match records from the database."""
    db, cur = connect()

    query = "DELETE FROM matches;"
    cur.execute(query)

    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db, cur = connect()

    query = "DELETE FROM players;"
    cur.execute(query)

    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db, cur = connect()

    query = "SELECT COUNT(*) FROM players;"
    cur.execute(query)
    player_count = cur.fetchone()[0]

    db.close()
    return player_count


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    db, cur = connect()

    query = """INSERT INTO players(name)
                VALUES(%s);"""
    parameter = (bleach.clean(name),)
    cur.execute(query, parameter)

    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db, cur = connect()

    cur.execute("SELECT * FROM standings;")
    rows = cur.fetchall()

    db.close()
    return rows


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db, cur = connect()

    query = """INSERT INTO matches(winner_id, loser_id)
                VALUES(%s, %s);"""
    parameter = (winner, loser)
    cur.execute(query, parameter)

    db.commit()
    db.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    # pull out data and split into two interleaving halves
    ranked_players = [(player[0], player[1]) for player in playerStandings()]
    left = ranked_players[::2]
    right = ranked_players[1::2]

    # create list of tuples with each player's tuple
    zipped_pairs = zip(left, right)

    # flatten paired tuples together
    pairings = [sum(pair, ()) for pair in zipped_pairs]

    return pairings
