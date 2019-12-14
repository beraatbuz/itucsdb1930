import os
import sys

import psycopg2 as dbapi2


INIT_STATEMENTS = [
                        """
                        CREATE TABLE IF NOT EXISTS  Teams
                        (
                                ID SERIAL PRIMARY KEY,
                                Teamname VARCHAR(30) NOT NULL,
                                NickName VARCHAR(30),
                                ShortName VARCHAR(30) NOT NULL,
                                FoundationDate VARCHAR(30),	
                                ManagerID INTEGER REFERENCES Manager (ID) ON DELETE cascade,
                                Location VARCHAR(50)
                        )
                        """,
                        
                        """

                        CREATE TABLE IF NOT EXISTS  Stadium
                        (
                                ID SERIAL PRIMARY KEY,
                                Team_ID INTEGER NOT NULL REFERENCES Teams (ID) ON DELETE cascade,
                                Stadiumname VARCHAR(30) NOT NULL,
                                Capacity INTEGER NOT NULL,
                                Built INTEGER NOT NULL,
                                PitchSize VARCHAR(10) NOT NULL,
                                Surface VARCHAR(10) NOT NULL
                        )
                        """,

                        

                        """                 
                        CREATE TABLE IF NOT EXISTS  Referee
                        (
                                ID SERIAL PRIMARY KEY,
                                RefereeName VARCHAR(30),
                                Age INTEGER,
                                TotalMatch INTEGER,
                                TotalRedCard INTEGER,
                                TotalYellowCard INTEGER
                        )
                        """,
                        """
                        CREATE TABLE IF NOT EXISTS  Standings
                        (
                                ID SERIAL PRIMARY KEY,
                                TeamID INTEGER NOT NULL REFERENCES Teams (ID) ON DELETE cascade,
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
                                HomeTeam INTEGER NOT NULL REFERENCES Teams (ID) ON DELETE cascade,
                                AwayTeam INTEGER NOT NULL REFERENCES Teams (ID) ON DELETE cascade,
                                Refereeid INTEGER REFERENCES Referee (ID),
                                HomeScore VARCHAR(2) DEFAULT '-',
                                AwayScore VARCHAR(2) DEFAULT '-',
                                Week INTEGER NOT NULL,
                                MatchDate VARCHAR(30),
                                Time VARCHAR(30),
                                Status VARCHAR(10) NOT NULL
                        )
                        """,
                        """
                                
                        CREATE TABLE IF NOT EXISTS  Player
                        (
                                ID SERIAL PRIMARY KEY,
                                PlayerName VARCHAR(30) NOT NULL,
                                PlayerAge INTEGER NOT NULL,
                                Position VARCHAR(30),
                                PlayerNationalty VARCHAR(30) NOT NULL,
                                PlayerHeight INTEGER NOT NULL,
                                PlaceOfBirth VARCHAR(30) NOT NULL,
                                TeamID INTEGER NOT NULL REFERENCES Teams (ID) ON DELETE cascade
                        )
                        """,
			
			"""

                        CREATE TABLE IF NOT EXISTS  Assist
			(
				ID serial NOT NULL,
				PlayerID integer REFERENCES Player (ID) ON DELETE cascade,
				MatchID integer  REFERENCES Fixtures (ID) ON DELETE cascade,
                                Minute INTEGER NOT NULL,
                                LastTouch VARCHAR(10) NOT NULL,
                                Format VARCHAR(15) NOT NULL,
                                GoldenAssist VARCHAR(3) NOT NULL,
                                StadiumHA VARCHAR(5) NOT NULL,
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
				PlayerID integer NOT NULL REFERENCES Player (ID) ON DELETE cascade,
				MatchID integer NOT NULL REFERENCES Fixtures (ID) ON DELETE cascade,
                                Minute INTEGER NOT NULL,
				PRIMARY KEY (ID)
			) 
			""",
			
			
			"""
			CREATE TABLE IF NOT EXISTS  Statistic
			(
				ID serial,
				MatchID integer NOT NULL  REFERENCES Fixtures (ID) ON DELETE cascade,
				HPossesion integer DEFAULT 0,
				HCorner integer DEFAULT 0,
				HFoul integer DEFAULT 0,
				HOffside integer DEFAULT 0,
				HShot integer DEFAULT 0,
				HShotOnTarget integer DEFAULT 0,
				HShotAccuracy integer DEFAULT 0,
				HPassAccuracy integer DEFAULT 0,
				APossesion integer DEFAULT 0,
				ACorner integer DEFAULT 0,
				AFoul integer DEFAULT 0,
				AOffside integer DEFAULT 0,
				AShot integer DEFAULT 0,
				AShotOnTarget integer DEFAULT 0,
				AShotAccuracy integer DEFAULT 0,
				APassAccuracy integer DEFAULT 0,
                                RefereeID integer NOT NULL REFERENCES Referee (ID),
				PRIMARY KEY (ID)
			)
			""",

                        """
			CREATE TABLE IF NOT EXISTS  MatchDetails
			(
				ID serial,
				MatchID integer NOT NULL  REFERENCES Fixtures (ID) ON DELETE cascade,
                                Detail VARCHAR(300) NOT NULL,
                                Minute integer NOT NULL,
				PRIMARY KEY (ID)
			)
			""",

                        """
  
                        CREATE TABLE IF NOT EXISTS  Manager
                        (
                                ID SERIAL PRIMARY KEY,
                                Name VARCHAR(30) NOT NULL,
                                Age INTEGER NOT NULL,
                                Nationalty VARCHAR(30) NOT NULL,
                                Height INTEGER NOT NULL,
                                PlaceOfBirth VARCHAR(30) NOT NULL,
                                teamid integer REFERENCES teams (ID) ON DELETE cascade
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
    url = os.getenv("url")
    if url is None:
        print("Usage: DATABASE_URL=url python dbinit.py", file=sys.stderr)
        sys.exit(1)
    initialize(url)
