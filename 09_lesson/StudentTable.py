from sqlalchemy import create_engine, inspect, text

class StudentTable:
    scripts = {
        "select": text("SELECT * FROM student"),
        "select_max_id": text("SELECT MAX(user_id) FROM student"),
        "delete_by_id": text("DELETE FROM student WHERE student.user_id = :new_user_id"),
        "insert_new": text("INSERT INTO student(\"level\") VALUES (:new_level)"),
        "create_id": text("UPDATE student SET user_id = :new_user_id WHERE student.level = :new_level")
    }

    def __init__(self) -> None:
        with open("password.txt", "r") as file:
            self.connection_string = file.read()
        self.db = create_engine(self.connection_string)

    def get_tables(self):
        inspector = inspect(self.db)
        res = inspector.get_table_names()
        assert res[2] == 'student'
        return res

    def insert_new(self, value_new):
        conn = self.db.connect()
        transaction = conn.begin()
        conn.execute(self.scripts["insert_new"], value_new)
        transaction.commit()
        conn.close()

    def update_new(self, value_id):
        conn = self.db.connect()
        transaction = conn.begin()
        conn.execute(self.scripts["create_id"], value_id)
        transaction.commit()
        conn.close()
    
    def delete_new(self, value_deleted):
        conn = self.db.connect()
        transaction = conn.begin()
        conn.execute(self.scripts["delete_by_id"], value_deleted)
        transaction.commit()
        conn.close()

    def get_max_id(self):
        conn = self.db.connect()
        result = conn.execute(self.scripts["select_max_id"])
        max_id = result.fetchone()[0]
        conn.close()
        return max_id if max_id is not None else 0
    
    def get_list(self):
        conn = self.db.connect()
        result = conn.execute(self.scripts["select"])
        rows = len(result.fetchall())
        conn.close()
        return rows