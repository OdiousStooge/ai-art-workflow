import os
from pytube import YouTube
from moviepy.editor import AudioFileClip


def download_and_convert_to_mp3(url, output_path):
    # Download video from YouTube
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True, file_extension="mp4").first()

    # Download and save the file
    output_file = video.download(output_path=output_path)

    # Extract audio and save as MP3
    audio_clip = AudioFileClip(output_file)
    mp3_file = output_file.replace(".mp4", ".mp3")
    audio_clip.write_audiofile(mp3_file)

    # Optionally, remove the original download (MP4 file)
    os.remove(output_file)

    return mp3_file


# Example usage
# url = "https://www.youtube.com/watch?v=9FWQmpn4oZ0&t=66s&ab_channel=DungeonSynth"
url = "https://www.youtube.com/watch?v=Eh9sFlQm51Q&ab_channel=TheDungeonSynthArchives"
output_path = "./output"
mp3_file = download_and_convert_to_mp3(url, output_path)
print(f"MP3 file saved as: {mp3_file}")
