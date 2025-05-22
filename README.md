# RTSP Stream Viewer

A Django-based WebSocket application for streaming RTSP video feeds using FFmpeg. This project allows users to input an RTSP URL and view the video stream in real-time.

---

## Features

- Accepts RTSP URLs for video streaming.
- Streams video frames via WebSocket to the client.
- Uses FFmpeg for processing RTSP streams.
- Displays video frames in the browser.

---

## Prerequisites

Before setting up the project, ensure you have the following installed:

1. **Python** (version 3.8 or higher)
2. **pip** (Python package manager)
3. **Django** (version 4.0 or higher)
4. **FFmpeg** (for processing RTSP streams)
5. **VLC Media Player** (optional, for testing RTSP URLs)

---

## Installation

Follow these steps to set up the project:

### 1. Clone the Repository

git clone https://github.com/your-username/rtsp-stream-viewer.git
cd rtsp-stream-viewer


2. Set Up a Virtual Environment
Create and activate a virtual environment:

3. Install Dependencies
Install the required Python packages:

4. Install FFmpeg
Ensure FFmpeg is installed and accessible from your system's PATH:

macOS: Install via Homebrew:
brew install ffmpeg

Ubuntu/Debian: Install via apt:
Windows: Download FFmpeg from FFmpeg.org and add it to your system's PATH.
Verify the installation:

5. Run Migrations
Set up the database by running migrations:

6. Start the Development Server
Run the Django development server:

Visit http://127.0.0.1:8000/ in your browser.

Usage
Input RTSP URL
Open the application in your browser.
Enter a valid RTSP URL (e.g., rtsp://184.72.239.149/vod/mp4:BigBuckBunny_175k.mov).
Click the "Start Stream" button to view the video stream.
Testing RTSP URLs
Public RTSP URLs
Here are some public RTSP URLs you can use for testing:

Big Buck Bunny (Low Quality): rtsp://184.72.239.149/vod/mp4:BigBuckBunny_175k.mov



