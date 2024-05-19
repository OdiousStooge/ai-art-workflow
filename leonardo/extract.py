import os
import re
import json
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from util.leo import leo_get_user_info, leo_get_user_generations


"""
Can't figure out how to get around this, Civitai won't load Prompt/Negative
prompt without this but this is essentially throwaway metadata to match
the civitai Format
"""
TEMPLATE_METADATA = """ Steps: 37, Sampler: DPM++ 2M Karras, CFG scale: 3.5, Seed: 724438993, Size: 832x1216, Clip skip: 2, Created Date: 2024-05-19T00:56:22.4653576Z, Civitai resources: []"""


def extract_ids_from_filenames(folder_path):
    pattern = re.compile(r"alchemyrefiner_alchemymagic_\d+_([a-f0-9-]+)_\d+\.jpg")
    files_info = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        match = pattern.match(filename)
        if match:
            file_id = match.group(1)
            files_info.append(
                {"file_path": file_path, "file_name": filename, "file_id": file_id}
            )
    return files_info


def save_json_to_file(data, file_path):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Data saved to {file_path}")


def extract_upscaled_images(user_generations):
    upscaled_images = []
    for generation in user_generations.get("generations", []):
        for generated_image in generation.get("generated_images", []):
            for variation in generated_image.get(
                "generated_image_variation_generics", []
            ):
                if variation.get("transformType") == "UPSCALE":
                    upscaled_images.append(
                        {
                            "upscaled_id": variation.get("id"),
                            "generated_image_id": generated_image.get("id"),
                            "prompt": generation.get("prompt"),
                            "negativePrompt": generation.get("negativePrompt"),
                        }
                    )
    return upscaled_images


def match_ids(files_info, upscaled_images):
    matches = []
    for file_info in files_info:
        for img in upscaled_images:
            if file_info["file_id"] == img["upscaled_id"]:
                matches.append(
                    {
                        "file_path": file_info["file_path"],
                        "file_name": file_info["file_name"],
                        "upscaled_id": img["upscaled_id"],
                        "generated_image_id": img["generated_image_id"],
                        "prompt": img["prompt"],
                        "negativePrompt": img["negativePrompt"],
                    }
                )
    return matches, len(upscaled_images)


def update_exif_data(image_path, prompt, negative_prompt):
    try:
        img = Image.open(image_path)
        exif_dict = img.info.get("exif", None)
        if negative_prompt:
            user_comment = (
                f"{prompt}, Negative prompt: {negative_prompt} {TEMPLATE_METADATA}"
            )
        else:
            user_comment = f"{prompt} {TEMPLATE_METADATA}"

        # Encode the user comment in UTF-16 without BOM and add the UNICODE prefix
        user_comment_utf16 = "UNICODE\x00\x00".encode("ascii") + user_comment.encode(
            "utf-16-le"
        )

        exif = img.getexif()
        exif[37510] = user_comment_utf16  # 37510 is the EXIF tag for UserComment

        # Save the image with updated EXIF data
        img.save(image_path, exif=exif)
        print(f"Updated EXIF data for {image_path}")
    except Exception as e:
        print(f"Error updating EXIF data for {image_path}: {e}")


if __name__ == "__main__":
    # Fetch user info using leo_get_user_info
    user_info_response = leo_get_user_info()

    # Parse the response as JSON
    user_info = json.loads(user_info_response)

    # Unpack user_details.user.id from the first element in the user_details list
    user_details = user_info.get("user_details", [])
    if user_details and isinstance(user_details, list) and len(user_details) > 0:
        user_id = user_details[0].get("user", {}).get("id")
        print(f"User ID: {user_id}")

        # Fetch user generations using leo_get_user_generations if user_id is found
        user_generations_response = leo_get_user_generations(user_id)
        user_generations = json.loads(user_generations_response)

        # Define the path to save the user generations info
        user_generations_path = "data/userGenerations.json"

        # Save user generations to file
        save_json_to_file(user_generations, user_generations_path)

        # Extract upscaled images
        upscaled_images = extract_upscaled_images(user_generations)
        print(
            "Upscaled Images and their Associated Generated Image IDs:", upscaled_images
        )

        # Define the path to save the upscaled images info
        upscaled_images_path = "data/upscaledImages.json"

        # Save upscaled images to file
        save_json_to_file(upscaled_images, upscaled_images_path)
    else:
        user_id = None
        print("No user info found or data are not in the expected format.")

    # Define the path to save the user info
    user_info_path = "data/userInfo.json"

    # Save user info to file
    save_json_to_file(user_info, user_info_path)

    # Define the folder path for extracting IDs
    folder_path = "../image-fix/output/"

    # Extract IDs from filenames
    files_info = extract_ids_from_filenames(folder_path)

    # Print extracted IDs and their count
    extracted_ids = [file["file_id"] for file in files_info]

    # Match IDs from extracted_ids with upscaled_ids and print the result
    if user_id:
        matched_images, total_upscaled = match_ids(files_info, upscaled_images)
        print(
            f"Matched {len(matched_images)} of {len(extracted_ids)} out of {total_upscaled} upscaled images"
        )

        # Update EXIF data for matched images
        for match in matched_images:
            update_exif_data(
                match["file_path"], match["prompt"], match["negativePrompt"]
            )
