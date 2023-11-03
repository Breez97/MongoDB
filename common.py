from tkinter import *
from tkinter import ttk
from pymongo import MongoClient
from tkinter.messagebox import showerror, showinfo

database = MongoClient()
collections = database['DB'].list_collection_names()

#Изменение размера окна в зависимости от количества коллекций
def windowSize(collections):
    resizeY = 110
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
def addingVacancyCollection(vacancyNameEntry, vacancyDescriptionEntry, salaryEntry, currentStatus):
    vacancyNameAdd = vacancyNameEntry.get()
    vacancyDescriptionAdd = vacancyDescriptionEntry.get("1.0", "end-1c")
    salaryAdd = salaryEntry.get()
    if(vacancyNameAdd == '' or vacancyDescriptionAdd == '' or salaryAdd == ''):
        showerror(title='Ошибка', message='Заполните все данные')
    else:
        dictAdd = {'Title': vacancyNameAdd, 'VacancyDescription': vacancyDescriptionAdd, 'Salary': salaryAdd, 'Status': currentStatus}
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


#Функция добавления кандидата (зависимая коллекция)
def addingCandidateCollection(currentTitle, candidateNameEntry, currentGender, dateOfBirthEntry, stageEntry, phoneNumberEntry):
    candidateNameAdd = candidateNameEntry.get()
    dateOfBirthAdd = dateOfBirthEntry.get()
    stageAdd = stageEntry.get()
    phoneNumberAdd = phoneNumberEntry.get()
    if(candidateNameAdd == '' or dateOfBirthAdd == '' or stageAdd == '' or phoneNumberAdd == ''):
        showerror(title='Ошибка', message='Заполните все данные')
    else:
        record = database['DB']['VacancyDocument'].find_one({'Title': currentTitle})
        dictAdd = {'VacancyDocument_id': record['_id'], 'Name': candidateNameAdd, 'Gender': currentGender, 'DateOfBirth': dateOfBirthAdd, 'Stage': stageAdd, 'PhoneNumber': phoneNumberAdd}
        database['DB']['CandidateDocument'].insert_one(dictAdd)
        showinfo(title='Инфо', message='Данные успешно добавлены')

#Функция измения вакансии (главная коллекция)
def updateVacancyCollection(oldTitle, vacancyNameEntry, vacancyDescriptionEntry, salaryEntry, currentStatus):
    vacancyNameUpdate = vacancyNameEntry.get()
    vacancyDescriptionUpdate = vacancyDescriptionEntry.get("1.0", "end-1c")
    salaryUpdate = salaryEntry.get()
    if(vacancyNameUpdate == '' or vacancyDescriptionUpdate == '' or salaryUpdate == ''):
        showerror(title='Ошибка', message='Заполните все данные')
    else:
        oldValues = {'Title': oldTitle}
        newValues = {'$set' : {'Title': vacancyNameUpdate, 'VacancyDescription': vacancyDescriptionUpdate, 'Salary': salaryUpdate, 'Status': currentStatus}}
        database['DB']['VacancyDocument'].update_one(oldValues, newValues)
        showinfo(title='Инфо', message='Данные успешно обновлены')

#Функция изменения компании (зависимая коллекция)
def updateEmployerCollection(oldCompanyName, currentTitle, companyNameEntry, companyDescriptionEntry, addressCityEntry, addressStreetEntry, addressHouseEntry):
    companyNameUpdate = companyNameEntry.get()
    companyDescriptionUpdate = companyDescriptionEntry.get("1.0", "end-1c")
    addressCityUpdate = addressCityEntry.get()
    addressStreetUpdate = addressStreetEntry.get()
    addressHouseUpdate = addressHouseEntry.get()
    if(companyNameUpdate == '' or companyDescriptionUpdate == '' or addressCityUpdate == '' or addressStreetUpdate == '' or addressHouseUpdate == ''):
        showerror(title='Ошибка', message='Заполните все данные')
    else:
        record = database['DB']['VacancyDocument'].find_one({'Title': currentTitle})
        oldValues = {'CompanyName': oldCompanyName}
        newValues = {'$set' : {'VacancyDocument_id': record['_id'], 'CompanyName': companyNameUpdate, 'CompanyDescription': companyDescriptionUpdate, 'AddressCity': addressCityUpdate, 'AddressStreet': addressStreetUpdate, 'AddressHouse': addressHouseUpdate}}
        database['DB']['EmployerDocument'].update_one(oldValues, newValues)
        showinfo(title='Инфо', message='Данные успешно обновлены')