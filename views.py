class Views:
    @staticmethod
    def show_menu():
        print("\n 1. Открыть файл\n 2. Сохранить файл\n 3. Показать все контакты\n 4. Найти контакт\n 5. Изменить контакт\n 6. Удалить контакт\n 7. Выход\n 8. Вернуться в главное меню\n" )
        return input("Введи пункт меню   ")

    @staticmethod
    def message(sms):
        return print(sms)
    
    @staticmethod
    def show_contact(contacts):
        for contact in contacts:
            print(contact['name'], contact['lastname'],contact['tel'], contact['email'], contact['work'], contact['age'])
         
    @staticmethod
    def vvod(contacts):
        print("Введи Name Контакта\n")  
        x=input()
        print("Введи Lastname Контакта\n")   
        y=input()
        for contact in contacts:
            if (x==contact['name'])&(y==contact['lastname']):
                        print(contact['name'], contact['lastname'], contact['tel'], contact['email'], contact['work'], contact['age'])
    

    @staticmethod
    def edit_contact(contacts):
         print("\n Введи Name контакта для редактирования\n")
         x=input()
         for contact in contacts:
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
                 
                 