from sqlalchemy import create_engine, inspect, text
connection_string = "postgresql://postgres:Xthnjdfext,f2025@localhost:5432/QA1"
__db = create_engine(connection_string)

def test_db_connection():
    inspector = inspect(__db)
    first_student = inspector.get_table_names()
    print(first_student[0])
    assert first_student[0] == 'users'

def test_select():
    connection = __db.connect()
    result = connection.execute(text("SELECT * FROM users"))
    rows = result.mappings().all()
    row1 = rows[0]
    print(row1)
    assert row1["user_id"] == 42568
    connection.close()

def test_insert():
    connection = __db.connect()
    connection.begin()
    sql = text("INSERT INTO users (\"user_email\") VALUES (:new_user_email)")
    connection.execute(sql, {"new_user_email" : "aaron-phoenix@mail.ru"})
    
    connection.close()
    
def test_update():
    connection = __db.connect()
    transaction = connection.begin()

    sql = text("UPDATE users SET user_id = :New_user_id WHERE user_email = :user_email")
    connection.execute(sql, {"New_user_id" : 22694, "user_email" : "aaron-phoenix@mail.ru"})

    
    transaction.commit()
    connection.close()

def test_delete():
    connection = __db.connect()
    transaction = connection.begin()

    sql = text("DELETE FROM users WHERE user_id = :id")
    connection.execute(sql, {"id": 22694})

    transaction.commit()
    connection.close()
