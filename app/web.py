import streamlit as st
import app.functions as functions

todos = functions.get_todos()


def add_todo():
    # session_state is dict
    # it contains widgets values, if it has key
    """
    Adds a new todo item from the session state to the todo list and persists the update.
    
    Retrieves the value associated with the "new todo" key from the Streamlit session state,
    appends it to the global todo list, and writes the updated list using the functions module.
    """
    new_todo = st.session_state["new todo"]
    todos.append(new_todo + "\n")
    functions.write_todos(todos)


st.title("Todo App")
st.subheader("This is web-based Todo App")
st.write("Store all your works to do here")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

# label is not optional parameter
# after calling add_todo the whole script will run
st.text_input(
    label="Enter a todo",
    label_visibility="hidden",
    placeholder="Add new todo...",
    on_change=add_todo,
    key="new todo",
)

# st.session_state
