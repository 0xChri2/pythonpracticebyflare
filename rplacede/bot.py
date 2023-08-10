import praw
import requests
from PIL import Image
from io import BytesIO
import time

# Reddit API credentials
reddit = praw.Reddit(client_id='YOUR_CLIENT_ID',
                     client_secret='YOUR_CLIENT_SECRET',
                     user_agent='YOUR_USER_AGENT',
                     username='YOUR_USERNAME',
                     password='YOUR_PASSWORD')

# Place canvas size
canvas_width = 1000
canvas_height = 1000

# Target image URL
target_image_url = "https://place.army/overlay_target.png"

def get_target_image():
    response = requests.get(target_image_url)
    target_image = Image.open(BytesIO(response.content))
    return target_image

def convert_color(pixel):
    # Add your color conversion logic here if needed
    return pixel

def main():
    target_image = get_target_image()
    target_image = target_image.resize((canvas_width, canvas_height))

    # Flatten the image to a list of pixels
    pixel_list = [convert_color(pixel) for pixel in target_image.getdata()]

    for y in range(canvas_height):
        for x in range(canvas_width):
            pixel = pixel_list[y * canvas_width + x]
            r, g, b, a = pixel
            # Convert RGBA to RGB (ignore alpha channel)
            color_rgb = (r, g, b)
            # Post the pixel to Reddit r/place
            try:
                reddit.subreddit('place').draw(x, y, color_rgb)
                print(f"Pixel at ({x}, {y}) posted successfully!")
            except praw.exceptions.APIException as e:
                # Handle API rate limit or other exceptions
                print(f"Error posting pixel at ({x}, {y}): {e}")
            time.sleep(5)  # Sleep for 5 seconds between each pixel post

if __name__ == "__main__":
    main()
