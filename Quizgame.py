import streamlit as st

st.title("Welcome to the Quiz Game")

ques = [
    "Q1: First Alphabet of English language..?\n  A) d  B) e  C) a  D) f",
    "Q2: Which of these is a mammal..?\nA) Duck  B) Hen  C) Owl  D) Whale",
    "Q3: Which is the largest ocean in the world?\nA) Indian  B) Pacific  C) Arctic  D) Atlantic",
    "Q4: Which is the National animal of India..?\nA) Fox  B) Cow  C) Tiger  D) Cat",
    "Q5: How many continents in the world..?\nA) 4  B) 7  C) 8  D) 9",
    "Q6: Which planet is known as the Red Planet?\nA) Earth  B) Mars  C) Jupiter  D) Saturn",
    "Q7: Which gas do plants absorb from air?\nA) Oxygen  B) Carbon Dioxide  C) Nitrogen  D) Hydrogen",
    "Q8: What is the capital of India?\nA) Mumbai  B) Delhi  C) Kolkata  D) Chennai",
    "Q9: Which is the largest animal on Earth?\nA) Elephant  B) Blue Whale  C) Giraffe  D) Shark",
    "Q10: Which festival is known as festival of lights?\nA) Holi  B) Diwali  C) Eid  D) Christmas"
]

# correct answers
anslist = ['C','D','B','C','B','B','B','B','B','B']

userans = []
for i in range(len(ques)):
    st.write(ques[i])
    a = st.text_input(f"Enter your answer for Q{i+1} (A/B/C/D):", key=i)
    userans.append(a)

if st.button("Submit"):
    score = 0
    for i in range(len(anslist)):
        if userans[i].upper() == anslist[i]:
            score += 1

    st.write("You scored", score, "out of", len(ques))

    if score == 10:
        st.balloons()
        st.write("Outstanding! You are topper of this quiz!")
    elif score >= 8:
        st.write("Excellent performance! Keep it up!")
    elif score >= 6:
        st.write("You passed the quiz. Good effort!")
    else:
        st.write("Better luck next time!")

st.sidebar.write("Quiz Menu")
