import subprocess
import os
import glob


def convert_and_crop_landscape_to_portrait(input_folder, output_folder):
    # Ensure output directory exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Find all .mp4 files in the input folder
    input_files = glob.glob(os.path.join(input_folder, "*.mp4"))

    for input_file in input_files:
        filename = os.path.basename(input_file)
        output_file = os.path.join(output_folder, filename)

        # Target dimensions
        target_width = 608
        target_height = 1080

        # Calculate scale and crop values
        scale_height = target_height
        scale_width = int(scale_height * (1920 / 1080))
        crop_x = int((scale_width - target_width) / 2)

        # Construct and execute ffmpeg command
        ffmpeg_command = [
            "ffmpeg",
            "-i",
            input_file,
            "-vf",
            f"scale={scale_width}:{scale_height},crop={target_width}:{target_height}:{crop_x}:0",
            "-c:a",
            "copy",
            output_file,
        ]

        try:
            subprocess.run(ffmpeg_command, check=True)
            print(f"Converted {filename} and saved to {output_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error converting {filename}: {e}")


# Example usage:
# Make sure to replace 'path/to/input_folder' and 'path/to/output_folder' with your actual folder paths
# convert_and_crop_landscape_to_portrait('path/to/input_folder', 'path/to/output_folder')


# Example usage
convert_and_crop_landscape_to_portrait("tok_input/", "tok_output/")
