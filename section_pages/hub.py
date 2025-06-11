import streamlit as st

from tables import Table, Timer
from practice_hub_config import ADDITION_TABLE_SIZE

def show_hub():
    """Display main hub with practice options for CAT sections"""
    st.title("CAT Practice Hub!")
    st.markdown("### Practice for the Common Admission Test (CAT)")
    st.markdown('----')
    
    # Create four sections for CAT topics
    col1, col2 = st.columns(2)
    
    with col1:
        # Reading Comprehension Section
        st.markdown("### 📚 Reading Comprehension")
        st.markdown("*Verbal Ability and Reading Comprehension*")
        if st.button("RC Practice", type="secondary", use_container_width=True, disabled=True):
            pass
        st.markdown("*Nothing yet*")
        
        st.markdown("---")
        
        # Quantitative Aptitude Section  
        st.markdown("### 🔢 Quantitative Aptitude")
        st.markdown("*Mathematics and Problem Solving*")
        
        # Percentage Practice
        if st.button("Percentages", type="primary", use_container_width=True):
            st.session_state.current_page = 'percentage'
            st.rerun()
        
        st.markdown("*Make more types pissboy!*")
    
    with col2:
        # Data Analysis Section
        st.markdown("### 📊 Data Analysis")
        st.markdown("*Data Interpretation and Logical Reasoning*")
        
        # Addition Table Practice
        if st.button("Addition Table", type="primary", use_container_width=True):
            # Initialize new table and timer
            st.session_state.table_obj = Table(ADDITION_TABLE_SIZE)
            st.session_state.table_obj.set_heads()
            st.session_state.table_obj.set_table()
            st.session_state.table_obj.calculate_values()
            st.session_state.timer = Timer()
            st.session_state.current_page = 'addition_table'
            st.rerun()
        
        st.markdown("*Make more types pissboy!*")
        
        st.markdown("---")
        
        # Logical Reasoning Section
        st.markdown("### 🧠 Logical Reasoning")
        st.markdown("*Logic and Critical Thinking*")
        if st.button("LR Practice", type="secondary", use_container_width=True, disabled=True):
            pass
        st.markdown("*Nothing yet*")
    
    st.markdown("---")
    st.markdown("- Click on a practice type to start")