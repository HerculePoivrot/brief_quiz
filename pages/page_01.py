# Création de questionnaire
import streamlit as st
import json
import random as rd

def play_quiz():
    st.markdown("# Jouer au quizz 🥳")
    st.image("lepers.jpeg", caption="oh oui oui oui!")
    file = 'content/data_quizz_1.JSON'
    #file = 'content/quizz_data.json'
    correct_answers_count = 0
    # Load quiz data defined in main page
    with open(file, 'r', encoding='utf-8') as f:
        st.session_state.quizz_data = json.load(f)
    print(st.session_state.quizz_data)
    print(f"PRINT{st.session_state.quizz_data["questions"]}")
    if not st.session_state.quizz_data["questions"]:
        st.error("Aucune question disponible. Veuillez en créer dans l'onglet 'Création de Quiz'.")
    
    
    # rd.shuffle(st.session_state.quizz_data["quiz"])

    print('########################')

    # Afficher les questions et les options

    user_answers = []
    for i, q in enumerate(st.session_state.quizz_data["questions"]):
        st.subheader(f"Question {i + 1}")
        st.write(q['question:'])
        user_answer = st.radio("Sélectionnez une réponse :", q['choices:'], key=f"question{i}")
        user_answers.append(user_answer)


    # Bouton pour soumettre les réponses
    if st.button("Soumettre les réponses"):
        for i, user_answer in enumerate(user_answers):
            print(i,user_answer)
            if user_answer in st.session_state.quizz_data["questions"][i]['answer:']:
                correct_answers_count += 1

        st.write(f"Vous avez obtenu {correct_answers_count} bonnes réponses sur {len(st.session_state.quizz_data["questions"])} questions.")
        if correct_answers_count == len(st.session_state.quizz_data["questions"]):
            st.write('Félicitations, vous remportez la grande coupe!!! 🏆')
            st.audio("sounds/oh_oui.mp3", format="audio/mpeg", loop=True, autoplay=True)

    # Function to display the current question and choices
    #def show_question(question): #question is a dict
    #    st.write(question['question']) # Selects the question within the dictionary being accessed by previous line within the quiz_data list.
    #    selected_choice = st.radio("Select your answer:", question['choices']) 
    #    submit_button = st.button("Submit") 
    #    if submit_button:
    #        check_answer(selected_choice)
    #        st.session_state.show_question = False




    #for item in st.session_state.quizz_data:
    #    print(item["id"], item["name"])
    st.sidebar.markdown("# Page 1 ")

play_quiz()