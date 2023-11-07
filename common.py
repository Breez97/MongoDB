from tkinter import *
from tkinter import ttk
from pymongo import MongoClient, UpdateOne
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

#Функция изменения кандидата (зависимая коллекция)
def updateCandidateCollection(oldName, currentTitle, candidateNameEntry, currentGender, dateOfBirthEntry, stageEntry, phoneNumberEntry):
    candidateNameUpdate = candidateNameEntry.get()
    dateOfBirthUpdate = dateOfBirthEntry.get()
    stageUpdate = stageEntry.get()
    phoneNumberUpdate = phoneNumberEntry.get()
    if(candidateNameUpdate == '' or dateOfBirthUpdate == '' or stageUpdate == ''):
        showerror(title='Ошибка', message='Заполните все данные')
    else:
        record = database['DB']['VacancyDocument'].find_one({'Title': currentTitle})
        oldValues = {'Name': oldName}
        newValues = {'$set': {'VacancyDocument_id': record['_id'], 'Name': candidateNameUpdate, 'Gender': currentGender, 'DateOfBirth': dateOfBirthUpdate, 'Stage': stageUpdate, 'PhoneNumber': phoneNumberUpdate}}
        database['DB']['CandidateDocument'].update_one(oldValues, newValues)
        showinfo(title='Инфо', message='Данные успешно обновлены')

#Функция удаления вакансий (главная коллекция)
def deleteVacancyCollection(title):
    deleteVacancyValues = {'Title': title}

    currentRecord = database['DB']['VacancyDocument'].find_one({'Title': title})
    currentRecordId = currentRecord['_id']

    allRecordsEmployerCollection = database['DB']['EmployerDocument'].find()
    for record in allRecordsEmployerCollection:
        if record['VacancyDocument_id'] == currentRecordId:
            deleteEmployerValues = {'VacancyDocument_id': currentRecordId}
            database['DB']['EmployerDocument'].delete_one(deleteEmployerValues)
    
    allRecordsCandidateCollection = database['DB']['CandidateDocument'].find()
    for record in allRecordsCandidateCollection:
        if record['VacancyDocument_id'] == currentRecordId:
            deleteCandidateValues = {'VacancyDocument_id': currentRecordId}
            database['DB']['CandidateDocument'].delete_one(deleteCandidateValues)

    database['DB']['VacancyDocument'].delete_one(deleteVacancyValues)
    showinfo(title='Инфо', message='Данные успешно удалены')

#Функция удаления компаний (зависимая коллекция)
def deleteEmployerCollection(companyName):
    deleteEmployerValues = {'CompanyName': companyName}
    database['DB']['EmployerDocument'].delete_one(deleteEmployerValues)
    showinfo(title='Инфо', message='Данные успешно удалены')

#Функция удаления кандидатов (зависимая коллекция)
def deleteCandidateCollection(name):
    deleteCandidateValues = {'Name': name}
    database['DB']['CandidateDocument'].delete_one(deleteCandidateValues)
    showinfo(title='Инфо', message='Данные успешно удалены')

#Функция добавления вакансии (денормализованная коллекиция)
def addingVacancyDenormalized(vacancyNameEntry, vacancyDescriptionEntry, salaryEntry, currentStatus):
    vacancyNameAdd = vacancyNameEntry.get()
    vacancyDescriptionAdd = vacancyDescriptionEntry.get("1.0", "end-1c")
    salaryAdd = salaryEntry.get()
    if(vacancyNameAdd == '' or vacancyDescriptionAdd == '' or salaryAdd == ''):
        showerror(title='Ошибка', message='Заполните все данные')
    else:
        dictAdd = {'Title': vacancyNameAdd, 'VacancyDescription': vacancyDescriptionAdd, 'Salary': salaryAdd, 'Status': currentStatus, "Employers": [], "Candidates": []}
        database['DB']['DenormalizedDocument'].insert_one(dictAdd)
        showinfo(title='Инфо', message='Данные успешно добавлены')

#Функция добавления компании (денормализованная коллекция)
def addingEmployerDenormalized(currentTitle, companyNameEntry, companyDescriptionEntry, addressCityEntry, addressStreetEntry, addressHouseEntry):
    companyNameAdd = companyNameEntry.get()
    companyDescriptionAdd = companyDescriptionEntry.get("1.0", "end-1c")
    addressCityAdd = addressCityEntry.get()
    addressStreetAdd = addressStreetEntry.get()
    addressHouseAdd = addressHouseEntry.get()
    if(companyNameAdd == '' or companyDescriptionAdd == '' or addressCityAdd == '' or addressStreetAdd == '' or addressHouseAdd == ''):
        showerror(title='Ошибка', message='Заполните все данные')
    else:
        record = database['DB']['DenormalizedDocument'].find_one({'Title': currentTitle})
        dictAdd = {'CompanyName': companyNameAdd, 'CompanyDescription': companyDescriptionAdd, 'AddressCity': addressCityAdd, 'AddressStreet': addressStreetAdd, 'AddressHouse': addressHouseAdd}
        filterCheck = {'Title': currentTitle}
        updateOperation = {
            '$push': {
                'Employers': dictAdd
            }
        }        
        update_one = UpdateOne(filterCheck, updateOperation)
        database['DB']['DenormalizedDocument'].update_one(filterCheck, updateOperation)
        showinfo(title='Инфо', message='Данные успешно добавлены')

#Функция добавления кандидата (денормализованная коллекция)
def addingCandidateDenormalized(currentTitle, candidateNameEntry, currentGender, dateOfBirthEntry, stageEntry, phoneNumberEntry):
    candidateNameAdd = candidateNameEntry.get()
    dateOfBirthAdd = dateOfBirthEntry.get()
    stageAdd = stageEntry.get()
    phoneNumberAdd = phoneNumberEntry.get()
    if(candidateNameAdd == '' or dateOfBirthAdd == '' or stageAdd == '' or phoneNumberAdd == ''):
        showerror(title='Ошибка', message='Заполните все данные')
    else:
        record = database['DB']['VacancyDocument'].find_one({'Title': currentTitle})
        dictAdd = {'Name': candidateNameAdd, 'Gender': currentGender, 'DateOfBirth': dateOfBirthAdd, 'Stage': stageAdd, 'PhoneNumber': phoneNumberAdd}
        filterCheck = {'Title': currentTitle}
        updateOperation = {
            '$push': {
                'Candidates': dictAdd
            }
        }        
        update_one = UpdateOne(filterCheck, updateOperation)
        database['DB']['DenormalizedDocument'].update_one(filterCheck, updateOperation)
        showinfo(title='Инфо', message='Данные успешно добавлены')

#Функция обновления данных вакансии (денормализованная коллекция)
def updateVacancyCollectionDenormalized(oldTitle, vacancyNameEntry, vacancyDescriptionEntry, salaryEntry, currentStatus):
    vacancyNameUpdate = vacancyNameEntry.get()
    vacancyDescriptionUpdate = vacancyDescriptionEntry.get("1.0", "end-1c")
    salaryUpdate = salaryEntry.get()
    if(vacancyNameUpdate == '' or vacancyDescriptionUpdate == '' or salaryUpdate == ''):
        showerror(title='Ошибка', message='Заполните все данные')
    else:
        oldValues = {'Title': oldTitle}
        newValues = {'$set' : {'Title': vacancyNameUpdate, 'VacancyDescription': vacancyDescriptionUpdate, 'Salary': salaryUpdate, 'Status': currentStatus}}
        database['DB']['DenormalizedDocument'].update_one(oldValues, newValues)
        showinfo(title='Инфо', message='Данные успешно обновлены')