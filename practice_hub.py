import streamlit as st

from practice_hub_config import ADDITION_TABLE_SIZE

from section_pages import DI, QA, LR, RC, hub
from helper import init_sess_state


st.set_page_config(
    page_title='Practice Hub',
    layout="wide"       # Use wide layout for full table display
)

# Initialize session state
def initialize_session_state():
    return init_sess_state.initialize_session_state()




### PAGES - PAGES FOR EVERYONE!
## Main hub
def show_hub():
    hub.show_hub()

## RC Pages
# if there were any

## DI Pages
def show_addition_table():
    return DI.show_addition_table()

## QA Pages
def show_percentage():
    QA.show_percentage()

## LR Pages
# if there were any






def main():
    initialize_session_state()
    
    # Route to appropriate page
    if st.session_state.current_page == 'hub':
        show_hub()
    elif st.session_state.current_page == 'addition_table':
        show_addition_table()
    elif st.session_state.current_page == 'percentage':
        show_percentage()


if __name__ == "__main__":
    main()