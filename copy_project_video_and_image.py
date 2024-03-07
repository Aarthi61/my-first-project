
!git clone https://github.com/jantic/DeOldify.git DeOldify

cd DeOldify

## Import necessary libraries and set GPU device
from deoldify import device
from deoldify.device_id import DeviceId

# Choose GPU0 or other GPU if available
device.set(device=DeviceId.GPU0)

!pip install ffmpeg-python

pip install yt-dlp

# Choose GPU0 or other GPU if available
device.set(device=DeviceId.GPU0)

# Import other required libraries
import fastai
from deoldify.visualize import *
from pathlib import Path
import torch
import warnings
warnings.filterwarnings("ignore", category=UserWarning, message=".*?Your .*? set is empty.*?")

# Create a 'models' directory and download the video colorization model
!mkdir 'models'
!wget https://data.deepai.org/deoldify/ColorizeVideo_gen.pth -O ./models/ColorizeVideo_gen.pth
!mkdir 'models'
!wget https://data.deepai.org/deoldify/ColorizeArtistic_gen.pth -O ./models/ColorizeArtistic_gen.pth

# Function to colorize a video from a given URL
def colorize_video(source_url, render_factor, watermarked=True):
    colorizer = get_video_colorizer(render_factor=render_factor)
    if source_url is not None and source_url !='':
        video_path = colorizer.colorize_from_url(source_url, 'video.mp4', watermarked=watermarked)
        show_video_in_notebook(video_path)
    else:
        print('Provide a video URL and try again.')

# Function to colorize an image from a given URL
def colorize_image(source_url, render_factor, watermarked=True):
    colorizer = get_image_colorizer(artistic=True)
    if source_url is not None and source_url !='':
        image_path = colorizer.plot_transformed_image_from_url(url=source_url, render_factor=render_factor, compare=True, watermarked=watermarked)
        show_image_in_notebook(image_path)
    else:
        print('Provide an image URL and try again.')

# Menu for user to choose image or video colorization
print("Choose an option:")
print("1. Colorize Video")
print("2. Colorize Image")
choice = input("Enter 1 or 2: ")

if choice == "1":
    # Video colorization
    source_url = input("Enter the video URL: ")
    render_factor = int(input("Enter the render factor (min: 5, max: 40): "))
    watermarked_input = input("Watermarked? (True/False): ").lower()
    watermarked = watermarked_input == "true"
    colorize_video(source_url, render_factor, watermarked)
elif choice == "2":
    # Image colorization
    source_url = input("Enter the image URL: ")
    render_factor = int(input("Enter the render factor (min: 7, max: 40): "))
    watermarked_input = input("Watermarked? (True/False): ").lower()
    watermarked = watermarked_input == "true"
    colorize_image(source_url, render_factor, watermarked)
else:
    print("Invalid choice. Please enter 1 or 2.")

# Function to colorize a video from a given URL
def colorize_video(source_url, render_factor, watermarked=True):
    colorizer = get_video_colorizer(render_factor=render_factor)
    if source_url is not None and source_url !='':
        video_path = colorizer.colorize_from_url(source_url, 'video.mp4', watermarked=watermarked)
        show_video_in_notebook(video_path)
    else:
        print('Provide a video URL and try again.')

# Function to colorize an image from a given URL
def colorize_image(source_url, render_factor, watermarked=True):
    colorizer = get_image_colorizer(artistic=True)
    if source_url is not None and source_url !='':
        image_path = colorizer.plot_transformed_image_from_url(url=source_url, render_factor=render_factor, compare=True, watermarked=watermarked)
        show_image_in_notebook(image_path)
    else:
        print('Provide an image URL and try again.')

# Menu for user to choose image or video colorization
print("Choose an option:")
print("1. Colorize Video")
print("2. Colorize Image")
choice = input("Enter 1 or 2: ")

if choice == "1":
    # Video colorization
    source_url = input("Enter the video URL: ")
    render_factor = int(input("Enter the render factor (min: 5, max: 40): "))
    watermarked_input = input("Watermarked? (True/False): ").lower()
    watermarked = watermarked_input == "true"
    colorize_video(source_url, render_factor, watermarked)
elif choice == "2":
    # Image colorization
    source_url = input("Enter the image URL: ")
    render_factor = int(input("Enter the render factor (min: 7, max: 40): "))
    watermarked_input = input("Watermarked? (True/False): ").lower()
    watermarked = watermarked_input == "true"
    colorize_image(source_url, render_factor, watermarked)
else:
    print("Invalid choice. Please enter 1 or 2.")

# Function to colorize a video from a given URL
def colorize_video(source_url, render_factor, watermarked=True):
    colorizer = get_video_colorizer(render_factor=render_factor)
    if source_url is not None and source_url !='':
        video_path = colorizer.colorize_from_url(source_url, 'video.mp4', watermarked=watermarked)
        show_video_in_notebook(video_path)
    else:
        print('Provide a video URL and try again.')

# Function to colorize an image from a given URL
def colorize_image(source_url, render_factor, watermarked=True):
    colorizer = get_image_colorizer(artistic=True)
    if source_url is not None and source_url !='':
        image_path = colorizer.plot_transformed_image_from_url(url=source_url, render_factor=render_factor, compare=True, watermarked=watermarked)
        show_image_in_notebook(image_path)
    else:
        print('Provide an image URL and try again.')

# Menu for user to choose image or video colorization
print("Choose an option:")
print("1. Colorize Video")
print("2. Colorize Image")
choice = input("Enter 1 or 2: ")

if choice == "1":
    # Video colorization
    source_url = input("Enter the video URL: ")
    render_factor = int(input("Enter the render factor (min: 5, max: 40): "))
    watermarked_input = input("Watermarked? (True/False): ").lower()
    watermarked = watermarked_input == "true"
    colorize_video(source_url, render_factor, watermarked)
elif choice == "2":
    # Image colorization
    source_url = input("Enter the image URL: ")
    render_factor = int(input("Enter the render factor (min: 7, max: 40): "))
    watermarked_input = input("Watermarked? (True/False): ").lower()
    watermarked = watermarked_input == "true"
    colorize_image(source_url, render_factor, watermarked)
else:
    print("Invalid choice. Please enter 1 or 2.")

image URL:https://www.alamy.com/the-indian-politician-mahatma-gandhi-in-marseilles-he-is-on-his-way-to-london-for-the-indian-round-table-conference-gandhi-was-nominated-several-times-for-the-nobel-peace-prize-during-his-lifetime-image247157689.html?imageid=B7A90904-7CD5-4C36-8F09-45C857FDF046&p=291620&pn=1&searchId=d187eb9e18db0eca74e3b21a8388b8d3&searchtype=0


https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQdXtfSj6xB2ybP8kif5R0vMnxOsCR4z36S7D74rlH6Ui9oj692UuNV_q1tk3VT81OL0ZQ&usqp=CAU
