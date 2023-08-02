import streamlit as st

from pocketbase_connection import PocketBaseConnection


def get_conn():
    return st.experimental_connection("pocketbase", type=PocketBaseConnection)


def manage_state():
    if "page" not in st.session_state:
        st.session_state.page = "login"

    if st.session_state.page == "login":
        login()
    elif st.session_state.page == "todos":
        todos()


def set_page(page):
    st.session_state.page = page
    st.experimental_rerun()


def login():
    conn = get_conn()
    if conn.is_logged_in():
        set_page("todos")
        return

    st.title("Login")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.form_submit_button("Login"):
            try:
                if not conn.is_logged_in():
                    conn.auth_with_password(
                        username_or_email=username, password=password
                    )
            except Exception as e:
                st.error(f"Login failed: {e}")
            finally:
                if conn.is_logged_in():
                    set_page("todos")


def todos():
    conn = get_conn()
    if not conn.is_logged_in():
        set_page("login")
        return

    st.title("My Todos")

    col1, col2 = st.columns([1, 7])
    if col1.button("Refresh"):
        st.experimental_rerun()
    if col2.button("Logout"):
        conn.logout()
        set_page("login")
        return

    st.divider()

    try:
        todos = conn.get_list("todos")
        for item in todos.items:
            todo(item)
        if len(todos.items) == 0:
            st.write("No todos")
    except Exception as e:
        st.error(f"Failed to fetch todos: {e}")

    content = st.chat_input("Enter new todo")
    if content:
        try:
            conn.create(
                "todos", body_params={"content": content, "user": conn.user().id}
            )
            st.experimental_rerun()
        except Exception as e:
            st.error(f"Failed to create todo: {e}")


def todo(item):
    col1, col2 = st.columns([8, 1])
    col1.write(item.content)
    with col2:
        if st.button("Delete", key=f"delete_{item.id}"):
            try:
                conn = get_conn()
                conn.delete("todos", item.id)
                st.experimental_rerun()
            except Exception as e:
                st.error(f"Failed to delete todo: {e}")


if __name__ == "__main__":
    manage_state()
