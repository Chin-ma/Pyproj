from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.gridlayout import GridLayout
import ast, re, time, datetime, os, shutil, send2trash
from kivy.config import Config
Config.set('graphics', 'resizable', True)
from kivy.uix.image import Image
from kivy.clock import Clock

class WelcomePage(FloatLayout):
    def __init__(self, **kwargs):
        super(WelcomePage, self).__init__(**kwargs)
        self.add_widget(Label(text='Welcome to your own diary', 
        pos_hint={'x':0, 'y':0.4}, font_size=40))
        self.login_butt = Button(text='Login', size_hint=(0.2, 0.1),
        pos_hint={'x':0.2, 'y':0.5},font_size=23)
        self.login_butt.bind(on_release=self.login)
        self.add_widget(self.login_butt)
        self.new_user_butt = Button(text='Create New User', size_hint=(0.23,0.1),
        pos_hint={'x':0.6, 'y':0.5},font_size=23)
        self.new_user_butt.bind(on_release=self.new_acc)
        self.add_widget(self.new_user_butt)

    def new_acc(self, ins):
        diary.screenmanager.current = 'NewAccPage'
        diary.screenmanager.transition.direction = 'left'

    def login(self, ins):
        diary.screenmanager.current = 'AllAccsPage'
        diary.screenmanager.transition.direction = 'left'


class NewAccPage(FloatLayout):
    def __init__(self, **kwargs):
        super(NewAccPage, self).__init__(**kwargs)
        self.add_widget(Label(text='Give me your name', font_size=25,
        pos_hint={'x':-0.2, 'y':0.2}))
        self.username = TextInput(multiline = False, size_hint = (0.2, 0.1),
        pos_hint={'x':0.6, 'y':0.65})
        self.add_widget(self.username)
        self.add_widget(Label(text='What will be your password', font_size=25,
        pos_hint={'x':-0.2, 'y':0}))
        self.password = TextInput(multiline = False, size_hint=(0.2, 0.1),
        pos_hint={'x':0.6, 'y':0.45})
        self.add_widget(self.password)
        self.create_acc_butt = Button(text='Create Account', size_hint = (0.22, 0.1),
        pos_hint = {'x':0.1, 'y':0.1},font_size=23)
        self.create_acc_butt.bind(on_release=self.save_info)
        self.add_widget(self.create_acc_butt)
        self.back_butt = Button(text='Back', size_hint = (0.2, 0.1),
        pos_hint={'x':0.73, 'y':0.1},font_size=23)
        self.back_butt.bind(on_release=self.back)
        self.add_widget(self.back_butt)
        self.account_created_message = Label(text = 'Your account got created!!',
        pos_hint={'x':0, 'y':-0.22}, font_size = 23)

    def back(self, ins):
        diary.screenmanager.current = 'WelcomePage'
        diary.screenmanager.transition.direction = 'right'
        self.remove_widget(self.account_created_message)
        
    def save_info(self, ins):
        file = open('.\\req files\\usernames and passwords.txt', 'a')
        file.write(str({'username':self.username.text, 'password':self.password.text})+'\n')
        file.close()
        os.mkdir(f'.\\req files\\{self.username.text}')
        self.add_widget(self.account_created_message)
        time.sleep(2)


