# Création de st.session_state.questionnaire
import streamlit as st
import json
import os
from pydantic import BaseModel #, FieldValidator


# Modèle Pydantic pour la réponse d'une question
class Question(BaseModel):
    question: str
    choices: list[str]
    answer: str
    # @FieldValidator(question)
    # def validate_question(cls,values):
    #     # if 
    #     #    RaiseError
    #     # else:
    #     #     return value


# Initilisation des variables persistantes entre runs
if 'count_question' not in st.session_state:
    st.session_state.count_question = 1

if not "quizz_data" in st.session_state:
    st.session_state.quizz_data = {} 
    st.session_state.quizz_data["questions"] = [] # Structure de stockage des questions


def create_quiz():

    # Titre de la page
    st.markdown("# Configuration du quizz")
    st.image("quizz_p1.jpeg", caption="")
    st.write(f"Question n° : {st.session_state.count_question}")

    question = st.text_input("Saisir une question") 
    answers = st.text_area("Ajout des réponses possibles (1/ligne)")
    possible_answers = answers.split('\n')
    #correct_answers = st.text_input("Bonne réponse")
    correct_answers = st.selectbox("Sélectionnez la réponse correcte :", possible_answers)


    if st.button("Add question", type="primary") is True:
        if isinstance(question,str) and question and isinstance(possible_answers,list) and possible_answers and isinstance(correct_answers,str) and correct_answers:
            dict_question = {"question:":question, "choices:":possible_answers, "answer:":correct_answers}
            print(dict_question)
            print(st.session_state.quizz_data)
            st.session_state.quizz_data['questions'].append(dict_question)
            print(st.session_state.quizz_data)
            st.session_state.count_question += 1
            print('true')
            st.success('Format correct, question ajoutée', icon="✅")
        else:
            st.error('Format incorrect, veuillez remplir tous les champs.',icon="😡")
    print(st.session_state.quizz_data)

    # Chargement des données existantes si le fichier existe
    # if os.path.exists("quizz_data.json"):
    #     with open("quizz_data.json", "r") as file:
    #         st.session_state.quizz_data = json.load(file)

    if st.button("Enregistrer le quizz", type="primary"):
        with open(('content/quizz_data.json'), "w") as file:
            json.dump(st.session_state.quizz_data, file, indent=4)
            st.success(f"Quiz enregistré avec succès !", icon="✅")


    # Affichage des questions enregistrées 
    st.markdown("### Questions enregistrées")
    #st.write(st.session_state.quizz_data)

    if st.session_state.quizz_data["questions"]:
        for idx, q in enumerate(st.session_state.quizz_data["questions"]):
            st.write(f"**Question {idx+1}: {q['question:']}**")
            for choice in q["choices:"]:
                st.write(f"- {choice}")
            st.write(f"Bonne réponse : *{q['answer:']}*")
    else:
        st.write("Aucune question ajoutée pour le moment.")


    # Ajoute une fonction pour réinitialiser le questionnaire
    if st.button("Réinitialiser le quizz", type="secondary"):
        st.session_state.quizz_data = {"questions": []}
        st.session_state.count_question = 1
        if os.path.exists("content/quizz_data.json"):
            os.remove("content/quizz_data.json")
        st.sidebar.success("Quizz réinitialisé avec succès !")


    st.sidebar.markdown("# Create ✍️")


create_quiz()

#st.page_link