 # List of 10 questions
import  streamlit as st
st.title("🎯 Simple Quiz Game")
st.write("Welcome to the quiz game...")
AL = []
    
def game():

    Ques = ( "Q1: First Alphabet of English language..?",
            "Q2: Which of these is a mammal..?",
            "Q3: Which is the largest ocean in the world?",
            "Q4: Which is the National animal of India..?",
            "Q5: How many continents in the world..?",
            "Q6: Which planet is known as the Red Planet?",
            "Q7: Which gas do plants absorb from the atmosphere?",
            "Q8: What is the capital of India?",
            "Q9: Which is the largest animal on Earth?",
            "Q10: Which festival is known as the festival of lights?")
    
    Answers = (("A) d", "B) e", "C) a", "D) f"),
              ("A) Duck", "B) Hen", "C) Owl", "D) Whale"),
              ("A) Indian ocean", "B) Pacific ocean", "C) Arctic ocean", "D) Atlantic ocean"),
              ("A) Fox", "B) Cow", "C) Tiger", "D) Cat"),
              ("A) 4", "B) 7", "C) 8", "D) 9"),
              ("A) Earth", "B) Saturn", "C) Jupiter", "D) Mars"),
              ("A) Oxygen", "B) Nitrogen", "C) Carbon Dioxide", "D) Hydrogen"),
              ("A) Delhi", "B) Mumbai", "C) Kolkata", "D) Chennai"),
              ("A) Elephant", "B) Blue Whale", "C) Giraffe", "D) Shark"),
              ("A) Holi", "B) Diwali", "C) Eid", "D) Christmas"))
    
    
    Score = 0
    Ques_num = 0
    
# Empty list to store user answers
    for i in range(len(Ques)):
        st.write("----------------------")
        st.write(Ques[i])
    
    # Show each option one by one
        for opt in Answers[i]:
            st.write(opt)
    
    # Take user answer
        ans = st.text_input(f"Enter your choice (A/B/C/D) for Q{i+1}:", key=f"q{i}")
        AL.append(ans)


    
    if st.button("Submit Quiz"):
        
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
        if AL[5] == 'D' or AL[5] == "d":
            Score += 1
        if AL[6] == 'C' or AL[6] == "c":
            Score += 1
        if AL[7] == 'A' or AL[7] == "a":
            Score += 1
        if AL[8] == 'B' or AL[8] == "b":
            Score += 1
        if AL[9] == 'B' or AL[9] == "b":
            Score += 1

    #st.write(f"\nYou scored {Score} out of {len(Ques)}")

        if Score == 10:
            st.balloons()
            st.success("Outstanding! You’re the topper of this quiz!")
        elif Score == 9:
            st.balloons()
            st.success("Excellent performance! Keep it up!")
        elif Score == 8:
            st.info("You have passed the Quiz with 8 points and got Third position")
        elif Score == 7:
            st.info("You have passed the Quiz with 7 points and got Fourth position")
        elif Score == 6:
            st.info("You passed the quiz. Good effort!")
        else:
            st.warning("Better Luck next time....")
   
    # game()
        st.write(f"✅ You scored {Score} out of {len(Ques)}")
        st.write("Correct answers is : C, D, B, C, B, D, C, A, B, B")
        st.write("\nYour Answers:", AL)



st.sidebar.markdown("RESET MENU")
opt = st.sidebar.button("🔄 Reset Quiz")
if opt == True:
    AL.clear()
    game()
    st.rerun()
#      ()
#     st.session_state.clear()
#     st.rerun()
game()
 
 
    
     
