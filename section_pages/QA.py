import streamlit as st

def show_percentage():
    """Display the percentage calculation practice."""
    st.title("Percentage Calculation practice - Quantitative Aptitude")
    
    # Navigation
    col1, col2, col3 = st.columns([1, 8, 1])
    with col1:
        if st.button("Hub", type="secondary"):
            st.session_state.current_page = 'hub'
            st.rerun()

    with col3:
        if st.button("Refresh page", type='secondary'):
            st.rerun()

    st.write('---')

    # random 2 or 3 digit(both num and den) percentage finding question generation
    import random
    num2 = random.randint(10,99)
    den2 = random.randint(10,99)
    num3 = random.randint(100,999)
    den3 = random.randint(100,999)
    perc2 = num2 / den2
    perc3 = num3 / den3