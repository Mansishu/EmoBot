import streamlit as st

st.set_page_config(page_title="EmoBot - Emotional Support Buddy", page_icon="🧠")

st.title("EmoBot 🧠")
st.subheader("An emotional support chatbot designed for students")

# Input from user
user_input = st.text_input("How are you feeling today? (e.g. stressed, sad, happy, anxious)")

# Button to submit
if st.button("Submit"):

    if user_input.strip() == "":
        st.warning("Please enter something before submitting.")
    else:
        # Convert input to lowercase for easier matching
        feeling = user_input.lower()

        # Basic responses based on keywords
        if "sad" in feeling or "depressed" in feeling or "unhappy" in feeling:
            st.write("I'm sorry you're feeling down. Try taking deep breaths or listening to some calming music. 🎵")
            st.write("You can watch this calming video to relax:")
            st.video("https://www.youtube.com/watch?v=2OEL4P1Rz04")  # Relaxing video

        elif "stressed" in feeling or "pressure" in feeling or "anxious" in feeling:
            st.write("Stress can be tough. Take a short break, maybe go for a walk or do some stretching exercises. 🚶‍♂")
            st.write("Here's a helpful video on stress relief:")
            st.video("https://www.youtube.com/watch?v=hnpQrMqDoqE")  # Stress relief video

        elif "happy" in feeling or "good" in feeling or "fine" in feeling:
            st.write("That's great to hear! Keep enjoying your day and spread the positivity! 😊")
            st.write("Remember to take small moments to celebrate yourself. 🎉")

        elif "suicidal" in feeling or "hopeless" in feeling or "tired" in feeling:
            st.error("I'm really sorry you're feeling this way. Please consider talking to a trusted friend, family member, or a counselor immediately. You're not alone. 💛")
            st.write("Here’s a resource that might help you:")
            st.markdown("[Suicide Prevention Hotline](https://suicidepreventionlifeline.org/)")

        else:
            st.write("Thanks for sharing how you feel. Remember, it's okay to feel this way sometimes. Try to do something you love or talk to someone you trust. 💬")
            st.write("Here’s a calming breathing exercise you can try:")
            st.video("https://www.youtube.com/watch?v=SEfs5TJZ6Nk")
            
st.markdown(
    """
    <hr style="border: none; height: 1px; background-color: #eee; margin-top: 50px;" />
    <div style='text-align: center; color: gray; font-size: 14px; margin-top: 10px;'>
        Made with love by Mansi ❤💛 For students, always.
    </div>
    """,
    unsafe_allow_html=True
)
