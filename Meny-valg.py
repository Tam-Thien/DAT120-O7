#husk å legge til exceptions for value error og type error.

emne_liste = []

#Printer ut menyen. Har ingen funksjon i seg selv, men trengs for å lese før folk kan velge.
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
    print("09. Frivillig: Slett et emne.")
    print("10. Frivillig: Fjern et emne fra studieprogrammet uten å slette det fra emnelista.")
    print("11. Frivillig: Legg til anbefalt valgemne.")
    print("12. Frivillig: Fjern anbefalt valgemne.")
    print("13. Frivillig: Legg til annet valgemne.")
    print("14. Frivillig: Fjern annet valgemne.")
#meny_liste()

#endre på kode for å legge til på ny måte:
def valg1(): #1) Lag et nytt emne. #ønsket struktur "DAT120": {"navn": data, "sesong": "høst", "studiepoeng": 10}
    
    emnekode = input("Skriv inn emnekode: ")
    navn = input("Skriv inn navn på emnet: ")
    sesong_input = int(input("Skriv inn 1 for høst eller 2 for vår: "))
    if sesong_input == 1: 
        sesong = "høst"
    elif sesong_input == 2:
        sesong = "vår"
    else:
        print("vennligst velg 1 (for høst) eller 2 (for vår)") # Lag en try except blokk senere..............    
    studiepoeng = int(input("Skriv inn studie poeng: "))

    emne = {"emnekode": emnekode, "navn": navn, "sesong": sesong, "studiepoeng": studiepoeng} 
    emne_liste.append(emne)
    print(f"Emne kode {emnekode} er lagt til.")


def valg3(): #Skriv ut liste over emner
    print("Emne liste:")
    for emne in emne_liste:
        print(f"Emnekode: {emne["emnekode"]}, Navn: {emne["navn"]}, Sesong: {emne["sesong"]}, Studiepoeng: {emne["studiepoeng"]}")
        # Vi vet at emne = {"emnekode": emnekode, "navn": navn, "sesong": sesong, "studiepoeng": studiepoeng}
        # f formaterer så vi kan bruke variabler.
        # {emne} henter variabler mens {emne['navn']} henter navn i emne.
        # emne er en "ordbok" --> a dictionary. Basically liste.
        # Begrunnelse for valg av dictionary istedenfor liste er fra anbefaling fra oppgaven. Det gjør det enklere å organisere,
        #f.eks når man skal slette. Ulempen er at det kan ta lengre tid å kode, og man må slå opp "katalog" for å finne kode på emnet.




 

#EDIT main loop her etterpå, dette er hvertfall starten.
def hoved_program():
    
    while True:
        meny_liste() #skriver ut meny valgene 
        
        valg = int(input("\nVelg et tall fra menyen: ")) #sikkrer at input tallet blir heltall så hele programmet ikke bare krasjer...  
        
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
        elif valg == 9:
            valg9()
        elif valg == 10:
            valg10()
        elif valg == 11:
            valg11()
        elif valg == 12:
            valg12()
        elif valg == 13:
            valg13()
        elif valg == 14: 
            #valg14()
            print("test14, i def_meny_valg for debug") #for debug, husk å rette opp koden før levering.
        else:
            print("Feil, velg et tall mellom 1 og 14.")
           
                      
#Kjører hoved programmet for menyen
hoved_program()
