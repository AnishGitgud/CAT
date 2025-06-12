import streamlit as st

from tables import Timer

def initialize_session_state():
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'hub'
    if 'table_obj' not in st.session_state:
        st.session_state.table_obj = None
    if 'timer' not in st.session_state:
        st.session_state.timer = Timer()
    if 'timer_placeholder' not in st.session_state:
        st.session_state.timer_placeholder = None
    if 'last_timer_update' not in st.session_state:
        st.session_state.last_timer_update = 0