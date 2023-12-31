from common import *
from validation import *

#Добавление денормазилованной вакансии
def addVacancyDenormalized(collectionName):
    root = Tk()

    currentCollection = Label(root, text=f'Выбранная коллекция : {collectionName}', font='Arial 12 bold', bg='#FFE4C4')
    currentCollection.pack(pady=5)

    def buttonAddClicked():
        currentStatus = comboBoxStatuses.get()
        addingVacancyDenormalized(vacancyNameEntry, vacancyDescriptionEntry, salaryEntry, currentStatus)
    
    def buttonBackClicked():
        root.destroy()
        createWindow(collectionName)

    ySize = 310

    formFrame = Frame(root, bg='#FFE4C4')
    formFrame.pack(expand=True)

    checkNameTitle = (root.register(limitNameTitle), '%P')
    checkNumber = (root.register(limitNumber), '%P')

    vacancyName = Label(formFrame, text='Название вакансии : ', font='Arial 12 bold', bg='#FFE4C4')
    vacancyName.grid(row=0, column=0, sticky='w')
    vacancyNameEntry = Entry(formFrame, font='Arial 12')
    vacancyNameEntry.grid(row=0, column=1, sticky='w', pady=5)
    vacancyNameEntry.configure(validate='key', validatecommand=checkNameTitle)

    vacancyDescription = Label(formFrame, text='Описание вакансии : ', font='Arial 12 bold', bg='#FFE4C4')
    vacancyDescription.grid(row=1, column=0, sticky='w')
    vacancyDescriptionEntry = Text(formFrame, font='Arial 12', width=20, height=3)
    vacancyDescriptionEntry.grid(row=1, column=1, sticky='w', pady=5)

    salary = Label(formFrame, text='Размер зарплаты : ', font='Arial 12 bold', bg='#FFE4C4')
    salary.grid(row=2, column=0, sticky='w')
    salaryEntry = Entry(formFrame, font='Arial 12')
    salaryEntry.grid(row=2, column=1, sticky='w', pady=5)
    salaryEntry.configure(validate='key', validatecommand=checkNumber)

    status = Label(formFrame, text='Статус : ', font='Arial 12 bold', bg='#FFE4C4')
    status.grid(row=3, column=0, sticky='w')
    statuses = ['True', 'False']
    statusVar = StringVar(value=statuses[0])
    comboBoxStatuses = ttk.Combobox(formFrame, font='Arial 12', textvariable=statusVar, values=statuses, state='readonly')
    comboBoxStatuses.grid(row=3, column=1, sticky='w')

    buttonAdd = Button(root, text='Добавить', command=buttonAddClicked)
    buttonAdd.pack(pady=5)
    buttonAdd.config(font='Arial 12 bold', bg='#FFCA8A')

    buttonBack = Button(root, text='Вернуться назад', command=buttonBackClicked)
    buttonBack.pack(pady=5)
    buttonBack.config(font='Arial 12 bold', bg='#FFCA8A')

    root.title('Добавление новых данных')
    root.geometry(f'450x{ySize}+550+250')
    root.resizable(False, False)
    root['bg'] = '#FFE4C4'
    root.mainloop()

#Добавление денормализованной компании
def addEmployerDenormalized(collectionName):
    root = Tk()

    currentCollection = Label(root, text=f'Выбранная коллекция : {collectionName}', font='Arial 12 bold', bg='#FFE4C4')
    currentCollection.pack(pady=5)

    def buttonBackClicked():
        root.destroy()
        createWindow(collectionName)
    
    def buttonAddClicked():
        currentTitle = comboBoxTitles.get()
        addingEmployerDenormalized(currentTitle, companyNameEntry, companyDescriptionEntry, addressCityEntry, addressStreetEntry, addressHouseEntry)
    
    ySize = 400

    formFrame = Frame(root, bg='#FFE4C4')
    formFrame.pack(expand=True)

    records = database['DB']['DenormalizedDocument'].find()
    titles = []
    for record in records:
        titles.append(record['Title'])

    checkNameTitle = (root.register(limitNameTitle), '%P')
    checkNumber = (root.register(limitNumber), '%P')

    vacancyName = Label(formFrame, text='Название вакансии :', font='Arial 12 bold', bg='#FFE4C4')
    vacancyName.grid(row=0, column=0, sticky='w')
    titlesVar = StringVar(value=titles[0])
    comboBoxTitles = ttk.Combobox(formFrame, font='Arial 12', textvariable=titlesVar, values=titles, state='readonly')
    comboBoxTitles.grid(row=0, column=1, sticky='w')

    companyName = Label(formFrame, text='Название компании : ', font='Arial 12 bold', bg='#FFE4C4')
    companyName.grid(row=1, column=0, sticky='w')
    companyNameEntry = Entry(formFrame, font='Arial 12')
    companyNameEntry.grid(row=1, column=1, sticky='w', pady=5)
    companyNameEntry.configure(validate='key', validatecommand=checkNameTitle)

    companyDescription = Label(formFrame, text='Описание компании : ', font='Arial 12 bold', bg='#FFE4C4')
    companyDescription.grid(row=2, column=0, sticky='w')
    companyDescriptionEntry = Text(formFrame, font='Arial 12', width=20, height=3)
    companyDescriptionEntry.grid(row=2, column=1, sticky='w', pady=5)

    addressCity = Label(formFrame, text='Город : ', font='Arial 12 bold', bg='#FFE4C4')
    addressCity.grid(row=3, column=0, sticky='w')
    addressCityEntry = Entry(formFrame, font='Arial 12')
    addressCityEntry.grid(row=3, column=1, sticky='w', pady=5)
    addressCityEntry.configure(validate='key', validatecommand=checkNameTitle)

    addressStreet = Label(formFrame, text='Улица : ', font='Arial 12 bold', bg='#FFE4C4')
    addressStreet.grid(row=4, column=0, sticky='w')
    addressStreetEntry = Entry(formFrame, font='Arial 12')
    addressStreetEntry.grid(row=4, column=1, sticky='w', pady=5)
    addressStreetEntry.configure(validate='key', validatecommand=checkNameTitle)

    addressHouse = Label(formFrame, text='Дом : ', font='Arial 12 bold', bg='#FFE4C4')
    addressHouse.grid(row=5, column=0, sticky='w')
    addressHouseEntry = Entry(formFrame, font='Arial 12')
    addressHouseEntry.grid(row=5, column=1, sticky='w', pady=5)
    addressHouseEntry.configure(validate='key', validatecommand=checkNumber)

    buttonAdd = Button(root, text='Добавить', command=buttonAddClicked)
    buttonAdd.pack(pady=5)
    buttonAdd.config(font='Arial 12 bold', bg='#FFCA8A')

    buttonBack = Button(root, text='Вернуться назад', command=buttonBackClicked)
    buttonBack.pack(pady=5)
    buttonBack.config(font='Arial 12 bold', bg='#FFCA8A')

    root.title('Добавление новых данных')
    root.geometry(f'450x{ySize}+550+250')
    root.resizable(False, False)
    root['bg'] = '#FFE4C4'
    root.mainloop()

#Добавление денормализованного кандидата
def addCandidateDenormalized(collectionName):
    root = Tk()

    currentCollection = Label(root, text=f'Выбранная коллекция : {collectionName}', font='Arial 12 bold', bg='#FFE4C4')
    currentCollection.pack(pady=5)

    formFrame = Frame(root, bg='#FFE4C4')
    formFrame.pack(expand=True)

    records = database['DB']['DenormalizedDocument'].find()
    titles = []
    for record in records:
        titles.append(record['Title'])
    
    def buttonBackClicked():
        root.destroy()
        createWindow(collectionName)
    
    def buttonAddClicked():
        currentTitle = comboBoxTitles.get()
        currentGender = comboBoxGender.get()
        addingCandidateDenormalized(currentTitle, candidateNameEntry, currentGender, dateOfBirthEntry, stageEntry, phoneNumberEntry)

    ySize = 340

    checkNameTitle = (root.register(limitNameTitle), '%P')
    checkDate = (root.register(limitDate), '%P')
    checkNumber = (root.register(limitNumber), '%P')
        
    vacancyName = Label(formFrame, text='Название вакансии :', font='Arial 12 bold', bg='#FFE4C4')
    vacancyName.grid(row=0, column=0, sticky='w')
    titlesVar = StringVar(value=titles[0])
    comboBoxTitles = ttk.Combobox(formFrame, font='Arial 12', textvariable=titlesVar, values=titles, state='readonly')
    comboBoxTitles.grid(row=0, column=1, sticky='w', pady=5)

    candidateName = Label(formFrame, text='Имя Фамилия :', font='Arial 12 bold', bg='#FFE4C4')
    candidateName.grid(row=1, column=0, sticky='w')
    candidateNameEntry = Entry(formFrame, font='Arial 12')
    candidateNameEntry.grid(row=1, column=1, sticky='w', pady=5)
    candidateNameEntry.configure(validate='key', validatecommand=checkNameTitle)

    genderLabel = Label(formFrame, text='Пол :', font='Arial 12 bold', bg='#FFE4C4')
    genderLabel.grid(row=2, column=0, sticky='w')
    genders = ['Male', 'Female']
    genderVar = StringVar(value=genders[0])
    comboBoxGender = ttk.Combobox(formFrame, font='Arial 12', textvariable=genderVar, values=genders, state='readonly')
    comboBoxGender.grid(row=2, column=1, sticky='w', pady=5)

    dateOfBirth = Label(formFrame, text='Дата рождения :', font='Arial 12 bold', bg='#FFE4C4')
    dateOfBirth.grid(row=3, column=0, sticky='w')
    dateOfBirthEntry = Entry(formFrame, font='Arial 12')
    dateOfBirthEntry.grid(row=3, column=1, sticky='w', pady=5)
    dateOfBirthEntry.configure(validate='key', validatecommand=checkDate)

    stage = Label(formFrame, text='Опыт работы :', font='Arial 12 bold', bg='#FFE4C4')
    stage.grid(row=4, column=0, sticky='w')
    stageEntry = Entry(formFrame, font='Arial 12')
    stageEntry.grid(row=4, column=1, sticky='w', pady=5)
    stageEntry.configure(validate='key', validatecommand=checkNumber)

    phoneNumber = Label(formFrame, text='Номер телефона : ', font='Arial 12 bold', bg='#FFE4C4')
    phoneNumber.grid(row=5, column=0, sticky='w')
    phoneNumberEntry = Entry(formFrame, font='Arial 12')
    phoneNumberEntry.grid(row=5, column=1, sticky='w', pady=5)
    phoneNumberEntry.configure(validate='key', validatecommand=checkNumber)
    
    buttonAdd = Button(root, text='Добавить', command=buttonAddClicked)
    buttonAdd.pack(pady=5)
    buttonAdd.config(font='Arial 12 bold', bg='#FFCA8A')

    buttonBack = Button(root, text='Вернуться назад', command=buttonBackClicked)
    buttonBack.pack(pady=5)
    buttonBack.config(font='Arial 12 bold', bg='#FFCA8A')

    root.title('Добавление новых данных')
    root.geometry(f'450x{ySize}+550+250')
    root.resizable(False, False)
    root['bg'] = '#FFE4C4'
    root.mainloop()

