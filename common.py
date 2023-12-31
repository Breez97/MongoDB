from functions import *

database = MongoClient()
collections = database['DB'].list_collection_names()
collectionToExclude = 'JoinedCollections'
filteredCollections = [col for col in collections if col != collectionToExclude]
collections = filteredCollections


#Функция добавления вакансий (главная коллекция)
def addingVacancyCollection(vacancyNameEntry, vacancyDescriptionEntry, salaryEntry, currentStatus):
    vacancyNameAdd = vacancyNameEntry.get()
    vacancyDescriptionAdd = vacancyDescriptionEntry.get("1.0", "end-1c")
    salaryAdd = int(salaryEntry.get())
    if vacancyNameAdd == '' or vacancyDescriptionAdd == '' or salaryAdd == '':
        showerror(title='Ошибка', message='Заполните все данные')
    else:
        existingDocument = database['DB']['VacancyDocument'].count_documents({'Title': vacancyNameAdd})
        if existingDocument > 0:
            showerror(title='Ошибка', message='Такая вакансия уже зарегистрирована')
        else:
            dictAdd = {'Title': vacancyNameAdd, 'VacancyDescription': vacancyDescriptionAdd, 'Salary': salaryAdd, 'Status': bool(currentStatus)}
            database['DB']['VacancyDocument'].insert_one(dictAdd)
            showinfo(title='Инфо', message='Данные успешно добавлены')

#Функция добавления компаний (зависимая коллекция)
def addingEmployerCollection(currentTitle, companyNameEntry, companyDescriptionEntry, addressCityEntry, addressStreetEntry, addressHouseEntry):
    record = database['DB']['VacancyDocument'].find_one({'Title': currentTitle})
    companyNameAdd = companyNameEntry.get()
    companyDescriptionAdd = companyDescriptionEntry.get("1.0", "end-1c")
    addressCityAdd = addressCityEntry.get()
    addressStreetAdd = addressStreetEntry.get()
    addressHouseAdd = int(addressHouseEntry.get())
    if(companyNameAdd == '' or companyDescriptionAdd == '' or addressCityAdd == '' or addressStreetAdd == '' or addressHouseAdd == ''):
        showerror(title='Ошибка', message='Заполните все данные')
    else:
        existingDocument = database['DB']['EmployerDocument'].count_documents({'VacancyDocument_id': record['_id'], 'CompanyName': companyNameAdd, 'CompanyDescription': companyDescriptionAdd, 'AddressCity': addressCityAdd, 'AddressStreet': addressStreetAdd, 'AddressHouse': addressHouseAdd})
        if existingDocument > 0:
            showerror(title='Ошибка', message='Такая компания уже зарегистрирована на данную вакансию')
        else:
            dictAdd = {'VacancyDocument_id' : record['_id'], 'CompanyName': companyNameAdd, 'CompanyDescription': companyDescriptionAdd, 'AddressCity': addressCityAdd, 'AddressStreet': addressStreetAdd, 'AddressHouse': addressHouseAdd}
            database['DB']['EmployerDocument'].insert_one(dictAdd)
            showinfo(title='Инфо', message='Данные успешно добавлены')


#Функция добавления кандидата (зависимая коллекция)
def addingCandidateCollection(currentTitle, candidateNameEntry, currentGender, dateOfBirthEntry, stageEntry, phoneNumberEntry):
    record = database['DB']['VacancyDocument'].find_one({'Title': currentTitle})
    candidateNameAdd = candidateNameEntry.get()
    dateOfBirthAdd = dateOfBirthEntry.get()
    stageAdd = int(stageEntry.get())
    phoneNumberAdd = int(phoneNumberEntry.get())
    if(candidateNameAdd == '' or dateOfBirthAdd == '' or stageAdd == '' or phoneNumberAdd == ''):
        showerror(title='Ошибка', message='Заполните все данные')
    else:
        existingDocument = database['DB']['CandidateDocument'].count_documents({'VacancyDocument_id': record['_id'], 'Name': candidateNameAdd, 'Gender': currentGender, 'DateOfBirth': dateOfBirthAdd, 'Stage': stageAdd, 'PhoneNumber': phoneNumberAdd})
        if existingDocument > 0:
            showerror(title='Ошибка', message='Такой кандидат уже зарегистрирован на данную вакансию')
        else:
            dictAdd = {'VacancyDocument_id': record['_id'], 'Name': candidateNameAdd, 'Gender': currentGender, 'DateOfBirth': dateOfBirthAdd, 'Stage': stageAdd, 'PhoneNumber': phoneNumberAdd}
            database['DB']['CandidateDocument'].insert_one(dictAdd)
            showinfo(title='Инфо', message='Данные успешно добавлены')

