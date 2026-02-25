import streamlit as st
st.title("👋 Hello, Add your notes here! 📝")
st.sidebar.title("Notes Buddy 😎")
st.sidebar.write("You can use me to jot down your thoughts, ideas, or anything you want to remember.")

import streamlit as st
import time

with st.sidebar:
    with st.echo():
        st.write("This code will be printed to the sidebar.")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")
