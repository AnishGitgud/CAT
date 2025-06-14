import streamlit as st
import pandas as pd
import time

from tables import Table, Timer
from practice_hub_config import ADDITION_TABLE_SIZE


def show_addition_table():
    """Display the addition table practice."""
    st.title("📊 Addition Table Practice - Data Analysis")
    
    # Navigation
    col1, col2, col3 = st.columns([1, 8, 1])
    with col1:
        if st.button("Hub", type="secondary"):
            st.session_state.current_page = 'hub'
            st.session_state.timer.stop()
            st.rerun()
    
    with col3:
        if st.button("New Table", type="secondary"):
            st.session_state.table_obj.reset_table()
            st.session_state.timer = Timer()
            st.session_state.timer.start()
            st.rerun()
    
    table_obj = st.session_state.table_obj
    timer = st.session_state.timer
    
    # Start timer if not already started
    if not timer.is_running() and timer.start_time is None:
        timer.start()
    
    # Timer display
    timer_col1, timer_col2 = st.columns([3, 1])
    with timer_col2:
        if timer.is_running():
            st.metric("Time", timer.format_time())
        else:
            st.metric("Final Time", timer.format_time())
    
    st.markdown("---")
    
    # Convert table to DataFrame for display
    df_data = []
    for row in table_obj.table:
        df_data.append([cell if cell != 'Null' else '' for cell in row])

    df = pd.DataFrame(df_data[1:], columns=df_data[0])

    # Create editable data editor
    edited_df = st.data_editor(
        df,
        use_container_width=True,
        disabled=['Heads'],
        key="table_editor",
        height=420
    )

    st.markdown("---")
    
    # Check answers button - moved outside of any conditional blocks
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Check Answers", type="primary", use_container_width=True):
            # Stop timer
            final_time = timer.stop()
            
            # Check if all cells are filled
            empty_cells = []
            for i in range(len(table_obj.solved_table)):
                for j in range(len(table_obj.solved_table[i])):
                    user_value = edited_df.iloc[i+1, j+1]
                    if user_value == '' or pd.isna(user_value):
                        empty_cells.append(f"Row {i+1}, Column {j+1}")
            
            if empty_cells:
                st.error("Fill all cells before checking answers dumbass!")
                st.write("**Empty cells:**")
                for cell in empty_cells:
                    st.write(f"- {cell}")
                # Restart timer if there are empty cells
                timer.start()
            else:
                # Get user answers
                user_answers = []
                for i in range(len(table_obj.solved_table)):
                    row_answers = []
                    for j in range(len(table_obj.solved_table[i])):
                        user_value = edited_df.iloc[i, j+1]
                        row_answers.append(str(user_value))
                    user_answers.append(row_answers)
                
                # Compare with correct answers
                correct_count = 0
                total_cells = 0
                wrong_cells = []
                
                for i in range(len(table_obj.solved_table)):
                    for j in range(len(table_obj.solved_table[i])):
                        total_cells += 1
                        correct_answer = table_obj.solved_table[i][j]
                        user_answer = user_answers[i][j]
                        
                        if user_answer == correct_answer:
                            correct_count += 1
                        else:
                            wrong_cells.append({
                                'row': i+1, 
                                'col': j+1, 
                                'correct': correct_answer,
                                'your_answer': user_answer
                            })
                
                # Display results
                st.markdown("---")
                st.subheader("Results")
                
                # Results in columns
                result_col1, result_col2, result_col3 = st.columns(3)
                
                with result_col1:
                    st.metric("Time Taken", timer.format_time())
                
                with result_col2:
                    st.metric("Correct", f"{correct_count}/{total_cells}")
                
                with result_col3:
                    accuracy = (correct_count/total_cells*100)
                    st.metric("Accuracy", f"{accuracy:.1f}%")
                
                if wrong_cells:
                    st.markdown("**Incorrect answers:**")
                    for cell in wrong_cells:
                        st.write(f"Row {cell['row']}, Column {cell['col']}: Your answer: **{cell['your_answer']}**, Correct: **{cell['correct']}**")
                else:
                    st.success("Perfect! All answers are correct!")
                
                # Performance message
                if accuracy == 100:
                    if final_time < 60:
                        st.balloons()
                        if ADDITION_TABLE_SIZE < 10:
                            st.success("You what? You did it for a small table didn't you? Maybe a 1x1? Useless bumass nigga - can't even win without cheating.")
                        else:
                            st.success("You what? You did it for a 1x1 table didn't you? No? Holy shit, you're good!")
                    elif final_time < 120:
                        st.success("Perfect accuracy? So what? You took longer than it takes me crank one out!")
                    else:
                        st.success("Perfect accuracy, but you could be faster if you STOPPED SUCKING ASS SO MUCH!")
                elif accuracy >= 90:
                    st.info("Eh, decent enough.")
                elif accuracy >= 75:
                    st.info("Failure! You fucked up big time!")
                else:
                    st.info("Useless bumass nigga! You need more practice!")

    # Update timer display if running
    if timer.is_running():
        time.sleep(1)  # Update every second
        st.rerun()

    st.markdown("---")
    st.markdown("**Instructions:** Fill in each cell with the sum of its row and column headers.")
    st.markdown("- Timer starts automatically when the table loads")
    st.markdown("- Complete all cells and click 'Check Answers' to see results")
    st.markdown("- Fill all cells before checking answers")
    st.markdown("- Use the 'New Table' button to reset the table")
    st.markdown("- Click 'Hub' to return to the main menu")