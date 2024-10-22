# Leaf Disease Detector Application 🌿

## Overview
The **Leaf Disease Detector Application** is a web-based tool designed to assist farmers, agricultural experts, and gardeners in detecting common leaf diseases. By analyzing images of affected leaves, the tool uses a deep learning model trained with **TensorFlow Lite** to recognize various leaf diseases. Users can upload an image from their device or use the camera to scan a leaf. Once the disease is predicted, users are offered a direct link to search for additional information on Google.

## Features 🌟
- **Image Capture or Upload**: Users can either take a photo using the device’s camera or upload an image from their device.
- **Disease Prediction**: The app uses a **TensorFlow Lite** model, hosted on a custom server, to predict one of several leaf diseases.
- **Google Search Link**: After a prediction, the app provides a link for users to search for more information on Google.
- **About Section**: A brief project description helps users understand the app's purpose and functionality.

## How the Application Works 🚀

### 1. **Front-End (User Interface)**
The front-end is built using **HTML**, **CSS**, and **JavaScript**. It offers a simple, intuitive interface for users to submit leaf images for analysis.

- **Scan Now Button**: Opens the device's camera, allowing users to take a live photo of a leaf.
- **Upload Image Button**: Lets users upload an image of a leaf from their device.

#### Interface Breakdown:
- **Header**: Displays the app's title, "Leaf Disease Detector", with a modern gradient text effect.
- **About Section**: Explains the tool's purpose in a short paragraph.
- **Results Section**: After submitting an image, the predicted disease is displayed along with a Google search link for more details.
- **Footer**: Shows the contributors who developed the application.

### 2. **Back-End (Flask API on a Local Web Server)**
The back-end is powered by **Flask**, serving the API that processes images and makes predictions using the **TensorFlow Lite** model. The API is hosted on your local server at https://ishaan.basthofer.com/predict.

- **Model Loading**: At startup, the Flask app loads the **TensorFlow Lite** model, which handles image data and returns predictions.
- **Image Preprocessing**: Before making predictions, images are resized and normalized to match the input format required by the **TensorFlow Lite** model.
- **Disease Prediction**: The model predicts one of the following leaf diseases:
  - ## Anthracnose
    ![sample image anthracnose 1](https://github.com/user-attachments/assets/4f3fc83a-fe76-47bc-989f-0decd2e3d89f)

  - ## Bacterial Blight
    ![sample image Bacterial Blight 1 (2)](https://github.com/user-attachments/assets/6bd69652-81b5-4541-8643-d12b47e2f6d1)

  - ## Cercospora Leaf Spot
    ![sample image Cercospora Leaf Spot (4)](https://github.com/user-attachments/assets/95c4079f-51e2-4123-9d18-864aa32e0675)

  - ## Powdery Mildew
    ![sample image Powdery Mildew (4)](https://github.com/user-attachments/assets/47f74d64-4dba-431b-9463-e64705fff2d2)

  - ## Shot Hole Disease
    ![sample image Shot Hole Disease (3)](https://github.com/user-attachments/assets/98f9baa2-8fd0-4f7d-8865-b14131021bf9)

- **Response**: The Flask server returns the predicted disease name in a JSON response to the front-end.

### 3. **Model Architecture and Training (TensorFlow)**
The deep learning model is built and trained using **TensorFlow** and converted to **TensorFlow Lite** for efficient, real-time predictions on mobile devices and web browsers.

#### Key Steps in Model Development:
- **Dataset**: The model was trained on a dataset of labeled images of diseased leaves.
- **Preprocessing**: Images were resized and normalized to fit the input requirements of the **MobileNetV2** architecture.
- **Model Training**: The model was trained using the **TensorFlow** framework and then converted to **TensorFlow Lite** format for deployment.
- **TensorFlow Lite Model**: The model is lightweight and optimized for use on mobile devices or browsers.

#### Training Pipeline:
- **Model Architecture**: A pre-trained **MobileNetV2** model was fine-tuned on the leaf disease dataset with a softmax output layer to classify one of the five diseases.
- **Optimization**: The model was trained using the **Adam optimizer** with **cross-entropy loss**, and the learning rate was dynamically adjusted during training.
- **Model Conversion**: The trained model was converted to **TensorFlow Lite** for efficient deployment in the Flask back-end.

### 4. **Deployment**
The project is deployed in two parts:

- **Front-End**: Hosted using **GitHub Pages** or **Vercel** for serving static web content.
- **Back-End (Flask API)**: Hosted on your local web server at https://ishaan.basthofer.com/predict to serve the model and process image submissions for predictions.

## Workflow 🛠️

1. **User Interaction**:
   - The user clicks "Scan Now" to open the camera, or "Upload Image" to select a file from their device.

2. **Image Capture/Upload**:
   - **Camera Capture**: Users capture an image using their device's camera.
   - **File Upload**: Users select and upload an image from their device.

3. **Sending Image to the Server**:
   - The image is sent to the Flask back-end via an HTTP POST request to https://ishaan.basthofer.com/predict.

4. **Model Prediction**:
   - The Flask back-end receives, preprocesses, and runs the image through the **TensorFlow Lite** model to predict the disease.

5. **Display Results**:
   - The predicted disease is displayed, along with a clickable Google search link for further information.

## Dependencies 📦
To run the project, the following dependencies are required:

- **Flask**: A web framework for creating the back-end API.
- **TensorFlow Lite**: Used for loading and running the deep learning model.
- **Pillow**: A Python library for image processing.
- **Flask-CORS**: To manage cross-origin requests between the front-end and back-end.
- **Gunicorn**: To run the Flask app in a production environment.

To install these dependencies, run:
bash
pip install -r requirements.txt




## Future Enhancements 🔮
- **Additional Disease Classes**: Expand the model to include more types of plant diseases.
- **Enhanced Camera UI**: Improve the camera interface to make image capturing easier.
- **Mobile App**: Extend the project to a mobile application using frameworks such as **React Native** or **Flutter**
