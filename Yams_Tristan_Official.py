# Jeu du Yams

import random
from turtle import pos

#Personnalisation
class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#Création des dés
class Dice():

    nb_face = 6

    # gestion du cas None
    value = None

    #Dés aléatoires
    def roll(self):
        self.value = random.randint(1, self.nb_face)

    #Récupération de la valeur
    def get_value(self):
        return self.value

    #Inscription de la valeur
    def set_value(self, value):
        self.value = value


#Lancement des dés
class Dices():
    dices = []
    count = 0

    new_start = None

    #Dés aléatoires
    def __init__(self):
        for i in range(1, 6):
            self.dices.append(Dice())
    
    #Valeurs des dés
    def __repr__(self):
        return str(self.dices[1].value) + " | " + str(self.dices[2].value) + " | " + str(self.dices[3].value) + " | " + str(self.dices[4].value) + " | " + str(self.dices[5].value)
    
    #Liste des dés
    def roll_all(self):
        for i in range(1, 6):
            self.dices[i].roll()
            print("Dé n°", i, "==>", self.dices[i].value)

    #Sélection des dés
    def roll_selected_dices(self, dices_selected):
        for i in dices_selected:
            self.dices[int(i)].roll()
        print(d)    

d = Dices()

# Score /
class Score():

    #Liste des combinaisons
    combinations = {
        "one" : None,
        "two" : None,
        "three" : None,
        "four" : None,
        "five" : None,
        "six" : None,
        "brelan" : None,
        "carre" : None,
        "full" : None,
        "little_suite" : None,
        "highest_suite" : None,
        "yams" : None,
        "chance" : None
    }  

    #Combinaison : YAMS (5 même chiffre)
    def yams( self, dices ):
        dices_value = self.dices_values_to_array(dices)

        for i in range(1, 7):
            equal_numbers = dices_value.count(i)
            if (equal_numbers == 5):
                return i

    #Combinaison : pour chaque chiffre
    def count_number(self, dices, number):
        counter = 0
        dices_value = self.dices_values_to_array(dices)

        for n in dices_value:
            if n == number:
                counter += 1
        
        return counter * number
    
    #Combinaison : BRELAN (3 même chiffre)
    def brelan( self, dices ):
        dices_value = self.dices_values_to_array(dices)

        for i in range(1, 7):
            equal_numbers = dices_value.count(i)
            if (equal_numbers >= 3):
                return i              

    #Combinaison : CARRE (4 même chiffre)
    def carre( self, dices ):
        dices_value = self.dices_values_to_array(dices)

        for i in range(1, 7):
            equal_numbers = dices_value.count(i)
            if (equal_numbers >= 4):
                return i              
 
    #Combinaison : FULL (3 même chiffre + 2 autres même chiffre = BRELAN + PAIR) 
    def full( self, dices ):
        is_brelan = False
        is_pair = False

        dices_value = self.dices_values_to_array(dices)

        for i in range(1, 7):
            equal_numbers = dices_value.count(i)
            if (equal_numbers >= 3):
                is_brelan = True 
            elif (equal_numbers >= 2):
                is_pair = True

        if (is_brelan and is_pair):
            return True      

    #Combinaison : GRANDE SUITE (12345 ou 23456)
    def highest_suite( self, dices ):
        
        dices_value = self.__sort_array_dices(dices)
        print(dices_value)
 
        if(dices_value == [1, 2, 3, 4, 5] or dices_value == [2, 3, 4, 5, 6]):
            return True

    #Combinaison : PETITE SUITE (1234 ou 2345 ou 3456)
    def little_suite( self, dices ):

        dices_value = self.__sort_array_dices(dices)

        if(dices_value == [1, 2, 3, 4] or dices_value == [2, 3, 4, 5] or dices_value == [3, 4, 5, 6]):
            return True

    def dices_values_to_array(self, dices):
        dices_value = []
        for i in range(0, 5):
            dices_value.append(dices[i].value)
        return dices_value
    
    def __sort_array_dices(self, dices):
        dices_values = self.dices_values_to_array(dices)
        return dices_values.sort()

