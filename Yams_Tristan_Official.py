# Jeu du Yams

import random

# Personnalisation


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

# Création des dés


class Dice():

    nb_face = 6

    # gestion du cas None
    value = None

    # Dés aléatoires
    def roll(self):
        self.value = random.randint(1, self.nb_face)

    # Récupération de la valeur
    def get_value(self):
        return self.value

    # Inscription de la valeur
    def set_value(self, value):
        self.value = value


# Lancement des dés
class Dices():
    dices = []

    # Dés aléatoires
    def __init__(self):
        for i in range(0, 5):
            self.dices.append(Dice())

    # Valeurs des dés
    def __repr__(self):
        return str(self.dices[1].value) + " | " + str(self.dices[2].value) + " | " + str(self.dices[3].value) + " | " + str(self.dices[4].value) + " | " + str(self.dices[5].value)

    # Liste des dés
    def roll_all(self):
        for i in range(1, 6):
            self.dices[i].roll()
            print("Dé n°", i, "==>", self.dices[i].value)

    # Sélection des dés
    def roll_selected_dices(self, dices_selected):
        for i in dices_selected:
            self.dices[int(i)].roll()
        print(d)


d = Dices()

# Score /


class Score():

    # Liste des combinaisons
    combinations = {"as": None, "two": None, "three": None, "four": None, "five": None, "six": None, "brelan": None,
                    "carre": None, "full": None, "small_suite": None, "big_suite": None, "yams": None, "chance": None}

    # Retourner la valeur des dés
    def dices_values_dices(self, dices):
        dices_value = []
        for i in range(1, 6):
            dices_value.append(dices[i].value)
        return dices_value

    # Combinaison : YAMS (5 même chiffre)
    def yams(self, dices):
        dices_value = self.dices_values_dices(dices)

        for i in range(1, 7):
            same_numbers = dices_value.count(i)
            if (same_numbers == 5):
                return i

        return False

    # Combinaison : pour chaque chiffre
    def count_number(self, dices, number):
        counter = 0
        dices_value = self.dices_values_dices(dices)

        for n in dices_value:
            if n == number:
                counter += 1

        return counter * number

    # Combinaison : BRELAN (3 même chiffre)
    def brelan(self, dices):
        dices_value = self.dices_values_dices(dices)

        for i in range(1, 7):
            same_numbers = dices_value.count(i)
            if (same_numbers >= 3):
                return i

        return False

    # Combinaison : CARRE (4 même chiffre)
    def carre(self, dices):
        dices_value = self.dices_values_dices(dices)

        for i in range(1, 7):
            same_numbers = dices_value.count(i)
            if (same_numbers >= 4):
                return i

        return False

    # Combinaison : FULL (3 même chiffre + 2 autres même chiffre = BRELAN + PAIR)
    def full(self, dices):
        brelan = False
        pair = False

        dices_value = self.dices_values_dices(dices)

        for i in range(1, 7):
            same_numbers = dices_value.count(i)
            if (same_numbers >= 3):
                brelan = True
            elif (same_numbers >= 2):
                pair = True

        if (brelan == True and pair == True):
            return True

        return False

    # Combinaison : GRANDE SUITE (12345 ou 23456)
    def big_suite(self, dices):

        dices_value = self.dices_values_dices(dices)

        dices_value.sort()

        if (dices_value[0] == 1 and dices_value[1] == 2 and dices_value[2] == 3 and dices_value[3] == 4 and dices_value[4] == 5 or dices_value[0] == 2 and dices_value[1] == 3 and dices_value[2] == 4 and dices_value[3] == 5 and dices_value[4] == 6):
            return True

        return False

    # Combinaison : PETITE SUITE (1234 ou 2345 ou 3456)
    def small_suite(self, dices):

        dices_value = self.dices_values_dices(dices)

        dices_value.sort()

        if (dices_value[0] == 1 and dices_value[1] == 2 and dices_value[2] == 3 and dices_value[3] == 4 or dices_value[0] == 2 and dices_value[1] == 3 and dices_value[2] == 4 and dices_value[3] == 5 or dices_value[0] == 3 and dices_value[1] == 4 and dices_value[2] == 5 and dices_value[3] == 6):
            return True

        return False


