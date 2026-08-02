import os
import google.genai as genai
from fastapi import APIRouter,HTTPException
from pydantic import BaseModel
class ChatRequest(BaseModel):
    question: str
gemini_model=genai.Client(api_key=os.environ.get('CHATBOT'))
# goodmorning how can I help you?
router = APIRouter()
def simple_bot(question):
  prompt=f""" The student has asked the {question}, give a structured and brief reply. If the {question} is not related to studies or performance enhancement factors like sleep hours,sleep quality,etc,refrain from replying."""
  try:
      response = gemini_model.models.generate_content(
      model="gemini-2.5-flash",contents=prompt)
      return response.text
    

  except Exception as e:
      print("Gemini error:", e)
      return "Chatbot temporarily unavailable."
@router.post("/")  
def chatbot(request:ChatRequest):
  text=request.question
  if text.lower() in ['quit', 'bye', 'goodbye', 'exit']:
        return {"reply": "Goodbye! Have a great day."}
  reply = simple_bot(text)
  return {"reply": reply}