#Функция измения вакансии (главная коллекция)
def updateVacancyCollection(oldTitle, vacancyNameEntry, vacancyDescriptionEntry, salaryEntry, currentStatus):
    vacancyNameUpdate = vacancyNameEntry.get()
    vacancyDescriptionUpdate = vacancyDescriptionEntry.get("1.0", "end-1c")
    salaryUpdate = int(salaryEntry.get())
    if(vacancyNameUpdate == '' or vacancyDescriptionUpdate == '' or salaryUpdate == ''):
        showerror(title='Ошибка', message='Заполните все данные')
    else:
        existingDocument = database['DB']['VacancyDocument'].count_documents({'Title': vacancyNameUpdate})
        if existingDocument > 0:
            showerror(title='Ошибка', message='Вакансия с таким именем уже зарегистрирована')
        else:
            oldValues = {'Title': oldTitle}
            newValues = {'$set' : {'Title': vacancyNameUpdate, 'VacancyDescription': vacancyDescriptionUpdate, 'Salary': salaryUpdate, 'Status': bool(currentStatus)}}
            database['DB']['VacancyDocument'].update_one(oldValues, newValues)
            showinfo(title='Инфо', message='Данные успешно обновлены')

#Функция изменения компании (зависимая коллекция)
def updateEmployerCollection(oldCompanyName, currentTitle, companyNameEntry, companyDescriptionEntry, addressCityEntry, addressStreetEntry, addressHouseEntry):
    record = database['DB']['VacancyDocument'].find_one({'Title': currentTitle})
    companyNameUpdate = companyNameEntry.get()
    companyDescriptionUpdate = companyDescriptionEntry.get("1.0", "end-1c")
    addressCityUpdate = addressCityEntry.get()
    addressStreetUpdate = addressStreetEntry.get()
    addressHouseUpdate = int(addressHouseEntry.get())
    if(companyNameUpdate == '' or companyDescriptionUpdate == '' or addressCityUpdate == '' or addressStreetUpdate == '' or addressHouseUpdate == ''):
        showerror(title='Ошибка', message='Заполните все данные')
    else:
        existingDocument = database['DB']['EmployerDocument'].count_documents({'VacancyDocument_id': record['_id'], 'CompanyName': companyNameUpdate, 'CompanyDescription': companyDescriptionUpdate, 'AddressCity': addressCityUpdate, 'AddressStreet': addressStreetUpdate, 'AddressHouse': addressHouseUpdate})
        if existingDocument > 0:
            showerror(title='Ошибка', message='Такая компания уже зарегистрирована на данную вакансию')
        else:
            oldValues = {'CompanyName': oldCompanyName}
            newValues = {'$set' : {'VacancyDocument_id': record['_id'], 'CompanyName': companyNameUpdate, 'CompanyDescription': companyDescriptionUpdate, 'AddressCity': addressCityUpdate, 'AddressStreet': addressStreetUpdate, 'AddressHouse': addressHouseUpdate}}
            database['DB']['EmployerDocument'].update_one(oldValues, newValues)
            showinfo(title='Инфо', message='Данные успешно обновлены')

