from tkinter import *
from tkinter import ttk
from pymongo import MongoClient
from tkinter.messagebox import showerror, showinfo

database = MongoClient()
collections = database['DB'].list_collection_names()

#Изменение размера окна в зависимости от количества коллекций
def windowSize(collections):
    resizeY = 75
    for i in range(0, len(collections)):
        resizeY += 50
    return resizeY

#Получение списка доступных коллекций
def availableCollections(collections):
    listAvailableCollections = ''
    for i in range(0, len(collections)):
        listAvailableCollections += f'{i + 1}. {collections[i]}'
        if(i != len(collections) - 1):
            listAvailableCollections += '\n\n'
    return listAvailableCollections

#Функция добавления вакансий (главная коллекция)
def addingVacancyCollection(vacancyNameEntry, vacancyDescriptionEntry, salaryEntry, statusEntry):
    vacancyNameAdd = vacancyNameEntry.get()
    vacancyDescriptionAdd = vacancyDescriptionEntry.get("1.0", "end-1c")
    salaryAdd = salaryEntry.get()
    statusAdd = statusEntry.get()
    if(vacancyNameAdd == '' or vacancyDescriptionAdd == '' or salaryAdd == '' or statusAdd == ''):
        showerror(title='Ошибка', message='Заполните все данные')
    else:
        dictAdd = {'Title': vacancyNameAdd, 'VacancyDescription': vacancyDescriptionAdd, 'Salary': salaryAdd, 'Status': statusAdd}
        database['DB']['VacancyDocument'].insert_one(dictAdd)
        showinfo(title='Инфо', message='Данные успешно добавлены')

#Функция добавления компаний (зависимая коллекция)
def addingEmployerCollection(currentTitle, companyNameEntry, companyDescriptionEntry, addressCityEntry, addressStreetEntry, addressHouseEntry):
    companyNameAdd = companyNameEntry.get()
    companyDescriptionAdd = companyDescriptionEntry.get("1.0", "end-1c")
    addressCityAdd = addressCityEntry.get()
    addressStreetAdd = addressStreetEntry.get()
    addressHouseAdd = addressHouseEntry.get()
    if(companyNameAdd == '' or companyDescriptionAdd == '' or addressCityAdd == '' or addressStreetAdd == '' or addressHouseAdd == ''):
        showerror(title='Ошибка', message='Заполните все данные')
    else:
        record = database['DB']['VacancyDocument'].find_one({'Title': currentTitle})
        dictAdd = {'VacancyDocument_id' : record['_id'], 'CompanyName': companyNameAdd, 'CompanyDescription': companyDescriptionAdd, 'AddressCity': addressCityAdd, 'AddressStreet': addressStreetAdd, 'AddressHouse': addressHouseAdd}
        database['DB']['EmployerDocument'].insert_one(dictAdd)
        showinfo(title='Инфо', message='Данные успешно добавлены')