#Окно добавления записей
def createWindow(collectionName):
    root = Tk()

    def buttonBackClicked():
        root.destroy()
        funcWindow(collectionName)
    
    def buttonAddClicked():
        if collectionName == 'VacancyDocument':
            currentStatus = comboBoxStatuses.get()
            addingVacancyCollection(vacancyNameEntry, vacancyDescriptionEntry, salaryEntry, currentStatus)
        if collectionName == 'EmployerDocument':
            currentTitle = comboBoxTitles.get()
            addingEmployerCollection(currentTitle, companyNameEntry, companyDescriptionEntry, addressCityEntry, addressStreetEntry, addressHouseEntry)
        if collectionName == 'CandidateDocument':
            currentTitle = comboBoxTitles.get()
            currentGender = comboBoxGender.get()
            addingCandidateCollection(currentTitle, candidateNameEntry, currentGender, dateOfBirthEntry, stageEntry, phoneNumberEntry)

    currentCollection = Label(root, text=f'Выбранная коллекция : {collectionName}', font='Arial 12 bold', bg='#FFE4C4')
    currentCollection.pack(pady=5)

    formFrame = Frame(root, bg='#FFE4C4')
    formFrame.pack(expand=True)

    checkNameTitle = (root.register(limitNameTitle), '%P')
    checkDate = (root.register(limitDate), '%P')
    checkNumber = (root.register(limitNumber), '%P')

    records = database['DB']['VacancyDocument'].find()
    titles = []
    for record in records:
        titles.append(record['Title'])

    if collectionName == 'VacancyDocument':
        ySize = 300
        vacancyName = Label(formFrame, text='Название вакансии : ', font='Arial 12 bold', bg='#FFE4C4')
        vacancyName.grid(row=0, column=0, sticky='w')
        vacancyNameEntry = Entry(formFrame, font='Arial 12')
        vacancyNameEntry.grid(row=0, column=1, sticky='w', pady=5)
        vacancyNameEntry.configure(validate='key', validatecommand=checkNameTitle)

        vacancyDescription = Label(formFrame, text='Описание вакансии : ', font='Arial 12 bold', bg='#FFE4C4')
        vacancyDescription.grid(row=1, column=0, sticky='w')
        vacancyDescriptionEntry = Text(formFrame, font='Arial 12', width=20, height=3)
        vacancyDescriptionEntry.grid(row=1, column=1, sticky='w', pady=5)

        salary = Label(formFrame, text='Размер зарплаты : ', font='Arial 12 bold', bg='#FFE4C4')
        salary.grid(row=2, column=0, sticky='w')
        salaryEntry = Entry(formFrame, font='Arial 12')
        salaryEntry.grid(row=2, column=1, sticky='w', pady=5)
        salaryEntry.configure(validate='key', validatecommand=checkNumber)

        status = Label(formFrame, text='Статус : ', font='Arial 12 bold', bg='#FFE4C4')
        status.grid(row=3, column=0, sticky='w')
        statuses = ['True', 'False']
        statusVar = StringVar(value=statuses[0])
        comboBoxStatuses = ttk.Combobox(formFrame, font='Arial 12', textvariable=statusVar, values=statuses, state='readonly')
        comboBoxStatuses.grid(row=3, column=1, sticky='w')

        buttonAdd = Button(root, text='Добавить', command=buttonAddClicked)
        buttonAdd.pack(pady=5)
        buttonAdd.config(font='Arial 12 bold', bg='#FFCA8A')
        
    if collectionName == 'EmployerDocument':
        ySize = 400

        vacancyName = Label(formFrame, text='Название вакансии :', font='Arial 12 bold', bg='#FFE4C4')
        vacancyName.grid(row=0, column=0, sticky='w')
        titlesVar = StringVar(value=titles[0])
        comboBoxTitles = ttk.Combobox(formFrame, font='Arial 12', textvariable=titlesVar, values=titles, state='readonly')
        comboBoxTitles.grid(row=0, column=1, sticky='w')

        companyName = Label(formFrame, text='Название компании : ', font='Arial 12 bold', bg='#FFE4C4')
        companyName.grid(row=1, column=0, sticky='w')
        companyNameEntry = Entry(formFrame, font='Arial 12')
        companyNameEntry.grid(row=1, column=1, sticky='w', pady=5)
        companyNameEntry.configure(validate='key', validatecommand=checkNameTitle)

        companyDescription = Label(formFrame, text='Описание компании : ', font='Arial 12 bold', bg='#FFE4C4')
        companyDescription.grid(row=2, column=0, sticky='w')
        companyDescriptionEntry = Text(formFrame, font='Arial 12', width=20, height=3)
        companyDescriptionEntry.grid(row=2, column=1, sticky='w', pady=5)

        addressCity = Label(formFrame, text='Город : ', font='Arial 12 bold', bg='#FFE4C4')
        addressCity.grid(row=3, column=0, sticky='w')
        addressCityEntry = Entry(formFrame, font='Arial 12')
        addressCityEntry.grid(row=3, column=1, sticky='w', pady=5)
        addressCityEntry.configure(validate='key', validatecommand=checkNameTitle)

        addressStreet = Label(formFrame, text='Улица : ', font='Arial 12 bold', bg='#FFE4C4')
        addressStreet.grid(row=4, column=0, sticky='w')
        addressStreetEntry = Entry(formFrame, font='Arial 12')
        addressStreetEntry.grid(row=4, column=1, sticky='w', pady=5)
        addressStreetEntry.configure(validate='key', validatecommand=checkNameTitle)

        addressHouse = Label(formFrame, text='Дом : ', font='Arial 12 bold', bg='#FFE4C4')
        addressHouse.grid(row=5, column=0, sticky='w')
        addressHouseEntry = Entry(formFrame, font='Arial 12')
        addressHouseEntry.grid(row=5, column=1, sticky='w', pady=5)
        addressHouseEntry.configure(validate='key', validatecommand=checkNumber)

        buttonAdd = Button(root, text='Добавить', command=buttonAddClicked)
        buttonAdd.pack(pady=5)
        buttonAdd.config(font='Arial 12 bold', bg='#FFCA8A')
        
    if collectionName == 'CandidateDocument':
        ySize = 340
        
        vacancyName = Label(formFrame, text='Название вакансии :', font='Arial 12 bold', bg='#FFE4C4')
        vacancyName.grid(row=0, column=0, sticky='w')
        titlesVar = StringVar(value=titles[0])
        comboBoxTitles = ttk.Combobox(formFrame, font='Arial 12', textvariable=titlesVar, values=titles, state='readonly')
        comboBoxTitles.grid(row=0, column=1, sticky='w', pady=5)

        candidateName = Label(formFrame, text='Имя Фамилия :', font='Arial 12 bold', bg='#FFE4C4')
        candidateName.grid(row=1, column=0, sticky='w')
        candidateNameEntry = Entry(formFrame, font='Arial 12')
        candidateNameEntry.grid(row=1, column=1, sticky='w', pady=5)
        candidateNameEntry.configure(validate='key', validatecommand=checkNameTitle)

        genderLabel = Label(formFrame, text='Пол :', font='Arial 12 bold', bg='#FFE4C4')
        genderLabel.grid(row=2, column=0, sticky='w')
        genders = ['Male', 'Female']
        genderVar = StringVar(value=genders[0])
        comboBoxGender = ttk.Combobox(formFrame, font='Arial 12', textvariable=genderVar, values=genders, state='readonly')
        comboBoxGender.grid(row=2, column=1, sticky='w', pady=5)

        dateOfBirth = Label(formFrame, text='Дата рождения :', font='Arial 12 bold', bg='#FFE4C4')
        dateOfBirth.grid(row=3, column=0, sticky='w')
        dateOfBirthEntry = Entry(formFrame, font='Arial 12')
        dateOfBirthEntry.grid(row=3, column=1, sticky='w', pady=5)
        dateOfBirthEntry.configure(validate='key', validatecommand=checkDate)

        stage = Label(formFrame, text='Опыт работы :', font='Arial 12 bold', bg='#FFE4C4')
        stage.grid(row=4, column=0, sticky='w')
        stageEntry = Entry(formFrame, font='Arial 12')
        stageEntry.grid(row=4, column=1, sticky='w', pady=5)
        stageEntry.configure(validate='key', validatecommand=checkNumber)

        phoneNumber = Label(formFrame, text='Номер телефона : ', font='Arial 12 bold', bg='#FFE4C4')
        phoneNumber.grid(row=5, column=0, sticky='w')
        phoneNumberEntry = Entry(formFrame, font='Arial 12')
        phoneNumberEntry.grid(row=5, column=1, sticky='w', pady=5)
        phoneNumberEntry.configure(validate='key', validatecommand=checkNumber)

        buttonAdd = Button(root, text='Добавить', command=buttonAddClicked)
        buttonAdd.pack(pady=5)
        buttonAdd.config(font='Arial 12 bold', bg='#FFCA8A')
    
    if collectionName == 'DenormalizedDocument':

        def buttonAddVacancyClicked():
            root.destroy()
            addVacancyDenormalized(collectionName)
        
        def buttonAddEmployerClicked():
            root.destroy()
            addEmployerDenormalized(collectionName)
        
        def buttonAddCandidateClicked():
            root.destroy()
            addCandidateDenormalized(collectionName)

        ySize = 200
        buttonAddVacancy = Button(root, text='Добавить вакансию', command=buttonAddVacancyClicked)
        buttonAddVacancy.pack(pady=2)
        buttonAddVacancy.config(font='Arial 12 bold', bg='#FFCA8A')

        buttonAddEmployer = Button(root, text='Добавить компанию', command=buttonAddEmployerClicked)
        buttonAddEmployer.pack(pady=2)
        buttonAddEmployer.config(font='Arial 12 bold', bg='#FFCA8A')

        buttonAddCandidate = Button(root, text='Добавить кандидата', command=buttonAddCandidateClicked)
        buttonAddCandidate.pack(pady=2)
        buttonAddCandidate.config(font='Arial 12 bold', bg='#FFCA8A')

    buttonBack = Button(root, text='Вернуться назад', command=buttonBackClicked)
    buttonBack.pack(pady=5)
    buttonBack.config(font='Arial 12 bold', bg='#FFCA8A')

    root.title('Добавление новых данных')
    root.geometry(f'450x{ySize}+550+250')
    root.resizable(False, False)
    root['bg'] = '#FFE4C4'
    root.mainloop()

