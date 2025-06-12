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

# deschidem fisierul ,,datorii.txt''
    fisier = open('datorii.txt', 'w')

# aceasta functie permite citirea unei datorii de la tastatura, obtinand date pentru actualizarea fisierului
def citeste_datorie():
    nume_datorie = input("Introduceti numele datoriei: ")
    valoare_datorie = float(input("Introduceti valoarea in bani a datoriei: "))
    data_datorie = input("Cand a aparut aceasta datorie?")
    este_achitata = input("Datoria este achitata? Alegeti intre Da si Nu")
    data_achitare_datorie = "" # lasam gol aici deocamdata
    if (este_achitata.casefold() == "Da".casefold()):
        este_achitata = True
    else: # presupunem ca datoria nu a fost achitata daca este alt raspuns decat Da/Nu
        este_achitata = False
    if este_achitata == True:
        data_achitare_datorie = input("Precizati data la care ati scapat de datorie")
    return [nume_datorie, valoare_datorie, data_datorie, este_achitata, data_achitare_datorie]

    """ functia de mai jos afiseaza intreg continutul fisierului in care sunt retinute datoriile
    """
def afisare_datorii():
    for line in fisier:
        print(line)
