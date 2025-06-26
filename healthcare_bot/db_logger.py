import mysql.connector
from db_config import config

def log_conversation(session_id, user_msg, bot_response, intent_name):
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        query = """
        INSERT INTO conversation_history (session_id, user_message, bot_response, intent_name)
        VALUES (%s, %s, %s, %s)
        """
        values = (session_id, user_msg, bot_response, intent_name)
        cursor.execute(query, values)
        conn.commit()

        print("Logged to DB ✅")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()