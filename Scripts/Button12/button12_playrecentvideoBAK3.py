import os
import subprocess
import ctypes
import heapq

def get_usb_drives():
    usb_drives = []
    drives = [f"{chr(drive)}:\\" for drive in range(65, 91) if ctypes.windll.kernel32.GetDriveTypeW(f"{chr(drive)}:\\") == 2]  # DriveType 2 is removable
    return drives

def find_two_most_recent_videos(usb_drive):
    recent_videos = []

    for root, dirs, files in os.walk(usb_drive):
        for file in files:
            if file.lower().endswith(('.mp4', '.mkv', '.avi', '.mov')):
                file_path = os.path.join(root, file)
                creation_time = os.path.getctime(file_path)
                if len(recent_videos) < 2:
                    heapq.heappush(recent_videos, (creation_time, file_path))
                else:
                    heapq.heappushpop(recent_videos, (creation_time, file_path))
    
    recent_videos.sort(reverse=True)  # Sort the videos by creation time in descending order
    return [video[1] for video in recent_videos]  # Return the file paths of the two most recent videos

def play_video(video_path):
    if video_path:
        try:
            # Provide the full path to the VLC executable
            vlc_path = r"C:\Program Files\VideoLAN\VLC\vlc.exe"
            subprocess.run([vlc_path, "--fullscreen", video_path])
        except Exception as e:
            print(f"Error playing video {video_path}: {e}")
    else:
        print("No video found to play.")

def main():
    usb_drives = get_usb_drives()
    if not usb_drives:
        print("No USB drives found.")
        return

    for usb in usb_drives:
        print(f"Searching in: {usb}")
        recent_videos = find_two_most_recent_videos(usb)
        if recent_videos:
            for video in recent_videos:
                print(f"Playing video: {video}")
                play_video(video)
        else:
            print("No video files found.")

if __name__ == "__main__":
    main()
