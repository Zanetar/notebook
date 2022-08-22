import textwrap
import fileinput
import sys
import os.path
class User:
    def __init__(self,name,last_name,name_of_document):
        self.name=name
        self.last_name=last_name
        self.name_of_document=name_of_document

def make_user():
    user = User(input('Wpisz swoje imię'), input('Wpisz swoje nawisko'), input('nazwa dokumentu'))
    return user.name_of_document

    def __repr__(self):
        return (f'to jest użytkownik:{self.name} {self.last_name}.')




class Notebook:
    def __init__(self,name):
        self.name=name

    def read(self):
        print('Podaj nazwę dokumentu')
        f = input('podaj nazwę')
        f = open(f, 'r')
        f = f.readline()
        print(f)
        return f

    def add(self):
        user=input('wpisz nazwę pliku, który chcesz nadpisać')
        print('Dodaj notatkę, aby zakończyć, wybierz enter')
        file_exists = os.path.exists(user)
        if file_exists==False:
            print('Nie ma takiego pliku')
        else:
            f = open(user, 'a')
            words = ' ' + input()
            wrapper = textwrap.TextWrapper(width=180)
            text = wrapper.fill(text=words)
            f.write(text)
            f.close()
            f = open(user)
            f = f.readline()
            print('Twoja cała notatka, to:')
            print(f)
    def write(self):
        user = make_user()
        print('Wpisz swoją notatkę, aby zakończyć, wybierz enter')
        f = open(user, 'w')
        words = input()
        wrapper = textwrap.TextWrapper(width=180)
        text = wrapper.fill(text=words)
        f.write(text)
        f.close()
        f = open(user)
        f = f.readline()
        print('Twoja cała notatka, to:')
        print(f)
        return f

    def menu(self):
        try:
            while True:
                print('Co chcesz zrobić?')
                print('1-Nowy dokument')
                print('2. Nadpisz stary dokument')
                print('3. Odczytać dokument')
                print('x- Wyjście')
                choice=input().upper()
                if choice=='X':
                    print('Do widzenia!')
                    break
                else:
                    choice=int(choice)
                    if choice==1:
                        self.write()
                    elif choice==2:
                        self.add()
                    elif choice==3:
                        self.read()
                    else:
                        print('Wybrałeś zły znak. Do widzenia')
                        break
        except ValueError:
            print('Wprowadzono zły znak.')

notebook1=Notebook('notebook')

notebook1.menu()




