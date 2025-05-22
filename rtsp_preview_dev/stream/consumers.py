import subprocess
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
import base64

class VideoStreamConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.process = None
        await self.accept()

    async def receive(self, text_data):
        rtsp_url = text_data.strip()
        print(f"Received RTSP URL: {rtsp_url}")  # Debug log
        try:
            self.process = await asyncio.create_subprocess_exec(
                'ffmpeg',
                '-rtsp_transport', 'tcp',
                '-i', rtsp_url,
                '-f', 'mjpeg',
                '-q:v', '5',
                '-',
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE  # Capture stderr for debugging
            )
            print("FFmpeg process started")  # Debug log
            asyncio.create_task(self.log_ffmpeg_stderr())  # Log FFmpeg stderr
            asyncio.create_task(self.send_frames())
        except FileNotFoundError:
            print("FFmpeg not found. Ensure it is installed and in your PATH.")  # Debug log
            await self.send("Error: FFmpeg not found. Ensure it is installed and in your PATH.")
        except Exception as e:
            print(f"Error starting FFmpeg process: {e}")  # Debug log
            await self.send(f"Error: {str(e)}")

    async def disconnect(self, close_code):
        if self.process:
            self.process.kill()
            await self.process.wait()

    async def send_frames(self):
        buffer = b""
        try:
            while True:
                chunk = await self.process.stdout.read(1024)
                if not chunk:
                    break
                buffer += chunk
                if b'\xff\xd9' in buffer:  # JPEG end marker
                    frame, _, buffer = buffer.partition(b'\xff\xd9')
                    frame += b'\xff\xd9'
                    print("Sending frame to client")  # Debug log
                    await self.send(base64.b64encode(frame).decode('utf-8'))
        except Exception as e:
            print(f"Error in send_frames: {e}")  # Debug log
            await self.send(f"Error: {str(e)}")

    async def log_ffmpeg_stderr(self):
        """Logs the stderr output from the FFmpeg process."""
        while True:
            line = await self.process.stderr.readline()
            if not line:
                break
            print(f"FFmpeg stderr: {line.decode().strip()}")