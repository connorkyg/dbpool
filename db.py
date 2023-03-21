import psycopg2.pool


class DatabaseManager:
    def __init__(self):
        self.min_conn = 1
        self.max_conn = 10
        self.dbpool = None

    def create_connection_pool(self):
        self.dbpool = psycopg2.pool.SimpleConnectionPool(
            host="192.168.203.222",
            dbname="dbkwon",
            user="connor",
            password="Dudrb12#",
            port="5432",
            minconn=self.min_conn,
            maxconn=self.max_conn
        )

    def get_conn(self):
        if self.dbpool is None:
            self.create_connection_pool()
        return self.dbpool.getconn()

    def put_conn(self, conn):
        if self.dbpool is not None:
            self.dbpool.putconn(conn)
