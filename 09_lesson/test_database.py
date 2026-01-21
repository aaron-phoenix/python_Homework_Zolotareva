from sqlalchemy import create_engine, inspect, text

db_connection_string = "postgresql://postgres:Xthnjdfext,f2025@localhost:5432/QA1"
db = create_engine(db_connection_string)

def test_db_connection():
    inspector = inspect(db)
    first_student = inspector.get_table_names()
    print(first_student[2])
    assert first_student[2] == 'student'

def test_select():
    connection = db.connect()
    result = connection.execute(text("SELECT * FROM users"))
    rows = result.mappings().all()
    row1 = rows[0]
    print(row1)
    assert row1["user_id"] == 42568
    connection.close()

def test_insert():
    connection = db.connect()
    transaction = connection.begin()
    sql = "INSERT INTO users (\"user_email\") VALUES (:new_user_email)"
    connection.execute(text(sql), {"new_user_email" : "aaron-phoenix@mail.ru"})
    transaction.commit()
    print("Данные успешно добавлены")
    connection.close()

def test_update():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("UPDATE users SET user_id = :New_user_id WHERE user_email = :user_email")
    connection.execute(sql, {"New_user_id" : 22694, "user_email" : "aaron-phoenix@mail.ru"})

    
    transaction.commit()
    connection.close()

def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("DELETE FROM users WHERE user_id = :id")
    connection.execute(sql, {"id": 22694})

    transaction.commit()
    connection.close()
