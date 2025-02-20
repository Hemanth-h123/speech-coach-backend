from fastapi import FastAPI, WebSocket
import uvicorn

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            if data:  # Ensure data exists before sending
                await websocket.send_text(f"Message received: {data}")
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        if websocket.client_state == 1:  # Check if still connected
            await websocket.close()  

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
