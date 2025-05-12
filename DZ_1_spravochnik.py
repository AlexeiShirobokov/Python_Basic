# Написать телефонный справочник, который будет сохранять контакты в файл и иметь следующий функционал:

# открыть файл
# сохранить файл
# показать все контакты
# создать контакт
# найти контакт
# изменить контакт
# удалить контакт
# выход

# Описание/Пошаговая инструкция выполнения домашнего задания:
# Пояснения и рекомендации:

# Данное задание можно выполнить в двух вариантах: использовать готовый файл с контактами (находится в материалах) или написать свою структуру:
# В качестве "хранилища" контактов можно использовать любой формат - txt, json, csv
# Контакт минимально должен содержать имя, телефон и комментарий (по желанию можно дополнить поля)
# Реализацию сохранения можно выполнить двумя способами: загружать файл, создавать буферную копию для работы и в дальнейшем сохранять (или нет) внесенные изменения, или вносить изменения сразу в файл
# Если выбран вариант буферизации - добавить функционал проверки изменений перед выходом (предлагать сохранить изменения) - опционально (делать необязательно)
# Поиск по контактам можно делать отдельно по полям (имя, телефон, комментарий), так и общий (поисковое слово ищет сразу во всех полях контакта)
# Для упрощения поиска, изменения и удаления рекомендуется добавить контактам - ID
# Добавить всевозможные проверки, чтобы программа не крашилась в случае введенных неверных данных
# Данное задание подразумевает отличное владение всеми навыками, затронутыми в первом модуле
# Сдавать ДЗ ссылкой на свой репозиторий.




# Создать файл json, Заполнить файл данными
import json

data = [{
    'name': 'Иван',
    'lastname': 'Иванов',
    'tel': '89127120012',
    'email': 'ivanov@gmail.com',
    'work': 'Иванов и Партнеры',
    'age': '40',
    },
    {
    'name': 'Кощей',
    'lastname': 'Бессмертных',
    'tel': '89127120000',
    'email': 'kochey@gmail.com',
    'work': 'Последний богатырь',
    'age': '940',
    },
    {'name': 'Баба',
    'lastname': 'Ягушина',
    'tel': '89127000000',
    'email': 'babayogo@gmail.com',
    'work': 'Последний богатырь',
    'age': '300',

    }]
file = '/Users/alexei/contact.json'
with open(file, 'w') as f:
    f.write(json.dumps(data, indent=4))

# Сделать функционал работы файла

# открыть файл
def opening():
    with open(file, 'r') as f:
            contact=json.load(f)
    print("Открыть файл\n") 
    print(contact)

# Показать все контакты
def show_contact():
     with open(file, 'r', encoding="utf-8") as f:
            contact=json.load(f)
     print("Все контакты\n")       
     for contact in data:
        print(contact['name'], contact['lastname'],contact['tel'], contact['email'], contact['work'], contact['age'])

# Найти контакт
def find_contact():
    with open(file, 'r') as f:
            contact=json.load(f)
    print("Найти контакт\n")
    print("Введи Name Контакта\n")   
    x=input()
    print("Введи Lastname Контакта\n")   
    y=input()
    for contact in data:
        if (x==contact['name'])&(y==contact['lastname']):
                    print(contact['name'], contact['lastname'], contact['tel'], contact['email'], contact['work'], contact['age'])


# Изменить контакт
def edit_contact():
    show_contact()
    with open(file, 'r+', encoding='utf-8') as f:
        contact=json.load(f)
        print("\n Введи Name контакта для редактирования\n")
        x=input()
        for contact in data:
            if (x==contact['name']):
                 print("Введи новое Name контакта\n")
                 x_name=input()
                 if x_name: contact['name']=x_name
 
                 print("Введи новое lastname контакта\n")
                 x_lastname=input()
                 if x_lastname: contact['lastname']=x_lastname
                
                 print("Введи новое tel контакта\n")
                 x_tel=input()
                 if x_tel: contact['tel']=x_tel
            
                 print("Введи новое email контакта\n")
                 x_email=input()
                 if x_email: contact['email']=x_email
                 
                 print("Введи новое work контакта\n")
                 x_work=input()
                 if x_work: contact['work']=x_work
            
                 print("Введи новое age контакта\n")
                 x_age=input()
                 if x_age: contact['age']=x_age
                 
                 f.seek(0)
                 f.write(json.dumps(contact))
                 show_contact()
                 main()
    
                  
          
# Сохранить файл
def saving():
     #спросить перед сохранением. сохранять или нет
     print("Сохранить файл: Да, Нет")
     x=input()
     if x=="Да":
         with open(file, 'w') as f:
            f.write(json.dumps(data, indent=4))
         main()
     main()
    
# Создание диалога
def main():
    print("\n 1. Открыть файл\n 2. Сохранить файл\n 3. Показать все контакты\n 4. Найти контакт\n 5. Изменить контакт\n 6. Удалить контакт\n 7. Выход\n 8. Вернуться в главное меню\n" )
    x=input()
    if x==str(1): 
        return opening(), print("\n Главное меню"), main()
    if x==str(3): 
        return show_contact(), print("\n Главное меню"), main()
    if x==str(4): 
        return find_contact(), print("\n Главное меню"), main()
    if x==str(8):
        return main() 
    if x==str(5):
        return edit_contact(), print("\n Главное меню"), main()    
    if x==str(7):
        return exit 
    if x==str(2):
        return saving(), print("\n Главное меню"), main()

main()

