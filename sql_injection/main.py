import sqlite3
from bottle import route, run, template, request


def get_db_connection():
    # TODO: add a db scheme - users: id,name,password
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@route('/', method='POST')
def main_page():
    name = request.forms.get('name')

    conn = get_db_connection()
    # TODO: there are some possible SQL injections here like the following: 
    # user1' or name='user2' or name='user3'--
    # ' or 1=1;--
    # ' union select password from users--
    # ' union select name || ':' || password from users--
    rows = conn.execute(f"SELECT id FROM users WHERE name='{name}'").fetchall()
    conn.close()

    users = [
        {
            'id': row['id'],
        }
        for row in rows
    ]
    return str(users)

if __name__ == '__main__':
    run(host='localhost', port=8080)

