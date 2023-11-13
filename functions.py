from tkinter import *
from tkinter import ttk
from pymongo import MongoClient, UpdateOne
from tkinter.messagebox import showerror, showinfo

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