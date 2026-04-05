from google import genai
from PIL import Image

client = genai.Client(api_key="AIzaSyB55eFiabHDdvvrYNNA-sWjKRQZsl18iiI")

def get_caption(image_path):
    try:
        image = Image.open(image_path)

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                "Generate a short catchy food caption with hashtags.",
                image
            ]
        )

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"