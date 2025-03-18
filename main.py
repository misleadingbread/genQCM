import os
import random
from docx import Document

class Genquestionqcm:
    def __init__(self, question,reponses,juste):
        self.question = question
        self.reponses = reponses #liste des réponses
        self.juste = juste

    def __str__(self):
        return f"question: {self.question}\nreponses: {', '.join(self.reponses)}\nreponse correcte: {self.juste}\n"

def lectureFichier(nomDeFichier):
    """Permet de récupérer les questions d'un fichier .txt"""
    listeQuestions = []
    with open(nomDeFichier, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        index = 0
        while index < len(lines):
            line = lines[index].strip()
            if line.endswith("?"):
                question = line
                rep_juste = lines[index+5].strip()
                reponses = [lines[index+1].strip(),lines[index+2].strip(),lines[index+3].strip(),lines[index+4].strip()]
                listeQuestions.append(Genquestionqcm(question, reponses, rep_juste))
                index += 6
            else:
                index += 1
        return listeQuestions
            
def qcmdocx(liste):
    qcm = Document()
    nbquestion = len(liste)
    for x in liste:
        qcm.add_paragraph(x.question)
        qcm.add_paragraph(x.reponses[0])
        qcm.add_paragraph(x.reponses[1])
        qcm.add_paragraph(x.reponses[2])
        qcm.add_paragraph(x.reponses[3])
        qcm.add_paragraph()
    if nbquestion == 5:
        tableau = qcm.add_table(rows=2, cols=5)
        for i in range(2):  # Parcourir les lignes
            for j in range(5):  # Parcourir les colonnes
                # Accéder à la cellule (i, j) et ajouter du texte
                cellule = tableau.cell(i, j)
                if i == 0:
                    cellule.text = f'{j+1}'
    elif nbquestion == 10:
        tableau = qcm.add_table(rows=2, cols=11)
        for i in range(2):  # Parcourir les lignes
            for j in range(11):  # Parcourir les colonnes
                # Accéder à la cellule (i, j) et ajouter du texte
                cellule = tableau.cell(i, j)
                if i == 0  and j < 5:
                    cellule.text = f'{j+1}'
                if i == 0  and j > 5:
                    cellule.text = f'{j}'

    elif nbquestion == 15:
        tableau1 = qcm.add_table(rows=2, cols=11)
        for i in range(2):  # Parcourir les lignes
            for j in range(11):  # Parcourir les colonnes
                cellule = tableau1.cell(i, j)
                if i == 0 and j < 5:
                    cellule.text = f'{j+1}'
                if i == 0 and j > 5:
                    cellule.text = f'{j}'
        tableau2 = qcm.add_table(rows=2, cols=5)  # 5 colonnes pour les questions 11 à 15
        for i in range(2):  # Parcourir les lignes
            for j in range(5):  # Parcourir les colonnes
                cellule = tableau2.cell(i, j)
                if i == 0:  # Remplir uniquement la première ligne
                    cellule.text = f'{j + 11}'  # Questions 11 à 15

    else:
        tableau = qcm.add_table(rows=2, cols=11)
        for i in range(2):  # Parcourir les lignes
            for j in range(11):  # Parcourir les colonnes
                # Accéder à la cellule (i, j) et ajouter du texte
                cellule = tableau.cell(i, j)
                if i == 0  and j < 5:
                    cellule.text = f'{j+1}'
                if i == 0  and j > 5:
                    cellule.text = f'{j}'
        tableau2 = qcm.add_table(rows=2, cols=11)
        for i in range(2):  # Parcourir les lignes
            for j in range(11):  # Parcourir les colonnes
                # Accéder à la cellule (i, j) et ajouter du texte
                cellule = tableau2.cell(i, j)
                if i == 0  and j < 5:
                    cellule.text = f'{j+11}'
                if i == 0  and j > 5:
                    cellule.text = f'{j+10}'
    qcm.save(r'C:\Users\natha\OneDrive\Bureau\Cours\Algo\genQCM\quiz_questions.docx')

def creation_sujets(liste):
    nb_suj = int(input("combien de sujets "))
    nb_qst = int(input("combien de questions (multiples de 5) "))
    sujets = []
    reponses_sujets = []
    for i in range (0,nb_suj):
        sujet = []
        reponses = ""
        while len(sujet)<nb_qst:
            choix_question = random.randint(0,len(liste)-1)
            if liste[choix_question] not in sujet:
                sujet.append(liste[choix_question])
                reponses += str(liste[choix_question].juste)
        sujets.append(sujet)
        reponses_sujets.append(reponses)
    return (sujets, reponses_sujets)




#print(lectureFichier(r"C:\Users\natha\OneDrive\Bureau\Cours\Algo\genQCM\QCM_cinema.txt"))
questions = lectureFichier(r"C:\Users\natha\OneDrive\Bureau\Cours\Algo\genQCM\QCM_cinema.txt")
#for question in questions:
#    print(question)
#qcmdocx(questions)
(sujers,reprenses) = creation_sujets(questions)
for question in sujers[0]:
    print(question)
print(reprenses[0])
qcmdocx(sujers[0])
