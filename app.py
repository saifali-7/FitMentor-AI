import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv()

# Page Configuration
st.set_page_config(
    page_title="FitMentor AI",
    page_icon="🏋️",
    layout="centered"
)

# Sidebar
with st.sidebar:
    st.title("🏋️ FitMentor AI Features")

    st.write("💪 Workout Plans")
    st.write("🥗 Nutrition Guidance")
    st.write("⚖️ Weight Loss Tips")
    st.write("📈 Weight Gain Plans")
    st.write("🏃 Cardio Recommendations")
    st.write("😴 Recovery & Sleep")
    st.write("💧 Hydration Tips")

# Main Page
st.title("🏋️ FitMentor AI Coach")

st.write("""
Welcome to the **FitMentor AI Coach**.

This AI helps users with:

- 💪 Workout Plans
- 🥗 Nutrition Advice
- ⚖️ Weight Loss Guidance
- 📈 Muscle Building
- 🏃 Cardio Training
- 😴 Recovery and Sleep
- 💧 Hydration
- ❤️ Healthy Lifestyle

Ask your fitness-related question below.
""")

# User Input
question = st.text_area(
    "🏋️ Enter Your Fitness Question"
)

# Ask AI Button
if st.button("Ask AI 💪"):

    if question.strip() == "":
        st.warning("Please enter a question.")
    else:

        llm = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=0.3
        )

        prompt = ChatPromptTemplate.from_template("""
You are a certified Fitness and Nutrition Coach.

Your job is to answer ONLY fitness-related questions.

Topics include:
- Workout Plans
- Muscle Building
- Weight Loss
- Weight Gain
- Nutrition
- Cardio
- Strength Training
- Recovery
- Sleep
- Hydration
- Healthy Lifestyle

If the user asks anything outside fitness and nutrition, reply exactly:

"Sorry, I only answer fitness and nutrition related questions."

Question:
{question}

Provide:

1. Simple Explanation
2. Step-by-step Guidance
3. Recommended Practices
4. Precautions (if needed)

Answer:
""")

        chain = prompt | llm

        response = chain.invoke(
            {
                "question": question
            }
        )

        st.success(response.content)

# Optional BMI Calculator
st.markdown("---")
st.subheader("⚖️ BMI Calculator")

weight = st.number_input(
    "Enter Weight (kg)",
    min_value=1.0,
    value=60.0
)

height = st.number_input(
    "Enter Height (meters)",
    min_value=0.5,
    value=1.70
)

if st.button("Calculate BMI"):

    bmi = weight / (height ** 2)

    st.info(f"Your BMI is: {bmi:.2f}")

    if bmi < 18.5:
        st.warning("Underweight")
    elif bmi < 25:
        st.success("Normal Weight")
    elif bmi < 30:
        st.warning("Overweight")
    else:
        st.error("Obese")