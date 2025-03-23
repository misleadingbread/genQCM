import os
import random
from genqcm_code.main import lectureFichier, creation_sujets, Genquestionqcm

def test_lectureFichier():
    # Créer un fichier de test temporaire
    test_filename = "test_QCM.txt"
    with open(test_filename, 'w', encoding='utf-8') as file:
        file.write("Question 1?\n")
        file.write("Réponse 1\n")
        file.write("Réponse 2\n")
        file.write("Réponse 3\n")
        file.write("Réponse 4\n")
        file.write("Réponse 1\n")  # Réponse correcte

    # Tester la fonction lectureFichier
    questions = lectureFichier(test_filename)
    assert len(questions) == 1
    assert questions[0].question == "Question 1?"
    assert questions[0].reponses == ["Réponse 1", "Réponse 2", "Réponse 3", "Réponse 4"]
    assert questions[0].juste == "Réponse 1"

    # Nettoyer le fichier de test
    os.remove(test_filename)

def test_creation_sujets():
    # Crée une liste de 20 questions pour les tests
    questions = [
        Genquestionqcm(f"Question {i}?", [f"Réponse A{i}", f"Réponse B{i}", f"Réponse C{i}", f"Réponse D{i}"], f"Réponse A{i}")
        for i in range(20)
    ]

    # Génère 2 sujets avec 20 questions chacun
    sujets, reponses = creation_sujets(questions, 2, 20)

    # Vérifie qu'il y a 2 sujets
    assert len(sujets) == 2

    # Vérifie qu'il y a 2 réponses
    assert len(reponses) == 2

    # Vérifie que chaque sujet contient 20 questions
    assert len(sujets[0]) == 20
    assert len(sujets[1]) == 20

    # Vérifier que les questions sont bien réparties
    for sujet in sujets:
        assert len(sujet) == 2
        for question in sujet:
            assert question in questions