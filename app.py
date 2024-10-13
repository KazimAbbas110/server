from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS to handle cross-origin requests
from transformers import BlipProcessor, BlipForConditionalGeneration
from transformers import MarianMTModel, MarianTokenizer
import base64
from PIL import Image
import io

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize models
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
translation_model = MarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-en-ur')
translation_tokenizer = MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-en-ur')

@app.route('/caption', methods=['POST'])
def caption_image():
    try:
        data = request.get_json()
        if 'image' not in data:
            return jsonify({"error": "No image data provided"}), 400

        # Decode the base64 image
        image_data = base64.b64decode(data['image'])
        image = Image.open(io.BytesIO(image_data))

        # Generate caption
        inputs = processor(image, return_tensors="pt")
        out = model.generate(**inputs)
        caption = processor.decode(out[0], skip_special_tokens=True)

        return jsonify({'caption': caption})
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return error message

@app.route('/translate', methods=['POST'])
def translate_text():
    try:
        data = request.get_json()
        if 'text' not in data:
            return jsonify({"error": "No text provided for translation"}), 400

        text = data['text']
        inputs = translation_tokenizer(text, return_tensors="pt")
        translated_tokens = translation_model.generate(**inputs)
        translated_text = translation_tokenizer.decode(translated_tokens[0], skip_special_tokens=True)

        return jsonify({'translation': translated_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return error message

if __name__ == '__main__':
    app.run(debug=True)
