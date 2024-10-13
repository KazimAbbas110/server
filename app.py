





# from flask import Flask, request, jsonify
# from PIL import Image
# from transformers import BlipProcessor, BlipForConditionalGeneration, MarianMTModel, MarianTokenizer
# import torch
# import base64
# import io
# from flask_cors import CORS  # Import CORS for handling cross-origin requests

# app = Flask(__name__)
# CORS(app)  # Enable CORS for all routes

# # Load the models once to avoid reloading every time
# processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
# model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
# translation_model_name = 'Helsinki-NLP/opus-mt-en-ur'  # Example: English to Urdu model
# tokenizer = MarianTokenizer.from_pretrained(translation_model_name)
# translation_model = MarianMTModel.from_pretrained(translation_model_name)

# @app.route('/caption', methods=['POST'])
# def caption_image():
#     data = request.get_json()
#     base64_image = data.get('url')  # Expect base64 string

#     # Decode the base64 image
#     try:
#         header, encoded = base64_image.split(',', 1)  # Split the header and data
#         image_data = base64.b64decode(encoded)  # Decode base64 to bytes
#         image = Image.open(io.BytesIO(image_data))  # Load image from bytes
#     except Exception as e:
#         print(f"Error loading image: {e}")
#         return jsonify({'error': 'Failed to load image from base64'}), 400

#     # Generate caption
#     inputs = processor(image, return_tensors="pt")
#     out = model.generate(**inputs)
#     caption = processor.decode(out[0], skip_special_tokens=True)

#     return jsonify({'caption': caption})

# @app.route('/translate', methods=['POST'])
# def translate_text():
#     data = request.get_json()
#     text = data.get('text')

#     # Translate text
#     inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
#     translated_tokens = translation_model.generate(**inputs)
#     translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)

#     return jsonify({'translated_text': translated_text})

# if __name__ == '__main__':
#     app.run(debug=True)












# from flask import Flask, request, jsonify
# from PIL import Image
# from transformers import BlipProcessor, BlipForConditionalGeneration, MarianMTModel, MarianTokenizer
# import torch
# import base64
# import io
# from flask_cors import CORS  # Import CORS for handling cross-origin requests

# app = Flask(__name__)
# CORS(app)  # Enable CORS for all routes

# # Load the models once to avoid reloading every time
# processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
# model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
# translation_model_name = 'Helsinki-NLP/opus-mt-en-ur'  # Example: English to Urdu model
# tokenizer = MarianTokenizer.from_pretrained(translation_model_name)
# translation_model = MarianMTModel.from_pretrained(translation_model_name)

# @app.route('/caption', methods=['POST'])
# def caption_image():
#     data = request.get_json()
#     if not data or 'url' not in data:
#         return jsonify({'error': 'No image data provided.'}), 400

#     base64_image = data.get('url')  # Expect base64 string

#     # Decode the base64 image
#     try:
#         header, encoded = base64_image.split(',', 1)  # Split the header and data
#         image_data = base64.b64decode(encoded)  # Decode base64 to bytes
#         image = Image.open(io.BytesIO(image_data))  # Load image from bytes
#     except Exception as e:
#         print(f"Error loading image: {e}")
#         return jsonify({'error': 'Failed to load image from base64'}), 400

#     # Generate caption
#     try:
#         inputs = processor(image, return_tensors="pt")
#         out = model.generate(**inputs)
#         caption = processor.decode(out[0], skip_special_tokens=True)
#     except Exception as e:
#         print(f"Error generating caption: {e}")
#         return jsonify({'error': 'Failed to generate caption.'}), 500

#     return jsonify({'caption': caption})

# @app.route('/translate', methods=['POST'])
# def translate_text():
#     data = request.get_json()
#     if not data or 'text' not in data:
#         return jsonify({'error': 'No text data provided.'}), 400

#     text = data.get('text')

#     # Translate text
#     try:
#         inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
#         translated_tokens = translation_model.generate(**inputs)
#         translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
#     except Exception as e:
#         print(f"Error translating text: {e}")
#         return jsonify({'error': 'Failed to translate text.'}), 500

#     return jsonify({'translated_text': translated_text})

# if __name__ == '__main__':
#     app.run(debug=True)












# from flask import Flask, request, jsonify
# from PIL import Image
# from transformers import BlipProcessor, BlipForConditionalGeneration, MarianMTModel, MarianTokenizer
# import torch
# import io
# from flask_cors import CORS  # Import CORS for handling cross-origin requests

# app = Flask(__name__)
# CORS(app)  # Enable CORS for all routes

# # Load the models once to avoid reloading every time
# processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
# model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# @app.route('/caption', methods=['POST'])
# def caption_image():
#     if 'image' not in request.files:
#         return jsonify({'error': 'No image file provided'}), 400
    
#     image_file = request.files['image']
    
#     # Open the image file
#     try:
#         image = Image.open(image_file.stream)  # Use stream for file-like object
#     except Exception as e:
#         print(f"Error loading image: {e}")
#         return jsonify({'error': 'Failed to load image'}), 400

#     # Generate caption
#     inputs = processor(image, return_tensors="pt")
#     out = model.generate(**inputs)
#     caption = processor.decode(out[0], skip_special_tokens=True)

#     return jsonify({'caption': caption})

# if __name__ == '__main__':
#     app.run(debug=True)













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
