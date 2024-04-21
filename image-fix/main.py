from PIL import Image, ImageFilter
import os


def resize_images_with_blurred_background(
    input_folder, output_folder, target_width, target_height
):
    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process each image in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            # Open the image
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)

            # Create a new image with the desired dimensions
            new_img = Image.new("RGB", (target_width, target_height), color="white")

            # Resize original image to fit within the new dimensions while maintaining aspect ratio
            img.thumbnail((target_width, target_height))

            # Calculate position to center the image
            x = (target_width - img.width) // 2
            y = (target_height - img.height) // 2

            # Create a blurred background
            blurred_background = img.filter(ImageFilter.GaussianBlur(15))
            blurred_background = blurred_background.resize(
                (target_width, target_height)
            )

            # Composite the blurred background and the original image
            new_img.paste(blurred_background, (0, 0))
            new_img.paste(img, (x, y), img.convert("RGBA"))

            # Save the new image
            new_img.save(os.path.join(output_folder, filename))


# Usage
resize_images_with_blurred_background("./input", "./output", 1920, 1080)
