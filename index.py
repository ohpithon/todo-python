import streamlit as st

# セッション状態の初期化
if 'todos' not in st.session_state:
    st.session_state.todos = []

def add_todo():
    if st.session_state.new_todo:
        st.session_state.todos.append(st.session_state.new_todo)
        st.session_state.new_todo = ""

st.title('TODOリストアプリ')

st.balloons()

# 新しいTODOの入力
st.text_input('新しいTODOを入力してください:', key='new_todo', on_change=add_todo)

# TODOリストの表示
for i, todo in enumerate(st.session_state.todos):
    col1, col2 = st.columns([4,1])
    col1.write(f"{i+1}. {todo}")
    if col2.button('完了', key=f'done_{i}'):
        st.session_state.todos.pop(i)
        st.rerun()

# TODOリストのクリア
if st.button('全てのTODOをクリア'):
    st.session_state.todos = []
    st.rerun()