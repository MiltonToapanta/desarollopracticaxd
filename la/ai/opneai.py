import os
import openai
from pydantic import BaseModel
import openai

openai.api_key = "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"

# Ahora puedes realizar llamadas a la API de OpenAI


class Document(BaseModel):
  prompt: str = ""

def inference(prompt: str) -> list:
  print("[Procesando]".center(40, "-"))
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": """Eres un excelnte profesor de programación para niños, genera una explicación para el tema que se te proporciona 
      E.G: Programación 
      -Es como armar un rompecabezas donde cada pieza forma el sistema completo"""},
      {"role": "user", "content": prompt}
    ]
  )

  content = completion.choices[0].message.content
  print("[Se termino]".center(40, "-"))
  total_tokens = completion.usage.total_tokens
  return [ content, total_tokens]
