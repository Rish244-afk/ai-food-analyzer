import gradio as gr
from PIL import Image

import label_image
from calorie_api import get_calories
from caption_api import get_caption

# Emoji map
EMOJI_MAP = {
    "Ice Cream": "🍨",
    "Fried Rice": "🍚",
    "Pizza": "🍕",
    "Sandwich": "🥪",
    "Samosa": "🌭"
}

# Fix model labels
FOOD_FIX = {
    "pizza": "Pizza",
    "ice_cream": "Ice Cream",
    "hotdog": "Sandwich",
    "plate": "Fried Rice",
    "dough": "Samosa"
}

def analyze_food(image):
    if image is None:
        return "Upload an image", "", "", ""

    # Save temp image
    image_path = "temp.jpg"
    image.save(image_path)

    # 🔹 Food Detection
    food, confidence = label_image.main(image_path)
    food = FOOD_FIX.get(food.lower(), food.title())

    emoji = EMOJI_MAP.get(food, "")

    # 🔹 Gemini
    calories = get_calories(image_path)
    caption = get_caption(image_path)

    # Output formatting
    food_result = f"{food} {emoji}"
    confidence_result = f"{confidence}%"

    return food_result, confidence_result, calories, caption


# UI
interface = gr.Interface(
    fn=analyze_food,
    inputs=gr.Image(type="pil", label="Upload Food Image"),
    outputs=[
        gr.Textbox(label="Food Detected"),
        gr.Textbox(label="Confidence"),
        gr.Textbox(label="Calories"),
        gr.Textbox(label="Caption")
    ],
    title="🍽️ AI Food Analyzer",
    description="Upload a food image to detect food, estimate calories, and generate caption.",
    theme="soft"
)

interface.launch()