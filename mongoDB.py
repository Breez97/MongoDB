from tkinter import *
from tkinter import ttk
from pymongo import MongoClient
from tkinter.messagebox import showerror, showinfo

def windowSize(collections):
    resizeY = 75
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


def addingVacancyCollection(collectionName, companyNameEntry, vacancyDescriptionEntry, salaryEntry, statusEntry):
    if collectionName == 'VacancyDocument':
        companyNameAdd = companyNameEntry.get()
        vacancyDescriptionAdd = vacancyDescriptionEntry.get("1.0", "end-1c")
        salaryAdd = salaryEntry.get()
        statusAdd = statusEntry.get()
        if(companyNameAdd == '' or vacancyDescriptionAdd == '' or salaryAdd == '' or statusAdd == ''):
            showerror(title='Ошибка', message='Заполните все данные')
        else:
            showinfo(title='Инфо', message='Данные успешно добавлены')
            dictAdd = {'Title': companyNameAdd, 'VacancyDescription': vacancyDescriptionAdd, 'Salary': salaryAdd, 'Status': statusAdd}
            database['DB'][f'{collectionName}'].insert_one(dictAdd)


def createWindow(collectionName):
    root = Tk()

    def buttonBackClicked():
        root.destroy()
        funcWindow(collectionName)
    
    def buttonAddClicked():
        if(collectionName == 'VacancyDocument'):
            addingVacancyCollection(collectionName, companyNameEntry, vacancyDescriptionEntry, salaryEntry, statusEntry)

    currentCollection = Label(root, text=f'Выбранная коллекция : {collectionName}', font='Arial 12 bold', bg='#FFE4C4')
    currentCollection.pack(pady=10)

    formFrame = Frame(root, bg='#FFE4C4')
    formFrame.pack(expand=True)

    if collectionName == 'VacancyDocument':
        companyName = Label(formFrame, text='Название компании : ', font='Arial 12 bold', bg='#FFE4C4')
        companyName.grid(row=0, column=0, sticky='w')
        companyNameEntry = Entry(formFrame, font='Arial 12')
        companyNameEntry.grid(row=0, column=1, sticky='w', pady=5)

        vacancyDescription = Label(formFrame, text='Описание компании : ', font='Arial 12 bold', bg='#FFE4C4')
        vacancyDescription.grid(row=1, column=0, sticky='w')
        vacancyDescriptionEntry = Text(formFrame, font='Arial 12', width=20, height=3)
        vacancyDescriptionEntry.grid(row=1, column=1, sticky='w', pady=5)

        salary = Label(formFrame, text='Размер зарплаты : ', font='Arial 12 bold', bg='#FFE4C4')
        salary.grid(row=2, column=0, sticky='w')
        salaryEntry = Entry(formFrame, font='Arial 12')
        salaryEntry.grid(row=2, column=1, sticky='w', pady=5)

        status = Label(formFrame, text='Статус : ', font='Arial 12 bold', bg='#FFE4C4')
        status.grid(row=3, column=0, sticky='w')
        statusEntry = Entry(formFrame, font='Arial 12')
        statusEntry.grid(row=3, column=1, sticky='w', pady=5)
    
    buttonAdd = Button(root, text='Добавить', command=buttonAddClicked)
    buttonAdd.pack(pady=5)
    buttonAdd.config(font='Arial 12 bold', bg='#FFCA8A')

    buttonBack = Button(root, text='Вернуться назад', command=buttonBackClicked)
    buttonBack.pack(pady=5)
    buttonBack.config(font='Arial 12 bold', bg='#FFCA8A')

    root.title('Добавление новых данных')
    root.geometry(f'400x300+550+250')
    root.resizable(False, False)
    root['bg'] = '#FFE4C4'
    root.mainloop()


