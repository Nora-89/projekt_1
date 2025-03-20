#seznam pro ukládání úkolů
ukoly=[]
#přidání úkolu
def pridat_ukol():
        ukol = input ("Zadejte nový úkol: ")
        popis_ukolu = input("Zadejte popis Ukolu:")
        if not ukol:
              print("Úkol nemůže být prázdný.")
        if not popis_ukolu:
            print ("Popis úkolu nemůže být prázdný.")      
        else:
              ukoly.append({"ukol":ukol, "popis úkolu":popis_ukolu})
              print("Úkol byl přidán.")


#Zobrazení úkolu
def zobrazit_ukoly():
        if not ukoly:
              print("Seznam úkolů je prázdný.")
        else:
              print("\nSeznam úkolů:")  
        for i, ukol in enumerate(ukoly, 1):
                print(f"{i}. {ukol['ukol']} -{ukol['popis úkolu']} ")

#Odstranení úkolu
def odstranit_ukol():
        zobrazit_ukoly()
        if not ukoly:
            return
            
        try:
            index = int(input("Zadejte číslo úkolu k odstranění: "))-1
            if 0 <= index < len(ukoly):
                vymaz = ukoly.pop(index)
                print(f"Úkol {vymaz['ukol']} byl odstraněn. ")
            else:
                print("Neplatné číslo úkolu. ")
        except ValueError:
             print("Zadejte prosím platné číslo. ")


#zobrazení menu
def Hlavní_menu():
        while True:
            print("\nSprávce úkolů - Hlavní menu")
            print("1. Přidat nový úkol")   
            print("2. Zobrazit úkoly") 
            print("3. Odstranit úkol ")
            print("4. Konec programu ")  

            volba= input("Vyberte možnost (1-4): ").strip()  

            if volba == "1":
                pridat_ukol()
            elif volba == "2":
                zobrazit_ukoly()
            elif volba == "3": 
                 odstranit_ukol()
            elif volba == "4":
                print("Konec programu. ") 
                break
            else:
                print("Neplatná volba, zkuste to znovu. ")

Hlavní_menu()





      