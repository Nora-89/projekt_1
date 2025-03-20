#seznam pro ukládání úkolů
ukoly=[]
#přidání úkolu
def pridat_ukol():
        ukol = input ("Zadejte nový úkol: ")
        if not ukol:
              print("Úkol nemůže být prázdný")
        else:
              ukoly.append(ukol)
              print(f"Úkol '{ukol}' byl přidán")

#Zobrazení úkolu
def zobrazit_ukoly():
        if not ukoly:
              print("Seznam úkolů je prázdný.")
        else:
              print("\nSeznam úkolů:")  
        for i, ukol in enumerate(ukoly, 1):
                print(f"{i}. {ukol}")

#Odstranení úkolu
def odstranit_ukol():
        zobrazit_ukoly()
        if ukoly:
            try:
                index = int(input("Zadejte číslo úkolu k odstranění: ")) 
                if 0 <= index < len(ukoly):
                        odstraneny = ukoly.pop(index)
                        print(f"Úkol '{odstraneny}' byl odstraněn. ")
                else:
                      print("Neplatné číslo úkolu. ")              
            except ValueError:
                  print("Zadejte prosím platné číslo. ")  
#zobrazení menu
def Hlavní_menu():
        ukoly = [] # Seznam úkolů
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
                print("Ukončuji program. ") 
                break
            else:
                print("Neplatná volba, zkuste to znovu. ")