import os
import sys

import psycopg2 as dbapi2


INIT_STATEMENTS = [
                        """
                        CREATE TABLE IF NOT EXISTS  Teams
                        (
                                ID SERIAL PRIMARY KEY,
                                Teamname VARCHAR(30) NOT NULL
                                
                        )
                        """,
                        
                        """
                        CREATE TABLE IF NOT EXISTS  Stadium
                        (
                                ID SERIAL PRIMARY KEY,
                                Team_ID INTEGER NOT NULL REFERENCES Teams (ID),
                                Stadiumname VARCHAR(30) NOT NULL
                        )
                        """,

                        """
                        CREATE TABLE IF NOT EXISTS  Referee
                        (
                                ID SERIAL PRIMARY KEY,
                                RefereeName VARCHAR(30),
                                TotalMatch INTEGER,
                                TotalRedCard INTEGER,
                                TotalYellowCard INTEGER
                        )
                        """,
                        """
                        CREATE TABLE IF NOT EXISTS  Standings
                        (
                                ID SERIAL PRIMARY KEY,
                                TeamID INTEGER NOT NULL REFERENCES Teams (ID),
                                Played INTEGER NOT NULL,
                                Won INTEGER NOT NULL,
                                Drawn INTEGER NOT NULL,
                                Lost INTEGER NOT NULL,
                                Goals_for INTEGER NOT NULL,
                                Goals_against INTEGER NOT NULL,
                                Goals_difference INTEGER NOT NULL,
                                Points INTEGER NOT NULL
                        )
                        """,

                         """
                        CREATE TABLE IF NOT EXISTS  Fixtures
                        (
                                ID SERIAL PRIMARY KEY,
                                HomeTeam INTEGER NOT NULL REFERENCES Teams (ID),
                                AwayTeam INTEGER NOT NULL REFERENCES Teams (ID),
                                Week INTEGER NOT NULL,
                                StadiumID INTEGER REFERENCES Stadium (ID),
                                RefereeID INTEGER  REFERENCES Referee (ID)
                        )
                        """,
                        """
                        ALTER TABLE Player ADD COLUMN IF NOT EXISTS PlayerAge INTEGER;
                        ALTER TABLE Player ADD COLUMN IF NOT EXISTS PlayerNationalty VARCHAR(30) NOT NULL;
                        ALTER TABLE Player ADD COLUMN IF NOT EXISTS PlayerHeight INTEGER NOT NULL;
                        ALTER TABLE Player ADD COLUMN IF NOT EXISTS TeamID INTEGER NOT NULL REFERENCES Teams (ID);
                                
                        CREATE TABLE IF NOT EXISTS  Player
                        (
                                ID SERIAL PRIMARY KEY,
                                PlayerName VARCHAR(30) NOT NULL,
                                PlayerAge INTEGER NOT NULL,
                                PlayerNationalty VARCHAR(30) NOT NULL,
                                PlayerHeight INTEGER NOT NULL,
                                TeamID INTEGER NOT NULL REFERENCES Teams (ID)
                        )
                        """,
			
			"""CREATE TABLE IF NOT EXISTS  Assist
			(
				ID serial NOT NULL,
				PlayerID integer REFERENCES Player (ID),
				MatchID integer  REFERENCES Matches (ID),
				PRIMARY KEY (ID)
			)""",
			
			""" 
			CREATE TABLE IF NOT EXISTS ADMINS
			(
				UserName VARCHAR(10) NOT NULL,
				ID serial ,
				UserPassword VARCHAR(16) NOT NULL,
				PRIMARY KEY (ID)
			)
			""",
			
			""" 
			CREATE TABLE IF NOT EXISTS  Goal
			(
				ID serial,
				PlayerID integer REFERENCES Player (ID),
				MatchID integer REFERENCES Matches (ID),
				PRIMARY KEY (ID)
			) 
			""",
			
			
			"""
			CREATE TABLE IF NOT EXISTS  Statistic
			(
				ID serial,
				MatchID integer NOT NULL  REFERENCES Matches (ID),
				HScore integer DEFAULT 0,
				HPossesion integer DEFAULT 0,
				HCorner integer DEFAULT 0,
				HInjure integer DEFAULT 0,
				HFoul integer DEFAULT 0,
				HOffside integer DEFAULT 0,
				HShot integer DEFAULT 0,
				HShotOnTarget integer DEFAULT 0,
				HShotAccuracy integer DEFAULT 0,
				HPassAccuracy integer DEFAULT 0,
				AScore integer DEFAULT 0,
				APossesion integer DEFAULT 0,
				ACorner integer DEFAULT 0,
				AInjure integer DEFAULT 0,
				AFoul integer DEFAULT 0,
				AOffside integer DEFAULT 0,
				AShot integer DEFAULT 0,
				AShotOnTarget integer DEFAULT 0,
				AShotAccuracy integer DEFAULT 0,
				APassAccuracy integer DEFAULT 0,
				Referee_UserName VARCHAR(30),
				PRIMARY KEY (ID)
			)
			""",

                        """
                        CREATE TABLE IF NOT EXISTS  Manager
                        (
                                ID SERIAL PRIMARY KEY,
                                Name VARCHAR(30) NOT NULL,
                                Age INTEGER NOT NULL,
                                TeamID INTEGER NOT NULL REFERENCES Teams (ID)
                                      
                        )
                        """
                
                        
                        
                        
			
			
]


def initialize(url):
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        for statement in INIT_STATEMENTS:
            cursor.execute(statement)
        cursor.close()


if __name__ == "__main__":
    url = "postgres://ydsnhphm:afmHtP2dhNoOfJQA7f_aX7YaaF9GMKWP@salt.db.elephantsql.com:5432/ydsnhphm"
    if url is None:
        print("Usage: DATABASE_URL=url python dbinit.py", file=sys.stderr)
        sys.exit(1)
    initialize(url)