#Окно просмотра записей
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
        table = ttk.Treeview(columns=columns, show='headings', selectmode='none')
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
        columns = ('VacancyName', 'CompanyName', 'CompanyDescription', 'AddressCity', 'AddressStreet', 'AddressHouse')
        table = ttk.Treeview(columns=columns, show='headings', selectmode='none')
        table.pack()

        style = ttk.Style()
        style.configure("Treeview", rowheight=50)

        table.tag_configure('data', background="#EDD1AF")
        table.heading('VacancyName', text='Связанная вакансия')
        table.heading('CompanyName', text='Название компании')
        table.heading('CompanyDescription', text='Описание компании')
        table.heading('AddressCity', text='Город')
        table.heading('AddressStreet', text='Улица')
        table.heading('AddressHouse', text='Дом')

        table.column('#1', width=120)
        table.column('#2', width=100)
        table.column('#3', width=200)
        table.column('#4', width=70)
        table.column('#5', width=50)
        table.column('#6', width=50)

        for record in allRecords:
            length += 1
            ySize += 50

            vacancyRecord = database['DB']['VacancyDocument'].find_one({'_id': record['VacancyDocument_id']})
            vacancyName = vacancyRecord['Title']
            companyName = record['CompanyName']
            companyDescription = record['CompanyDescription']
            addressCity = record['AddressCity']
            addressStreet = record['AddressStreet']
            addressHouse = record['AddressHouse']

            parsedRecord = (vacancyName, companyName, companyDescription, addressCity, addressStreet, addressHouse)
            table.insert('', END, values=parsedRecord, tags=('data',))
        table['height'] = length
    
    if collectionName == 'CandidateDocument':
        length = 0
        columns = ('VacancyName', 'Name', 'Gender', 'DateOfBirth', 'Stage', 'PhoneNumber')
        table = ttk.Treeview(columns=columns, show='headings', selectmode='none')
        table.pack()

        style = ttk.Style()
        style.configure("Treeview", rowheight=50)

        table.tag_configure('data', background="#EDD1AF")
        table.heading('VacancyName', text='Связанная вакансия')
        table.heading('Name', text='ФИО кандидата')
        table.heading('Gender', text='Пол')
        table.heading('DateOfBirth', text='Дата рождения')
        table.heading('Stage', text='Опыт работы')
        table.heading('PhoneNumber', text='Номер телефона')

        table.column('#1', width=120)
        table.column('#2', width=130)
        table.column('#3', width=80)
        table.column('#4', width=120)
        table.column('#5', width=80)
        table.column('#6', width=150)

        for record in allRecords:
            length += 1
            ySize += 50

            vacancyRecord = database['DB']['VacancyDocument'].find_one({'_id': record['VacancyDocument_id']})
            vacancyName = vacancyRecord['Title']
            name = record['Name']
            gender = record['Gender']
            dateOfBirth = record['DateOfBirth']
            stage = record['Stage']
            phoneNumber = record['PhoneNumber']

            parsedRecord = (vacancyName, name, gender, dateOfBirth, stage, phoneNumber)
            table.insert('', END, values=parsedRecord, tags=('data',))
        table['height'] = length
    
    if collectionName == 'DenormalizedDocument':
        def showData(collectionName, title):
            root.destroy()
            readWindowData(collectionName, title)

        length = 0
        vacancyLabel = Label(root, text='Нажмите для просмотра дополнительной информации', font='Arial 12 bold', bg='#FFE4C4')
        vacancyLabel.pack(pady=5)

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

        def itemSelected(event):
            selectedStrings = ''
            for selected in table.selection():
                item = table.item(selected)
                string = item['values']
                showData(collectionName, string[0])
        table.bind("<<TreeviewSelect>>", itemSelected)

    buttonBack = Button(root, text='Вернуться назад', command=buttonBackClicked)
    buttonBack.pack(pady=5)
    buttonBack.config(font='Arial 12 bold', bg='#FFCA8A')

    root.title('Просмотр данных')
    root.geometry(f'700x{ySize}+550+250')
    root.resizable(True, False)
    root['bg'] = '#FFE4C4'
    root.mainloop()

#Просмотр дополниельной информации для денормализованной коллекции
def readWindowData(collectionName, title):
    root = Tk()

    ySize = 150
    lengthEmployers = 0

    def buttonBackClicked():
        root.destroy()
        readWindow(collectionName)

    currentCollection = Label(root, text=f'Выбранная коллекция : {collectionName}', font='Arial 12 bold', bg='#FFE4C4')
    currentCollection.pack(pady=10)

    allRecords = database['DB'][f'{collectionName}'].find({'Title': title})

    length = 0
    columns = ('CompanyName', 'CompanyDescription', 'AddressCity', 'AddressStreet', 'AddressHouse')
    tableEmployers = ttk.Treeview(columns=columns, show='headings', selectmode='none')
    tableEmployers.pack(pady=10)

    style = ttk.Style()
    style.configure("Treeview", rowheight=50)

    tableEmployers.tag_configure('data', background="#EDD1AF")
    tableEmployers.heading('CompanyName', text='Название компании')
    tableEmployers.heading('CompanyDescription', text='Описание компании')
    tableEmployers.heading('AddressCity', text='Город')
    tableEmployers.heading('AddressStreet', text='Улица')
    tableEmployers.heading('AddressHouse', text='Дом')

    tableEmployers.column('#1', width=100)
    tableEmployers.column('#2', width=200)
    tableEmployers.column('#3', width=70)
    tableEmployers.column('#4', width=50)
    tableEmployers.column('#5', width=50)

    for document in allRecords:
        recordEmployers = document['Employers']
        for record in recordEmployers:
            lengthEmployers += 1
            ySize += 50

            companyName = record['CompanyName']
            companyDescription = record['CompanyDescription']
            addressCity = record['AddressCity']
            addressStreet = record['AddressStreet']
            addressHouse = record['AddressHouse']

            parsedRecord = (companyName, companyDescription, addressCity, addressStreet, addressHouse)
            tableEmployers.insert('', END, values=parsedRecord, tags=('data',))
    tableEmployers['height'] = lengthEmployers


    allRecords = database['DB'][f'{collectionName}'].find({'Title': title})
    lengthCandidates = 0

    columns = ('Name', 'Gender', 'DateOfBirth', 'Stage', 'PhoneNumber')
    tableCandidates = ttk.Treeview(columns=columns, show='headings', selectmode='none')
    tableCandidates.pack()

    style = ttk.Style()
    style.configure("Treeview", rowheight=50)

    tableCandidates.tag_configure('data', background="#EDD1AF")
    tableCandidates.heading('Name', text='ФИО кандидата')
    tableCandidates.heading('Gender', text='Пол')
    tableCandidates.heading('DateOfBirth', text='Дата рождения')
    tableCandidates.heading('Stage', text='Опыт работы')
    tableCandidates.heading('PhoneNumber', text='Номер телефона')

    tableCandidates.column('#1', width=130)
    tableCandidates.column('#2', width=80)
    tableCandidates.column('#3', width=120)
    tableCandidates.column('#4', width=80)
    tableCandidates.column('#5', width=150)

    for document in allRecords:
        recordCandidate = document['Candidates']
        for record in recordCandidate:
            lengthCandidates += 1
            ySize += 50

            name = record['Name']
            gender = record['Gender']
            dateOfBirth = record['DateOfBirth']
            stage = record['Stage']
            phoneNumber = record['PhoneNumber']

            parsedRecord = (name, gender, dateOfBirth, stage, phoneNumber)
            tableCandidates.insert('', END, values=parsedRecord, tags=('data',))
    tableCandidates['height'] = lengthCandidates

    buttonBack = Button(root, text='Вернуться назад', command=buttonBackClicked)
    buttonBack.pack(pady=5)
    buttonBack.config(font='Arial 12 bold', bg='#FFCA8A')

    root.title('Просмотр данных')
    root.geometry(f'700x{ySize}+550+250')
    root.resizable(True, False)
    root['bg'] = '#FFE4C4'
    root.mainloop()

