from pytube import YouTube
import os
import subprocess

def get_video_quality_streams(yt):
    video_audio_streams = yt.streams.filter(only_video=True, file_extension='mp4')
    print("Available video quality options:")
    for i, stream in enumerate(video_audio_streams):
        print(f"{i + 1}. {stream.resolution} - {stream.mime_type}")

    while True:
        try:
            choice = int(input("Enter the number for the desired video quality: "))
            if 1 <= choice <= len(video_audio_streams):
                return video_audio_streams[choice - 1]
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def download_video_audio(video_stream, video_filename, audio_stream, audio_filename):
    print(f"Downloading video in {video_stream.resolution} with audio...")
    video_stream.download(output_path="downloads", filename=video_filename)
    audio_stream.download(output_path="downloads", filename=audio_filename)

def merge_video_audio(video_filename, audio_filename, output_filename):
    print("Merging video and audio...")
    subprocess.run(['ffmpeg', '-i', f'downloads/{video_filename}.mp4', '-i', f'downloads/{audio_filename}.mp4', '-c', 'copy', f'downloads/{output_filename}.mp4'])

def main():
    video_url = input("Enter the YouTube video URL: ")

    try:
        yt = YouTube(video_url)
        video_stream = get_video_quality_streams(yt)
        audio_stream = yt.streams.filter(only_audio=True).first()

        video_filename = "video"
        audio_filename = "audio"
        output_filename = "video_with_audio"

        download_video_audio(video_stream, video_filename, audio_stream, audio_filename)
        merge_video_audio(video_filename, audio_filename, output_filename)

        print("Video with audio downloaded successfully!")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()
