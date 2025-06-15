from utils.randomMethods import random_generator as rg

import streamlit as st

def set_values():
    st.session_state.percentage_question = {
            'num2' : rg.rand2Dig(),
            'den2' : rg.rand2Dig(),
            'num3' : rg.rand3Dig(),
            'den3' : rg.rand3Dig(),
            'percent' : rg.randDec3()
        }

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
            set_values()
            st.rerun()

    st.write('---')

    # generater random 2 and 3 digit numbers(both num and den)
    if 'percentage_question' not in st.session_state:
        set_values()

    # get current values and calculate
    num2 = st.session_state.percentage_question['num2']
    num3 = st.session_state.percentage_question['num3']
    den2 = st.session_state.percentage_question['den2']
    den3 = st.session_state.percentage_question['den3']
    percento = st.session_state.percentage_question['percent']

    perc2 = round((num2 / den2) * 100, 2)
    perc3 = round((num3 / den3) * 100, 2)

    # # Display percent calculation question
    c1, c2, c3 = st.columns(3)

    with c1:
        st.write(f"Calculate these percentages dumbass :")
        
        with st.form("percentage_form"):
            st.write(f"{num2}/{den2} = ")
            answer1_text = st.text_input(
                "Enter your answer (up to 2 decimal places):",
                placeholder="e.g., 75.25",
                key="answer1"
            )
            
            st.write(f"{num3}/{den3} = ")
            answer2_text = st.text_input(
                "Enter your answer (up to 2 decimal places):",
                placeholder="e.g., 12.34",
                key="answer2"
            )
            
            submitted = st.form_submit_button("Check Answers", type="primary")
            
            if submitted:
                # Check answers
                correct_answers = 0
                
                # Validate and convert answers
                try:
                    answer1 = float(answer1_text) if answer1_text else 0
                    answer2 = float(answer2_text) if answer2_text else 0
                    
                    # Check answer 1
                    if answer1_text and abs(answer1 - perc2) < 0.01:  # Allow for small floating point errors
                        st.success(f"✅ Question 1: Correct! {num2}/{den2} = {perc2}%")
                        correct_answers += 1
                    else:
                        st.error(f"❌ Question 1: Incorrect. Your answer: {answer1}%, Correct answer: {perc2}%")
                    
                    # Check answer 2
                    if answer2_text and abs(answer2 - perc3) < 0.01:  # Allow for small floating point errors
                        st.success(f"✅ Question 2: Correct! {num3}/{den3} = {perc3}%")
                        correct_answers += 1
                    else:
                        st.error(f"❌ Question 2: Incorrect. Your answer: {answer2}%, Correct answer: {perc3}%")
                
                except ValueError:
                    st.error("Please enter valid numbers for both answers.")
                
                # Overall score
                if correct_answers == 2:
                    st.balloons()
                    st.success("ok")
                elif correct_answers == 1:
                    st.info("only one correct? KYS now!")
                else:
                    st.warning("useless bum ass nigga")

    with c3:

        st.write('you know what to do:')

        with st.form('multiply my a-'):
            st.write(f'{percento* 100} percent of {num2}')
            answer3_text = st.text_input(
                "Enter your answer (up to 2 decimal places):",
                key="answer3"
            )
            st.write(f'{percento* 100} percent of {num3}')
            answer4_text = st.text_input(
                "Enter your answer (up to 2 decimal places):",
                key="answer4"
            )

            other_submitted = st.form_submit_button("Check Answers", type="primary")

            if other_submitted:
                answer3 = float(answer3_text) if answer3_text else 0
                answer4 = float(answer4_text) if answer4_text else 0

                st.info(f"{percento* 100} percent of {num2} = {percento * num2}\n{percento* 100} percent of {num3} = {percento * num3}")