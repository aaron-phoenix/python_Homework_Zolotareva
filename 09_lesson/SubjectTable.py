from sqlalchemy import create_engine, inspect, text

class SubjectTable:
    scripts = {
        "select": text("SELECT * FROM subject"),
        "select_max_id": text("SELECT MAX(subject_id) FROM subject"),
        "delete_by_id": text("DELETE FROM subject WHERE subject.subject_id = :new_subject_id"),
        "insert_new": text("INSERT INTO subject(\"subject_title\") VALUES (:new_subject_title)"),
        "create_id": text("UPDATE subject SET subject_id = :new_subject_id WHERE subject.subject_id = :new_subject_id")
    }

    def __init__(self) -> None:
        with open("password.txt", "r") as file:
            self.connection_string = file.read()
        self.db = create_engine(self.connection_string)

    def get_tables(self):
        inspector = inspect(self.db)
        res = inspector.get_table_names()
        assert res[1] == 'subject'
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