# Fruit-classification-and-Ripeness-detection
Fruit Classification and Ripeness Detection
Overview
This project is a deep learning-based application designed to classify different types of fruits and assess their ripeness. It uses convolutional neural networks (CNNs) with transfer learning to identify fruits such as apples, bananas, oranges, mangoes, pomegranates, and papayas, and categorize their ripeness stages (e.g., Ripe, Unripe). 
Features

Fruit Classification: Identifies the type of fruit from an input image.
Ripeness Detection: Determines the ripeness stage (Ripe or Unripe) for supported fruits.
Web Interface: A Flask-based web application for uploading images or using a live video feed for real-time detection.
Data Augmentation: Enhances model robustness with techniques like rotation, flipping, and zooming.
High Accuracy: Achieves over 92% validation accuracy on the fruit classification and ripeness detection tasks.

Requirements
Python 3.8+
TensorFlow 2.5+
Keras
OpenCV
Flask
Selenium
NumPy
Matplotlib

Clone the Repository:
git clone https://github.com/rishithaa9/Fruit-classification-and-Ripeness-detection.git
cd Fruit-classification-and-Ripeness-detection




Download the Dataset:

Run the provided scrape_images.py script to collect images from Google Images, or
Download a pre-collected dataset and place it in the data/fruits directory.

Usage
Training the Model

Organize the dataset in the data/fruits directory with subfolders for each class (e.g., ripe_apple, unripe_banana).
Run the training script:python train.py


The trained model will be saved in the models/ directory.

Running the Web Application

Start the Streamlit server:streamlit run app.py


Access the application at http://localhost:3000 in your browser.
Upload an image or use a live video feed to classify fruits and detect ripeness.

