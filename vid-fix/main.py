import ffmpeg
import os


def resize_and_crop_video(input_path, output_path):
    # Probe video to get its width and height
    probe = ffmpeg.probe(input_path)
    video_stream = next(
        (stream for stream in probe["streams"] if stream["codec_type"] == "video"), None
    )
    width = int(video_stream["width"])
    height = int(video_stream["height"])

    # Calculate scaling factor to maintain aspect ratio
    aspect_ratio = width / height
    target_aspect_ratio = 1920 / 1080

    if aspect_ratio > target_aspect_ratio:
        # Video is wider than target, calculate new dimensions
        new_height = 1080
        new_width = int(new_height * aspect_ratio)
    else:
        # Video is taller than target, calculate new dimensions
        new_width = 1920
        new_height = int(new_width / aspect_ratio)

    # Calculate cropping to center the video
    x_crop = max(0, new_width - 1920) // 2
    y_crop = max(0, new_height - 1080) // 2

    # Resize and crop using ffmpeg
    (
        ffmpeg.input(input_path)
        .filter("scale", new_width, new_height)
        .filter("crop", 1920, 1080, x_crop, y_crop)
        .output(output_path)
        .run(overwrite_output=True)
    )


def process_folder(input_folder, output_folder):
    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".mp4"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            print(f"Processing {filename}...")
            resize_and_crop_video(input_path, output_path)
            print(f"{filename} processed successfully.")


# Example usage
input_folder = "input/"
output_folder = "output/"
process_folder(input_folder, output_folder)