class AllAccsPage(FloatLayout):
    def __init__(self, **kwargs):
        super(AllAccsPage, self).__init__(**kwargs)
        self.back_butt = Button(text='Back', pos_hint={'x':0.05, 'y':0.08},
        size_hint=(0.2,0.1),font_size=23)
        self.back_butt.bind(on_release=self.back)
        self.add_widget(self.back_butt)
        usernames = self.grab_accounts()
        self.butt_height = 0.8
        all_butts = {}
        for ind in range(len(usernames)):
            all_butts[f'butt{ind}'] = Button(text=usernames[ind], size_hint = (0.2, 0.1),
            font_size = 25, pos_hint = {'x':0.1, 'y':self.butt_height}, background_color=(0,0,0,1))
            all_butts[f'butt{ind}'].bind(on_release= self.open_acc)
            self.add_widget(all_butts[f'butt{ind}'])
            self.butt_height -= 0.1
        for x in all_butts.keys():
            def save_info(self, x=x):
                with open('.\\req files\\usernames.txt', 'w') as file:
                    file.write(all_butts[x].text)
            all_butts[x].bind(on_press=save_info)
        self.delete_accs_butt = Button(text='Delete all Accounts', size_hint=(0.26,0.1),
        pos_hint={'x':0.73, 'y':0.08},font_size=23)
        self.delete_accs_butt.bind(on_press=self.delete_accounts)
        self.add_widget(self.delete_accs_butt)
        self.deleted_message = Label(text='All existing accounts deleted..',
        pos_hint={'x':0, 'y':-0.25})


    def grab_accounts(self):
        my_f = open('.\\req files\\usernames and passwords.txt', 'r')
        text = my_f.readlines()
        plain_text = [re.sub('\n','', line) for line in text]
        all_dict = [ast.literal_eval(line) for line in plain_text]
        all_usernames = [each['username'] for each in all_dict]
        return all_usernames

    def open_acc(self, ins):
        diary.screenmanager.current = 'PasswordPage'
        diary.screenmanager.transition.direction = 'left' 

    def back(self, ins):
        diary.screenmanager.current = 'WelcomePage'
        diary.screenmanager.transition.direction = 'right'
        self.remove_widget(self.deleted_message)

    def delete_accounts(self, ins):
        with open('.\\req files\\usernames and passwords.txt', 'w') as filenew:
            filenew.write('')
        with open('.\\req files\\usernames.txt', 'w') as filenew:
            filenew.write('')
        self.add_widget(self.deleted_message)
        for root_folder, foldername, filename in os.walk('.\\req files'):
            if len(foldername) != 0:
                for folders in foldername:
                    shutil.rmtree(f'.\\req files\\{folders}')

        time.sleep(3)

class PasswordPage(FloatLayout):
    def __init__(self, **kwargs):
        super(PasswordPage, self).__init__(**kwargs)
        self.back_butt = Button(text='Back', pos_hint={'x':0.05, 'y':0.08},
        size_hint=(0.2,0.1),font_size=23)
        self.back_butt.bind(on_release=self.back)
        self.add_widget(self.back_butt)
        self.usernames_passwords = self.grab_usernames_and_passwords()
        self.add_widget(Label(text='Enter your password:', size_hint=(0.2, 0.1),
        pos_hint = {'x':0.4, 'y':0.55}, font_size=25))
        self.passw = TextInput(size_hint=(0.23, 0.05), pos_hint={'x':0.38, 'y':0.48}, multiline=False)
        self.add_widget(self.passw)
        self.enter_acc_butt = Button(text='Enter the Account', size_hint=(0.25, 0.1),
        pos_hint = {'x':0.72, 'y':0.08},font_size=23)
        self.enter_acc_butt.bind(on_release=self.verify_password)
        self.add_widget(self.enter_acc_butt)
        self.incorrect_password = Label(text='Check the password motherfucker!!',
        font_size=25, pos_hint={'x':0, 'y':-0.25})

    def back(self, ins):
        diary.screenmanager.current = 'AllAccsPage'
        diary.screenmanager.transition.direction = 'right'
        self.remove_widget(self.incorrect_password)

    def grab_usernames_and_passwords(self):
        my_f = open('.\\req files\\usernames and passwords.txt', 'r')
        text = my_f.readlines()
        plain_text = [re.sub('\n','', line) for line in text]
        all_usernames_passwords = [ast.literal_eval(line) for line in plain_text]
        usernames = [el['username'] for el in all_usernames_passwords]
        passwords = [el['password'] for el in all_usernames_passwords]
        usernames_to_passwords = dict(zip(usernames, passwords))
        return usernames_to_passwords

    def verify_password(self, ins):
        with open('.\\req files\\usernames.txt', 'r') as fil:
            clicked_username = fil.read()
            if self.passw.text == self.usernames_passwords[clicked_username]:
                diary.screenmanager.current = 'DatesPage'
                diary.screenmanager.transition.direction = 'left'
            else:
                self.add_widget(self.incorrect_password)
            self.passw.text=''
                