# Game /
class Game():

    #Récupération de la classe des dés et du score
    dices = Dices()
    score = Score()

    #Début de la partie
    def game_start(self):
        print("------------------------------")
        print("------------------------------")
        print(Bcolors.WARNING + "     Le *Yams* commence !     " + Bcolors.ENDC)
        print("------------------------------")
        print("------------------------------")


    #Gestion des rounds
    def round(self):
            print(Bcolors.OKCYAN + "New Round :" + Bcolors.ENDC)
            print("------------------------------")
            response = input(Bcolors.HEADER + "Voulez vous lancer les dés ? " + Bcolors.ENDC)

    
            if "oui" in response:
                print("------------------------------")
                print(Bcolors.UNDERLINE + "Voici les dés lancés :" + Bcolors.ENDC)
                g.dices.roll_all()
                print("------------------------------")
                print(Bcolors.FAIL + "Essai restant : 2" + Bcolors.ENDC)
                g.game_continue()

            
            elif "non" in response:
                print("------------------------------")
                g.game_end()
                exit()

            
            elif response != "oui" or "non":
                print("------------------------------")
                print(Bcolors.FAIL + "Erreur ! Veuillez entrer oui ou non " + Bcolors.ENDC)
                print("------------------------------")
                return(g.round())
    
    #Déroulé de la partie
    def game_continue(self):
        print("------------------------------")
        response = input(Bcolors.HEADER + "Voulez-vous relancer les dés ? oui ? non ? tous les dés ? ==> " + Bcolors.ENDC)
        if "non" in response:
            print("------------------------------")
            self.possibilities = self.__get_possibilities()
            self.show_possibilities(self.possibilities)
            self.show_combinations(self.score.combinations)
            choixCombinaison = input(Bcolors.HEADER + "Quelle combinaison voulez-vous choisir ? ==> " + Bcolors.ENDC)
            print("------------------------------")
            g.round()


        if "oui" in response:
            print("------------------------------")
            dices_question = input(Bcolors.HEADER + "Quel(s) dé(s) voulez-vous relancer ? (1/2/3/4/5) ==> " + Bcolors.ENDC)
            print("------------------------------")
            print(Bcolors.UNDERLINE +"Résultat des dés : " + Bcolors.ENDC)
            g.dices.roll_selected_dices(str(dices_question))
            print("------------------------------")
            print(Bcolors.FAIL + "Essai restant : 1" + Bcolors.ENDC)
            print("------------------------------")
            response = input(Bcolors.HEADER + "Voulez-vous relancer les dés ? " + Bcolors.ENDC)
            if "non" in response:
                print("------------------------------")
                self.possibilities = self.__get_possibilities()
                self.show_possibilities(self.possibilities)
                self.show_combinations(self.score.combinations)
                choixCombinaison = input(Bcolors.HEADER + "Quelle combinaison voulez-vous choisir ? ==> " + Bcolors.ENDC)
                g.round()
                print("------------------------------")
                g.round()
            if "oui" in response:
                print("------------------------------")
                dices_question = input(Bcolors.HEADER + "Quel(s) dé(s) voulez-vous relancer ? (1/2/3/4/5) => " + Bcolors.ENDC)
                print("------------------------------")
                print(Bcolors.UNDERLINE + "Résultat des dés : " + Bcolors.ENDC)
                g.dices.roll_selected_dices(str(dices_question))
                print("------------------------------")
                print(Bcolors.FAIL + "Vous n'avez plus d'essai" + Bcolors.ENDC)
                print("------------------------------")
                self.possibilities = self.__get_possibilities()
                self.show_possibilities(self.possibilities)
                self.show_combinations(self.score.combinations)
                choixCombinaison = input(Bcolors.HEADER + "Quelle combinaison voulez-vous choisir ? ==> " + Bcolors.ENDC)
                g.round()


        if "tous les dés" in response:
            g.dices.roll_all()
            print("------------------------------")
            print(Bcolors.FAIL + "Essai restant : 1" + Bcolors.ENDC)
            print("------------------------------")
            response = input(Bcolors.HEADER + "Voulez-vous relancer les dés ? " + Bcolors.ENDC)
            if "non" in response:
                print("------------------------------")
                self.possibilities = self.__get_possibilities()
                self.show_possibilities(self.possibilities)
                self.show_combinations(self.score.combinations)
                choixCombinaison = input(Bcolors.HEADER + "Quelle combinaison voulez-vous choisir ? ==> " + Bcolors.ENDC)
                g.round()
                print("------------------------------")
                g.round()
            if "oui" in response:
                print("------------------------------")
                dices_question = input(Bcolors.HEADER + "Quel(s) dé(s) voulez-vous relancer ? (1/2/3/4/5) => " + Bcolors.ENDC)
                print("------------------------------")
                print(Bcolors.UNDERLINE + "Résultat des dés : " + Bcolors.ENDC)
                g.dices.roll_selected_dices(str(dices_question))
                print("------------------------------")
                print(Bcolors.FAIL + "Vous n'avez plus d'essai" + Bcolors.ENDC)
                print("------------------------------")
                self.possibilities = self.__get_possibilities()
                self.show_possibilities(self.possibilities)
                self.show_combinations(self.score.combinations)
                choixCombinaison = input(Bcolors.HEADER + "Quelle combinaison voulez-vous choisir ? ==> " + Bcolors.ENDC)
                g.round()
            if "tous les dés" in response:
                g.dices.roll_all()
                print("------------------------------")
                print(Bcolors.FAIL + "Vous n'avez plus d'essai" + Bcolors.ENDC)
                print("------------------------------")
                self.possibilities = self.__get_possibilities()
                self.show_possibilities(self.possibilities)
                self.show_combinations(self.score.combinations)
                choixCombinaison = input(Bcolors.HEADER + "Quelle combinaison voulez-vous choisir ? ==> " + Bcolors.ENDC)
                print("------------------------------")
                g.round()

        self.__set_scores(choixCombinaison)

    #Présenter les différentes possibilités
    def show_possibilities(self, possibilities):
        print('\nPossibilitées possibles : ' + str(possibilities) + '\n')

    #Présenter les différentes combinaisons possibles
    def show_combinations(self, combinations):
        for line in combinations:
            print (Bcolors.WARNING + '--------------------' + Bcolors.ENDC)
            if (combinations[line] == None):
                print(Bcolors.WARNING + '|' + line + '|   ' + Bcolors.ENDC)
            else:
                print(Bcolors.WARNING + '|' + line + '| ' + str(combinations[line]) + Bcolors.ENDC)


    #Gestion des possibilités pour les combinaisons
    def __get_possibilities(self):
        possibilities = []

        if (self.score.combinations["chance"] == None):
            possibilities.append('chance')

        yams = self.score.yams( self.dices.dices )
        if (yams > 0 and yams < 7):
            if (self.score.combinations["yams"] == None):
                possibilities.append('yams')

        if (self.score.combinations["one"] == None):
            possibilities.append('one')
        if (self.score.combinations["two"] == None):
            possibilities.append('two')
        if (self.score.combinations["three"] == None):
            possibilities.append('three')
        if (self.score.combinations["four"] == None):
            possibilities.append('four')
        if (self.score.combinations["five"] == None):
            possibilities.append('five')
        if (self.score.combinations["six"] == None):
            possibilities.append('six')

        brelan = self.score.brelan( self.dices.dices )
        if (brelan != False):
            if (self.score.combinations["brelan"] == None):
                possibilities.append('brelan')

        carre = self.score.carre( self.dices.dices )
        if (carre != False):
            if (self.score.combinations["carre"] == None):
                possibilities.append('carre')

        full = self.score.full( self.dices.dices )
        if (full == True):
            if (self.score.combinations["full"] == None):
                possibilities.append('full')

        highest_suite = self.score.highest_suite( self.dices.dices )
        if (highest_suite == True):
            if (self.score.combinations["highest_suite"] == None):
                possibilities.append('highest_suite')
            if (self.score.combinations["little_suite"] == None):
                possibilities.append('little_suite')

        little_suite = self.score.little_suite( self.dices.dices )
        if (little_suite == True):
            if (self.score.combinations["little_suite"] == None):
                possibilities.append('little_suite')
        
        return possibilities

    def __set_scores(self, choixCombinaison):
        if (choixCombinaison == "one"):
            count = self.score.count_number(self.dices.dices, 1)
            self.score.combinations[choixCombinaison] = count
        elif (choixCombinaison == "two"):
            count = self.score.count_number(self.dices.dices, 2)
            self.score.combinations[choixCombinaison] = count
        elif (choixCombinaison == "three"):
            count = self.score.count_number(self.dices.dices, 3)
            self.score.combinations[choixCombinaison] = count
        elif (choixCombinaison == "four"):
            count = self.score.count_number(self.dices.dices, 4)
            self.score.combinations[choixCombinaison] = count
        elif (choixCombinaison == "five"):
            count = self.score.count_number(self.dices.dices, 5)
            self.score.combinations[choixCombinaison] = count
        elif (choixCombinaison == "six"):
            count = self.score.count_number(self.dices.dices, 6)
            self.score.combinations[choixCombinaison] = count
        elif (choixCombinaison == "brelan"):
            self.score.combinations[choixCombinaison] = self.score.brelan(self.dices)
        elif (choixCombinaison == "carre"):
            self.score.combinations[choixCombinaison] = self.score.carre(self.dices)
        elif (choixCombinaison == "full"):
            self.score.combinations[choixCombinaison] = 25
        elif (choixCombinaison == "little_suite"):
            self.score.combinations[choixCombinaison] = 30
        elif (choixCombinaison == "highest_suite"):
            self.score.combinations[choixCombinaison] = 40
        elif (choixCombinaison == "yams"):
            self.score.combinations[choixCombinaison] = 50
        elif (choixCombinaison == "chance"):
            self.score.combinations[choixCombinaison] = sum(self.score.dices_values_to_array(self.dices.dices))

    #Relancer une partie
    def game_restart(self):
        response = input(Bcolors.OKBLUE + "Voulez-vous relancer une partie ? " + Bcolors.ENDC)
        if "oui" in response:
            g.game_start()


    #Terminer une partie
    def game_end(self):
        response = input(Bcolors.OKBLUE + "Quitter le jeu ? " + Bcolors.ENDC)
        if "oui" in response:
            print("------------------------------")
            print(Bcolors.FAIL + Bcolors.BOLD + "Fin du jeu !" + Bcolors.ENDC)
            exit()   


g = Game()
s = Score()
g.game_start()
g.round()
g.game_continue()
g.game_end()