#Функция изменения кандидата (зависимая коллекция)
def updateCandidateCollection(oldName, currentTitle, candidateNameEntry, currentGender, dateOfBirthEntry, stageEntry, phoneNumberEntry):
    record = database['DB']['VacancyDocument'].find_one({'Title': currentTitle})
    candidateNameUpdate = candidateNameEntry.get()
    dateOfBirthUpdate = dateOfBirthEntry.get()
    stageUpdate = int(stageEntry.get())
    phoneNumberUpdate = int(phoneNumberEntry.get())
    if(candidateNameUpdate == '' or dateOfBirthUpdate == '' or stageUpdate == ''):
        showerror(title='Ошибка', message='Заполните все данные')
    else:
        existingDocument = database['DB']['CandidateDocument'].count_documents({'VacancyDocument_id': record['_id'], 'Name': candidateNameUpdate, 'Gender': currentGender, 'DateOfBirth': dateOfBirthUpdate, 'Stage': stageUpdate, 'PhoneNumber': phoneNumberUpdate})
        if existingDocument > 0:
            showerror(title='Ошибка', message='Такой кандидат уже зарегистрирован на данную вакансию')
        else:
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
    salaryAdd = int(salaryEntry.get())
    if(vacancyNameAdd == '' or vacancyDescriptionAdd == '' or salaryAdd == ''):
        showerror(title='Ошибка', message='Заполните все данные')
    else:
        existingDocument = database['DB']['DenormalizedDocument'].count_documents({'Title': vacancyNameAdd})
        if existingDocument > 0:
            showerror(title='Ошибка', message='Вакансия с таким названием уже существует')
        else:
            dictAdd = {'Title': vacancyNameAdd, 'VacancyDescription': vacancyDescriptionAdd, 'Salary': salaryAdd, 'Status': bool(currentStatus), "Employers": [], "Candidates": []}
            database['DB']['DenormalizedDocument'].insert_one(dictAdd)
            showinfo(title='Инфо', message='Данные успешно добавлены')

#Функция добавления компании (денормализованная коллекция)
def addingEmployerDenormalized(currentTitle, companyNameEntry, companyDescriptionEntry, addressCityEntry, addressStreetEntry, addressHouseEntry):
    companyNameAdd = companyNameEntry.get()
    companyDescriptionAdd = companyDescriptionEntry.get("1.0", "end-1c")
    addressCityAdd = addressCityEntry.get()
    addressStreetAdd = addressStreetEntry.get()
    addressHouseAdd = int(addressHouseEntry.get())
    if(companyNameAdd == '' or companyDescriptionAdd == '' or addressCityAdd == '' or addressStreetAdd == '' or addressHouseAdd == ''):
        showerror(title='Ошибка', message='Заполните все данные')
    else:
        existingDocument = database['DB']['DenormalizedDocument'].count_documents({'Title': currentTitle, 'Employers.CompanyName': companyNameAdd, 'Employers.CompanyDescription': companyDescriptionAdd, 'Employers.AddressCity': addressCityAdd, 'Employers.AddressStreet': addressStreetAdd, 'Employers.AddressHouse': addressHouseAdd})
        if existingDocument > 0:
            showerror(title='Ошибка', message='Компания с таким названием уже существует')
        else:
            dictAdd = {'CompanyName': companyNameAdd, 'CompanyDescription': companyDescriptionAdd, 'AddressCity': addressCityAdd, 'AddressStreet': addressStreetAdd, 'AddressHouse': addressHouseAdd}
            filterCheck = {'Title': currentTitle}
            updateOperation = {
                '$push': {
                    'Employers': dictAdd
                }
            }
            database['DB']['DenormalizedDocument'].update_one(filterCheck, updateOperation)
            showinfo(title='Инфо', message='Данные успешно добавлены')

