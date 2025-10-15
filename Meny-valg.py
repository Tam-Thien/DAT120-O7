
emner = {} # Istedenfor eempty list bruker vi empty dictionary. 
#kan skrive studieplan = {semester: [] for semester in range(1, 7)} men ønsker å ha listene klart. Egen prefferanse, men koden med "for-løkke" er bedre
"""studieplan = {
    "sem1": [],
    "sem2": [],
    "sem3": [],
    "sem4": [],
    "sem5": [],
    "sem6": [],
}    """""

#Jeg bare koder denne delen enklere ved å bare bruke tall, så slipper vi f streng formateringen og hele pakken.
#Ok, viser seg at jeg måtte bruke f streng formatering like vell, men det ble mer oversiktlig i valg2(). 
#Printer ut semester listene inne i studieplan.
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
    try:
        studiepoeng = int(input("Skriv inn studie poeng: "))
    except ValueError:
        print("Skriv et tall")
        return
    emner[emnekode] = {
        "navn": navn,
        "sesong": sesong,
        "studiepoeng": studiepoeng
    }
    print(f"Emnekode: {emnekode} er lagt til.")    
#--- OK, tror jeg forstår feilen nå. når vi endrer på valg()1 så gjør endringen error i valg3() pga.  f formatering av emnekode.
#skal prøve å fikse det.
#Fiksa :D
def valg2():  # Legg til et emne i studieplanen
    valg3()  # Skriver ut tilgjengelige emner

    emnekode = input("Skriv inn emnekoden du vil legge til i studieplanen: ").strip().lower()

    # Sjekk om emnet allerede finnes i studieplanen
    for semester_emner in studieplan.values():
        if emnekode in semester_emner:
            print("Emnet er allerede i studieplanen.")
            return  

    emne = emner.get(emnekode)
    if not emne:
        print("Emnet finnes ikke :(")
        return

    sesong = emne['sesong']

    print("Velg semesteret du ønsker å legge emnet i.")

    while True:
        try:
            semester = int(input("Skriv et tall fra 1 til 6: "))
            if 1 <= semester <= 6:

                if sesong == "Høst" and semester not in [1, 3, 5]:
                    print("Dette emnet kan bare legges i HØST-semester (1, 3, 5).")
                    return
                if sesong == "Vår" and semester not in [2, 4, 6]:
                    print("Dette emnet kan bare legges i VÅR-semester (2, 4, 6).")
                    return

                # Sjekk om emnet kan legges til uten å overstige 30 studiepoeng
                nåværende_poeng = sum(emner.get(k, {}).get("studiepoeng", 0) for k in studieplan[semester])
                nytt_total = nåværende_poeng + emne["studiepoeng"]

                if nytt_total > 30:
                    print(f"Kan ikke legge til. Semester {semester} fordi {nytt_total} studiepoeng (maks er 30).")
                    return

                # Alt OK, legg til emne
                studieplan[semester].append(emnekode)
                print(f"{emnekode} ble lagt til i semester {semester}.")
                return

            else:
                print("Velg et tall mellom 1 og 6.")
        except ValueError:
            print("Skriv inn et gyldig tall.")




           
    
                
      
                           
    

    #semester = int(input("Hvilket semester skal"))
    #studieplan[semester]





def valg3(): #Skriv ut liste over emner
    print("\nEmner:") # Denne ligger før "for løkken" siden vi bare ønsker å printe ut overskriften en gang.
    for kode, data in emner.items(): # siden dictionary går par-vis som nøkkel og verdi. 
        print(f"Emnekode: {kode}, Navn: {data['navn']}, Sesong: {data['sesong']}, Studiepoeng: {data['studiepoeng']} ") 
        #kode er emnekode, data er verdier i emner. #tilsvarende kode på generisk form blir vell nøkkel og verdi som dictionaries har. 

'''
def valg4(): #Vis studieplan #husk å teste denne, blir ikke ferdig idag, det er sent på natta... v1.5.1
    print("\nStudieplan:")
    for semester, emnekoder in studieplan.items(): #alternativt, se *** nede:
        print(f"Semester {semester}") #

    for kode in emnekoder:
        emne = emner.get(kode) 
        if emne:
            print(f"Emnekode: {kode}, Navn: {emne['navn']}, Sesong: {emne['sesong']}, Studiepoeng: {emne['studiepoeng']}")   
        '''
        
#  *** alternativt kan vi skrive slikt hvis vi ikke ønsker .items()   : 
'''
def valg4():  # Vis hele studieplanen
    print("\nStudieplan:")
    for semester in studieplan:  # iterates over keys
        emnekoder = studieplan[semester]  # gets value from key
        print(f"\n{semester}:")
        for emnekode in emnekoder:
            print(f"{emnekode}")
'''
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
   #--------------------------------------------------------------------------------------------------------------
#koden fungerer endelig, men må sette inn sperre for duplikat. Må også sette inn try except, elif, else, osv... 
 #--------------------------------------------------------------------------------------------------------------------




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