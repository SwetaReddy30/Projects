import streamlit as st
st.title("👋 Hello, Add your notes here! 📝")
st.sidebar.title("Notes Buddy 😎")
st.sidebar.write("You can use me to jot down your thoughts, ideas, or anything you want to remember.")
with st.sidebar:
    with st.echo():
        st.write("➕ Add new notes below:")
        st.write("🗒️ View Notes")
        st.write("🔎 Search Notes")
        st.write("📊 Analytics")

st.popover(label="Add Notes", content="Here you can add your notes. Just type in the box and hit enter!", disabled=False)
