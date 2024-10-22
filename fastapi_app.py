from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI()

IMAGE_DIR = Path("/app")

@app.get("/")
async def root():
    return {"message": "Welcome to the Image Serving API!"}

@app.get("/image/{image_name}")
async def serve_image(image_name: str):
    image_path = IMAGE_DIR / image_name
    if not image_path.exists():
        raise HTTPException(status_code=404, detail="Image not found")
    return FileResponse(image_path)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
    