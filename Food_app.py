from flask import *
import os
from werkzeug.utils import secure_filename
import label_image

from calorie_api import get_calories
from caption_api import get_caption

app = Flask(__name__)

EMOJI_MAP = {
    "Ice Cream": "🍨",
    "Fried Rice": "🍚",
    "Pizza": "🍕",
    "Sandwich": "🥪",
    "Samosa": "🌭"
}

FOOD_FIX = {
    "pizza": "Pizza",
    "ice_cream": "Ice Cream",
    "hotdog": "Sandwich",
    "plate": "Fried Rice",
    "dough": "Samosa"
}

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file uploaded"

    file = request.files['file']

    if file.filename == '':
        return "No selected file"

    file_path = secure_filename(file.filename)
    file.save(file_path)

    try:
        # 🔹 Food Detection
        food, confidence = label_image.main(file_path)

        # 🔹 Fix label
        food = FOOD_FIX.get(food.lower(), food.title())

        # 🔹 Emoji
        emoji = EMOJI_MAP.get(food, "")

        # 🔹 Gemini AI
        calories = get_calories(file_path)
        caption = get_caption(file_path)

        return render_template(
            "index.html",
            food=food,
            confidence=confidence,
            emoji=emoji,
            calories=calories,
            caption=caption
        )

    except Exception as e:
        return f"Error: {str(e)}"

    finally:
        if os.path.exists(file_path):
            os.remove(file_path)


if __name__ == '__main__':
    app.run(debug=False)