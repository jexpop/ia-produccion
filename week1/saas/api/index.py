from fastapi import FastAPI  # type: ignore
from fastapi.responses import StreamingResponse  # type: ignore
from openai import OpenAI  # type: ignore

app = FastAPI()

@app.get("/api")
def idea():
    client = OpenAI()
    prompt = [{"role": "user", 
    "content": "Responde con nuevas ideas de negocio para agentes de IA con temática de fiestas populares y divertidas, formateadas con encabezados, subtítulos y viñetas y subpuntos descriptivos"}]
    stream = client.chat.completions.create(model="gpt-5-nano", messages=prompt, stream=True)

    def event_stream():
        for chunk in stream:
            text = chunk.choices[0].delta.content
            if text:
                for line in text.split("\n"):
                    yield f"data: {line}\n"
                yield "\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")