
def check_credentials(username, password):
    return username == "admin" and password == "1234"

def is_authenticated():
    return st.session_state.get("logged_in", False)
