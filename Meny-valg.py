#Liten notat om at jeg T.T har laget denne delen av koden kl 3 midt på natta på en søndags-morning...
#Dette er bare meny utskriften, den funksjonelle delen kommer senere nedover koden.  
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

def meny_valg(): 
         
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
        valg8()
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


def valg1(): #1) Lag et nytt emne.
    print("\ntest print for valg 1")

    




































#EDIT main loop her etterpå, dette er hvertfall starten.
meny_liste() #skriver ut meny valgene
meny_valg()   #funksjon for hva som skjer når velger tallet. 
              #Når du f.eks velger 1 går du inn i valg1() funksjonen som er å lage et nytt emne.
    






