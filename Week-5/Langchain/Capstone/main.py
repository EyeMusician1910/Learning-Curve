import pets_namer as ptn
import streamlit as st

st.title("Petty Namer")

animal_type = st.sidebar.selectbox("what is your pet?", ("Cat","Dog","Hamster","Cow",))

if animal_type =="Cat" :
    pet_color = st.sidebar.text_area(label="what color is your cat?",max_chars=15)
if animal_type =="Dog" :
    pet_color = st.sidebar.text_area(label="what color is your dog?",max_chars=15)
if animal_type =="Hamster" :
    pet_color = st.sidebar.text_area(label="what color is your hamster?",max_chars=15)
if animal_type =="Cow" :
    pet_color = st.sidebar.text_area(label="what color is your cow?",max_chars=15)

if pet_color:
    response=ptn.generate_pet_name(animal_type,pet_color)
    st.text(response)