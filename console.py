import cv2
import numpy as np
import os
import sys
import subprocess
import threading
import time
from PIL import Image

ASCII_CHARS = " .:-=+*#%@"
VIDEO_FILE = "video.mp4"

WIDTH = 150  
HEIGHT = 35  

def preprocess_frames(video_file):
    frames = []
    cap = cv2.VideoCapture(video_file)
    if not cap.isOpened():
        print(f"Error: Unable to open video file {video_file}")
        return frames

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print("Processing frames...")

    for i in range(frame_count):
        ret, frame = cap.read()
        if not ret:
            break

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        image = Image.fromarray(gray_frame)
        image = scale_image(image)
        ascii_art = convert_to_ascii(image)
        frames.append(ascii_art)

        progress = (i + 1) / frame_count * 100
        sys.stdout.write(f'\rProcessing frames: {progress:.2f}%')
        sys.stdout.flush()

    cap.release()
    print("\nFrame processing completed.")
    return frames

def scale_image(image, new_width=WIDTH, new_height=HEIGHT):
    (original_width, original_height) = image.size
    aspect_ratio = original_height / original_width
    new_height = int(aspect_ratio * new_width * 0.55)  
    resized_image = image.resize((new_width, new_height))
    return resized_image

def convert_to_ascii(image, width=WIDTH):
    pixels = np.array(image)
    ascii_str = ''.join([ASCII_CHARS[(pixel // 32) if pixel > 0 else 0] for pixel in pixels.flatten()])
    ascii_str = '\n'.join([ascii_str[i:i+width] for i in range(0, len(ascii_str), width)])
    return ascii_str

def play_video_in_command_prompt(frames, fps, start_time):
    frame_interval = 1 / fps
    frame_count = len(frames)
    
    for i in range(frame_count):
        current_time = time.time()
        expected_time = start_time + (i * frame_interval)
        sleep_time = expected_time - current_time

        if sleep_time > 0:
            time.sleep(sleep_time)
        
        sys.stdout.write('\033[H\033[J')
        sys.stdout.write(frames[i])
        sys.stdout.flush()

    sys.stdout.write('\033[H\033[J')
    sys.stdout.flush()

def play_video_in_window():
    try:
        if os.name == 'nt':
            subprocess.Popen(['start', VIDEO_FILE], shell=True)
        elif os.name == 'posix':
            subprocess.Popen(['xdg-open', VIDEO_FILE])
        else:
            print("Unsupported OS")
            return
    except Exception as e:
        print(f"Error opening video file: {e}")

def process_video():
    global frames, fps
    try:
        frames = preprocess_frames(VIDEO_FILE)
        if not frames:
            print(f"Error processing video file {VIDEO_FILE}")
            return
        
        cap = cv2.VideoCapture(VIDEO_FILE)
        if not cap.isOpened():
            print(f"Error: Unable to open video file {VIDEO_FILE}")
            return
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        cap.release()
    except Exception as e:
        print(f"Error processing video: {e}")

def main():
    try:
        if os.path.isfile(VIDEO_FILE):
            processing_thread = threading.Thread(target=process_video)
            processing_thread.start()
            processing_thread.join()

            video_window_thread = threading.Thread(target=play_video_in_window)
            video_window_thread.start()

            time.sleep(1)

            start_time = time.time()
            play_video_in_command_prompt(frames, fps, start_time)

            video_window_thread.join()

            print("Playback finished. Exiting...")
        else:
            print(f"No video file named {VIDEO_FILE} found.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
