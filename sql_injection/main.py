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
        DROP TABLE IF EXISTS users;
        CREATE TABLE users (
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


@route('/', method='GET')
def index():
    with open('./index.html', 'r') as file:
        html = file.read()
    return template(html) 


@route('/', method='POST')
def main_page():
    name = request.forms.get('name')

    conn = get_db_connection()
    query = f"SELECT id FROM users WHERE name='{name}'"
    rows = conn.execute(query).fetchall()
    conn.close()

    users = [
        {
            'id': row['id'],
        }
        for row in rows
    ]
    return template(f'<p>{users}</p><br><i>{query}</i>')

if __name__ == '__main__':
    fill_database()
    run(host='localhost', port=8080)

