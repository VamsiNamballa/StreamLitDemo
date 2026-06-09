import streamlit as st

st.title("User Information Form")

with st.form("user_form"):
    first_name = st.text_input("First Name")
    middle_name = st.text_input("Middle Name")
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    
    submitted = st.form_submit_button("Submit")

if submitted:
    if not first_name:
        st.error("Please enter your first name.")
    else:
        st.success("Form submitted successfully!")
        st.write(f"**First Name:** {first_name}")
        st.write(f"**Middle Name:** {middle_name if middle_name else 'N/A'}")
        st.write(f"**Age:** {int(age)}")