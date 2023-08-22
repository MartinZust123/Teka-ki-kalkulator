import psycopg2
import psycopg2.extras
import data.auth_public as auth

class UserData:
    def __init__(self):
        self.conn = psycopg2.connect(database=auth.db, host=auth.host, user=auth.user, password=auth.password)
        self.conn.autocommit = True
        self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def close_connection(self):
        self.cur.close()
        self.conn.close()

    def register_user(self, username, password):
        try:
            query = "INSERT INTO users (username, password) VALUES (%s, %s);"
            self.cur.execute(query, (username, password))
            return True
        except Exception as e:
            print("Error:", e)
            return False

    def authenticate_user(self, username, password):
        query = "SELECT * FROM users WHERE username = %s AND password = %s;"
        self.cur.execute(query, (username, password))
        return self.cur.fetchone()

# Example usage
user_data = UserData()

# Register a user
user_data.register_user("user1", "password1")

# Authenticate a user
authenticated_user = user_data.authenticate_user("user1", "password1")
if authenticated_user:
    print("Authentication successful:", authenticated_user)
else:
    print("Authentication failed.")

# Close the connection
user_data.close_connection()