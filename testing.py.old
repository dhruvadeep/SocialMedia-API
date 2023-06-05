import tkinter as tk
import requests

# Create a Tkinter window
root = tk.Tk()
root.title("Social Media Feed")

# Create a header section
header = tk.Frame(root, bg='white', padx=10, pady=10)
header.pack(fill='x')

# Add a label to the header section
header_label = tk.Label(header, text='Social Media Feed', font=('Arial', 18, 'bold'))
header_label.pack()

# Create a canvas to hold the post frame
canvas = tk.Canvas(root, bg='white', highlightthickness=0)
canvas.pack(side='left', fill='both', expand=True)

# Create a scrollbar for the post frame
scrollbar = tk.Scrollbar(root, orient='vertical', command=canvas.yview)
scrollbar.pack(side='right', fill='y')

# Configure the canvas to use the scrollbar
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

# Create a frame to hold the posts
post_frame = tk.Frame(canvas, bg='white', padx=10, pady=10)
canvas.create_window((0, 0), window=post_frame, anchor='nw')

# Define the API endpoint to fetch posts
API_ENDPOINT = 'https://jsonplaceholder.typicode.com/posts'

# Define the number of posts to fetch per request
POSTS_PER_REQUEST = 10

# Define a variable to keep track of the current page number
current_page = 1

def fetch_posts():
    """
    Fetch posts from the API using the Fetch API.
    """
    global current_page
    # Send a GET request to the API endpoint with the current page number and the number of posts per request
    response = requests.get(f'{API_ENDPOINT}?_page={current_page}&_limit={POSTS_PER_REQUEST}')
    # Parse the response JSON and return the data
    return response.json()

def load_posts():
    """
    Load posts into the post frame.
    """
    global current_page
    # Fetch the posts from the API
    posts = fetch_posts()
    # Iterate over the posts and create a label for each one
    for post in posts:
        post_label = tk.Label(post_frame, text=post['title'], font=('Arial', 14))
        post_label.pack(fill='x', pady=10)
    # Increment the current page number
    current_page += 1

def on_scroll(event):
    """
    Load more posts when the user scrolls to the bottom of the post frame.
    """
    # Check if the user has scrolled to the bottom
    if canvas.yview()[1] == 1.0:
        # Load more posts
        load_posts()

# Bind the on_scroll function to the canvas's scrollbar
canvas.bind('<MouseWheel>', on_scroll)

# Load the initial posts
load_posts()

# Start the Tkinter event loop
root.mainloop()
