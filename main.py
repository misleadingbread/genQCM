import os

class Genquestionqcm:
    def __init__(self, question,reponses,juste):
        self.question = question
        self.reponses = reponses #liste des réponses
        self.juste = juste

def lectureFichier(nomDeFichier):
    """Permet de récupérer les questions d'un fichier .txt"""
    listeQuestions = []
    index = 0
    with open(nomDeFichier, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            #Récupère les questions grâce au ligne finissant par un "?"
            if line.endswith("?"):
                question = line
                r1 = line.readline()
                r2 = line.readline()
                r3 = line.readline()
                r4 = line.readline()
                reponses = [r1,r2,r3,r4]
                rep = line.readline()
                listeQuestions.append(Genquestionqcm(question, reponses, rep))

    return listeQuestions
            
print(lectureFichier(r"C:\Users\natha\OneDrive\Bureau\Cours\Algo\genQCM\QCM_cinema.txt"))

