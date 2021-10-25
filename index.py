import streamlit as st

st.title("Streamlit Tutorials")

st.header("I'm a header")
st.subheader("I'm a subheader")

st.text("text")

st.success("success")
st.info("info")
st.warning("warning")
st.error("error")
st.exception("NameError('I'm so handsome')")

vid_file = open("squat1.mp4", "rb").read()
st.video(vid_file)

if st.checkbox("Show/Hide"):
    st.text("hello!")

status = st.selectbox("What's your gender?", ["male", "Female", "Other"])

favorite_fruits = st.multiselect("Please pick three fruits you like the most:", ("apple", "banana", "peach",
                                                                                 "strawberry", "pineapple"))

age = st.slider("How old are you?", 0, 100)

if st.button("push me"):
    st.text(":)")

name = st.text_input("What's your name?", "Please input your name here")
if name != "Please input your name here":
    st.text(f"hello, {name}!")

