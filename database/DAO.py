from database.DB_connect import DBConnect
from model.aeroporto import Aeroporto


class DAO():
    def __init__(self):
        pass


    @staticmethod
    def getAllAeroporti():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select * from airports"""

        cursor.execute(query)

        for row in cursor:
            result.append(Aeroporto(**row))

        cursor.close()
        conn.close()
        return result


    @staticmethod
    def getAllEdges(distanza):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT LEAST(ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID) AS airportP,
                    GREATEST(ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID) AS airportD, AVG(DISTANCE) AS media
                    FROM flights
                    GROUP BY LEAST(ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID), GREATEST(ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID)
                    HAVING media > %s"""

        cursor.execute(query, (distanza,))

        for row in cursor:
            result.append((row["airportP"], row["airportD"], row["media"]))

        cursor.close()
        conn.close()
        return result