#Окно изменения записей 'VacancyDocument'
def updateVacancyDocument(oldValues, collectionName):
    root = Tk()
    def buttonBackClicked():
        root.destroy()
        updateWindow(collectionName)
    
    def buttonUpdateClicked():
        currentStatus = comboBoxStatuses.get()
        updateVacancyCollection(oldValues['Title'], vacancyNameEntry, vacancyDescriptionEntry, salaryEntry, currentStatus)

    currentCollection = Label(root, text=f'Выбранная коллекция : {collectionName}', font='Arial 12 bold', bg='#FFE4C4')
    currentCollection.pack(pady=5)

    changeText = Label(root, text=f'Измените данные', font='Arial 12 bold', bg='#FFE4C4')
    changeText.pack(pady=5)

    formFrame = Frame(root, bg='#FFE4C4')
    formFrame.pack(expand=True)

    checkNameTitle = (root.register(limitNameTitle), '%P')
    checkDate = (root.register(limitDate), '%P')
    checkNumber = (root.register(limitNumber), '%P')

    ySize = 330

    vacancyName = Label(formFrame, text='Название вакансии : ', font='Arial 12 bold', bg='#FFE4C4')
    vacancyName.grid(row=0, column=0, sticky='w')
    vacancyNameVariable = StringVar()
    vacancyNameEntry = Entry(formFrame, textvariable=vacancyNameVariable, font='Arial 12')
    vacancyNameEntry.grid(row=0, column=1, sticky='w', pady=5)
    vacancyNameVariable.set(oldValues['Title'])
    vacancyNameEntry.configure(validate='key', validatecommand=checkNameTitle)

    vacancyDescription = Label(formFrame, text='Описание вакансии : ', font='Arial 12 bold', bg='#FFE4C4')
    vacancyDescription.grid(row=1, column=0, sticky='w')
    vacancyDescriptionEntry = Text(formFrame, font='Arial 12', width=20, height=3)
    vacancyDescriptionEntry.grid(row=1, column=1, sticky='w', pady=5)
    vacancyDescriptionEntry.insert("1.0", oldValues['VacancyDescription'])

    salary = Label(formFrame, text='Размер зарплаты : ', font='Arial 12 bold', bg='#FFE4C4')
    salary.grid(row=2, column=0, sticky='w')
    salaryEntryVariable = StringVar()
    salaryEntry = Entry(formFrame, textvariable=salaryEntryVariable, font='Arial 12')
    salaryEntry.grid(row=2, column=1, sticky='w', pady=5)
    salaryEntryVariable.set(oldValues['Salary'])
    salaryEntry.configure(validate='key', validatecommand=checkNumber)

    status = Label(formFrame, text='Статус : ', font='Arial 12 bold', bg='#FFE4C4')
    status.grid(row=3, column=0, sticky='w')
    statuses = ['True', 'False']
    statusVar = StringVar(value=oldValues['Status'])
    comboBoxStatuses = ttk.Combobox(formFrame, font='Arial 12', textvariable=statusVar, values=statuses, state='readonly')
    comboBoxStatuses.grid(row=3, column=1, sticky='w')

    buttonUpdate = Button(root, text='Изменить', command=buttonUpdateClicked)
    buttonUpdate.pack(pady=5)
    buttonUpdate.config(font='Arial 12 bold', bg='#FFCA8A')

    buttonBack = Button(root, text='Вернуться назад', command=buttonBackClicked)
    buttonBack.pack(pady=5)
    buttonBack.config(font='Arial 12 bold', bg='#FFCA8A')

    root.title('Изменение данных')
    root.geometry(f'450x{ySize}+550+250')
    root.resizable(True, False)
    root['bg'] = '#FFE4C4'
    root.mainloop()

#Окно изменения записей 'EmployerDocument'
def updateEmployerDocument(oldValues, collectionName):
    root = Tk()

    def buttonBackClicked():
        root.destroy()
        updateWindow(collectionName)
    
    def buttonUpdateClicked():
        currentTitle = comboBoxTitles.get()
        updateEmployerCollection(oldValues['CompanyName'], currentTitle, companyNameEntry, companyDescriptionEntry, addressCityEntry, addressStreetEntry, addressHouseEntry)

    currentCollection = Label(root, text=f'Выбранная коллекция : {collectionName}', font='Arial 12 bold', bg='#FFE4C4')
    currentCollection.pack(pady=5)

    changeText = Label(root, text=f'Измените данные', font='Arial 12 bold', bg='#FFE4C4')
    changeText.pack(pady=5)

    formFrame = Frame(root, bg='#FFE4C4')
    formFrame.pack(expand=True)

    checkNameTitle = (root.register(limitNameTitle), '%P')
    checkDate = (root.register(limitDate), '%P')
    checkNumber = (root.register(limitNumber), '%P')

    ySize = 400

    vacancyName = Label(formFrame, text='Название вакансии :', font='Arial 12 bold', bg='#FFE4C4')
    vacancyName.grid(row=0, column=0, sticky='w')
    titlesVar = StringVar(value=oldValues['Title'])
    records = database['DB']['VacancyDocument'].find()
    titles = []
    for record in records:
        titles.append(record['Title'])
    comboBoxTitles = ttk.Combobox(formFrame, font='Arial 12', textvariable=titlesVar, values=titles, state='readonly')
    comboBoxTitles.grid(row=0, column=1, sticky='w')

    companyName = Label(formFrame, text='Название компании : ', font='Arial 12 bold', bg='#FFE4C4')
    companyName.grid(row=1, column=0, sticky='w')
    companyNameVariable = StringVar()
    companyNameEntry = Entry(formFrame, textvariable=companyNameVariable, font='Arial 12')
    companyNameEntry.grid(row=1, column=1, sticky='w', pady=5)
    companyNameVariable.set(oldValues['CompanyName'])
    companyNameEntry.configure(validate='key', validatecommand=checkNameTitle)

    companyDescription = Label(formFrame, text='Описание компании : ', font='Arial 12 bold', bg='#FFE4C4')
    companyDescription.grid(row=2, column=0, sticky='w')
    companyDescriptionEntry = Text(formFrame, font='Arial 12', width=20, height=3)
    companyDescriptionEntry.grid(row=2, column=1, sticky='w', pady=5)
    companyDescriptionEntry.insert("1.0", oldValues['CompanyDescription'])

    addressCity = Label(formFrame, text='Город : ', font='Arial 12 bold', bg='#FFE4C4')
    addressCity.grid(row=3, column=0, sticky='w')
    addressCityEntryVariable = StringVar()
    addressCityEntry = Entry(formFrame, textvariable=addressCityEntryVariable, font='Arial 12')
    addressCityEntry.grid(row=3, column=1, sticky='w', pady=5)
    addressCityEntryVariable.set(oldValues['AddressCity'])
    addressCityEntry.configure(validate='key', validatecommand=checkNameTitle)

    addressStreet = Label(formFrame, text='Улица : ', font='Arial 12 bold', bg='#FFE4C4')
    addressStreet.grid(row=4, column=0, sticky='w')
    addressStreetVariable = StringVar()
    addressStreetEntry = Entry(formFrame, textvariable=addressStreetVariable, font='Arial 12')
    addressStreetEntry.grid(row=4, column=1, sticky='w', pady=5)
    addressStreetVariable.set(oldValues['AddressStreet'])
    addressStreetEntry.configure(validate='key', validatecommand=checkNameTitle)

    addressHouse = Label(formFrame, text='Дом : ', font='Arial 12 bold', bg='#FFE4C4')
    addressHouse.grid(row=5, column=0, sticky='w')
    addressHouseVariable = StringVar()
    addressHouseEntry = Entry(formFrame, textvariable=addressHouseVariable, font='Arial 12')
    addressHouseEntry.grid(row=5, column=1, sticky='w', pady=5)
    addressHouseVariable.set(oldValues['AddressHouse'])
    addressHouseEntry.configure(validate='key', validatecommand=checkNumber)

    buttonUpdate = Button(root, text='Изменить', command=buttonUpdateClicked)
    buttonUpdate.pack(pady=5)
    buttonUpdate.config(font='Arial 12 bold', bg='#FFCA8A')

    buttonBack = Button(root, text='Вернуться назад', command=buttonBackClicked)
    buttonBack.pack(pady=5)
    buttonBack.config(font='Arial 12 bold', bg='#FFCA8A')

    root.title('Изменение данных')
    root.geometry(f'450x{ySize}+550+250')
    root.resizable(True, False)
    root['bg'] = '#FFE4C4'
    root.mainloop()

#Окно изменения записей 'CandidateDocument'
def updateCandidateDocument(oldValues, collectionName):
    root = Tk()

    def buttonBackClicked():
        root.destroy()
        updateWindow(collectionName)
    
    def buttonUpdateClicked():
        currentTitle = comboBoxTitles.get()
        currentGender = comboBoxGender.get()
        updateCandidateCollection(oldValues['Name'], currentTitle, candidateNameEntry, currentGender, dateOfBirthEntry, stageEntry, phoneNumberEntry)

    currentCollection = Label(root, text=f'Выбранная коллекция : {collectionName}', font='Arial 12 bold', bg='#FFE4C4')
    currentCollection.pack(pady=5)

    changeText = Label(root, text=f'Измените данные', font='Arial 12 bold', bg='#FFE4C4')
    changeText.pack(pady=5)

    formFrame = Frame(root, bg='#FFE4C4')
    formFrame.pack(expand=True)

    checkNameTitle = (root.register(limitNameTitle), '%P')
    checkDate = (root.register(limitDate), '%P')
    checkNumber = (root.register(limitNumber), '%P')

    ySize = 400
        
    vacancyName = Label(formFrame, text='Название вакансии :', font='Arial 12 bold', bg='#FFE4C4')
    vacancyName.grid(row=0, column=0, sticky='w')
    titlesVar = StringVar(value=oldValues['Title'])
    records = database['DB']['VacancyDocument'].find()
    titles = []
    for record in records:
        titles.append(record['Title'])
    comboBoxTitles = ttk.Combobox(formFrame, font='Arial 12', textvariable=titlesVar, values=titles, state='readonly')
    comboBoxTitles.grid(row=0, column=1, sticky='w', pady=5)

    candidateName = Label(formFrame, text='Имя Фамилия :', font='Arial 12 bold', bg='#FFE4C4')
    candidateName.grid(row=1, column=0, sticky='w')
    candidateNameVariable = StringVar()
    candidateNameEntry = Entry(formFrame, textvariable=candidateNameVariable, font='Arial 12')
    candidateNameEntry.grid(row=1, column=1, sticky='w', pady=5)
    candidateNameVariable.set(oldValues['Name'])
    candidateNameEntry.configure(validate='key', validatecommand=checkNameTitle)

    genderLabel = Label(formFrame, text='Пол :', font='Arial 12 bold', bg='#FFE4C4')
    genderLabel.grid(row=2, column=0, sticky='w')
    genders = ['Male', 'Female']
    genderVar = StringVar(value=oldValues['Gender'])
    comboBoxGender = ttk.Combobox(formFrame, font='Arial 12', textvariable=genderVar, values=genders, state='readonly')
    comboBoxGender.grid(row=2, column=1, sticky='w', pady=5)

    dateOfBirth = Label(formFrame, text='Дата рождения :', font='Arial 12 bold', bg='#FFE4C4')
    dateOfBirth.grid(row=3, column=0, sticky='w')
    dateOfBirthVariable = StringVar()
    dateOfBirthEntry = Entry(formFrame, textvariable=dateOfBirthVariable, font='Arial 12')
    dateOfBirthEntry.grid(row=3, column=1, sticky='w', pady=5)
    dateOfBirthVariable.set(oldValues['DateOfBirth'])
    dateOfBirthEntry.configure(validate='key', validatecommand=checkDate)

    stage = Label(formFrame, text='Опыт работы :', font='Arial 12 bold', bg='#FFE4C4')
    stage.grid(row=4, column=0, sticky='w')
    stageVariable = StringVar()
    stageEntry = Entry(formFrame, textvariable=stageVariable, font='Arial 12')
    stageEntry.grid(row=4, column=1, sticky='w', pady=5)
    stageVariable.set(oldValues['Stage'])
    stageEntry.configure(validate='key', validatecommand=checkNumber)

    phoneNumber = Label(formFrame, text='Номер телефона : ', font='Arial 12 bold', bg='#FFE4C4')
    phoneNumber.grid(row=5, column=0, sticky='w')
    phoneNumberVariable = StringVar()
    phoneNumberEntry = Entry(formFrame, textvariable=phoneNumberVariable, font='Arial 12')
    phoneNumberEntry.grid(row=5, column=1, sticky='w', pady=5)
    phoneNumberVariable.set(oldValues['PhoneNumber'])
    phoneNumberEntry.configure(validate='key', validatecommand=checkNumber)

    buttonUpdate = Button(root, text='Изменить', command=buttonUpdateClicked)
    buttonUpdate.pack(pady=5)
    buttonUpdate.config(font='Arial 12 bold', bg='#FFCA8A')

    buttonBack = Button(root, text='Вернуться назад', command=buttonBackClicked)
    buttonBack.pack(pady=5)
    buttonBack.config(font='Arial 12 bold', bg='#FFCA8A')

    root.title('Изменение данных')
    root.geometry(f'450x{ySize}+550+250')
    root.resizable(True, False)
    root['bg'] = '#FFE4C4'
    root.mainloop()

