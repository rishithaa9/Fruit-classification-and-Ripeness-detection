import streamlit as st
import tensorflow as tf
import numpy as np

# Tensorflow Model Prediction
def model_prediction(test_image):
    model = tf.keras.models.load_model("model.h5")
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(64, 64))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])  # Convert single image to batch
    predictions = model.predict(input_arr)
    return np.argmax(predictions)  # Return index of max element


# Main Page
st.title("FRUIT CLASSIFICATION AND RIPENESS DETECION")

# Prediction Section
st.header("Prediction")
test_image = st.file_uploader("Upload an Image:", type=["jpg", "jpeg", "png"])
if test_image is not None:
    st.image(test_image, use_container_width=True)

    # Predict button
    if st.button("Predict"):        
        result_index = model_prediction(test_image)
        #st.write(f"Result Index: {result_index}") #printing Model labels
        # Reading Labels
        with open("labels.txt") as f:
            content = f.readlines()
        label = [i.strip() for i in content]
        #st.write(f"Number of Labels: {len(label)}") #printing label.txt labels
        st.success("Predicted Fruit: {}".format(label[result_index]))
