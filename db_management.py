import sqlite3

def save_response(id, user_id, topic, subtopic, question, response, interpreted_response):
    # Connect to the database
    connection = sqlite3.connect("responses.db")
    cursor = connection.cursor()

    # Insert the response
    cursor.execute('''
    INSERT INTO responses (
        id, user_id, topic, subtopic, question, response, interpreted_response
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (id, user_id, topic, subtopic, question, response, interpreted_response))

    # Commit and close the connection
    connection.commit()
    connection.close()

    print("Response saved successfully.")

def get_all_responses():
    # Connect to the database
    connection = sqlite3.connect("user_responses.db")
    cursor = connection.cursor()

    # Query the data
    cursor.execute("SELECT * FROM user_responses")
    responses = cursor.fetchall()

    # Close the connection
    connection.close()
    return responses
