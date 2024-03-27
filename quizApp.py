
# Importation du module random pour générer des questions aléatoires
import random

# Définition du tableau des questions
# Chaque question est un élément du tableau, et chaque élément est lui-même un tableau de 6 éléments:
# - La question
# - 4 réponses possibles
# - La lettre de la bonne réponse
tableauDesQuestions = [
    ["En quel savan nous dévons le mérité d'avoir découvert la loi d'inertie ","Jean Paul sartre","Archimede","Gandhi","Socrate","b"],
    ["Parmis ces gens l'un n'est pas parmis les 12 disciples  de Jésus","Mathieu","Paul","Simon Pierre","Phillipe","b"],
    ["Quel est la langue officiel de l'Espagne ","Mandarin","Anglais","Français","Spanish","d"],
    ["Quel est la langue officiel de l'Allemagne ","Allemande","Anglais","Français","Chinois","a"],
    ["Quel est le pay colonisateur de l'Argenite ","Angleterre","Français","Espagne","Chine","c"],
    ["Quel est le pay colonisateur de la RDC ","Angleterre","Français","Espagne","Belgique","c"],
    ["Quel est le pay colonisateur du Rwanda ","Belgique","Français","Espagne","RDC","a"],
    ["Quel est le pay colonisateur de la TANZANIE ","Angleterre","Français","Espagne","Belgique","a"],
    ["En quel année la RDC a eu son indépendance ","2010","1956","2001","1960","d"],
    ["Quel phrase Neil Amstrong à proncer quand il est arriver sur la Lune ","Nous avons réussie","Eureka","Petit pas pour l'homme, grand pas pour l'humanité","Never give up","c"],
    ["Quel ville au monde contient beaucoup plus d'habitant ","Paris","Tokyo","Kinshasa","Washington","b"],
    ["Quel pays à comme capital Buenos-Air ","ARGENTINE","Brazil","Urugay","Mexique","a"],
    ["A qui l'histoire reconnait la découverte de l'Embouchire du fleuve congo ","Maradonat","Crhistophe Colombe","Diego-Chaos","Lumumba","b"],
    ["Parmis ces pays lequelle n'est pas dans l'espace OHADA ","RDC","CAMEROUN","Cote d'Ivoire","RWANDA","c"],
    ["En informatique le langage SQL sert à  ","Crée des algorithmes","Pirater les réseau","Interroger la base des données","Acune bonne répoonse","c"],
    ["L'équipe national de quel pay est appéllé les Elephants ","Cameroun","Cote d'ivoire","Guinée","RDC","b"],
    ["Quel est le nom de l'Equipe national du MALI ","Diable rouge","Anglais","Les léopards","Les Aigles","c"],
    ["Quel est le pays vainquerre de la Coupe du monde 2010 ","Espagne","Allemagne","Brazil","Italy","a"],
    ["Si le corbeau chanté, que fait le sérpent ","Il rorone","Il claxione","Il siflé","il n'a aucune cris","a"],
    ["L'un de ces auteurs économistes est un pilier de l'école des ressources humains ","Adam Smith","Elton Mayo","Taylor","Ricardo","b"],
    ["Parmis ces termes lequelle désigne une personne qui confonde les couleurs ","Mavoyanst","Macho","Daltonier","Conficolor","c"],
    ["Parmis ces termes lequelle désigne une personne qui n'a qu'une seul mains ","Mavoyanst","Macho","Daltonier","Conficolor","b"],
    ["Quel est le chapitre le plus long de la Bible","Psaume 23","Psaume 99","Psaume 150","Psaume 119","d"],
    ["Chez les christianismes quel fête est celebrer en comémoration de la mort et de la résurection du Christ ","Christmas","Pantecote","Sabbat Saint","Paque","a"],
    ["Poutine est le président de quel pays ","France","Chine","Ukraine","Irak","e"],
    ["En grec quel est le sens du mot église (Eclésia) ","garde hors de...","quité babylonne","Maison du Seigneur","Temple Bénie","a"]
    
    # ... (les autres questions)
]

# Fonction pour poser une question
# Cette fonction prend en paramètre la question, les 4 réponses possibles et la lettre de la bonne réponse
# Elle affiche la question et les réponses possibles, demande à l'utilisateur de choisir une réponse
# et retourne True si la réponse est correcte, False sinon
def poser_question(question, r1, r2, r3, r4, bonne_reponse):
    """
    Fonction pour poser une question à l'utilisateur

    Args:
        question (str): La question à poser
        r1 (str): La première réponse possible
        r2 (str): La deuxième réponse possible
        r3 (str): La troisième réponse possible
        r4 (str): La quatrième réponse possible
        bonne_reponse (str): La lettre de la bonne réponse

    Returns:
        bool: True si la réponse est correcte, False sinon
    """

    print("Question : \n" + question + "\n choissisez la lettre qui corresponde à la bonne réponse \n"
          + " a. " + r1 + "\n b. " + r2 + " \n c. " + r3 + " \n d. " + r4)
    reponse = input("Votre réponse : ")

    # On compare la réponse de l'utilisateur avec la bonne réponse
    return reponse.lower() == bonne_reponse.lower()

# Fonction pour lancer le quizz
def boucle():
    """
    Fonction pour lancer le quizz
    """

    # Initialisation du score
    score = 0

    # Boucle sur 10 questions aléatoires
    compteur = 0
    while compteur < 10:

        # Génération d'un nombre aléatoire entre 0 et la longueur du tableau des questions
        questionAleatoire = random.randint(0, len(tableauDesQuestions) - 1)

        # On pose la question à l'utilisateur
        if poser_question(tableauDesQuestions[questionAleatoire][0],
                          tableauDesQuestions[questionAleatoire][1],
                          tableauDesQuestions[questionAleatoire][2],
                          tableauDesQuestions[questionAleatoire][3],
                          tableauDesQuestions[questionAleatoire][4],
                          tableauDesQuestions[questionAleatoire][5]):

            # Incrémentation du score si la réponse est correcte
            score += 10

            # Affichage d'un message indiquant que la réponse est correcte
            print("Bonne réponse !")
        else:
            # Affichage d'un message indiquant que la réponse est incorrecte
            print("Mauvaise réponse !")

        # Incrémentation du compteur
        compteur += 1

    # Affichage du score final
    print("Vous avez eu une note de ", score * 100 / 100, " %")

# Lancement du quizz
boucle()
