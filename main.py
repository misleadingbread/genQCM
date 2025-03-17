import os
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
    for x in liste:
        qcm.add_paragraph(x.question)
        qcm.add_paragraph(x.reponses[0])
        qcm.add_paragraph(x.reponses[1])
        qcm.add_paragraph(x.reponses[2])
        qcm.add_paragraph(x.reponses[3])
        qcm.add_paragraph(x.juste)
        qcm.add_paragraph()
    qcm.save('quiz_questions.docx')





#print(lectureFichier(r"C:\Users\natha\OneDrive\Bureau\Cours\Algo\genQCM\QCM_cinema.txt"))
questions = lectureFichier(r"C:\Users\quentin\Documents\coursbsd2024\genQCM\QCM_culture_generale.txt")
for question in questions:
    print(question)
qcmdocx(questions)