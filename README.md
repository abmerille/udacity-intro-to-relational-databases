Swiss Tournament Project
====

Project built for Udacity's Intro To Relational Databases course.
Created for use with [Full Stack Developer VM](https://github.com/udacity/fullstack-nanodegree-vm)

How To Use
------------
See the included requirements.txt for what libraries and python version used.

To set up the database and tables: `psql -f tournament.sql`

To run the tests: `python tournament_test.py`

FUNCTIONS
__________
    connect(database_name='tournament')
        Connect to the PostgreSQL database.
        Returns a database connection and cursor.

    countPlayers()
        Returns the number of players currently registered.

    deleteMatches()
        Remove all the match records from the database.

    deletePlayers()
        Remove all the player records from the database.

    playerStandings()
        Returns a list of the players and their win records, sorted by wins.

        The first entry in the list should be the player in first place, or a
        player tied for first place if there is currently a tie.

        Returns:
          A list of tuples, each of which contains (id, name, wins, matches):
            id: the player's unique id (assigned by the database)
            wins: the number of matches the player has won
            matches: the number of matches the player has played

   registerPlayer(name)
       Adds a player to the tournament database.

       The database assigns a unique serial id number for the player.  (This
       should be handled by your SQL database schema, not in your Python code.)

       Args:
         name: the player's full name (need not be unique).

   reportMatch(winner, loser)
       Records the outcome of a single match between two players.

       Args:
         winner:  the id number of the player who won
         loser:  the id number of the player who lost

   swissPairings()
       Returns a list of pairs of players for the next round of a match.

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
