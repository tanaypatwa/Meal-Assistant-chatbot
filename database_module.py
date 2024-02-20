# import psycopg2
# import os
# from contextlib import contextmanager

# # Use environment variables for sensitive information
# DATABASE = os.getenv('DB_NAME', 'DBname')
# USER = os.getenv('DB_USER', 'dbuser')
# PASSWORD = os.getenv('DB_PASSWORD', '')
# HOST = os.getenv('DB_HOST', 'localhost')
# PORT = os.getenv('DB_PORT', '5432')

# @contextmanager
# def get_db_connection():
#     connection = None
#     try:
#         connection = psycopg2.connect(
#             database=DATABASE,
#             user=USER,
#             password=PASSWORD,
#             host=HOST,
#             port=PORT
#         )
#         yield connection
#     except psycopg2.Error as e:
#         print(f"Database connection error: {e}")
#     finally:
#         if connection:
#             connection.close()

# @contextmanager
# def get_db_cursor(commit=False):
#     with get_db_connection() as connection:
#         cursor = connection.cursor()
#         try:
#             yield cursor
#             if commit:
#                 connection.commit()
#         finally:
#             cursor.close()

# def query_database(sql_query, params=None):
#     with get_db_cursor() as cursor:
#         try:
#             cursor.execute(sql_query, params or ())
#             return cursor.fetchall()
#         except psycopg2.Error as e:
#             print(f"Query execution error: {e}")
#             return None

# def modify_database(sql_query, params=None):
#     with get_db_cursor(commit=True) as cursor:
#         try:
#             cursor.execute(sql_query, params or ())
#         except psycopg2.Error as e:
#             print(f"Modification error: {e}")
# def construct_query(attributes):
#     conditions = " AND ".join([f'"{attr}"=TRUE' for attr in attributes])
#     query = f"SELECT \"Meal Name\" FROM meals WHERE {conditions};"
#     return query

# def query_database(sql_query):
#     # Assuming you have a function like this to execute your query
#     connection = psycopg2.connect(database="postgres", user="postgres", password='')
#     cursor = connection.cursor()
#     cursor.execute(sql_query)
#     meals = cursor.fetchall()
#     cursor.close()
#     connection.close()
#     return meals

import psycopg2
import os

# Assuming the use of environment variables for database configuration
DATABASE = os.getenv('DB_NAME', 'postgres')
USER = os.getenv('DB_USER', 'postgres')
PASSWORD = os.getenv('DB_PASSWORD', '')
HOST = os.getenv('DB_HOST', 'localhost')
PORT = os.getenv('DB_PORT', '5432')

def get_db_connection():
    """
    Creates a connection to the database.
    """
    return psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)

def query_database(sql_query):
    """
    Executes a given SQL query and returns the results.

    :param sql_query: The SQL query to execute (string).
    :return: Query results as a list of tuples.
    """
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql_query)
            return cur.fetchall()  # Fetches all rows of a query result
print("jello")


