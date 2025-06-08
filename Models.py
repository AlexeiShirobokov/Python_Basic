import json

class Model:
    #хранение файл
    
    def __init__(self, filename):
        self.filename=filename
        self.data = [{
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
    
    def save_file(self):
        try:
            with open(self.filename, 'w') as f:
                f.write(json.dumps(self.data, indent=4))
            print("файл сохранен")    
        except:
            print("ошибка при сохранении")

    
    # открыть файл
    def opening(self):
        with open(self.filename, 'r') as f:
             contact=json.load(f)

    # Показать все контакты
    def show_contact(self):
         return self.data
    
    # Изменить контакт
    def edit_contact(self, update):
        self.data=update
        self.save_file()
        return self.data

# filename='/Users/alexei/contact.json'
# result=Model(filename)
# result.opening()