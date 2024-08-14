import mysql.connector
from mysql.connector import Error


class MySQLConnector:
    """
    A class to handle MySQL database connections and operations.

    Attributes:
    ----------
    host : str
        The hostname of the MySQL server.
    database : str
        The name of the database to connect to.
    user : str
        The username to use for authentication.
    password : str
        The password to use for authentication.
    connection : mysql.connector.connection_cext.CMySQLConnection or None
        The MySQL connection object.
    """

    def __init__(self, host, database, user, password):
        """
        Constructs all the necessary attributes for the MySQLConnector object and initializes the connection to None.

        Parameters:
        ----------
        host : str
            The hostname of the MySQL server.
        database : str
            The name of the database to connect to.
        user : str
            The username to use for authentication.
        password : str
            The password to use for authentication.
        """
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        """
        Establishes a connection to the MySQL database.

        Raises:
        ------
        Error
            If there is an error connecting to the database.
        """
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if self.connection.is_connected():
                # print("Connected to MySQL database")
                pass
        except Error as e:
            print(f"Error: {e}")
            self.connection = None

    def execute_query(self, query, params=None):
        """
        Executes a given SQL query.

        Parameters:
        ----------
        query : str
            The SQL query to execute.
        params : tuple or None
            The parameters to pass to the SQL query.

        Returns:
        -------
        list
            The result of the query as a list of tuples.

        Raises:
        ------
        Error
            If there is an error executing the query.
        """
        if self.connection is None:
            raise Error("Connection is not established")

        cursor = self.cursor()
        try:
            cursor.execute(query, params)
            result = cursor.fetchone()
            return result
        except Error as e:
            print(f"Error: {e}")
            return []
        finally:
            cursor.close()

    def cursor(self):
        """
        Returns a cursor object for the MySQL connection.

        Returns:
        -------
        mysql.connector.cursor_cext.CMySQLCursor
            The cursor object.
        """
        return self.connection.cursor()

    def commit(self):
        """
        Commits the current transaction to the MySQL database.
        """
        self.connection.commit()

    def close(self):
        """
        Closes the connection to the MySQL database.
        """
        if self.connection is not None and self.connection.is_connected():
            self.connection.close()
            print("MySQL connection is closed")