# Game /
class Game():

    # Récupération de la classe des dés et du score
    dices = Dices()
    score = Score()

    # Début de la partie
    def game_start(self):
        print("------------------------------")
        print("------------------------------")
        print(Bcolors.FAIL + Bcolors.BOLD + "     Le *Yams* commence !     " + Bcolors.ENDC)
        print("------------------------------")
        self.round()

    nbRound = 0

    # Gestion des rounds
    def round(self):
        self.nbRound += 1
        while self.nbRound < 14:
            print("------------------------------")
            print(Bcolors.WARNING + "Round n° " +
                  str(self.nbRound) + ' sur 14' + Bcolors.ENDC)
            print("------------------------------")
            self.load()
        print(Bcolors.FAIL + Bcolors.BOLD + "Fin du jeu ! " + Bcolors.ENDC)

        # Gestion du bonus de fin de game
        if (self.score.combinations.get("as") + self.score.combinations.get("two") + self.score.combinations.get("three") + self.score.combinations.get("four") + self.score.combinations.get("five") + self.score.combinations.get("six") >= 63):
            bonus = 35
            bonus = bonus + sum(self.score.combinations.values())
            print("------------------------------")
            print(Bcolors.OKBLUE + "BONUS ! 35 points de plus pour avoir dépasser 63 points pour les combinaisons : as, two, three, four, five et six ! Bien joué." + Bcolors.ENDC)
            print("------------------------------")
            print(Bcolors.OKGREEN + "Votre score total est de : " + str(bonus) + " points" + Bcolors.ENDC)
            print("------------------------------")
            exit()

        elif (self.score.combinations.get("as") + self.score.combinations.get("two") + self.score.combinations.get("three") + self.score.combinations.get("four") + self.score.combinations.get("five") + self.score.combinations.get("six") < 63):
            print("------------------------------")
            print(Bcolors.OKGREEN + "Votre score total est de : " +
                  str(sum(self.score.combinations.values())) + " points" + Bcolors.ENDC)
            print("------------------------------")
            exit()

    # Commencement de la partie

    def load(self):
        response = input(Bcolors.HEADER +
                         "Voulez vous lancer les dés ? " + Bcolors.ENDC)

        if "oui" in response:
            print("------------------------------")
            print(Bcolors.UNDERLINE + "Voici les dés lancés :" + Bcolors.ENDC)
            self.dices.roll_all()
            print("------------------------------")
            print(Bcolors.FAIL + "Essai restant : 2" + Bcolors.ENDC)
            self.game_continue()

        if "non" in response:
            print("------------------------------")
            self.game_restart()
            exit()

        if response != "oui" or "non":
            print("------------------------------")
            print(Bcolors.FAIL + "Erreur ! Veuillez entrer oui ou non " + Bcolors.ENDC)
            print("------------------------------")
            response = input(Bcolors.HEADER +
                             "Voulez vous lancer les dés ? " + Bcolors.ENDC)

    # Déroulé de la partie

    def game_continue(self):
        print("------------------------------")
        response = input(
            Bcolors.HEADER + "Voulez-vous relancer les dés ? oui ? non ? tous les dés ? ==> " + Bcolors.ENDC)
        if "non" in response:
            print("------------------------------")
            possibilities = self.__get_possibilities()
            self.show_possibilities(possibilities)
            self.show_combinations(self.score.combinations)
            print("------------------------------")
            choixCombinaison = input(
                Bcolors.HEADER + "Quelle combinaison voulez-vous choisir ou à sacrifier si aucune possibilité ? ==> " + Bcolors.ENDC)
            self.possibilities_set_score(choixCombinaison, possibilities)
            print(Bcolors.BOLD +
                  "\nVotre score a bien été enregistré !\n" + Bcolors.ENDC)
            print("------------------------------")
            self.round()

        if "oui" in response:
            print("------------------------------")
            dices_question = input(
                Bcolors.HEADER + "Quel(s) dé(s) voulez-vous relancer ? (1/2/3/4/5) ==> " + Bcolors.ENDC)
            print("------------------------------")
            print(Bcolors.UNDERLINE + "Résultat des dés : " + Bcolors.ENDC)
            self.dices.roll_selected_dices(str(dices_question))
            print("------------------------------")
            print(Bcolors.FAIL + "Essai restant : 1" + Bcolors.ENDC)
            print("------------------------------")
            response = input(
                Bcolors.HEADER + "Voulez-vous relancer les dés ? oui ? non ? tous les dés ? ==> " + Bcolors.ENDC)
            if "non" in response:
                print("------------------------------")
                possibilities = self.__get_possibilities()
                self.show_possibilities(possibilities)
                self.show_combinations(self.score.combinations)
                print("------------------------------")
                choixCombinaison = input(
                    Bcolors.HEADER + "Quelle combinaison voulez-vous choisir ou à sacrifier si aucune possibilité ? ==> " + Bcolors.ENDC)
                self.possibilities_set_score(choixCombinaison, possibilities)
                print(Bcolors.BOLD +
                      "\nVotre score a bien été enregistré !\n" + Bcolors.ENDC)
                print("------------------------------")
                self.round()
            if "oui" in response:
                print("------------------------------")
                dices_question = input(
                    Bcolors.HEADER + "Quel(s) dé(s) voulez-vous relancer ? (1/2/3/4/5) => " + Bcolors.ENDC)
                print("------------------------------")
                print(Bcolors.UNDERLINE + "Résultat des dés : " + Bcolors.ENDC)
                self.dices.roll_selected_dices(str(dices_question))
                print("------------------------------")
                print(Bcolors.FAIL + "Vous n'avez plus d'essai" + Bcolors.ENDC)
                print("------------------------------")
                possibilities = self.__get_possibilities()
                self.show_possibilities(possibilities)
                self.show_combinations(self.score.combinations)
                print("------------------------------")
                choixCombinaison = input(
                    Bcolors.HEADER + "Quelle combinaison voulez-vous choisir ou à sacrifier si aucune possibilité ? ==> " + Bcolors.ENDC)
                self.possibilities_set_score(choixCombinaison, possibilities)
                print(Bcolors.BOLD +
                      "\nVotre score a bien été enregistré !\n" + Bcolors.ENDC)
                self.round()
            if "tous les dés" in response:
                self.dices.roll_all()
                print("------------------------------")
                print(Bcolors.FAIL + "Vous n'avez plus d'essai" + Bcolors.ENDC)
                print("------------------------------")
                possibilities = self.__get_possibilities()
                self.show_possibilities(possibilities)
                self.show_combinations(self.score.combinations)
                print("------------------------------")
                choixCombinaison = input(
                    Bcolors.HEADER + "Quelle combinaison voulez-vous choisir ou à sacrifier si aucune possibilité ? ==> " + Bcolors.ENDC)
                self.possibilities_set_score(choixCombinaison, possibilities)
                print(Bcolors.BOLD +
                      "\nVotre score a bien été enregistré !\n" + Bcolors.ENDC)
                print("------------------------------")
                self.round()

        if "tous les dés" in response:
            self.dices.roll_all()
            print("------------------------------")
            print(Bcolors.FAIL + "Essai restant : 1" + Bcolors.ENDC)
            print("------------------------------")
            response = input(
                Bcolors.HEADER + "Voulez-vous relancer les dés ? oui ? non ? tous les dés ? ==> " + Bcolors.ENDC)
            if "non" in response:
                print("------------------------------")
                possibilities = self.__get_possibilities()
                self.show_possibilities(possibilities)
                self.show_combinations(self.score.combinations)
                print("------------------------------")
                choixCombinaison = input(
                    Bcolors.HEADER + "Quelle combinaison voulez-vous choisir ou à sacrifier si aucune possibilité ? ==> " + Bcolors.ENDC)
                self.possibilities_set_score(choixCombinaison, possibilities)
                print(Bcolors.BOLD +
                      "\nVotre score a bien été enregistré !\n" + Bcolors.ENDC)
                self.round()
                print("------------------------------")
                self.round()
            if "oui" in response:
                print("------------------------------")
                dices_question = input(
                    Bcolors.HEADER + "Quel(s) dé(s) voulez-vous relancer ? (1/2/3/4/5) => " + Bcolors.ENDC)
                print("------------------------------")
                print(Bcolors.UNDERLINE + "Résultat des dés : " + Bcolors.ENDC)
                self.dices.roll_selected_dices(str(dices_question))
                print("------------------------------")
                print(Bcolors.FAIL + "Vous n'avez plus d'essai" + Bcolors.ENDC)
                print("------------------------------")
                possibilities = self.__get_possibilities()
                self.show_possibilities(possibilities)
                self.show_combinations(self.score.combinations)
                print("------------------------------")
                choixCombinaison = input(
                    Bcolors.HEADER + "Quelle combinaison voulez-vous choisir ou à sacrifier si aucune possibilité ? ==> " + Bcolors.ENDC)
                self.possibilities_set_score(choixCombinaison, possibilities)
                print(Bcolors.BOLD +
                      "\nVotre score a bien été enregistré !\n" + Bcolors.ENDC)
                self.round()
            if "tous les dés" in response:
                self.dices.roll_all()
                print("------------------------------")
                print(Bcolors.FAIL + "Vous n'avez plus d'essai" + Bcolors.ENDC)
                print("------------------------------")
                possibilities = self.__get_possibilities()
                self.show_possibilities(possibilities)
                self.show_combinations(self.score.combinations)
                print("------------------------------")
                choixCombinaison = input(
                    Bcolors.HEADER + "Quelle combinaison voulez-vous choisir ou à sacrifier si aucune possibilité ? ==> " + Bcolors.ENDC)
                self.possibilities_set_score(choixCombinaison, possibilities)
                print(Bcolors.BOLD +
                      "\nVotre score a bien été enregistré !\n" + Bcolors.ENDC)
                print("------------------------------")
                self.round()

        if response != "oui" or "non" or "tous les dés":
            print("------------------------------")
            print(
                Bcolors.FAIL + "Erreur ! Veuillez entrer oui / non ou tous les dés" + Bcolors.ENDC)
            return (self.game_continue())

    # Présenter les différentes possibilités

    def show_possibilities(self, possibilities):
        print('\nCombinaisons possibles : ' + str(possibilities) + '\n')

    # Présenter les différentes combinaisons possibles
    def show_combinations(self, combinations):
        print('------------------------------')
        print((Bcolors.WARNING + "Combinaisons" + Bcolors.ENDC) +
              "  ==>  " + (Bcolors.OKGREEN + "Score" + Bcolors.ENDC))
        for table in combinations:
            print('------------------------------')
            if (combinations[table] == None):
                print(Bcolors.OKBLUE + table + Bcolors.ENDC)
            else:
                print((Bcolors.WARNING + table + Bcolors.ENDC) + '  ==>  ' +
                      (Bcolors.OKGREEN + '|' + str(combinations[table]) + '|' + Bcolors.ENDC))

    # Gestion des possibilités pour les combinaisons
    def __get_possibilities(self):
        possibilities = []

        if (self.score.combinations["chance"] == None):
            possibilities.append('chance')

        if (self.score.combinations["as"] == None):
            possibilities.append('as')

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

        yams = self.score.yams(self.dices.dices)
        if (yams == 5):
            if (self.score.combinations["yams"] == None):
                possibilities.append('yams')

        brelan = self.score.brelan(self.dices.dices)
        if (brelan != False):
            if (self.score.combinations["brelan"] == None):
                possibilities.append('brelan')

        carre = self.score.carre(self.dices.dices)
        if (carre != False):
            if (self.score.combinations["carre"] == None):
                possibilities.append('carre')

        full = self.score.full(self.dices.dices)
        if (full == True):
            if (self.score.combinations["full"] == None):
                possibilities.append('full')

        big_suite = self.score.big_suite(self.dices.dices)
        if (big_suite == True):
            if (self.score.combinations["big_suite"] == None):
                possibilities.append('big_suite')

        small_suite = self.score.small_suite(self.dices.dices)
        if (small_suite == True):
            if (self.score.combinations["small_suite"] == None):
                possibilities.append('small_suite')

        return possibilities

    # Gestion des scores pour chaque combinaison
    def __set_scores(self, choixCombinaison):

        if (choixCombinaison == "as"):
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
            self.score.combinations[choixCombinaison] = self.score.brelan(
                self.dices.dices)*3

        elif (choixCombinaison == "carre"):
            self.score.combinations[choixCombinaison] = self.score.carre(
                self.dices.dices)*4

        elif (choixCombinaison == "full"):
            self.score.combinations[choixCombinaison] = 25

        elif (choixCombinaison == "small_suite"):
            self.score.combinations[choixCombinaison] = 30

        elif (choixCombinaison == "big_suite"):
            self.score.combinations[choixCombinaison] = 40

        elif (choixCombinaison == "yams"):
            self.score.combinations[choixCombinaison] = 50

        elif (choixCombinaison == "chance"):
            self.score.combinations[choixCombinaison] = sum(
                self.score.dices_values_dices(self.dices.dices))

    # Possibilité ou non d'inscire un score si case vide ou non

    def possibilities_set_score(self, choixCombinaison, possibilities):
        if (self.score.combinations[choixCombinaison] == None):
            self.__set_scores(choixCombinaison)
        elif (self.score.combinations[choixCombinaison] != None):
            print(Bcolors.FAIL + "Erreur : vous avez déjà choisi cette option, veuillez réessayer ! Ou choisissez une case à sacrifier !" + Bcolors.ENDC)
            print("------------------------------")
            choixCombinaison = input(
                Bcolors.HEADER + "Quelle combinaison voulez-vous choisir ? ==> " + Bcolors.ENDC)
            self.__set_scores(choixCombinaison)
            self.round()
        if not possibilities:
            print("------------------------------")
            response = str(input(Bcolors.FAIL + Bcolors.BOLD + "Êtes vous sûr de sacrifier une case ? " + Bcolors.ENDC))
            if "oui" in response:
                self.score.combinations[choixCombinaison] = 0
            if "non" in response:
                self.possibilities_set_score(choixCombinaison, possibilities)

    # Relancer une partie

    def game_restart(self):
        response = input(Bcolors.OKBLUE +
                         "Voulez-vous relancer une partie ? " + Bcolors.ENDC)
        if "oui" in response:
            self.game_start()
        if "non" in response:
            self.game_end()

    # Terminer une partie

    def game_end(self):
        print("------------------------------")
        response = input(Bcolors.OKBLUE + "Quitter le jeu ? " + Bcolors.ENDC)
        if "oui" in response:
            print("------------------------------")
            print(Bcolors.FAIL + Bcolors.BOLD + "A bientôt !" + Bcolors.ENDC)
            exit()
        if "non" in response:
            print("------------------------------")
            self.game_restart()


g = Game()
s = Score()
g.game_start()
