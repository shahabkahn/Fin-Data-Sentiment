from fastapi import FastAPI, HTTPException
from transformers import pipeline
from pydantic import BaseModel
import nest_asyncio
#from pyngrok import ngrok
from fastapi.responses import RedirectResponse

app = FastAPI()

# Load the model
text_classifier = pipeline("text-classification", model="mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis")

# Input data model
class TextInput(BaseModel):
    text: str

@app.post('/analyze')
async def Predict_Sentiment(text_input: TextInput):
    text = text_input.text

    # Validate input text
    if not text.strip():  # Check if text is empty or contains only whitespace
        raise HTTPException(status_code=400, detail="Input text is empty or contains only whitespace.")
    elif text.strip() == "--":  # Check if text is "--"
        raise HTTPException(status_code=400, detail="Invalid input text.")
    elif text.isdigit():  # Check if text contains only digits
        raise HTTPException(status_code=400, detail="Input text contains only digits.")
    elif not any(c.isalpha() for c in text):  # Check if text contains any alphabetic characters
        raise HTTPException(status_code=400, detail="Input text contains no alphabetic characters.")

    # Perform sentiment analysis
    try:
        return text_classifier(text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get('/')
async def html():
    return "Welcome to Financial Sentiment Analysis API"


#ngrok_tunnel = ngrok.connect(8000)
#print('Public URL:', ngrok_tunnel.public_url)
nest_asyncio.apply()
#uvicorn.run(app, port=8000)