#Окно изменения записи
def updateWindow(collectionName):
    root = Tk()

    def buttonBackClicked():
        root.destroy()
        funcWindow(collectionName)
    
    def updateData(oldValues, collectionName):
        root.destroy()
        if collectionName == 'VacancyDocument':
            updateVacancyDocument(oldValues, collectionName)
        if collectionName == 'EmployerDocument':
            updateEmployerDocument(oldValues, collectionName)
        if collectionName == 'CandidateDocument':
            updateCandidateDocument(oldValues, collectionName)


    currentCollection = Label(root, text=f'Выбранная коллекция : {collectionName}', font='Arial 12 bold', bg='#FFE4C4')
    currentCollection.pack(pady=10)

    changeLabel = Label(root, text='Выберите строку для изменения данных', font='Arial 12 bold', bg='#FFE4C4')
    changeLabel.pack(pady=10)

    allRecords = database['DB'][f'{collectionName}'].find()

    ySize = 200
    
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

        def itemSelected(event):
            selectedStrings = ''
            for selected in table.selection():
                item = table.item(selected)
                string = item['values']
                oldValues = {'Title': string[0], 'VacancyDescription': string[1], 'Salary': string[2], 'Status': string[3]}
                updateData(oldValues, collectionName)
        table.bind("<<TreeviewSelect>>", itemSelected)

    if collectionName == 'EmployerDocument':
        length = 0
        columns = ('VacancyName', 'CompanyName', 'CompanyDescription', 'AddressCity', 'AddressStreet', 'AddressHouse')
        table = ttk.Treeview(columns=columns, show='headings')
        table.pack()

        style = ttk.Style()
        style.configure("Treeview", rowheight=50)

        table.tag_configure('data', background="#EDD1AF")
        table.heading('VacancyName', text='Связанная вакансия')
        table.heading('CompanyName', text='Название компании')
        table.heading('CompanyDescription', text='Описание компании')
        table.heading('AddressCity', text='Город')
        table.heading('AddressStreet', text='Улица')
        table.heading('AddressHouse', text='Дом')

        table.column('#1', width=120)
        table.column('#2', width=100)
        table.column('#3', width=200)
        table.column('#4', width=70)
        table.column('#5', width=50)
        table.column('#6', width=50)

        for record in allRecords:
            length += 1
            ySize += 50

            vacancyRecord = database['DB']['VacancyDocument'].find_one({'_id': record['VacancyDocument_id']})
            vacancyName = vacancyRecord['Title']
            companyName = record['CompanyName']
            companyDescription = record['CompanyDescription']
            addressCity = record['AddressCity']
            addressStreet = record['AddressStreet']
            addressHouse = record['AddressHouse']

            parsedRecord = (vacancyName, companyName, companyDescription, addressCity, addressStreet, addressHouse)
            table.insert('', END, values=parsedRecord, tags=('data',))
        table['height'] = length

        def itemSelected(event):
            selectedStrings = ''
            for selected in table.selection():
                item = table.item(selected)
                string = item['values']
                oldValues = {'Title': string[0], 'CompanyName': string[1], 'CompanyDescription': string[2], 'AddressCity': string[3], 'AddressStreet': string[4], 'AddressHouse': string[5]}
                updateData(oldValues, collectionName)
        table.bind("<<TreeviewSelect>>", itemSelected)
    
    if collectionName == 'CandidateDocument':
        length = 0
        columns = ('VacancyName', 'Name', 'Gender', 'DateOfBirth', 'Stage', 'PhoneNumber')
        table = ttk.Treeview(columns=columns, show='headings')
        table.pack()

        style = ttk.Style()
        style.configure("Treeview", rowheight=50)

        table.tag_configure('data', background="#EDD1AF")
        table.heading('VacancyName', text='Связанная вакансия')
        table.heading('Name', text='ФИО кандидата')
        table.heading('Gender', text='Пол')
        table.heading('DateOfBirth', text='Дата рождения')
        table.heading('Stage', text='Опыт работы')
        table.heading('PhoneNumber', text='Номер телефона')

        table.column('#1', width=120)
        table.column('#2', width=130)
        table.column('#3', width=80)
        table.column('#4', width=120)
        table.column('#5', width=80)
        table.column('#6', width=150)

        for record in allRecords:
            length += 1
            ySize += 50

            vacancyRecord = database['DB']['VacancyDocument'].find_one({'_id': record['VacancyDocument_id']})
            vacancyName = vacancyRecord['Title']
            name = record['Name']
            gender = record['Gender']
            dateOfBirth = record['DateOfBirth']
            stage = record['Stage']
            phoneNumber = record['PhoneNumber']

            parsedRecord = (vacancyName, name, gender, dateOfBirth, stage, phoneNumber)
            table.insert('', END, values=parsedRecord, tags=('data',))
        table['height'] = length

        def itemSelected(event):
            selectedStrings = ''
            for selected in table.selection():
                item = table.item(selected)
                string = item['values']
                oldValues = {'Title': string[0], 'Name': string[1], 'Gender': string[2], 'DateOfBirth': string[3], 'Stage': string[4], 'PhoneNumber': string[5]}
                updateData(oldValues, collectionName)
        table.bind("<<TreeviewSelect>>", itemSelected)
    
    if collectionName == 'DenormalizedDocument':
        ySize = 320

        def buttonUpdateVacancyClicked():
            currentVacancy = comboBoxTitles.get()
            root.destroy()
            showUpdateVacancyWindow(collectionName, currentVacancy)
        
        def buttonUpdateEmployerClicked():
            currentVacancy = comboBoxTitles.get()
            root.destroy()
            showUpdateEmployerWindow(collectionName, currentVacancy)
        
        def buttonUpdateCandidateClicked():
            currentVacancy = comboBoxTitles.get()
            root.destroy()
            showUpdateCandidateWindow(collectionName, currentVacancy)
        
        length = 0
        columns = ('Title', 'VacancyDescription', 'Salary', 'Status')
        table = ttk.Treeview(columns=columns, show='headings', selectmode='none')
        table.pack(pady=5)

        formFrame = Frame(root, bg='#FFE4C4')
        formFrame.pack(expand=True, pady=5)

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

        records = database['DB']['DenormalizedDocument'].find()
        titles = []
        for record in records:
            titles.append(record['Title'])

        vacancyName = Label(formFrame, text='Название вакансии : ', font='Arial 12 bold', bg='#FFE4C4')
        vacancyName.grid(row=0, column=0, sticky='w')
        titlesVar = StringVar(value=titles[0])
        comboBoxTitles = ttk.Combobox(formFrame, font='Arial 12', textvariable=titlesVar, values=titles, state='readonly')
        comboBoxTitles.grid(row=0, column=1, sticky='w')

        buttonUpdateVacancy = Button(root, text='Обновить вакансию', command=buttonUpdateVacancyClicked)
        buttonUpdateVacancy.pack(pady=5)
        buttonUpdateVacancy.config(font='Arial 12 bold', bg='#FFCA8A')
        buttonUpdateEmployer = Button(root, text='Обновить компанию', command=buttonUpdateEmployerClicked)
        buttonUpdateEmployer.pack(pady=5)
        buttonUpdateEmployer.config(font='Arial 12 bold', bg='#FFCA8A')
        
        buttonUpdateCandidate = Button(root, text='Обновить кандидата', command=buttonUpdateCandidateClicked)
        buttonUpdateCandidate.pack(pady=5)
        buttonUpdateCandidate.config(font='Arial 12 bold', bg='#FFCA8A')

    buttonBack = Button(root, text='Вернуться назад', command=buttonBackClicked)
    buttonBack.pack(pady=5)
    buttonBack.config(font='Arial 12 bold', bg='#FFCA8A')

    root.title('Обновление данных')
    root.geometry(f'700x{ySize}+550+250')
    root.resizable(False, False)
    root['bg'] = '#FFE4C4'
    root.mainloop()

