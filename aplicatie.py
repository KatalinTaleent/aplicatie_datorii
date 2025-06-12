# aceasta este o simpla aplicatie care lucreaza cu diverse datorii proprii, de zi cu zi
# datoriile sunt stocate intr-un fisier de tip text, cu urmatoarea structura:
#   numele datoriei - tip string
#   suma de bani - tip float sau string (daca se doreste si valoarea monetara folosita)
#   data crearii datoriei - tip string
#   daca datoria este achitata - tip bool
#   data incheierii datoriei - tip string, cu data achitarii datoriei (,,-'' daca datoria nu a fost achitata)
# operatiunile pe care le efectueaza aplicatia sunt de tip CRUD (creare, citire, actualizare, stergere)

""" cu aceasta functie incepe propriu-zis aplicatia
    fisierul in care apar datoriile este ,,datorii.txt'' """
def initializeaza_fisier():
#deschidem fisierul ,,datorii.txt''
    fisier = open('datorii.txt', 'w')

#aceasta functie permite citirea unei datorii de la tastatura, actualizand astfel fisierul
def citeste_datorie():
    nume_datorie = input("Introduceti numele datoriei:", end = "")
    valoare_datorie = float(input("Introduceti valoarea in bani a datoriei:", end = ""))
    data_datorie = input("Cand a aparut aceasta datorie?", end = "")
#TODO
