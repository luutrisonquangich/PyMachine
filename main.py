from io import BytesIO
import uvicorn
from fastapi import FastAPI
from gtts import gTTS
from fastapi.responses import StreamingResponse



app = FastAPI()
@app.get('/{key}')
async def index(key:str):
    ctext = key
    clang = "vi"
    output = gTTS(text=ctext, lang=clang, slow=False)
    mp3_fp = BytesIO()
    output.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    return StreamingResponse(mp3_fp,  media_type="audio/mp3")

if __name__ == "__main__":
    uvicorn.run(app,host="localhost", port=5555)