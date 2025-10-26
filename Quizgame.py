# List of 10 questions
import  streamlit as st


st.write("Welcome to the quiz game...")
ques = [
    "Q1: First Alphabet of English language..?\nA) d\tB) e\nC) a\tD) f",
    "Q2: Which of these is a mammal..?\nA) Duck\tB) Hen\nC) Owl\tD) Whale",
    "Q3: Which is the largest ocean in the world?\nA) Indian ocean\tB) Pacific ocean\nC) Arctic ocean\tD) Atlantic ocean",
    "Q4: Which is the National animal of India..?\nA) Fox\tB) Cow\nC) Tiger\tD) Cat",
    "Q5: How many continents in the world..?\nA) 4\tB) 7\nC) 8\tD) 9",
    "Q6: Which planet is known as the Red Planet?\nA) Earth\tB) Mars\tC) Jupiter\tD) Saturn",
    "Q7: Which gas do plants absorb from the atmosphere?\nA) Oxygen\tB) Carbon Dioxide\tC) Nitrogen\tD) Hydrogen",
    "Q8: What is the capital of India?\nA) Mumbai\tB) Delhi\tC) Kolkata\tD) Chennai",
    "Q9: Which is the largest animal on Earth?\nA) Elephant\tB) Blue Whale\tC) Giraffe\tD) Shark",
    "Q10: Which festival is known as the festival of lights?\nA) Holi\tB) Diwali\tC) Eid\tD) Christmas"
]

# Empty list to store user answers
AL = []
for i in range(len(ques)):
    st.write(ques[i])
    ans = st.text_input("Enter your choice (A/B/C/D): ",key = i)  
    AL.append(ans)
    print("<....................................>")

Score = 0

if AL[0] == 'C' or AL[0] == "c":
    Score += 1
if AL[1] == 'D' or AL[1] == "d":
    Score += 1
if AL[2] == 'B' or AL[2] == "b":
    Score += 1
if AL[3] == 'C' or AL[3] == "c":
    Score += 1
if AL[4] == 'B' or AL[4] == "b":
    Score += 1
if AL[5] == 'B' or AL[5] == "b":
    Score += 1
if AL[6] == 'B' or AL[6] == "b":
    Score += 1
if AL[7] == 'B' or AL[7] == "b":
    Score += 1
if AL[8] == 'B' or AL[8] == "b":
    Score += 1
if AL[9] == 'B' or AL[9] == "b":
    Score += 1

print(f"\nYou scored {Score} out of {len(ques)}")

if Score == 10:
    st.balloons()
    print("Outstanding! You’re the topper of this quiz!")
elif Score == 9:
    st.balloons()
    print("Excellent performance! Keep it up!")
elif Score == 8:
    st.balloons()
    print("You have passed the Quiz with 8 points and got Third position")
elif Score > 7:
    st.balloons()
    print("You have passed the Quiz with 7 points and got Fourth position")
elif Score == 6:
    print("You passed the quiz. Good effort!")
else:
    print("Better Luck next time....")
print("\nYour Answers:", AL)

st.sidebar.markdown("Restart")
