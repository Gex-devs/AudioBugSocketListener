import asyncio
import pyaudio
import websockets

async def audio_handler(websocket, path):
    print("Connected to client.")
    # Set up PyAudio to play audio.
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, output=True,frames_per_buffer=3528)

    while True:
        # Receive audio data over the WebSocket connection.
        data = await websocket.recv()

        # Process the audio data as needed.
        processed_data = process_audio(data)

        # Play the processed audio data.
        stream.write(processed_data)

def process_audio(data):
    # This function is called when audio data is received. You can modify it
    # to perform any processing or analysis on the audio data.
    print(f'Received {len(data)} bytes of audio data.')
    return data

async def start_server():
    # Start the WebSocket server.
    running = True
    #8762 
    server = await websockets.serve(audio_handler, '0.0.0.0', 8762)
    print("Server hosted")

    while running:
        await asyncio.sleep(1)
    # Run the server until interrupted.
    await server.wait_closed()

if __name__ == '__main__':
    asyncio.run(start_server())
