# Projet Quiz Time !

Le projet est structuré en deux pages principales :
## main _page.py - Création du quiz

Dans cette page, l'utilisateur peut créer un quiz en ajoutant des questions avec plusieurs choix de réponses et en définissant la réponse correcte. Le quiz est ensuite enregistré dans un fichier JSON (content/quizz_data.json).
Fonctionnement :

    Création de la question :
        L'utilisateur entre une question.
        L'utilisateur ajoute les réponses possibles, une par ligne.
        L'utilisateur sélectionne la réponse correcte parmi les choix.
        L'utilisateur peut ajouter plusieurs questions, et chaque question est ajoutée à un quiz stocké en mémoire.

    Validation des données :
        Le modèle Pydantic est utilisé pour valider les questions, les choix et la réponse correcte avant d'ajouter la question au quiz.

    Enregistrement du quiz :
        Une fois les questions ajoutées, l'utilisateur peut enregistrer le quiz sous forme de fichier JSON.
        Les données sont stockées sous content/quizz_data.json.

    Réinitialisation du quiz :
        L'utilisateur peut réinitialiser le quiz, effacer toutes les questions et supprimer le fichier JSON si nécessaire.

## Page 1 - Jouer au quiz

Dans cette page, l'utilisateur peut charger un quiz à partir du fichier JSON enregistré et répondre aux questions. À la fin, le score est affiché, et un message de félicitations est donné si l'utilisateur répond correctement à toutes les questions.
Fonctionnement :

    Chargement du quiz :
        L'utilisateur charge le fichier JSON du quiz.
        Les questions et les choix sont affichés, et l'utilisateur sélectionne ses réponses.

    Soumettre les réponses :
        Une fois toutes les questions répondues, l'utilisateur peut soumettre ses réponses.
        Le score est calculé et affiché.

    Message de félicitations :
        Si l'utilisateur répond correctement à toutes les questions, un message de félicitations avec une animation audio est affiché.

Utilisation
Page 1 : Création d'un quiz

    Lancez l'application avec Streamlit :

    streamlit run app.py

    Sur la première page, entrez une question dans le champ "Saisir une question".

    Ajoutez les choix possibles dans la zone de texte "Ajout des réponses possibles".

    Sélectionnez la réponse correcte.

    Cliquez sur le bouton "Add question" pour ajouter la question.

    Répétez les étapes pour ajouter d'autres questions.

    Cliquez sur "Enregistrer le quizz" pour sauvegarder le quiz sous forme de fichier JSON.

    Vous pouvez réinitialiser le quiz à tout moment en cliquant sur "Réinitialiser le quizz".

Page 2 : Jouer au quiz

    Allez sur la page de jeu pour charger un quiz existant.
    Le fichier JSON du quiz sera chargé automatiquement.
    Répondez aux questions en sélectionnant une option pour chaque question.
    Cliquez sur "Soumettre les réponses" pour voir votre score.
    Si vous avez répondu correctement à toutes les questions, vous recevrez un message de félicitations et une animation sonore.

Exemple de fichier JSON

Voici un exemple de structure de fichier JSON généré par l'application :

{
    "questions": [
        {
            "question:": "Quelle est la capitale de la France ?",
            "choices:": ["Paris", "Londres", "Rome", "Madrid"],
            "answer:": "Paris"
        },
        {
            "question:": "Quel est le plus grand océan du monde ?",
            "choices:": ["Atlantique", "Pacifique", "Indien", "Arctique"],
            "answer:": "Pacifique"
        }
    ]
}