#Окно обновления вакансии (денормализованная коллекция)
def showUpdateVacancyWindow(collectionName, currentVacancy):
    root = Tk()

    record = database['DB']['DenormalizedDocument'].find_one({'Title': currentVacancy})
    oldTitle = record['Title']

    def buttonBackClicked():
        root.destroy()
        updateWindow(collectionName)
    
    def buttonUpdateClicked():
        currentStatus = comboBoxStatuses.get()
        updateVacancyCollectionDenormalized(oldTitle, vacancyNameEntry, vacancyDescriptionEntry, salaryEntry, currentStatus)
    
    currentCollection = Label(root, text=f'Выбранная коллекция : {collectionName}', font='Arial 12 bold', bg='#FFE4C4')
    currentCollection.pack(pady=5)

    changeText = Label(root, text=f'Измените данные', font='Arial 12 bold', bg='#FFE4C4')
    changeText.pack(pady=5)

    formFrame = Frame(root, bg='#FFE4C4')
    formFrame.pack(expand=True)

    checkNameTitle = (root.register(limitNameTitle), '%P')
    checkDate = (root.register(limitDate), '%P')
    checkNumber = (root.register(limitNumber), '%P')

    ySize = 330

    vacancyName = Label(formFrame, text='Название вакансии : ', font='Arial 12 bold', bg='#FFE4C4')
    vacancyName.grid(row=0, column=0, sticky='w')
    vacancyNameEntryVariable = StringVar()
    vacancyNameEntry = Entry(formFrame, text=vacancyNameEntryVariable, font='Arial 12')
    vacancyNameEntry.grid(row=0, column=1, sticky='w')
    vacancyNameEntryVariable.set(record['Title'])
    vacancyNameEntry.configure(validate='key', validatecommand=checkNameTitle)

    vacancyDescription = Label(formFrame, text='Описание вакансии : ', font='Arial 12 bold', bg='#FFE4C4')
    vacancyDescription.grid(row=1, column=0, sticky='w')
    vacancyDescriptionEntry = Text(formFrame, font='Arial 12', width=20, height=3)
    vacancyDescriptionEntry.grid(row=1, column=1, sticky='w', pady=5)
    vacancyDescriptionEntry.insert("1.0", record['VacancyDescription'])

    salary = Label(formFrame, text='Размер зарплаты : ', font='Arial 12 bold', bg='#FFE4C4')
    salary.grid(row=2, column=0, sticky='w')
    salaryEntryVariable = StringVar()
    salaryEntry = Entry(formFrame, textvariable=salaryEntryVariable, font='Arial 12')
    salaryEntry.grid(row=2, column=1, sticky='w', pady=5)
    salaryEntryVariable.set(record['Salary'])
    salaryEntry.configure(validate='key', validatecommand=checkNumber)

    status = Label(formFrame, text='Статус : ', font='Arial 12 bold', bg='#FFE4C4')
    status.grid(row=3, column=0, sticky='w')
    statuses = ['True', 'False']
    statusVar = StringVar(value=str(record['Status']))
    comboBoxStatuses = ttk.Combobox(formFrame, font='Arial 12', textvariable=statusVar, values=statuses, state='readonly')
    comboBoxStatuses.grid(row=3, column=1, sticky='w')

    buttonUpdate = Button(root, text='Изменить', command=buttonUpdateClicked)
    buttonUpdate.pack(pady=5)
    buttonUpdate.config(font='Arial 12 bold', bg='#FFCA8A')

    buttonBack = Button(root, text='Вернуться назад', command=buttonBackClicked)
    buttonBack.pack(pady=5)
    buttonBack.config(font='Arial 12 bold', bg='#FFCA8A')

    root.title('Обновление данных')
    root.geometry(f'700x{ySize}+550+250')
    root.resizable(False, False)
    root['bg'] = '#FFE4C4'
    root.mainloop()

#Окно выбора изменения компании (денормализованная коллекция)
def showUpdateEmployerWindow(collectionName, currentVacancy):
    root = Tk()

    ySize = 200

    def buttonBackClicked():
        root.destroy()
        updateWindow(collectionName)
    
    def updateData(oldValues, collectionName, currentVacancy):
        root.destroy()
        updateEmployerDenormalized(oldValues, collectionName, currentVacancy)
    
    currentCollection = Label(root, text=f'Выбранная коллекция : {collectionName}', font='Arial 12 bold', bg='#FFE4C4')
    currentCollection.pack(pady=5)

    changeText = Label(root, text=f'Измените данные', font='Arial 12 bold', bg='#FFE4C4')
    changeText.pack(pady=5)

    allRecords = database['DB'][f'{collectionName}'].find({'Title': currentVacancy})

    length = 0
    columns = ('CompanyName', 'CompanyDescription', 'AddressCity', 'AddressStreet', 'AddressHouse')
    table = ttk.Treeview(columns=columns, show='headings')
    table.pack(pady=10)

    style = ttk.Style()
    style.configure("Treeview", rowheight=50)

    table.tag_configure('data', background="#EDD1AF")
    table.heading('CompanyName', text='Название компании')
    table.heading('CompanyDescription', text='Описание компании')
    table.heading('AddressCity', text='Город')
    table.heading('AddressStreet', text='Улица')
    table.heading('AddressHouse', text='Дом')

    table.column('#1', width=100)
    table.column('#2', width=200)
    table.column('#3', width=70)
    table.column('#4', width=50)
    table.column('#5', width=50)

    for document in allRecords:
        recordEmployers = document['Employers']
        for record in recordEmployers:
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

    def itemSelected(event):
        selectedStrings = ''
        for selected in table.selection():
            item = table.item(selected)
            string = item['values']
            oldValues = {'CompanyName': string[0], 'CompanyDescription': string[1], 'AddressCity': string[2], 'AddressStreet': string[3], 'AddressHouse': string[4]}
            updateData(oldValues, collectionName, currentVacancy)
    table.bind("<<TreeviewSelect>>", itemSelected)

    buttonBack = Button(root, text='Вернуться назад', command=buttonBackClicked)
    buttonBack.pack(pady=5)
    buttonBack.config(font='Arial 12 bold', bg='#FFCA8A')

    root.title('Обновление данных')
    root.geometry(f'700x{ySize}+550+250')
    root.resizable(False, False)
    root['bg'] = '#FFE4C4'
    root.mainloop()

#Окно изменения компании (денормализованная коллекиця)
def updateEmployerDenormalized(oldValues, collectionName, currentVacancy):
    root = Tk()

    def buttonBackClicked():
        root.destroy()
        showUpdateEmployerWindow(collectionName, currentVacancy)
    
    def buttonUpdateClicked():
        oldName = oldValues['CompanyName']
        updateEmployerCollectionDenormalized(currentVacancy, oldName, companyNameEntry, companyDescriptionEntry, addressCityEntry, addressStreetEntry, addressHouseEntry)
    
    checkNameTitle = (root.register(limitNameTitle), '%P')
    checkDate = (root.register(limitDate), '%P')
    checkNumber = (root.register(limitNumber), '%P')
    
    ySize = 400

    currentCollection = Label(root, text=f'Выбранная коллекция : {collectionName}', font='Arial 12 bold', bg='#FFE4C4')
    currentCollection.pack(pady=5)

    currentVacancyText = Label(root, text=f'Текущая вакансия : {currentVacancy}', font='Arial 12 bold', bg='#FFE4C4')
    currentVacancyText.pack(pady=5)

    changeText = Label(root, text=f'Измените данные', font='Arial 12 bold', bg='#FFE4C4')
    changeText.pack(pady=5)

    formFrame = Frame(root, bg='#FFE4C4')
    formFrame.pack(expand=True)

    companyName = Label(formFrame, text='Название компании : ', font='Arial 12 bold', bg='#FFE4C4')
    companyName.grid(row=1, column=0, sticky='w')
    companyNameVariable = StringVar()
    companyNameEntry = Entry(formFrame, textvariable=companyNameVariable, font='Arial 12')
    companyNameEntry.grid(row=1, column=1, sticky='w', pady=5)
    companyNameVariable.set(oldValues['CompanyName'])
    companyNameEntry.configure(validate='key', validatecommand=checkNameTitle)

    companyDescription = Label(formFrame, text='Описание компании : ', font='Arial 12 bold', bg='#FFE4C4')
    companyDescription.grid(row=2, column=0, sticky='w')
    companyDescriptionEntry = Text(formFrame, font='Arial 12', width=20, height=3)
    companyDescriptionEntry.grid(row=2, column=1, sticky='w', pady=5)
    companyDescriptionEntry.insert("1.0", oldValues['CompanyDescription'])

    addressCity = Label(formFrame, text='Город : ', font='Arial 12 bold', bg='#FFE4C4')
    addressCity.grid(row=3, column=0, sticky='w')
    addressCityEntryVariable = StringVar()
    addressCityEntry = Entry(formFrame, textvariable=addressCityEntryVariable, font='Arial 12')
    addressCityEntry.grid(row=3, column=1, sticky='w', pady=5)
    addressCityEntryVariable.set(oldValues['AddressCity'])
    addressCityEntry.configure(validate='key', validatecommand=checkNameTitle)

    addressStreet = Label(formFrame, text='Улица : ', font='Arial 12 bold', bg='#FFE4C4')
    addressStreet.grid(row=4, column=0, sticky='w')
    addressStreetVariable = StringVar()
    addressStreetEntry = Entry(formFrame, textvariable=addressStreetVariable, font='Arial 12')
    addressStreetEntry.grid(row=4, column=1, sticky='w', pady=5)
    addressStreetVariable.set(oldValues['AddressStreet'])
    addressStreetEntry.configure(validate='key', validatecommand=checkNameTitle)

    addressHouse = Label(formFrame, text='Дом : ', font='Arial 12 bold', bg='#FFE4C4')
    addressHouse.grid(row=5, column=0, sticky='w')
    addressHouseVariable = StringVar()
    addressHouseEntry = Entry(formFrame, textvariable=addressHouseVariable, font='Arial 12')
    addressHouseEntry.grid(row=5, column=1, sticky='w', pady=5)
    addressHouseVariable.set(oldValues['AddressHouse'])
    addressHouseEntry.configure(validate='key', validatecommand=checkNumber)
    
    buttonUpdate = Button(root, text='Изменить', command=buttonUpdateClicked)
    buttonUpdate.pack(pady=5)
    buttonUpdate.config(font='Arial 12 bold', bg='#FFCA8A')

    buttonBack = Button(root, text='Вернуться назад', command=buttonBackClicked)
    buttonBack.pack(pady=5)
    buttonBack.config(font='Arial 12 bold', bg='#FFCA8A')

    root.title('Обновление данных')
    root.geometry(f'450x{ySize}+550+250')
    root.resizable(False, False)
    root['bg'] = '#FFE4C4'
    root.mainloop()

