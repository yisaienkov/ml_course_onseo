import streamlit as st

from modules.simple_ml_models import SentimentModel

@st.cache
def load_model():
    print("Load model...")
    return SentimentModel()


if __name__ == "__main__":
    model = load_model()

    mapping = {
        1: "positive",
        0: "neutral",
        -1: "negative",
    }

    st.title("SentimentModel")

    with st.form("sentiment_form"):
        text = st.text_area("text")

        submitted = st.form_submit_button("Submit")
        if submitted:
            prediction = model(text=text)
            label = mapping[prediction]
            st.write(f"Sentiment: {label}")
            if prediction == 1:
                st.balloons()
