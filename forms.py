import psycopg2 as dbapi
import os

url = os.getenv("url")

class FootballStats:

	def Team_add(self, TeamName, NickName, ShortName, FoundationDate, ManagerID,Location):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ INSERT INTO Teams(TeamName, NickName, ShortName, FoundationDate,  ManagerID,Location) VALUES(%s,%s,%s,%s,%s,%s);"""
				cursor.execute(statement,([TeamName, NickName, ShortName, FoundationDate, ManagerID,Location]))

	def Team_update(self, TeamID, TeamName, NickName, ShortName, FoundationDate, ManagerID,Location):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement="""Update Teams Set Teamname=%s, NickName=%s, ShortName=%s, FoundationDate=%s, ManagerID=%s,Location=%s  Where ID=%s;"""
				cursor.execute(statement,([TeamName, NickName, ShortName, FoundationDate, ManagerID, Location, TeamID]))
	
	def Team_delete(self, TeamID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ DELETE FROM Teams WHERE ID = %s;"""
				cursor.execute(statement,[TeamID])		

	def Stadium(self):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select Stadium.id, Teamname, StadiumName, capacity,built,pitchsize,surface,team_id FROM Stadium,teams Where Teams.id=team_id ORDER BY Teamname"""
				cursor.execute(statement)
				cursor_list=cursor.fetchall()
				return cursor_list
	
	def Stadium_add(self, TeamId, StadiumName, Capacity, Built, PitchSize, Surface):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ INSERT INTO Stadium(Team_ID,Stadiumname,Capacity,Built,PitchSize,Surface) VALUES(%s,%s,%s,%s,%s,%s);"""
				cursor.execute(statement,([TeamId, StadiumName, Capacity, Built, PitchSize, Surface]))
	
	def Stadium_delete(self,StadiumId):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement="""Delete From Stadium Where ID = %s;"""
				cursor.execute(statement,([StadiumId]))

	def Stadium_update(self, StadiumId, TeamId, StadiumName, Capacity, Built, PitchSize, Surface):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement="""Update Stadium Set Team_ID=%s, Stadiumname=%s, Capacity=%s, Built=%s, PitchSize=%s, Surface=%s Where ID=%s;"""
				cursor.execute(statement,([TeamId, StadiumName, Capacity, Built, PitchSize, Surface, StadiumId]))
				
	def Stadium_update_info(self, ID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ Select * From Stadium where ID = %s;"""
				cursor.execute(statement,([ID]))
				cursor_list=cursor.fetchall()
				return cursor_list	

	def Assist(self):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select Assist.id,Player.playername,Assist.minute,home.teamname as HomeTeam, away.teamname as AwayTeam,Assist.lasttouch,Assist.format,Assist.goldenassist,Assist.stadiumha, Player.id, HomeTeam,Awayteam,MatchID FROM Assist, Player,Teams as home, Teams as away, Fixtures 
				where Assist.playerid = Player.id and Assist.matchid = fixtures.id
				and home.id=fixtures.hometeam
				and away.id=fixtures.awayteam ORDER BY fixtures.ID"""
				cursor.execute(statement)
				cursor_list=cursor.fetchall()
				return cursor_list
			
	def Assist_add(self, PlayerId, MatchId, Minute, LastTouch, Format, GoldenAssist, StadiumHA):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ INSERT INTO Assist(PlayerId,MatchId,Minute,LastTouch,Format,GoldenAssist,StadiumHA) VALUES(%s,%s,%s,%s,%s,%s,%s);"""
				cursor.execute(statement,([PlayerId, MatchId,Minute,LastTouch,Format,GoldenAssist,StadiumHA]))

	def Assist_delete(self, AssistId):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement="""Delete From Assist Where ID = %s; """
				cursor.execute(statement,([AssistId]))

	def Assist_update(self, AssistId, PlayerId, MatchId, Minute, LastTouch, Format, GoldenAssist, StadiumHA):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement="""Update Assist Set PlayerID=%s, MatchID=%s, Minute=%s, LastTouch=%s, Format=%s,GoldenAssist=%s,StadiumHA=%s Where ID=%s;"""
				cursor.execute(statement,([PlayerId, MatchId, Minute, LastTouch, Format, GoldenAssist, StadiumHA, AssistId]))

	def Assist_update_info(self, ID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ Select * From Assist where ID = %s;"""
				cursor.execute(statement,([ID]))
				cursor_list=cursor.fetchall()
				return cursor_list

	def Detail_add(self, MatchId, Detail, Minute):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ INSERT INTO MatchDetails(MatchID, Detail, Minute) VALUES(%s,%s,%s);"""
				cursor.execute(statement,([MatchId, Detail, Minute]))

	def Detail_update(self, DetailID, MatchId,Detail ,Minute):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement="""Update MatchDetails Set MatchID=%s, Detail=%s, Minute=%s Where ID=%s;"""
				cursor.execute(statement,([MatchId,Detail ,Minute, DetailID]))

	def Detail_delete(self, ID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ DELETE FROM MatchDetails WHERE ID = %s;"""
				cursor.execute(statement,[ID])

	def Detail_update_info(self, ID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ Select * From MatchDetails where ID = %s;"""
				cursor.execute(statement,([ID]))
				cursor_list=cursor.fetchall()
				return cursor_list

	def Admins_add(self, UserName, UserPassword):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ INSERT INTO ADMINS(UserName,UserPassword) VALUES(%s,%s);"""
				cursor.execute(statement,([UserName, UserPassword]))
	
	def Goal_add(self, PlayerID, MatchID, Minute):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ INSERT INTO Goal(PlayerID, MatchID, Minute) VALUES(%s,%s,%s);"""
				cursor.execute(statement,([PlayerID, MatchID,Minute]))
	
	def Goal_update(self, GoalID, PlayerID, MatchID, Minute):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement="""Update Goal Set PlayerID=%s, MatchID=%s, Minute=%s Where ID=%s;"""
				cursor.execute(statement,([PlayerID, MatchID, Minute, GoalID]))
	
	def Goal_delete(self, GoalID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ DELETE FROM Goal WHERE ID = %s;"""
				cursor.execute(statement,[GoalID])	

	def Statistic(self):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select statistic.ID, matchid, HPossesion, HCorner, HFoul, HOffside, HShot, HShotOnTarget, HShotAccuracy, HPassAccuracy, 
APossesion, ACorner, AFoul, AOffside, AShot, AShotOnTarget, AShotAccuracy, APassAccuracy, RefereeName FROM Statistic,Referee where "RefereeID"=Referee.ID ORDER BY MatchID"""
				cursor.execute(statement)
				cursor_list=cursor.fetchall()
				return cursor_list
	
	def Statistic_add(self, MatchID, HPossesion, HCorner, HFoul, HOffside, HShot, HShotOnTarget, HShotAccuracy, HPassAccuracy, APossesion, ACorner, AFoul, AOffside, AShot, AShotOnTarget, AShotAccuracy, APassAccuracy, RefereeID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ INSERT INTO Statistic(MatchID, HPossesion, HCorner, HFoul, HOffside, HShot, HShotOnTarget, HShotAccuracy, HPassAccuracy, APossesion, ACorner, AFoul, AOffside, AShot, AShotOnTarget, AShotAccuracy, APassAccuracy, "RefereeID") VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
				cursor.execute(statement,([MatchID, HPossesion, HCorner, HFoul, HOffside, HShot, HShotOnTarget, HShotAccuracy, HPassAccuracy, APossesion, ACorner, AFoul, AOffside, AShot, AShotOnTarget, AShotAccuracy, APassAccuracy, RefereeID]))

	def Statistic_delete(self, StatisticId):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement="""Delete From Statistic Where ID = %s; """
				cursor.execute(statement,([StatisticId]))

	def Statistic_Update(self, StatisticId, MatchID, HPossesion, HCorner, HFoul, HOffside, HShot, HShotOnTarget, HShotAccuracy, HPassAccuracy, APossesion, ACorner, AFoul, AOffside, AShot, AShotOnTarget, AShotAccuracy, APassAccuracy, RefereeID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement="""Update Statistic Set MatchID=%s, HPossesion=%s, HCorner=%s, HFoul=%s, HOffside=%s, HShot=%s, HShotOnTarget=%s, HShotAccuracy=%s, HPassAccuracy=%s, APossesion=%s, ACorner=%s, AFoul=%s, AOffside=%s, AShot=%s, AShotOnTarget=%s, AShotAccuracy=%s, APassAccuracy=%s, "RefereeID"=%s Where ID=%s;"""
				cursor.execute(statement,([MatchID, HPossesion, HCorner, HFoul, HOffside, HShot, HShotOnTarget, HShotAccuracy, HPassAccuracy, APossesion, ACorner, AFoul, AOffside, AShot, AShotOnTarget, AShotAccuracy, APassAccuracy, RefereeID,StatisticId]))
	
	def Statistic_update_info(self, ID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select * FROM Statistic where ID = %s;"""
				cursor.execute(statement,([ID]))
				cursor_list=cursor.fetchall()
				return cursor_list


	def Player_add(self, PlayerName, PlayerAge, Position, PlayerNationalty, PlayerHeight, PlaceOfBirth, TeamID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """
                                INSERT INTO Player(PlayerName, PlayerAge, Position, PlayerNationalty, PlayerHeight, PlaceOfBirth, TeamID) VALUES(%s,%s,%s,%s,%s,%s,%s);"""
				cursor.execute(statement,([PlayerName, PlayerAge, Position, PlayerNationalty, PlayerHeight, PlaceOfBirth, TeamID]))
	
	def Player_delete(self, PlayerID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ DELETE FROM Player WHERE ID = %s;"""
				cursor.execute(statement,[PlayerID])

	def Player_update(self, PlayerID, PlayerName, PlayerAge, Position, PlayerNationalty, PlayerHeight, PlaceOfBirth, TeamID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement="""Update Player Set PlayerName=%s, PlayerAge=%s, Position=%s, PlayerNationalty=%s, PlayerHeight=%s, PlaceOfBirth=%s, TeamID=%s Where ID=%s;"""
				cursor.execute(statement,([PlayerName, PlayerAge, Position, PlayerNationalty, PlayerHeight, PlaceOfBirth, TeamID, PlayerID]))
	
	def Manager_add(self, Name, Age, Nationalty, Height, PlaceOfBirth):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """INSERT INTO Manager(Name, Age, Nationalty, Height, PlaceOfBirth) VALUES(%s,%s,%s,%s,%s);"""
				cursor.execute(statement,([Name, Age, Nationalty, Height, PlaceOfBirth]))			
	
	def Manager_update(self, ManagerID, Name, Age, Nationalty, Height, PlaceOfBirth):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement="""Update Manager Set Name=%s, Age=%s, Nationalty=%s, Height=%s, PlaceOfBirth=%s Where ID=%s;"""
				cursor.execute(statement,([Name, Age, Nationalty, Height, PlaceOfBirth, ManagerID]))
	
	def Manager_delete(self, ManagerID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ DELETE FROM Manager WHERE ID = %s;"""
				cursor.execute(statement,[ManagerID])	
	
	def Team(self):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select Teams.ID,Teamname,NickName,ShortName,FoundationDate,Name,Location, ManagerID FROM Teams,Manager WHERE Teams.ID=Teams.ID and Manager.ID=ManagerID ORDER BY Teamname ASC;"""
				cursor.execute(statement)
				cursor_list=cursor.fetchall()
				return cursor_list

	def Player(self):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select Player.ID,PlayerName,PlayerAge,Position,PlayerNationalty,PlayerHeight,PlaceOfBirth,Teamname,TeamID FROM Player,Teams WHERE Player.ID=Player.ID and Teams.ID=TeamID ORDER BY PlayerName,Teamname ASC;"""
				cursor.execute(statement)
				cursor_list=cursor.fetchall()
				return cursor_list
	
	def Goal(self):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select Goal.ID, PlayerName, MatchID,Minute FROM Goal,Fixtures,Player WHERE Goal.ID=Goal.ID and Player.ID=PlayerID and MatchID=Fixtures.ID ORDER BY PlayerID,MatchID ASC;"""
				cursor.execute(statement)
				cursor_list=cursor.fetchall()
				return cursor_list

	def Detail(self):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select distinct MatchDetails.ID, MatchID, Detail, Minute From MatchDetails, Fixtures Where MatchDetails.ID=MatchDetails.ID and MatchID=MatchID Order By MatchID,Minute"""
				cursor.execute(statement)
				cursor_list=cursor.fetchall()
				return cursor_list
	
	def Standings(self):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select Standings.ID,TeamName,Played,Won,Drawn,Lost,Goals_for,Goals_against,Goals_difference,Points, Teams.id FROM Standings,Teams WHERE Teams.ID=TeamID ORDER BY Points DESC,Goals_difference DESC,TeamName;"""
				cursor.execute(statement)
				cursor_list=cursor.fetchall()
				return cursor_list
	
	def Fixtures(self,week):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select Fixtures.ID,T1.TeamName ,T2.TeamName,Week,MatchDate,Time,HomeScore,AwayScore,Status,RefereeName, HomeTeam, AwayTeam,Refereeid FROM Fixtures,Teams AS T1,Teams AS T2,Referee WHERE Week = %s AND T1.ID=HomeTeam AND T2.ID=AwayTeam AND Refereeid=Referee.id ORDER BY MatchDate,Time;"""
				cursor.execute(statement,([week]))
				cursor_list=cursor.fetchall()
				return cursor_list

	def Referee(self):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select * FROM Referee ORDER BY RefereeName"""
				cursor.execute(statement)
				cursor_list=cursor.fetchall()
				return cursor_list

	def Manager(self):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select Manager.id, Name, Age,Nationalty,height,placeofbirth, Teamname,Teams.id FROM Manager,teams Where ManagerID=manager.id ORDER BY Name"""
				cursor.execute(statement)
				cursor_list=cursor.fetchall()
				return cursor_list
	
	def Referee_add(self, RefereeName,Age,TotalMatch,TotalRedCard,TotalYellowCard):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ INSERT INTO Referee(RefereeName,Age,TotalMatch,TotalRedCard,TotalYellowCard) VALUES(%s,%s,%s,%s,%s);"""
				cursor.execute(statement,([RefereeName,Age,TotalMatch,TotalRedCard,TotalYellowCard]))
	
	def Referee_delete(self,RefereeId):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement="""Delete From Referee Where ID = %s;"""
				cursor.execute(statement,([RefereeId]))

	def Referee_update(self, RefereeID,RefereeName,Age,TotalMatch,TotalRedCard,TotalYellowCard):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement="""Update Referee Set RefereeName=%s, Age=%s, TotalMatch=%s, TotalRedCard=%s, TotalYellowCard=%s Where ID=%s;"""
				cursor.execute(statement,([RefereeName,Age,TotalMatch,TotalRedCard,TotalYellowCard,RefereeID]))
	def Referee_update_info(self, ID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ Select * From Referee where ID = %s;"""
				cursor.execute(statement,([ID]))
				cursor_list=cursor.fetchall()
				return cursor_list
	
	
	def Standing_add(self, TeamID,Played,Won,Drawn,Lost,Goals_for,Goals_against):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ INSERT INTO Standings(TeamID,Played,Won,Drawn,Lost,Goals_for,Goals_against,Goals_difference,Points) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
				cursor.execute(statement,([TeamID,Played,Won,Drawn,Lost,Goals_for,Goals_against,(int(Goals_for)-int(Goals_against)),(3*int(Won)+int(Drawn))]))
	
	def Standing_delete(self,StandingId):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement="""Delete From Standings Where ID = %s;"""
				cursor.execute(statement,([StandingId]))

	def Standing_update(self, StandingId,TeamID,Played,Won,Drawn,Lost,Goals_for,Goals_against):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement="""Update Standings Set TeamID=%s, Played=%s, Won=%s, Drawn=%s, Lost=%s,Goals_for=%s,Goals_against=%s,Goals_difference=%s,Points=%s Where ID=%s;"""
				cursor.execute(statement,([TeamID,Played,Won,Drawn,Lost,Goals_for,Goals_against,(int(Goals_for)-int(Goals_against)),(3*int(Won)+int(Drawn)),StandingId]))
	def Standing_update_info(self, ID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ Select * From Standings where ID = %s;"""
				cursor.execute(statement,([ID]))
				cursor_list=cursor.fetchall()
				return cursor_list
				
	def Fixture_add(self, HomeTeam,AwayTeam,HomeScore,AwayScore,Week,MatchDate,Time,Status,Refereeid):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ INSERT INTO Fixtures(HomeTeam,AwayTeam,HomeScore,AwayScore,Week,MatchDate,Time,Status,Refereeid) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
				cursor.execute(statement,([HomeTeam,AwayTeam,HomeScore,AwayScore,Week,MatchDate,Time,Status,Refereeid]))
	
	def Fixture_delete(self,FixtureId):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement="""Delete From Fixtures Where ID = %s;"""
				cursor.execute(statement,([FixtureId]))

	def Fixture_update(self, FixtureID,HomeTeam,AwayTeam,HomeScore,AwayScore,Week,MatchDate,Time,Status,Refereeid):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement="""Update Fixtures Set HomeTeam=%s, AwayTeam=%s, HomeScore=%s, AwayScore=%s, Week=%s,MatchDate=%s,Time=%s,Status=%s,Refereeid=%s Where ID=%s;"""
				cursor.execute(statement,([HomeTeam,AwayTeam,HomeScore,AwayScore,Week,MatchDate,Time,Status,Refereeid,FixtureID]))
	def Fixture_update_info(self, ID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ Select * From Fixtures where ID = %s;"""
				cursor.execute(statement,([ID]))
				cursor_list=cursor.fetchall()
				return cursor_list
	
	def Goal_update_info(self, ID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ Select * From Goal where ID = %s;"""
				cursor.execute(statement,([ID]))
				cursor_list=cursor.fetchall()
				return cursor_list
	
	def Manager_update_info(self, ID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ Select * From Manager where ID = %s;"""
				cursor.execute(statement,([ID]))
				cursor_list=cursor.fetchall()
				return cursor_list

	def Team_update_info(self, ID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ Select * From Teams where ID = %s;"""
				cursor.execute(statement,([ID]))
				cursor_list=cursor.fetchall()
				return cursor_list

	def Player_update_info(self, ID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ Select * From Player where ID = %s;"""
				cursor.execute(statement,([ID]))
				cursor_list=cursor.fetchall()
				return cursor_list

	def Player_key(self,Key):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select Player.ID,PlayerName,PlayerAge,Position,PlayerNationalty,PlayerHeight,PlaceOfBirth,Teamname,Teams.ID FROM Player,Teams WHERE Player.ID=%s and Teams.ID=TeamID ORDER BY Teamname ASC;"""
				cursor.execute(statement, [Key])
				cursor_list=cursor.fetchall()
				return cursor_list
	
	def Team_key(self,Key):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select Teams.ID,Teamname,NickName,ShortName,FoundationDate,Name,Location, ManagerID FROM Teams,Manager WHERE Teams.ID=%s and Manager.ID=ManagerID ORDER BY Teamname ASC;"""
				cursor.execute(statement, [Key])
				cursor_list=cursor.fetchall()
				return cursor_list
	
	def Goal_key(self,Key):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select Goal.ID, PlayerName, MatchID,Minute FROM Goal,Fixtures,Player WHERE Goal.ID=%s and Player.ID=PlayerID and MatchID=Fixtures.ID ORDER BY PlayerID,MatchID ASC;"""
				cursor.execute(statement, [Key])
				cursor_list=cursor.fetchall()
				return cursor_list
	
	def Manager_key(self,Key):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """SELECT manager.id, manager.name, manager.age, manager.nationalty, manager.height, manager.placeofbirth, teams.teamname from manager left join teams on manager.id = teams.managerid where manager.id=%s Order By Name"""
				cursor.execute(statement, [Key])
				cursor_list=cursor.fetchall()
				return cursor_list

	def Top_goal(self):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select Player.ID, PlayerName, count(PlayerID),Position,Teamname,Player.TeamID FROM Goal,Player,Teams WHERE Goal.ID=Goal.ID and Player.ID=PlayerID and Player.TeamID=Teams.ID Group BY PlayerName,player.id,Teams.Teamname ORDER BY count(PlayerID) DESC;"""
				cursor.execute(statement)
				cursor_list=cursor.fetchall()
				return cursor_list

	def Manager_user(self):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """SELECT manager.id, manager.name, manager.age, manager.nationalty, manager.height, manager.placeofbirth, teams.teamname, teams.id from manager left join teams on manager.id = teams.managerid where manager.id=manager.id Order By Name"""
				cursor.execute(statement)
				cursor_list=cursor.fetchall()
				return cursor_list

	def Team_user_key(self,Key):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select Teams.ID,Teamname,NickName,ShortName,FoundationDate,Name,Location, ManagerID FROM Teams,Manager WHERE Teams.ID=%s and Manager.ID=ManagerID ORDER BY Teamname ASC;"""
				cursor.execute(statement, [Key])
				cursor_list=cursor.fetchall()
				return cursor_list

	def Fixtures2(self):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select Fixtures.ID,T1.TeamName ,T2.TeamName,Week,MatchDate,Time,HomeScore,AwayScore,Status,RefereeName FROM Fixtures,Teams AS T1,Teams AS T2,Referee WHERE T1.ID=HomeTeam AND T2.ID=AwayTeam AND Refereeid=Referee.id ORDER BY MatchDate,Time;"""
				cursor.execute(statement)
				cursor_list=cursor.fetchall()
				return cursor_list

	def Referee_user_key(self,Key):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select Referee.id,RefereeName,TotalMatch,TotalRedCard,TotalYellowCard,Age FROM Referee Where Referee.ID=%s ORDER BY RefereeName"""
				cursor.execute(statement, [Key])
				cursor_list=cursor.fetchall()
				return cursor_list

	def Player_team_user(self,Key):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select Player.ID,PlayerName,PlayerAge,Position,PlayerNationalty,PlayerHeight,PlaceOfBirth,Teamname,Teams.ID FROM Player,Teams WHERE Player.ID=Player.ID and Teams.ID=TeamID and Teams.ID=%s  ORDER BY Teamname ASC;"""
				cursor.execute(statement, [Key])
				cursor_list=cursor.fetchall()
				return cursor_list
	
	def Player_team(self,Key):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select Player.ID,PlayerName,PlayerAge,Position,PlayerNationalty,PlayerHeight,PlaceOfBirth,Teamname,Teams.ID FROM Player,Teams WHERE Player.ID=Player.ID and Teams.ID=TeamID and Teams.ID=%s  ORDER BY Teamname ASC;"""
				cursor.execute(statement, [Key])
				cursor_list=cursor.fetchall()
				return cursor_list
	
	def Detail_user(self,Key):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select distinct MatchDetails.ID, Detail, Minute, MatchID From MatchDetails, Fixtures Where MatchDetails.ID=MatchDetails.ID and MatchID=%s Order By MatchID,Minute"""
				cursor.execute(statement, [Key])
				cursor_list=cursor.fetchall()
				return cursor_list
	
	def Stadium_key(self,Key):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select Stadium.id, Teamname, StadiumName, capacity,built,pitchsize,surface,team_id FROM Stadium,teams Where Teams.id=team_id and team_id=%s ORDER BY Teamname"""
				cursor.execute(statement, [Key])
				cursor_list=cursor.fetchall()
				return cursor_list

	def Fixture_key(self,Key):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select Fixtures.ID,T1.TeamName ,T2.TeamName,Week,MatchDate,Time,HomeScore,AwayScore,Status,RefereeName,HomeTeam,AwayTeam,Refereeid FROM Fixtures,Teams AS T1,Teams AS T2,Referee 
				WHERE T1.ID=HomeTeam AND T2.ID=AwayTeam AND Refereeid=Referee.id and Fixtures.id=%s ORDER BY MatchDate,Time;"""
				cursor.execute(statement, [Key])
				cursor_list=cursor.fetchall()
				return cursor_list

	def Top_assist(self):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select Player.ID, PlayerName, count(PlayerID) FROM Assist,Player WHERE Assist.ID=Assist.ID and Player.ID=PlayerID Group BY PlayerName,player.id ORDER BY count(PlayerID) DESC;"""
				cursor.execute(statement)
				cursor_list=cursor.fetchall()
				return cursor_list

	def Goal_user(self,Key):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select distinct Goal.ID, PlayerName, Teamname,  Goal.Minute, Fixtures.id, Goal.MatchID,PlayerID,teams.id FROM Goal,Fixtures,Player,MatchDetails,Teams 
WHERE Goal.ID=Goal.id and Player.ID=PlayerID 
and Goal.MatchID=Fixtures.ID and Player.TeamID=Teams.id and fixtures.id=%s
ORDER BY Goal.Minute ASC;"""
				cursor.execute(statement,[Key])
				cursor_list=cursor.fetchall()
				return cursor_list

	def Assist_user(self,Key):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select Assist.id,Player.playername,Teams.Teamname, Assist.minute,Assist.lasttouch,Assist.format,Assist.goldenassist,Assist.stadiumha, Player.id, Player.teamid FROM Assist, Player,Teams,Fixtures 
				where Assist.playerid = Player.id and Assist.matchid = fixtures.id and fixtures.id=%s and Teams.id=Player.Teamid
				 ORDER BY minute"""
				cursor.execute(statement,[Key])
				cursor_list=cursor.fetchall()
				return cursor_list
				
	def Assist_information_of_user(self):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement2 = """ SELECT playerid,lasttouch, Count(lasttouch) FROM assist group by lasttouch,playerid;"""
				statement3 = """ SELECT playerid,format, Count(format) FROM assist group by format,playerid """
				statement4 = """ SELECT playerid,goldenassist, Count(goldenassist) FROM assist group by goldenassist,playerid having goldenassist='Yes' """
				statement5 = """ SELECT playerid,stadiumha, Count(stadiumha) FROM assist group by stadiumha,playerid """
				cursor.execute(statement2)
				cursor_list2=cursor.fetchall()
				cursor.execute(statement3)
				cursor_list3=cursor.fetchall()
				cursor.execute(statement4)
				cursor_list4=cursor.fetchall()
				cursor.execute(statement5)
				cursor_list5=cursor.fetchall()
				return [cursor_list2, cursor_list3, cursor_list4, cursor_list5]

	def Statistic_user(self,Key):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select statistic.ID, matchid, HPossesion, HCorner, HFoul, HOffside, HShot, HShotOnTarget, HShotAccuracy, HPassAccuracy, 
APossesion, ACorner, AFoul, AOffside, AShot, AShotOnTarget, AShotAccuracy, APassAccuracy, RefereeName, Statistic."RefereeID" FROM Statistic, Referee  Where matchid=%s and Statistic."RefereeID"=Referee.id ORDER BY MatchID"""
				cursor.execute(statement,[Key])
				cursor_list=cursor.fetchall()
				return cursor_list

	def Player_fixture_team(self,Key):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select Player.ID,PlayerName,Teamname,PlayerAge,Position,PlayerNationalty,PlayerHeight,PlaceOfBirth, Fixtures.HomeTeam, Fixtures.ID,Player.TeamID  From Player, Fixtures, Teams Where ((Teams.ID=Fixtures.HomeTeam and Player.TeamID=Fixtures.HomeTeam) 
or (Teams.ID=Fixtures.AwayTeam and Player.TeamID=Fixtures.AwayTeam))
 and Fixtures.ID=%s Order By Teamname"""
				cursor.execute(statement,[Key])
				cursor_list=cursor.fetchall()
				return cursor_list


	def Standing_key(self,Key):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select Standings.ID,TeamName,Played,Won,Drawn,Lost,Goals_for,Goals_against,Goals_difference,Points, Teams.id FROM Standings,Teams,Fixtures WHERE Teams.ID=TeamID 
and (Fixtures.HomeTeam=Teams.id or Fixtures.AwayTeam=Teams.id) and Fixtures.ID=%s
ORDER BY Points DESC,Goals_difference DESC,TeamName;"""
				cursor.execute(statement,[Key])
				cursor_list=cursor.fetchall()
				return cursor_list
		
	def Fixture_team_key(self,Key):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select distinct Fixtures.ID,T1.Teamname ,T2.Teamname,Week,MatchDate,Time,HomeScore,AwayScore,Status,RefereeName,HomeTeam,AwayTeam,Refereeid FROM Fixtures,Teams AS T1,Teams AS T2,Referee 
WHERE (( T1.ID=HomeTeam AND T2.ID=AwayTeam and Fixtures.Hometeam=T1.ID and HomeTeam=T1.ID) )  
AND Refereeid=Referee.id  and (T1.ID=%s or T2.ID=%s)  ORDER BY MatchDate,Time"""
				cursor.execute(statement,[Key,Key])
				cursor_list=cursor.fetchall()
				return cursor_list

	def Manager_team_key(self,Key):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """SELECT manager.id, manager.name, manager.age, manager.nationalty, manager.height, manager.placeofbirth, teams.teamname, Teams.ID from manager left join teams on manager.id = teams.managerid 
where manager.id=manager.id and Teams.ManagerID=Manager.ID and Teams.ID=%s Order By Name"""
				cursor.execute(statement,[Key])
				cursor_list=cursor.fetchall()
				return cursor_list