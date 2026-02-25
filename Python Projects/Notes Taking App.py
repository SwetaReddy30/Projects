import streamlit as st

st.title("👋 Hello, Add your notes here! 📝")

st.sidebar.title("Notes Buddy 😎")
st.sidebar.write("You can use me to jot down your thoughts, ideas, or anything you want to remember.")

st.sidebar.write("➕ Add new notes below:")
st.sidebar.write("🗒️ View Notes")
st.sidebar.write("🔎 Search Notes")
st.sidebar.write("📊 Analytics")


# Create a button to open dialog
if st.button("➕ Add Notes"):
    open_dialog = True
else:
    open_dialog = False


# Create Dialog
@st.dialog("📝 Add Your Note")
def add_note_dialog():
    st.write("Here you can add your notes. Just type in the box below and hit 'Save'.")

    note = st.text_area("Your Note", height=250, width=1000)

    if st.button("Save"):
        st.success("Note saved successfully!")
        st.rerun()


# Open dialog if button clicked
if open_dialog:
    add_note_dialog()
