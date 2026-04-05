# 🍽️ AI-Powered Food Analyzer

![Python](https://img.shields.io/badge/Python-3.11-blue)
![TensorFlow](https://img.shields.io/badge/DeepLearning-CNN-orange)
![Gemini](https://img.shields.io/badge/AI-Gemini-green)
![UI](https://img.shields.io/badge/UI-Gradio-purple)

---

## 🚀 Overview

An AI-powered application that analyzes food images to identify food items, estimate calories, and generate captions using Deep Learning and Google Gemini API.

---

## 🎯 Features

* 📸 Upload food images
* 🍔 Detect food using Deep Learning (MobileNetV2)
* 📊 Display prediction confidence
* 🔥 Estimate calories using Gemini API
* 🖼️ Generate captions with hashtags
* 🎨 Interactive UI using Gradio

---

## 🧠 Architecture

```
Image Input
   ↓
MobileNetV2 (CNN)
   ↓
Food Label + Confidence
   ↓
Gemini API
   ↓
Calories + Caption
```

---

## ⚙️ Tech Stack

* Python
* TensorFlow / Keras
* Deep Learning (CNN - MobileNetV2)
* Google Gemini API
* Gradio
* Computer Vision

---

## 📊 Results

* ⏱️ Processing Time: ~2–4 seconds per image
* 🎯 Accuracy: ~85%–98% (pretrained model)
* 🤖 Multimodal AI system (vision + generative AI)

---

## 🛠️ Installation

```bash
git clone https://github.com/Rish244-afk/ai-food-analyzer.git
cd ai-food-analyzer
pip install -r requirements.txt
```

---

## 🔑 Setup API Key

Open the following files:

* `calorie_api.py`
* `caption_api.py`

Replace:

```python
api_key="YOUR_GEMINI_API_KEY"
```

with your actual Gemini API key.

---

## ▶️ Run the App

```bash
python app.py
```

Then open:

```
http://127.0.0.1:7860
```

---

## 📸 Demo

<img width="1896" height="899" alt="Screenshot 2026-04-05 203250" src="https://github.com/user-attachments/assets/d395375d-3db0-4a07-af26-f7af66c4837c" />
<img width="1897" height="953" alt="Screenshot 2026-04-05 203308" src="https://github.com/user-attachments/assets/ca3d3c25-cdb9-4212-b470-80b5a2ca0dcd" />


---

## 💡 Future Improvements

* Train custom food dataset (Food-101)
* Improve calorie estimation accuracy
* Deploy as web/mobile app
* Add diet tracking system

---

## 🧠 Key Learnings

* Integration of Deep Learning and Generative AI
* Working with pretrained CNN models
* API integration (Gemini)
* Building interactive ML applications

---

## 👨‍💻 Author

**Rishhav**
🔗 https://github.com/Rish244-afk

---

## ⭐ If you like this project, give it a star!