class DatesPage(FloatLayout):
    def __init__(self, **kwargs):
        super(DatesPage, self).__init__(**kwargs)
        self.add_butt = Button(text='Add New', size_hint=(0.2, 0.1),
        pos_hint={'x':0.75, 'y':0.83},font_size=23)
        self.add_butt.bind(on_press=self.add_entry)
        self.add_widget(self.add_butt)
        self.back_butt = Button(text='Back', size_hint=(0.2, 0.1), pos_hint={'x':0.08, 'y':0.83},
        font_size=23)
        self.back_butt.bind(on_press=self.go_back)
        self.add_widget(self.back_butt)

    def add_entry(self, ins):
        diary.screenmanager.current = 'NewEntryPage'    
        diary.screenmanager.transition.direction = 'left'
    def go_back(self, ins):
        diary.screenmanager.current = 'AllAccsPage'
        diary.screenmanager.transition.direction = 'right'
    def get_user_dates(self):
        with open('.\\req files\\usernames.txt', 'r') as file:
            username = file.read()
        for root, folders, files in os.walk(f'.\\req files\\{username}'):
            files = files
        files = [re.sub('.txt', '', file) for file in files]
        return files, username



class NewEntryPage(FloatLayout):
    def __init__(self, **kwargs): 
        super(NewEntryPage, self).__init__(**kwargs)
        self.back_butt = Button(text='Back', font_size=23, size_hint=(0.2, 0.1), pos_hint={'x':0.75, 'y':0.05})
        self.back_butt.bind(on_press=self.go_back)
        self.add_widget(self.back_butt)
        current_date = datetime.datetime.now()
        self.just_date = current_date.strftime('%d %B %Y, %A')
        self.just_time = current_date.strftime('%H:%M') 
        self.add_widget(Label(text=f'{self.just_date}\n{self.just_time}', font_size=24,
        pos_hint={'x':-0.3, 'y':0.4}))
        self.main_text = TextInput(size_hint=(0.95, 0.6), pos_hint = {'x':0.025 , 'y':0.2},
        font_size=22)
        self.add_widget(self.main_text)
        self.save_butt = Button(text='Save', font_size=23, pos_hint={'x':0.05, 'y':0.05}, size_hint=(0.2, 0.1))
        self.save_butt.bind(on_press=self.save_info)    
        self.add_widget(self.save_butt)
        self.saved_message = Label(text='Your entry got saved', font_size = 24,
        pos_hint={'x':0, 'y':-0.35})

    def go_back(self, ins):
        diary.screenmanager.current = 'DatesPage'
        diary.screenmanager.transition.direction = 'right'
    def save_info(self, ins):
        with open('.\\req files\\usernames.txt', 'r') as file:
            username = file.read()
        with open(f'.\\req files\\{username}\\{self.just_date}.txt', 'w') as date_file:
            date_file.write(f'{self.just_date}\n{self.just_time}\n\n{self.main_text.text}')
        self.add_widget(self.saved_message)
        time.sleep(2)
        self.remove_widget(self.saved_message)
        diary.screenmanager.current = 'DatesPage'
        diary.screenmanager.transition.direction = 'right'

class DiaryApp(App):
    def build(self):    
        self.screenmanager = ScreenManager()
        self.create_screen('welcomepage', 'WelcomePage', WelcomePage)
        self.create_screen('newaccpage', 'NewAccPage', NewAccPage)
        self.create_screen('allaccspage', 'AllAccsPage', AllAccsPage)
        self.create_screen('passwordpage', 'PasswordPage', PasswordPage)
        self.create_screen('datespage', 'DatesPage', DatesPage)
        self.create_screen('newentrypage', 'NewEntryPage', NewEntryPage)
        return self.screenmanager
        
    def create_screen(self, var_name,name, classs):
        self.var_name = classs()
        self.screen = Screen(name=name)
        self.screen.add_widget(self.var_name)
        self.screenmanager.add_widget(self.screen)


if __name__=='__main__':
    diary = DiaryApp()
    diary.run()