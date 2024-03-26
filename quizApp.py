
score =0
def poser_question(question,r1,r2,r3,r4,bonne_reponse):
    compeur=0
    global score
    while compeur<10:
        print("Question : \n"+question+"\n choissisez la lettre qui corresponde à la bonne réponse \n"+ " a. ",r1,"\n b. ",r2," \n c. ",r3," \n d. ",r4)
        reponse= input("Votre réponse : ") 
        if reponse==bonne_reponse:
            score+=10
            print("Bonne réponse !")
        else:
            print("Mauvaise réponse !")
            compeur+=1
    print("Vous avez eu une note de ",score*100/100," %")
    
poser_question("Quel est la capital de l'Espagne ","Paris","Barcelone","Madrid","Seville","c")
'''poser_question("Quel est la langue officiel de la chine ","Mandarin","Anglais","Français","Chinois","a")
poser_question("Parmis ces gens l'un n'est pas parmis les 12 disciples  de Jésus","Mathieu","Paul","Simon Pierre","Phillipe","b")
poser_question("En quel savan nous dévons le mérité d'avoir découvert la loi d'inertie ","Jean Paul sartre","Archimede","Gandhi","Socrate","b")
'''

    