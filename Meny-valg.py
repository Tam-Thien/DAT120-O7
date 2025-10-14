
emner = {} # I stedenfor eempty list bruker vi empty dictionary. 
#kan skrive studieplan = {semester: [] for semester in range(1, 7)} men ønsker å ha listene klart. Egen prefferanse, men koden med "for-løkke" er bedre
'''studieplan = {
    "sem1": [],
    "sem2": [],
    "sem3": [],
    "sem4": [],
    "sem5": [],
    "sem6": [],
}    
'''
studieplan = {semester: [] for semester in range(1, 7)}

#Printer ut menyen. #Midlertidig kommentert ut meny 9-14 for oversiktlighet. 
def meny_liste():
    print("\n________Meny:_______")   
    print("01. Lag et nytt emne.")
    print("02. Legg til et emne i studieplanen.")
    print("03. Skriv ut en liste over alle registrerte emner.")
    print("04. Skriv ut studieplanen med hvilke emner som er i hvert semester.")
    print("05. Sjekk om studieplanen er gyldig eller ikke.")
    print("06. Lagre emnene og studieplanen til fil")
    print("07. Les inn emnene og studieplanen fra fil.")
    print("08. Avslutt.")
 
# valg1() v1.3. # Dette erstatter tidligere kode som het emne_liste
def valg1(): 
    

    emnekode = input("Skriv inn emnekode: ")
    navn = input("Skriv inn navn på emnet: ")
    sesong_input = int(input("Skriv inn 1 for høst eller 2 for vår: ")) # kan lage try except blokk for å få prøve tall igjen hvis ikke int.
    

    if sesong_input == 1: #grunnen til at det står sesong og ikke semester som i høst/vår semester er for å unngå overlapp i navn og forvirring siden i oppgave 2 trenger man å bruke "semester" i koden.
        sesong = "Høst"
    elif sesong_input == 2:
        sesong = "Vår"
    else:
        print("vennligst velg 1 (for høst) eller 2 (for vår)") # Lag en try except blokk senere..............    
    
    studiepoeng = int(input("Skriv inn studie poeng: "))

    emner[emnekode] = {
        "navn": navn,
        "sesong": sesong,
        "studiepoeng": studiepoeng
    }
    print(f"Emnekode: {emnekode} er lagt til.")    

def valg2(): #Legg til et emne i studieplanen #Husk å legge til try except senere etter v1.4. 
    #print("\nVelg emne:") # husk å legge til kode for å sjekke... basically bare aktiver valg3() funksjon og print ut emner. Og i neste kode, bruk valget til å sette inn i lista.
    valg3() # funksjonen skriver ut emne lister som er tilgjengelige.
    emnekode = input("Skriv inn emnekoden du vil legge til i studieplanet.") # kan prøve å filtrere / gjøre ryddigere ved f.eks .strip(), .lower()  eller lignende. Skal bare kode den funksjonelle delen før jeg setter meg for mye inn i feilhåndtering og exept blokk osv...
    

    if emnekode not in emner:
        print("Feil. Emne finnes ikke.")
        return
    

    print("Velg semesteret du ønsker å legge emnet i.")
    for i in range(1, 7):
        #print(f"{i}: sem{i}") #Egentlig kan vi simplifisere det ved å bare bruke 1-6 isteden for sem 1-6...
        print(f"Semester {i}")             

    semester = int(input("Skriv et tall fra 1 til 6: "))# legg til try except senere, dette var v1.5
    # husk value error, elif, else osv.....
    studieplan[semester].append(emnekode)
    print(f"Emnekode: {emnekode} ble lagt til i Semester {semester}")


def valg3(): #Skriv ut liste over emner
    print("\nEmner:") # Denne ligger før "for løkken" siden vi bare ønsker å printe ut overskriften en gang.
    for kode, data in emner.items(): # siden dictionary går par-vis som nøkkel og verdi. 
        print(f"Emnekode: {kode}, Navn: {data['navn']}, Sesong: {data['sesong']}, Studiepoeng: {data['studiepoeng']} ") 
        #kode er emnekode, data er verdier i emner. #tilsvarende kode på generisk form blir vell nøkkel og verdi som dictionaries har. 


#Skal kommentere mer på denne etterpå...
def valg4():  # Vis hele studieplanen v1.7
    print("\nStudieplan:")
    for semester, emnekoder in studieplan.items():
        print(f"\nSemester {semester}:")
        if not emnekoder:
            print("  (Ingen emner)")  # If the semester list is empty
        else:
            for kode in emnekoder:
                emne = emner.get(kode)
                if emne:
                    print(f"  {kode}: {emne['navn']} ({emne['sesong']}, {emne['studiepoeng']} studiepoeng)")
                else:
                    print(f"  {kode}: (Ukjent emne)")

def valg5():  #Sjekk om studieplanen er gyldig
    print("\nSjekker om studieplanen er gyldig...")
    ugyldige_semestere = []

    for semester, emnekoder in studieplan.items():
        total_studiepoeng = 0
        for kode in emnekoder:
            emne = emner.get(kode)
            if emne:
                total_studiepoeng += emne["studiepoeng"]
        
        if total_studiepoeng != 30:
            ugyldige_semestere.append((semester, total_studiepoeng))

    if not ugyldige_semestere:
        print("Studieplanen er gyldig. Hvert semester har 30 studiepoeng.")
    else:
        print("Studieplanen er ikke gyldig.")
        for semester, poeng in ugyldige_semestere:
            print(f"Semester {semester} har {poeng} studiepoeng.")



def hoved_program(): #EDIT main loop her etterpå, dette er hvertfall starten.
    
    while True:
        meny_liste() #skriver ut meny valgene 
        
        valg = int(input("\nVelg et tall fra menyen: ")) #sikkrer at input tallet blir heltall så hele programmet ikke bare krasjer...  
        #midlertidig kommentert ut valg 9-14.
        if valg == 1:
            valg1()
        elif valg == 2: 
            valg2()
        elif valg == 3:
            valg3()
        elif valg == 4:
            valg4()
        elif valg == 5:
            valg5()
        elif valg == 6:
            valg6()
        elif valg == 7:
            valg7()
        elif valg == 8:
            print("Avslutter programmet")
            break
        else:
            print("Feil, velg et tall mellom 1 og 8.") #husk å endre fra 8 til 14 når det implimenteres. 
            #Slettet de andre, siden koden crashet da jeg kommenterte ut de andre.


#Kjører hoved programmet for menyen
hoved_program()
