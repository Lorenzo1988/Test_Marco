import streamlit as st
import modules.functions as functions
#il comando per fare run di una web app è: --> streamlit run /home/lorenzo/pythonProjects/pythonMegaCourse_project1/web.py

todos = functions.get_todos()
for todo_index,todo_value in enumerate(todos):
    checkbox = st.checkbox(todo_value,key=todo_value)
    if checkbox:
        todos.pop(todo_index)
        functions.write_todos(todos)
        del st.session_state[todo_value]
        st._rerun()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo APP")
st.subheader("Lista di attività")
st.text("\n Inserire qui sotto le attività da aggiungere."
        "\n Facendo Check su un'attività la si considera completata e quindi si elimina")

#st.checkbox("Attività 1")

# VERIFICA SE ESISTE IL FILE todos_bkp.txt altrimenti lo crea
verifica_todo= functions.verify_if_exist_file()
print(verifica_todo)




st.text_input(label=""
              , placeholder="Add new todo.."
              ,on_change=add_todo,key="new_todo")


print ("Hello")
st.session_state