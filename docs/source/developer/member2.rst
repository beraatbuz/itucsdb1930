Parts Implemented by Muhammed Enes Tırnakçı
================================

Database Design
---------------

   .. figure:: erDiagramEnes.png
         :scale: 50 %
         :alt: E/R Diagram for Teams, Player, Manager, Goal Table 


Code
----

   .. code-block:: python

      def Team_add(self, TeamName, NickName, ShortName, FoundationDate, ManagerID,Location):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ INSERT INTO Teams(TeamName, NickName, ShortName, FoundationDate,  ManagerID,Location) VALUES(%s,%s,%s,%s,%s,%s);"""
				cursor.execute(statement,([TeamName, NickName, ShortName, FoundationDate, ManagerID,Location]))

    This method adds new team.

 