#Окно выбора изменения кандидата (денормализованная коллекция)
def showUpdateCandidateWindow(collectionName, currentVacancy):
    root = Tk()

    def buttonBackClicked():
        root.destroy()
        updateWindow(collectionName)
    
    def updateData(oldValues, collectionName, currentVacancy):
        root.destroy()
        updateCandidateDenormalized(oldValues, collectionName, currentVacancy)
    
    ySize = 150
    
    currentCollection = Label(root, text=f'Выбранная коллекция : {collectionName}', font='Arial 12 bold', bg='#FFE4C4')
    currentCollection.pack(pady=5)

    changeText = Label(root, text=f'Измените данные', font='Arial 12 bold', bg='#FFE4C4')
    changeText.pack(pady=5)

    allRecords = database['DB'][f'{collectionName}'].find({'Title': currentVacancy})

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

    for document in allRecords:
        recordCandidate = document['Candidates']
        for record in recordCandidate:
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

    def itemSelected(event):
        selectedStrings = ''
        for selected in table.selection():
            item = table.item(selected)
            string = item['values']
            oldValues = {'Name': string[0], 'Gender': string[1], 'DateOfBirth': string[2], 'Stage': string[3], 'PhoneNumber': string[4]}
            updateData(oldValues, collectionName, currentVacancy)
    table.bind("<<TreeviewSelect>>", itemSelected)

    buttonBack = Button(root, text='Вернуться назад', command=buttonBackClicked)
    buttonBack.pack(pady=5)
    buttonBack.config(font='Arial 12 bold', bg='#FFCA8A')

    root.title('Обновление данных')
    root.geometry(f'700x{ySize}+550+250')
    root.resizable(False, False)
    root['bg'] = '#FFE4C4'
    root.mainloop()

#Окно изменения кандидата (денормализовання коллекция)
def updateCandidateDenormalized(oldValues, collectionName, currentVacancy):
    root = Tk()

    ySize = 400

    def buttonBackClicked():
        root.destroy()
        showUpdateCandidateWindow(collectionName, currentVacancy)
    
    def buttonUpdateClicked():
        oldName = oldValues['Name']
        currentGender = comboBoxGender.get()
        updateCandidateCollectionDenormalized(currentVacancy, oldName, candidateNameEntry, currentGender, dateOfBirthEntry, stageEntry, phoneNumberEntry)
    
    currentCollection = Label(root, text=f'Выбранная коллекция : {collectionName}', font='Arial 12 bold', bg='#FFE4C4')
    currentCollection.pack(pady=5)

    currentVacancyText = Label(root, text=f'Текущая вакансия : {currentVacancy}', font='Arial 12 bold', bg='#FFE4C4')
    currentVacancyText.pack(pady=5)

    changeText = Label(root, text=f'Измените данные', font='Arial 12 bold', bg='#FFE4C4')
    changeText.pack(pady=5)

    formFrame = Frame(root, bg='#FFE4C4')
    formFrame.pack(expand=True)

    checkNameTitle = (root.register(limitNameTitle), '%P')
    checkDate = (root.register(limitDate), '%P')
    checkNumber = (root.register(limitNumber), '%P')

    candidateName = Label(formFrame, text='Имя Фамилия :', font='Arial 12 bold', bg='#FFE4C4')
    candidateName.grid(row=1, column=0, sticky='w')
    candidateNameVariable = StringVar()
    candidateNameEntry = Entry(formFrame, textvariable=candidateNameVariable, font='Arial 12')
    candidateNameEntry.grid(row=1, column=1, sticky='w', pady=5)
    candidateNameVariable.set(oldValues['Name'])
    candidateNameEntry.configure(validate='key', validatecommand=checkNameTitle)

    genderLabel = Label(formFrame, text='Пол :', font='Arial 12 bold', bg='#FFE4C4')
    genderLabel.grid(row=2, column=0, sticky='w')
    genders = ['Male', 'Female']
    genderVar = StringVar(value=oldValues['Gender'])
    comboBoxGender = ttk.Combobox(formFrame, font='Arial 12', textvariable=genderVar, values=genders, state='readonly')
    comboBoxGender.grid(row=2, column=1, sticky='w', pady=5)

    dateOfBirth = Label(formFrame, text='Дата рождения :', font='Arial 12 bold', bg='#FFE4C4')
    dateOfBirth.grid(row=3, column=0, sticky='w')
    dateOfBirthVariable = StringVar()
    dateOfBirthEntry = Entry(formFrame, textvariable=dateOfBirthVariable, font='Arial 12')
    dateOfBirthEntry.grid(row=3, column=1, sticky='w', pady=5)
    dateOfBirthVariable.set(oldValues['DateOfBirth'])
    dateOfBirthEntry.configure(validate='key', validatecommand=checkDate)

    stage = Label(formFrame, text='Опыт работы :', font='Arial 12 bold', bg='#FFE4C4')
    stage.grid(row=4, column=0, sticky='w')
    stageVariable = StringVar()
    stageEntry = Entry(formFrame, textvariable=stageVariable, font='Arial 12')
    stageEntry.grid(row=4, column=1, sticky='w', pady=5)
    stageVariable.set(oldValues['Stage'])
    stageEntry.configure(validate='key', validatecommand=checkNumber)

    phoneNumber = Label(formFrame, text='Номер телефона : ', font='Arial 12 bold', bg='#FFE4C4')
    phoneNumber.grid(row=5, column=0, sticky='w')
    phoneNumberVariable = StringVar()
    phoneNumberEntry = Entry(formFrame, textvariable=phoneNumberVariable, font='Arial 12')
    phoneNumberEntry.grid(row=5, column=1, sticky='w', pady=5)
    phoneNumberVariable.set(oldValues['PhoneNumber'])
    phoneNumberEntry.configure(validate='key', validatecommand=checkNumber)

    buttonUpdate = Button(root, text='Изменить', command=buttonUpdateClicked)
    buttonUpdate.pack(pady=5)
    buttonUpdate.config(font='Arial 12 bold', bg='#FFCA8A')

    buttonBack = Button(root, text='Вернуться назад', command=buttonBackClicked)
    buttonBack.pack(pady=5)
    buttonBack.config(font='Arial 12 bold', bg='#FFCA8A')

    root.title('Обновление данных')
    root.geometry(f'450x{ySize}+550+250')
    root.resizable(False, False)
    root['bg'] = '#FFE4C4'
    root.mainloop()

