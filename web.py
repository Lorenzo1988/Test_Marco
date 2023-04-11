import streamlit as st
import modules.functions as functions
#il comando per fare run di una web app è: --> streamlit run /home/lorenzo/pythonProjects/pythonMegaCourse_project1/web.py

st.title("My Todo APP")
st.subheader("Lista di attività")
st.text("ProvaProva")

#st.checkbox("Attività 1")

# VERIFICA SE ESISTE IL FILE todos_bkp.txt altrimenti lo crea
verifica_todo= functions.verify_if_exist_file()
print(verifica_todo)


todos = functions.get_todos()
for todo in todos:
    print(f"Pippo: {todo}")
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo..")