#Функция добавления кандидата (денормализованная коллекция)
def addingCandidateDenormalized(currentTitle, candidateNameEntry, currentGender, dateOfBirthEntry, stageEntry, phoneNumberEntry):
    candidateNameAdd = candidateNameEntry.get()
    dateOfBirthAdd = dateOfBirthEntry.get()
    stageAdd = int(stageEntry.get())
    phoneNumberAdd = int(phoneNumberEntry.get())
    if(candidateNameAdd == '' or dateOfBirthAdd == '' or stageAdd == '' or phoneNumberAdd == ''):
        showerror(title='Ошибка', message='Заполните все данные')
    else:
        existingDocument = database['DB']['DenormalizedDocument'].count_documents({'Title': currentTitle, 'Candidates.Name': candidateNameAdd, 'Candidates.Gender': currentGender, 'Candidates.DateOfBirth': dateOfBirthAdd, 'Candidates.Stage': stageAdd, 'Candidates.PhoneNumber': phoneNumberAdd})
        if existingDocument > 0:
            showerror(title='Ошибка', message='Кандидат с таким именем уже существует')
        else:
            dictAdd = {'Name': candidateNameAdd, 'Gender': currentGender, 'DateOfBirth': dateOfBirthAdd, 'Stage': stageAdd, 'PhoneNumber': phoneNumberAdd}
            filterCheck = {'Title': currentTitle}
            updateOperation = {
                '$push': {
                    'Candidates': dictAdd
                }
            }
            database['DB']['DenormalizedDocument'].update_one(filterCheck, updateOperation)
            showinfo(title='Инфо', message='Данные успешно добавлены')

#Функция обновления данных вакансии (денормализованная коллекция)
def updateVacancyCollectionDenormalized(oldTitle, vacancyNameEntry, vacancyDescriptionEntry, salaryEntry, currentStatus):
    vacancyNameUpdate = vacancyNameEntry.get()
    vacancyDescriptionUpdate = vacancyDescriptionEntry.get("1.0", "end-1c")
    salaryUpdate = int(salaryEntry.get())
    if(vacancyNameUpdate == '' or vacancyDescriptionUpdate == '' or salaryUpdate == ''):
        showerror(title='Ошибка', message='Заполните все данные')
    else:
        existingDocument = database['DB']['DenormalizedDocument'].count_documents({'Title': vacancyNameUpdate})
        if existingDocument > 0:
            showerror(title='Ошибка', message='Вакансия с таким названием уже существует')
        else:
            oldValues = {'Title': oldTitle}
            newValues = {'$set' : {'Title': vacancyNameUpdate, 'VacancyDescription': vacancyDescriptionUpdate, 'Salary': salaryUpdate, 'Status': bool(currentStatus)}}
            database['DB']['DenormalizedDocument'].update_one(oldValues, newValues)
            showinfo(title='Инфо', message='Данные успешно обновлены')

#Функция обновления данных компании (денормализованная коллекиця)
def updateEmployerCollectionDenormalized(currentVacancy, oldName, companyNameEntry, companyDescriptionEntry, addressCityEntry, addressStreetEntry, addressHouseEntry):
    companyNameUpdate = companyNameEntry.get()
    companyDescriptionUpdate = companyDescriptionEntry.get("1.0", "end-1c")
    addressCityUpdate = addressCityEntry.get()
    addressStreetUpdate = addressStreetEntry.get()
    addressHouseUpdate = int(addressHouseEntry.get())
    if(companyNameUpdate == '' or companyDescriptionUpdate == '' or addressCityUpdate == '' or addressStreetUpdate == '' or addressHouseUpdate == ''):
        showerror(title='Ошибка', message='Заполните все данные')
    else:
        existingDocument = database['DB']['DenormalizedDocument'].count_documents({'Title': currentVacancy, 'Employers.CompanyName': companyNameUpdate, 'Employers.CompanyDescription': companyDescriptionUpdate, 'Employers.AddressCity': addressCityUpdate, 'Employers.AddressStreet': addressStreetUpdate, 'Employers.AddressHouse': addressHouseUpdate})
        if existingDocument > 0:
            showerror(title='Ошибка', message='Компания с таким названием уже зарегистрирована на данную вакансию')
        else:
            database['DB']['DenormalizedDocument'].update_one(
                {'Title': currentVacancy, 'Employers.CompanyName': oldName},
                {'$set': {
                    'Employers.$.CompanyName': companyNameUpdate,
                    'Employers.$.CompanyDescription': companyDescriptionUpdate,
                    'Employers.$.AddressCity': addressCityUpdate,
                    'Employers.$.AddressStreet': addressStreetUpdate,
                    'Employers.$.AddressHouse': addressHouseUpdate
                    }
                }
            )
            showinfo(title='Инфо', message='Данные успешно обновлены')

