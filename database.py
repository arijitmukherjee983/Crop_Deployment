import sqlite3


def get_responses():
    with sqlite3.connect('responses.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM responses")
        rows = cursor.fetchall()
        return rows


responses = get_responses()
for response in responses:
    print(response)

