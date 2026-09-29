import streamlit as st
import tensorflow as tf
import numpy as np
import json
from PIL import Image
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent


# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="Bharatanatyam Mudra Recognition",
    page_icon="*",
    
    layout="centered"
)


# -----------------------------
# Load model
# -----------------------------

@st.cache_resource
def load_model():
    return tf.keras.models.load_model(PROJECT_ROOT / "mudra_classifier.keras")


@st.cache_data
def load_class_names():
    with open(PROJECT_ROOT / "class_names.json", "r") as f:
        return json.load(f)


model = load_model()
class_names = load_class_names()


# -----------------------------
# App UI
# -----------------------------

st.title("🖐️ Bharatanatyam Mudra Recognition")

st.write(
    "Upload an image of a Bharatanatyam mudra "
    "and the model will predict its class."
)

uploaded_file = st.file_uploader(
    "Upload a mudra image",
    type=["jpg", "jpeg", "png"]
)


# -----------------------------
# Prediction
# -----------------------------

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    if st.button("Predict Mudra"):

        # Resize image
        image = image.resize((128, 128))

        # Convert to numpy
        image_array = np.array(image)

        # Add batch dimension
        image_array = np.expand_dims(image_array, axis=0)

        # Prediction
        predictions = model.predict(image_array)

        predicted_index = np.argmax(predictions[0])
        confidence = np.max(predictions[0])

        predicted_class = class_names[predicted_index]

        st.success(
            f"Predicted Mudra: {predicted_class}"
        )

        st.write(
            f"Confidence: {confidence:.2%}"
        )