import sqlite3
from bottle import route, run, template, request


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def fill_database():
    conn = get_db_connection()
    conn.executescript(
        '''
        BEGIN;
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            password TEXT
        );
        INSERT INTO users (name, password) VALUES ('user1', 'aksdjfkk');
        INSERT INTO users (name, password) VALUES ('user2', 'ijj32338');
        INSERT INTO users (name, password) VALUES ('user3', 'aks]d]g]3');
        COMMIT;
        ''',
    )
    conn.commit()
    conn.close()


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
    fill_database()
    run(host='localhost', port=8080)

