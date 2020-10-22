import mysql.connector


def get_db_config():
    return {
        "host": "localhost",
        "user": "dummy_user",
        "password": "dummy_password",
        "database": "dummy_database"
    }


def insert_into_db(agent_id, password):
    db_conn = None
    cursor = None
    try:
        db_config = get_db_config()
        db_conn = mysql.connector.connect(**db_config)
        sql = "INSERT INTO agents (agent_id, password) VALUES (%s, %s)"
        val = (agent_id, password)
        cursor = db_conn.cursor()
        cursor.execute(sql, val)

        db_conn.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db_conn.close()


def get_agent_credential(agent_id):
    db_conn = None
    cursor = None
    try:
        db_config = get_db_config()
        db_conn = mysql.connector.connect(**db_config)
        cursor = db_conn.cursor()

        sql = "SELECT agent_id, password FROM agents where agent_id = %s"
        val = (agent_id, )
        cursor.execute(sql, val)

        result = cursor.fetchall()
        agent_cred = {
            "agent_id": result[0],
            "password": result[1]
        }
        return agent_cred
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db_conn.close()


def get_items_from_db(agent_id):
    db_conn = None
    cursor = None
    try:
        db_config = get_db_config()
        db_conn = mysql.connector.connect(**db_config)
        cursor = db_conn.cursor()

        sql = "SELECT agent_id, title, description, category, due_date FROM todo_items where agent_id = %s ORDER BY " \
              "due_date DESC"
        val = (agent_id, )
        cursor.execute(sql, val)

        result = cursor.fetchall()
        todo_items = []
        for row in result:
            todo_items = {
                "agent_id": row[1],
                "title": row[2],
                "description": row[3],
                "category": row[4],
                "due_date": row[5],
            }
        return todo_items
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db_conn.close()


def save_todo_item_in_db(agent_id, title, description, category, due_date):
    db_conn = None
    cursor = None
    try:
        db_config = get_db_config()
        db_conn = mysql.connector.connect(**db_config)
        cursor = db_conn.cursor()

        sql = "SELECT agent_id, title, description, category, due_date FROM todo_items where agent_id = %s ORDER " \
              "BY due_date DESC"
        val = (agent_id, title, description, category, due_date, )
        cursor.execute(sql, val)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        db_conn.close()
