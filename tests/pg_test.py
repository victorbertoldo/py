from locust import HttpUser, task, between
import psycopg2

class PostgresUser(HttpUser):
    wait_time = between(1, 3)  # Set wait time between consecutive tasks

    def on_start(self):
        # Initialize the database connection
        self.connection = psycopg2.connect(
            host='localhost',
            port=5432,
            dbname='Dados_RFB',
            user='postgres',
            password='postgres'
        )

    def on_stop(self):
        # Close the database connection
        self.connection.close()


    @task
    def execute_query(self):
        # Define your database query here
        query = "SELECT natureza_juridica, sum(capital_social) as cap_social FROM public.empresa group by natureza_juridica"

        # Execute the query
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()

        # Use the query result for further processing, if needed
        # ...