#Окно удаления записи
def deleteWindow(collectionName):
    root = Tk()

    def buttonBackClicked():
        root.destroy()
        funcWindow(collectionName)
    
    def deleteData(values, collectionName):
        if collectionName == 'VacancyDocument':
            deleteVacancyCollection(values['Title'])
        if collectionName == 'EmployerDocument':
            deleteEmployerCollection(values['CompanyName'])
        if collectionName == 'CandidateDocument':
            deleteCandidateCollection(values['Name'])
        root.destroy()
        deleteWindow(collectionName)

    currentCollection = Label(root, text=f'Выбранная коллекция : {collectionName}', font='Arial 12 bold', bg='#FFE4C4')
    currentCollection.pack(pady=10)

    changeLabel = Label(root, text='Выберите строку для удаления данных', font='Arial 12 bold', bg='#FFE4C4')
    changeLabel.pack(pady=10)

    allRecords = database['DB'][f'{collectionName}'].find()
    ySize = 200

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

        def itemSelected(event):
            selectedStrings = ''
            for selected in table.selection():
                item = table.item(selected)
                string = item['values']
                values = {'Title': string[0], 'VacancyDescription': string[1], 'Salary': string[2], 'Status': string[3]}
                deleteData(values, collectionName)
        table.bind("<<TreeviewSelect>>", itemSelected)
    
    if collectionName == 'EmployerDocument':
        length = 0
        columns = ('VacancyName', 'CompanyName', 'CompanyDescription', 'AddressCity', 'AddressStreet', 'AddressHouse')
        table = ttk.Treeview(columns=columns, show='headings')
        table.pack()

        style = ttk.Style()
        style.configure("Treeview", rowheight=50)

        table.tag_configure('data', background="#EDD1AF")
        table.heading('VacancyName', text='Связанная вакансия')
        table.heading('CompanyName', text='Название компании')
        table.heading('CompanyDescription', text='Описание компании')
        table.heading('AddressCity', text='Город')
        table.heading('AddressStreet', text='Улица')
        table.heading('AddressHouse', text='Дом')

        table.column('#1', width=120)
        table.column('#2', width=100)
        table.column('#3', width=200)
        table.column('#4', width=70)
        table.column('#5', width=50)
        table.column('#6', width=50)

        for record in allRecords:
            length += 1
            ySize += 50

            vacancyRecord = database['DB']['VacancyDocument'].find_one({'_id': record['VacancyDocument_id']})
            vacancyName = vacancyRecord['Title']
            companyName = record['CompanyName']
            companyDescription = record['CompanyDescription']
            addressCity = record['AddressCity']
            addressStreet = record['AddressStreet']
            addressHouse = record['AddressHouse']

            parsedRecord = (vacancyName, companyName, companyDescription, addressCity, addressStreet, addressHouse)
            table.insert('', END, values=parsedRecord, tags=('data',))
        table['height'] = length

        def itemSelected(event):
            selectedStrings = ''
            for selected in table.selection():
                item = table.item(selected)
                string = item['values']
                values = {'Title': string[0], 'CompanyName': string[1], 'CompanyDescription': string[2], 'AddressCity': string[3], 'AddressStreet': string[4], 'AddressHouse': string[5]}
                deleteData(values, collectionName)
        table.bind("<<TreeviewSelect>>", itemSelected)
    
    if collectionName == 'CandidateDocument':
        length = 0
        columns = ('VacancyName', 'Name', 'Gender', 'DateOfBirth', 'Stage', 'PhoneNumber')
        table = ttk.Treeview(columns=columns, show='headings')
        table.pack()

        style = ttk.Style()
        style.configure("Treeview", rowheight=50)

        table.tag_configure('data', background="#EDD1AF")
        table.heading('VacancyName', text='Связанная вакансия')
        table.heading('Name', text='ФИО кандидата')
        table.heading('Gender', text='Пол')
        table.heading('DateOfBirth', text='Дата рождения')
        table.heading('Stage', text='Опыт работы')
        table.heading('PhoneNumber', text='Номер телефона')

        table.column('#1', width=120)
        table.column('#2', width=130)
        table.column('#3', width=80)
        table.column('#4', width=120)
        table.column('#5', width=80)
        table.column('#6', width=150)

        for record in allRecords:
            length += 1
            ySize += 50

            vacancyRecord = database['DB']['VacancyDocument'].find_one({'_id': record['VacancyDocument_id']})
            vacancyName = vacancyRecord['Title']
            name = record['Name']
            gender = record['Gender']
            dateOfBirth = record['DateOfBirth']
            stage = record['Stage']
            phoneNumber = record['PhoneNumber']

            parsedRecord = (vacancyName, name, gender, dateOfBirth, stage, phoneNumber)
            table.insert('', END, values=parsedRecord, tags=('data',))
        table['height'] = length

        def itemSelected(event):
            selectedStrings = ''
            for selected in table.selection():
                item = table.item(selected)
                string = item['values']
                values = {'Title': string[0], 'Name': string[1], 'Gender': string[2], 'DateOfBirth': string[3], 'Stage': string[4], 'PhoneNumber': string[5]}
                deleteData(values, collectionName)
        table.bind("<<TreeviewSelect>>", itemSelected)
    
    if collectionName == 'DenormalizedDocument':
        ySize = 320

        def buttonDeleteVacancyClicked():
            currentVacancy = comboBoxTitles.get()
            deleteVacancyCollectionDenormalized(currentVacancy)
            root.destroy()
            deleteWindow(collectionName)
        
        def buttonDeleteEmployerClicked():
            currentVacancy = comboBoxTitles.get()
            root.destroy()
            showDeleteEmployerWindow(collectionName, currentVacancy)
        
        def buttonDeleteCandidateClicked():
            currentVacancy = comboBoxTitles.get()
            root.destroy()
            showDeleteCandidateWindow(collectionName, currentVacancy)
        
        length = 0
        columns = ('Title', 'VacancyDescription', 'Salary', 'Status')
        table = ttk.Treeview(columns=columns, show='headings', selectmode='none')
        table.pack(pady=5)

        formFrame = Frame(root, bg='#FFE4C4')
        formFrame.pack(expand=True, pady=5)

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

        records = database['DB']['DenormalizedDocument'].find()
        titles = []
        for record in records:
            titles.append(record['Title'])

        vacancyName = Label(formFrame, text='Название вакансии : ', font='Arial 12 bold', bg='#FFE4C4')
        vacancyName.grid(row=0, column=0, sticky='w')
        titlesVar = StringVar(value=titles[0])
        comboBoxTitles = ttk.Combobox(formFrame, font='Arial 12', textvariable=titlesVar, values=titles, state='readonly')
        comboBoxTitles.grid(row=0, column=1, sticky='w')

        buttonDeleteVacancy = Button(root, text='Удалить вакансию', command=buttonDeleteVacancyClicked)
        buttonDeleteVacancy.pack(pady=5)
        buttonDeleteVacancy.config(font='Arial 12 bold', bg='#FFCA8A')

        buttonDeleteEmployer = Button(root, text='Удалить компанию', command=buttonDeleteEmployerClicked)
        buttonDeleteEmployer.pack(pady=5)
        buttonDeleteEmployer.config(font='Arial 12 bold', bg='#FFCA8A')
        
        buttonDeleteCandidate = Button(root, text='Удалить кандидата', command=buttonDeleteCandidateClicked)
        buttonDeleteCandidate.pack(pady=5)
        buttonDeleteCandidate.config(font='Arial 12 bold', bg='#FFCA8A')
    
    buttonBack = Button(root, text='Вернуться назад', command=buttonBackClicked)
    buttonBack.pack(pady=5)
    buttonBack.config(font='Arial 12 bold', bg='#FFCA8A')

    root.title('Удаление данных')
    root.geometry(f'700x{ySize}+550+250')
    root.resizable(False, False)
    root['bg'] = '#FFE4C4'
    root.mainloop()

#Окно удаления компании (денормализованная коллекция)
def showDeleteEmployerWindow(collectionName, currentVacancy):
    root = Tk()

    ySize = 200

    def buttonBackClicked():
        root.destroy()
        deleteWindow(collectionName)
    
    def deleteData(oldValues, currentVacancy):
        deleteEmployerCollectionDenormalized(oldValues, currentVacancy)
        root.destroy()
        showDeleteEmployerWindow(collectionName, currentVacancy)

    
    currentCollection = Label(root, text=f'Выбранная коллекция : {collectionName}', font='Arial 12 bold', bg='#FFE4C4')
    currentCollection.pack(pady=5)

    changeText = Label(root, text=f'Измените данные', font='Arial 12 bold', bg='#FFE4C4')
    changeText.pack(pady=5)

    allRecords = database['DB'][f'{collectionName}'].find({'Title': currentVacancy})

    length = 0
    columns = ('CompanyName', 'CompanyDescription', 'AddressCity', 'AddressStreet', 'AddressHouse')
    table = ttk.Treeview(columns=columns, show='headings')
    table.pack(pady=10)

    style = ttk.Style()
    style.configure("Treeview", rowheight=50)

    table.tag_configure('data', background="#EDD1AF")
    table.heading('CompanyName', text='Название компании')
    table.heading('CompanyDescription', text='Описание компании')
    table.heading('AddressCity', text='Город')
    table.heading('AddressStreet', text='Улица')
    table.heading('AddressHouse', text='Дом')

    table.column('#1', width=100)
    table.column('#2', width=200)
    table.column('#3', width=70)
    table.column('#4', width=50)
    table.column('#5', width=50)

    for document in allRecords:
        recordEmployers = document['Employers']
        for record in recordEmployers:
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

    def itemSelected(event):
        selectedStrings = ''
        for selected in table.selection():
            item = table.item(selected)
            string = item['values']
            oldValues = {'CompanyName': string[0], 'CompanyDescription': string[1], 'AddressCity': string[2], 'AddressStreet': string[3], 'AddressHouse': string[4]}
            deleteData(oldValues, currentVacancy)
    table.bind("<<TreeviewSelect>>", itemSelected)

    buttonBack = Button(root, text='Вернуться назад', command=buttonBackClicked)
    buttonBack.pack(pady=5)
    buttonBack.config(font='Arial 12 bold', bg='#FFCA8A')

    root.title('Обновление данных')
    root.geometry(f'700x{ySize}+550+250')
    root.resizable(False, False)
    root['bg'] = '#FFE4C4'
    root.mainloop()

#Окно удаления кандидата (денормализованная коллекция)
def showDeleteCandidateWindow(collectionName, currentVacancy):
    root = Tk()

    def buttonBackClicked():
        root.destroy()
        updateWindow(collectionName)
    
    def deleteData(oldValues, currentVacancy):
        deleteCandidateCollectionDenormalized(oldValues, currentVacancy)
        root.destroy()
        showDeleteCandidateWindow(collectionName, currentVacancy)
    
    ySize = 150
    
    currentCollection = Label(root, text=f'Выбранная коллекция : {collectionName}', font='Arial 12 bold', bg='#FFE4C4')
    currentCollection.pack(pady=5)

    changeText = Label(root, text=f'Измените данные', font='Arial 12 bold', bg='#FFE4C4')
    changeText.pack(pady=5)

    allRecords = database['DB'][f'{collectionName}'].find({'Title': currentVacancy})

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

    for document in allRecords:
        recordCandidate = document['Candidates']
        for record in recordCandidate:
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

    def itemSelected(event):
        selectedStrings = ''
        for selected in table.selection():
            item = table.item(selected)
            string = item['values']
            oldValues = {'Name': string[0], 'Gender': string[1], 'DateOfBirth': string[2], 'Stage': string[3], 'PhoneNumber': string[4]}
            deleteData(oldValues, currentVacancy)
    table.bind("<<TreeviewSelect>>", itemSelected)

    buttonBack = Button(root, text='Вернуться назад', command=buttonBackClicked)
    buttonBack.pack(pady=5)
    buttonBack.config(font='Arial 12 bold', bg='#FFCA8A')

    root.title('Обновление данных')
    root.geometry(f'700x{ySize}+550+250')
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

#Главное окно для выбора коллекции для подключения
def mainUI():
    sizeY = windowSize(collections)
    root = Tk()

    def buttonClicked():
        collectionName = comboBoxCollections.get()
        root.destroy()
        funcWindow(collectionName)
    
    def buttonQuitClicked():
        root.destroy()
    
    def buttonJoinClicked():
        joinCollections()
        showinfo(title='Инфо', message='Данные успешно объеденены')

    textAvailable = Label(text='Available collections:', font='Arial 12 bold', bg='#FFE4C4')
    textAvailable.pack(pady=10)

    listAvailableCollections = availableCollections(collections)
    collectionsLabel = Label(text=listAvailableCollections, font='Arial 12', bg='#FFE4C4')
    collectionsLabel.pack()

    formFrame = Frame(root, bg='#FFE4C4')
    formFrame.pack(expand=True)

    collectionsVar = StringVar(value=collections[2])
    comboBoxCollections = ttk.Combobox(root, font='Arial 12', textvariable=collectionsVar, values=collections, state='readonly')
    comboBoxCollections.pack()

    buttonConnection = Button(root, text='Подключиться', command=buttonClicked)
    buttonConnection.pack(pady=10)
    buttonConnection.config(font='Arial 12 bold', bg='#FFCA8A')

    buttonJoin = Button(root, text='Объединить коллекции', command=buttonJoinClicked)
    buttonJoin.pack(pady=10)
    buttonJoin.config(font='Arial 12 bold', bg='#FFCA8A')

    buttonQuit = Button(root, text='Выйти', command=buttonQuitClicked)
    buttonQuit.pack(pady=5)
    buttonQuit.config(font='Arial 12 bold', bg='#FFCA8A')
    
    root.title('Окно взаимодействия с базой данных')
    root.geometry(f'400x{sizeY}+550+250')
    root.resizable(False, False)
    root['bg'] = '#FFE4C4'
    root.mainloop()

def main():
    mainUI()


if __name__ == '__main__':
    main()