def readWindow(collectionName):
    root = Tk()

    def buttonBackClicked():
        root.destroy()
        funcWindow(collectionName)

    currentCollection = Label(root, text=f'Выбранная коллекция : {collectionName}', font='Arial 12 bold', bg='#FFE4C4')
    currentCollection.pack(pady=10)

    allRecords = database['DB'][f'{collectionName}'].find()
    ySize = 150
    if collectionName == 'VacancyDocument':
        length = 0
        columns = ('Title', 'VacancyDescription', 'Salary', 'Status')
        table = ttk.Treeview(columns=columns, show='headings')
        table.pack()
        style = ttk.Style()
        style.configure("Treeview", rowheight=50)
        table.tag_configure('data', background="#EDD1AF")
        table.heading('Title', text='Название')
        table.heading('VacancyDescription', text='Описание вакансии')
        table.heading('Salary', text='Зарплата')
        table.heading('Status', text='Статус')
        table.column('#1', width=100)
        table.column('#2', width=200)
        table.column('#3', width=100)
        table.column('#4', width=100)
        for record in allRecords:
            length += 1
            ySize += 50
            title = record['Title']
            vacancyDescription = record['VacancyDescription']
            salary = record['Salary']
            status = record['Status']
            parsedRecord = (title, vacancyDescription, salary, status)
            table.insert('', END, values=parsedRecord, tags=('data',))
        table['height'] = length
    
    if collectionName == 'EmployerDocument':
        length = 0
        columns = ('CompanyName', 'CompanyDescription', 'AddressCity', 'AddressStreet', 'AddressHouse')
        table = ttk.Treeview(columns=columns, show='headings')
        table.pack()
        style = ttk.Style()
        style.configure("Treeview", rowheight=50)
        table.tag_configure('data', background="#EDD1AF")
        table.heading('CompanyName', text='Название компании')
        table.heading('CompanyDescription', text='Описание компании'),
        table.heading('AddressCity', text='Город')
        table.heading('AddressStreet', text='Улица'),
        table.heading('AddressHouse', text='Дом')
        table.column('#1', width=100)
        table.column('#2', width=200)
        table.column('#3', width=70)
        table.column('#4', width=50)
        table.column('#5', width=50)
        for record in allRecords:
            length += 1
            ySize += 50
            companyName = record['CompanyName']
            companyDescription = record['CompanyDescription']
            addressCity = record['AddressCity']
            addressStreet = record['AddressStreet']
            addressHouse = record['AddressHouse']
            parsedRecord = (companyName, companyDescription, addressCity, addressStreet, addressHouse)
            table.insert('', END, values=parsedRecord, tags=('data',))
        table['height'] = length
    
    if collectionName == 'CandidateDocument':
        length = 0
        columns = ('Name', 'Gender', 'DateOfBirth', 'Stage', 'PhoneNumber')
        table = ttk.Treeview(columns=columns, show='headings')
        table.pack()
        style = ttk.Style()
        style.configure("Treeview", rowheight=50)
        table.tag_configure('data', background="#EDD1AF")
        table.heading('Name', text='ФИО кандидата')
        table.heading('Gender', text='Пол')
        table.heading('DateOfBirth', text='Дата рождения')
        table.heading('Stage', text='Опыт работы')
        table.heading('PhoneNumber', text='Номер телефона')
        table.column('#1', width=130)
        table.column('#2', width=80)
        table.column('#3', width=120)
        table.column('#4', width=80)
        table.column('#5', width=150)
        for record in allRecords:
            length += 1
            ySize += 50
            name = record['Name']
            gender = record['Gender']
            dateOfBirth = record['DateOfBirth']
            stage = record['Stage']
            phoneNumber = record['PhoneNumber']
            parsedRecord = (name, gender, dateOfBirth, stage, phoneNumber)
            table.insert('', END, values=parsedRecord, tags=('data',))
        table['height'] = length

    buttonBack = Button(root, text='Вернуться назад', command=buttonBackClicked)
    buttonBack.pack(pady=5)
    buttonBack.config(font='Arial 12 bold', bg='#FFCA8A')

    root.title('Просмотр данных')
    root.geometry(f'600x{ySize}+550+250')
    root.resizable(True, False)
    root['bg'] = '#FFE4C4'
    root.mainloop()


def updateWindow(collectionName):
    root = Tk()
    root.title('Обновление данных')
    root.geometry(f'400x400+550+250')
    root.resizable(False, False)
    root['bg'] = '#FFE4C4'
    root.mainloop()


def buttonDeleteClicked(collectionName):
    root = Tk()
    root.title('Обновление данных')
    root.geometry(f'400x400+550+250')
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

    buttonCreate = Button(root, text='Создать (CREATE)', command=buttonCreateClicked)
    buttonCreate.pack(pady=5)
    buttonCreate.config(font='Arial 12 bold', bg='#FFCA8A')

    buttonRead = Button(root, text='Прочитать (READ)', command=buttonReadClicked)
    buttonRead.pack(pady=5)
    buttonRead.config(font='Arial 12 bold', bg='#FFCA8A')

    buttonUpdate = Button(root, text='Обновить (UPDATE)', command=buttonUpdateClicked)
    buttonUpdate.pack(pady=5)
    buttonUpdate.config(font='Arial 12 bold', bg='#FFCA8A')

    buttonDelete = Button(root, text='Удалить (DELETE)', command=buttonDeleteClicked)
    buttonDelete.pack(pady=5)
    buttonDelete.config(font='Arial 12 bold', bg='#FFCA8A')

    buttonBack = Button(root, text='Вернуться назад', command=buttonBackClicked)
    buttonBack.pack(pady=5)
    buttonBack.config(font='Arial 12 bold', bg='#FFCA8A')

    root.title('Окно взаимодействия с базой данных')
    root.geometry(f'400x250+550+250')
    root.resizable(False, False)
    root['bg'] = '#FFE4C4'
    root.mainloop()

#Подключение к окну выбора функции
def connectionFuncWindow(collectionName):
    funcWindow(collectionName)


#Главное окно для выбора коллекции для подключения
def mainUI():

    #Кнопка подключения
    def buttonClicked():
        collectionName = comboBoxCollections.get()
        root.destroy()
        connectionFuncWindow(collectionName)

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
    buttonConnection.pack(pady=10)
    buttonConnection.config(font='Arial 12 bold', bg='#FFCA8A')
    
    root.title('Окно взаимодействия с базой данных')
    root.geometry(f'400x{sizeY}+550+250')
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
