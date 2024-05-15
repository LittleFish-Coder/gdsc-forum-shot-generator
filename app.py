import streamlit as st
from PIL import Image
import io

# Set page config
st.set_page_config(
    page_title="GDSC-Forum shot generator",
    page_icon="🚀",
    layout="centered",
)

# Title
st.title("GDSC-Forum shot generator")
st.write("Upload your image")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display image
    st.image(uploaded_file, caption="Uploaded image", use_column_width=True)
    st.write("Processing...")

    # Process image
    background = Image.open("watermark.png")
    foreground = Image.open(uploaded_file)

    background_width, background_height = background.size
    foreground_width, foreground_height = foreground.size

    # Resize foreground image
    new_width = int(background_width)
    new_height = int(foreground_height * new_width / foreground_width)

    foreground = foreground.resize((new_width, new_height))

    # Center image
    padding = (background_height - new_height) // 2

    # Create new image
    new_image = Image.new("RGB", (background_width, background_height), (255, 255, 255))

    # Paste images
    new_image.paste(foreground, (0, padding))

    # add logo
    new_image.paste(background, (0, 0), background)

    # Display result
    st.image(new_image, caption="Result", use_column_width=True)

    # Download result
    st.markdown("### Download result")
    st.markdown("Click the button below to download the result.")

    # Create download link
    img_byte_arr = io.BytesIO()
    new_image.save(img_byte_arr, format="JPEG")
    img_byte_arr = img_byte_arr.getvalue()
    st.download_button(
        label="Download result",
        data=img_byte_arr,
        file_name="result.jpg",
        mime="image/jpeg",
    )
