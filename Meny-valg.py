#husk å legge til exceptions for value error og type error.

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



emne_liste = []    

'''prøver på denne fremgangsmåten: Vi kan ha en liste for emner, men i listen kan hvert emne være en dictionary.
På den måten kan vi endre og legge til enklere uten å referere til index, siden sletting kan endre index 
rekkefølgen. Ulempen er at det tar lengre til å kode, og at bruker må lete i en oppslags katalog for å finne
ut hva koden til emnet er. Men jeg tror dette er den bedre metoden, mer fleksibelt.'''

def valg1(): #1) Lag et nytt emne.
    emnekode = input("Skriv inn emnekode: ")
    navn = input("Skriv inn navn på emnet: ")
    sesong_input = int(input("Skriv inn 1 for høst og 2 for vår: "))
    studiepoeng = int(input("Skriv inn studie poeng: "))


    if sesong_input == 1: 
        sesong = "høst"
    elif sesong_input == 2:
        sesong = "vår"
    else:
        print("vennligst velg 1 eller 2") # Lag en try except blokk senere..............

    emne_liste.append({
        "emnekode": emnekode,
        "navn": navn,
        "sesong": sesong,
        "studiepoeng": studiepoeng
        })
    print(emne_liste) #for debug, for å se at den går gjennom.

    #print("\ntest print for valg 1") # placeholder debug for precode.
#valg1()
   
def valg3():
    print(emne_liste)

































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






