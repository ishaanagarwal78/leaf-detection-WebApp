from flask import Flask, request, jsonify
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import io

app = Flask(__name__)

# Set device (GPU if available, else CPU)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load the trained model architecture
model = models.resnet18(weights=None)  # Do not load pre-trained weights
num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, 5)  # Replace 5 with the number of classes in your dataset

# Load the trained model's weights
model.load_state_dict(torch.load('leaf_disease_model.pth', map_location=device))  # Ensure to map to the correct device
model = model.to(device)
model.eval()  # Set the model to evaluation mode

# Define preprocessing for a single test image
preprocess = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

# Prediction function
def predict_image(image):
    img_tensor = preprocess(image).unsqueeze(0)  # Add batch dimension
    img_tensor = img_tensor.to(device)

    # Make predictions
    with torch.no_grad():
        outputs = model(img_tensor)
        _, preds = torch.max(outputs, 1)

    # Map prediction index to class name
    class_names = ['Anthracnose', 'Bacterial_Blight', 'Cercospora_Leaf_Spot', 'Powdery_Mildew', 'Shot_Hole_Disease']  # Adjust with your class names
    predicted_class = class_names[preds.item()]
    
    return predicted_class

# Route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    file = request.files['image']
    try:
        # Read the image file
        image = Image.open(io.BytesIO(file.read())).convert('RGB')

        # Predict the class of the image
        predicted_class = predict_image(image)

        # Return the predicted class as JSON
        return jsonify({'predicted_class': predicted_class})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
