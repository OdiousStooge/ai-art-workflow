from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS


def get_exif_data(image_path):
    """Extract EXIF data from an image."""
    image = Image.open(image_path)
    exif_data = {}
    info = image._getexif()
    if info:
        for tag, value in info.items():
            tag_name = TAGS.get(tag, tag)
            exif_data[tag_name] = value
    return exif_data


def compare_user_comment(image_path1, image_path2):
    """Compare the UserComment EXIF property of two images."""
    exif_data1 = get_exif_data(image_path1)
    exif_data2 = get_exif_data(image_path2)

    user_comment1 = exif_data1.get("UserComment", "Not found")
    user_comment2 = exif_data2.get("UserComment", "Not found")

    print(f"UserComment of {image_path1}: {user_comment1}")
    print(f"UserComment of {image_path2}: {user_comment2}")

    if user_comment1 == user_comment2:
        print("The UserComment EXIF property is the same in both images.")
    else:
        print("The UserComment EXIF property is different in the two images.")


# Replace 'image1.jpg' and 'image2.jpg' with the paths to your images
compare_user_comment(
    "../image-fix/input/alchemyrefiner_alchemymagic_3_328d4bc8-93bb-4cdb-9aea-d1bd3e131c15_0.jpg",
    "../image-fix/input/5DFDF4D0B0C8A24CD108F180ACC79C183EDA541B4EEF4C4C6F2CC801A59EBC12.jpeg",
)
