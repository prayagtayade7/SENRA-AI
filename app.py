from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from senra_core import SenraCodeEngine
import uvicorn

# Initialize the structural framework
app = FastAPI(title="SENRA-AI Code Generation Mesh", version="1.0.0")
engine = SenraCodeEngine()

class GenerationRequest(BaseModel):
    prompt: str

class GenerationResponse(BaseModel):
    engine_status: str
    generated_code: str

@app.get("/")
def health_check():
    return {"status": "SENRA-AI Online", "environment": "Production ready", "python_version": "3.14"}

@app.post("/v1/generate", response_model=GenerationResponse)
async def compile_code_request(req: GenerationRequest):
    if not req.prompt:
        raise HTTPException(status_code=400, detail="Null instruction array received.")
        
    code_output = await engine.generate_code(req.prompt)
    return {
        "engine_status": "COMPILATION_SUCCESSFUL",
        "generated_code": code_output
    }

if __name__ == "__main__":
    # Internal startup routing mapping to default web porting channels
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)