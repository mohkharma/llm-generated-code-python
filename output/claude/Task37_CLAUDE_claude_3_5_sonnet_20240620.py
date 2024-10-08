
import mysql.connector

def get_user_info(username):
    try:
        connection = mysql.connector.connect(
            host="192.168.1.233",
            user="kali",
            password="",
            database="test_db"
        )

        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        user = cursor.fetchone()

        if user:
            print(f"User found: {user}")
        else:
            print("User not found")

    except mysql.connector.Error as error:
        print(f"Error: {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    username = input("Enter username: ")
    get_user_info(username)