#Функция обновления данных кандидата (денормализованная коллекция)
def updateCandidateCollectionDenormalized(currentVacancy, oldName, candidateNameEntry, currentGender, dateOfBirthEntry, stageEntry, phoneNumberEntry):
    candidateNameUpdate = candidateNameEntry.get()
    dateOfBirthUpdate = dateOfBirthEntry.get()
    stageUpdate = int(stageEntry.get())
    phoneNumberUpdate = int(phoneNumberEntry.get())
    if(candidateNameUpdate == '' or dateOfBirthUpdate == '' or stageUpdate == '' or phoneNumberUpdate == ''):
        showerror(title='Ошибка', message='Заполните все данные')
    else:
        existingDocument = database['DB']['DenormalizedDocument'].count_documents({'Title': currentVacancy, 'Candidates.Name': candidateNameUpdate, 'Candidates.Gender': currentGender, 'Candidates.DateOfBirth': dateOfBirthUpdate, 'Candidates.Stage': stageUpdate, 'Candidates.PhoneNumber': phoneNumberUpdate})
        database['DB']['DenormalizedDocument'].update_one(
            {'Title': currentVacancy, 'Candidates.Name': oldName},
            {'$set': {
                'Candidates.$.Name': candidateNameUpdate,
                'Candidates.$.Gender': currentGender,
                'Candidates.$.DateOfBirth': dateOfBirthUpdate,
                'Candidates.$.Stage': stageUpdate,
                'Candidates.$.PhoneNumber': phoneNumberUpdate
                }
            }
        )
        showinfo(title='Инфо', message='Данные успешно обновлены')

#Функция удаления вакансии (денормализованная коллекция)
def deleteVacancyCollectionDenormalized(currentVacancy):
    deleteVacancyValues = {'Title': currentVacancy}
    database['DB']['DenormalizedDocument'].delete_one(deleteVacancyValues)
    showinfo(title='Инфо', message='Данные успешно удалены')

#Функция удаления компании (денормализованная коллекция)
def deleteEmployerCollectionDenormalized(oldValues, currentVacancy):
    database['DB']['DenormalizedDocument'].update_one({'Title': currentVacancy}, {'$pull': {'Employers' : {'CompanyName': oldValues['CompanyName']}}})
    showinfo(title='Инфо', message='Данные успешно удалены')

#Функция удаления кандидата (денормализованная коллекция)
def deleteCandidateCollectionDenormalized(oldValues, currentVacancy):
    database['DB']['DenormalizedDocument'].update_one({'Title': currentVacancy}, {'$pull': {'Candidates' : {'Name': oldValues['Name']}}})
    showinfo(title='Инфо', message='Данные успешно удалены')

#Функция объединения коллекций (JOIN)
def joinCollections():
    client = MongoClient()
    session = client.start_session()
    db = database['DB']
    database['DB']['JoinedCollections'].drop()
    
    result = db['VacancyDocument'].aggregate([
        {
            '$lookup': {
                'from': 'EmployerDocument',
                'localField': '_id',
                'foreignField': 'VacancyDocument_id',
                'as': 'employers'
            }
        },
        {
            '$lookup': {
                'from': 'CandidateDocument',
                'localField': '_id',
                'foreignField': 'VacancyDocument_id',
                'as': 'candidates'
            }
        },
        {
            '$project': {
                '_id': 1,
                'Title': 1,
                'VacancyDescription': 1,
                'Salary': 1,
                'Status': 1,
                'employers': {
                    'CompanyName': 1,
                    'CompanyDescription': 1,
                    'AddressCity': 1,
                    'AddressStreet': 1,
                    'AddressHouse': 1
                },
                'candidates': {
                    'Name': 1,
                    'Gender': 1,
                    'DateOfBirth': 1,
                    'Stage': 1,
                    'PhoneNumber': 1,
                }
            }
        }
    ])
    
    documents_to_insert = list(result)
    
    with session.start_transaction():
        db['JoinedCollections'].insert_many(documents_to_insert)
    session.end_session()
