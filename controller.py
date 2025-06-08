from Models import Model 
from views import Views 
class Controller:

    def __init__(self):
        self.model = Model('/Users/alexei/Documents/Education/Python basic/contact.json')
        self.views = Views()

    def show(self):
            
        choise=self.views.show_menu()
        if choise == '1':
           self.model.opening()

        if choise == '3':
           contacts=self.model.show_contact()
           self.views.show_contact(contacts)

        if choise == '4':
           contacts=self.model.show_contact()  
           self.views.show_contact(contacts)
           self.views.vvod(contacts)

        if choise == '5':
           contacts=self.model.show_contact()  
           self.views.show_contact(contacts)
           update=self.views.edit_contact(contacts)
           self.model.edit_contact(update)
           self.views.show_contact(contacts)

result = Controller()
result.show()

