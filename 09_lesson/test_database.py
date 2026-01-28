from UserTable import UserTable
from StudentTable import StudentTable
from SubjectTable import SubjectTable

with open("password.txt", "r") as file:
    connection_string = file.read()

usbd = UserTable()
stbd = StudentTable()
subd = SubjectTable()

def test_insert_new_user():
    usbd.get_tables()
    len_before = usbd.get_list()
    new_email = "aaron-phoenix@mail.ru"
    usbd.insert_new({"new_user_email": new_email})
    len_after = usbd.get_list()
    
    assert len_after == len_before + 1
    
    max_id = usbd.get_max_id()
    value_ID = max_id + 1 if max_id > 0 else 1  
    usbd.update_new({"new_user_id": value_ID, "new_user_email": new_email})
    
    usbd.delete_new({"new_user_email": new_email})
    print("Тест пройден успешно!")

if __name__ == "__main__":
    test_insert_new_user()

def test_insert_new_student():
    stbd.get_tables()
    len_before = stbd.get_list()
    new_level = "Advanced"
    stbd.insert_new({"new_level": new_level})
    len_after = stbd.get_list()
    
    assert len_after == len_before + 1
    
    max_id = stbd.get_max_id()
    value_ID = max_id + 1 if max_id > 0 else 1  
    stbd.update_new({"new_user_id": value_ID, "new_level": new_level})
    
    stbd.delete_new({"new_user_id": value_ID})
    print("Тест пройден успешно!")

if __name__ == "__main__":
    test_insert_new_student()

def test_insert_new_subject():
    subd.get_tables()
    len_before = subd.get_list()
    new_subject = "OBZR"
    subd.insert_new({"new_subject": new_subject})
    len_after = subd.get_list()
    
    assert len_after == len_before + 1
    
    max_id = subd.get_max_id()
    value_ID = max_id + 1 if max_id > 0 else 1  
    subd.update_new({"new_subject_id": value_ID, "new_subject": new_subject})
    
    subd.delete_new({"new_subject_id": value_ID})
    print("Тест пройден успешно!")

if __name__ == "__main__":
    test_insert_new_student()
