# Import necessary libraries
import streamlit as st
from story import generate_story  # GPT-2 story generator
from image import combine_images  # Image composition logic
from PIL import Image

# Streamlit app setup
st.title("Comics Generator for Kids")

# Section 1: User Inputs
st.sidebar.header("Customize Your Story")
# Dropdown for character selection
characters = st.sidebar.multiselect("Select Characters", ["Venom", "Godzilla", "Nael", "Naim"], default=["Venom", "Godzilla"])

# Dropdown for environment selection
environment = st.sidebar.selectbox("Select Environment", ["Space", "Beach", "Forest", "Castle"])

# Dropdown for action selection
action = st.sidebar.selectbox("Select Action", ["Fight", "Treasure Hunt"])

# Dropdown for ending selection
ending = st.sidebar.selectbox("Select Ending", ["Happy", "Sad", "end"])

# Section 2: Generate Comics Button
if st.button("Generate"):
    # Step 1: Generate Story
    story = generate_story(characters, environment, action, ending)
    
    # Step 2: Compose Images
    images = combine_images(characters[0], characters[1], environment, action, ending)  # Returns a list of PIL images
    
    # Step 3: Display Results
    st.subheader("Your Generated Comic")
    for i in range(4):
        st.image(images[i], caption=story[i], use_column_width=True)
