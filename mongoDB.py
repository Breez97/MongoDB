from tkinter import *
from tkinter import ttk
from pymongo import MongoClient
from tkinter.messagebox import showerror, showinfo

comboBoxCollections = None
database = None
collections = None

def windowSize(collections):
    resizeY = 70
    for i in range(0, len(collections)):
        resizeY += 50
    return resizeY


def availableCollections(collections):
    listAvailableCollections = ''
    for i in range(0, len(collections)):
        listAvailableCollections += f'{i + 1}. {collections[i]}'
        if(i != len(collections) - 1):
            listAvailableCollections += '\n\n'
    return listAvailableCollections


def createWindow(collectionName):
    root = Tk()
    root.title('Добавление новых данных')
    root.geometry(f'400x400')
    root.resizable(False, False)
    root['bg'] = '#FFE4C4'
    root.mainloop()


def readWindow(collectionName):
    root = Tk()
    root.title('Просмотр данных')
    root.geometry(f'400x400')
    root.resizable(False, False)
    root['bg'] = '#FFE4C4'
    root.mainloop()


def updateWindow(collectionName):
    root = Tk()
    root.title('Обновление данных')
    root.geometry(f'400x400')
    root.resizable(False, False)
    root['bg'] = '#FFE4C4'
    root.mainloop()


def buttonDeleteClicked(collectionName):
    root = Tk()
    root.title('Обновление данных')
    root.geometry(f'400x400')
    root.resizable(False, False)
    root['bg'] = '#FFE4C4'
    root.mainloop()



#Выбор функции для взаимодействия
def funcWindow(collectionName):
    def buttonCreateClicked():
        root.destroy()
        createWindow(collectionName)
    
    def buttonReadClicked():
        root.destroy()
        readWindow(collectionName)
    
    def buttonUpdateClicked():
        root.destroy()
        updateWindow(collectionName)

    
    def buttonDeleteClicked():
        root.destroy()
        deleteWindow(collectionName)
    

    def buttonBackClicked():
        root.destroy()
        mainUI()
        


    root = Tk()
    currentCollection = Label(root, text=f'Выбранная коллекция : {collectionName}', font='Arial 12 bold', bg='#FFE4C4')
    currentCollection.pack()

    buttonCreate = Button(root, text='Создать', command=buttonCreateClicked)
    buttonCreate.pack(pady=5)
    buttonCreate.config(font='Arial 12 bold', bg='#FFCA8A')

    buttonRead = Button(root, text='Прочитать', command=buttonReadClicked)
    buttonRead.pack(pady=5)
    buttonRead.config(font='Arial 12 bold', bg='#FFCA8A')

    buttonUpdate = Button(root, text='Обновить', command=buttonUpdateClicked)
    buttonUpdate.pack(pady=5)
    buttonUpdate.config(font='Arial 12 bold', bg='#FFCA8A')

    buttonDelete = Button(root, text='Удалить', command=buttonDeleteClicked)
    buttonDelete.pack(pady=5)
    buttonDelete.config(font='Arial 12 bold', bg='#FFCA8A')

    buttonBack = Button(root, text='Вернуться назад', command=buttonBackClicked)
    buttonBack.pack(pady=5)
    buttonBack.config(font='Arial 12 bold', bg='#FFCA8A')

    root.title('Окно взаимодействия с базой данных')
    root.geometry(f'400x250')
    root.resizable(False, False)
    root['bg'] = '#FFE4C4'
    root.mainloop()

#Подключение к окну выбора функции
def connectionFuncWindow(nameCollection):    
    print(database['DB'][f'{nameCollection}'].find_one({"Name": "Elizabeth Rutland"}))
    funcWindow(nameCollection)


#Главное окно для выбора коллекции для подключения
def mainUI():
    global comboBoxCollections, collections

    #Кнопка подключения
    def buttonClicked():
        nameCollection = comboBoxCollections.get()
        root.destroy()
        connectionFuncWindow(nameCollection)

    sizeY = windowSize(collections)
    root = Tk()

    textAVailable = Label(text='Available collections:', font='Arial 12 bold', bg='#FFE4C4')
    textAVailable.pack(pady=10)

    listAvailableCollections = availableCollections(collections)
    collectionsLabel = Label(text=listAvailableCollections, font='Arial 12', bg='#FFE4C4')
    collectionsLabel.pack()

    formFrame = Frame(root, bg='#FFE4C4')
    formFrame.pack(expand=True)

    collectionsVar = StringVar(value=collections[0])
    comboBoxCollections = ttk.Combobox(root, font='Arial 12', textvariable=collectionsVar, values=collections, state='readonly')
    comboBoxCollections.pack()

    buttonConnection = Button(root, text='Подключиться', command=buttonClicked)
    buttonConnection.pack(pady=5)
    buttonConnection.config(font='Arial 12 bold', bg='#FFCA8A')
    
    root.title('Окно взаимодействия с базой данных')
    root.geometry(f'400x{sizeY}')
    root.resizable(False, False)
    root['bg'] = '#FFE4C4'
    root.mainloop()


def main():
    global database, collections
    database = MongoClient()
    collections = database['DB'].list_collection_names()
    mainUI()


if __name__ == '__main__':
    main()
