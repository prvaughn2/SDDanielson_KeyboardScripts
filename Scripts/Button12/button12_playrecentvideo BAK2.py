import os
import subprocess
import ctypes

def get_usb_drives():
    usb_drives = []
    drives = [f"{chr(drive)}:\\" for drive in range(65, 91) if ctypes.windll.kernel32.GetDriveTypeW(f"{chr(drive)}:\\") == 2]  # DriveType 2 is removable
    return drives

def find_most_recent_video(usb_drive):
    recent_video = None
    recent_time = 0

    for root, dirs, files in os.walk(usb_drive):
        for file in files:
            if file.lower().endswith(('.mp4', '.mkv', '.avi', '.mov')):
                file_path = os.path.join(root, file)
                creation_time = os.path.getctime(file_path)
                if creation_time > recent_time:
                    recent_time = creation_time
                    recent_video = file_path
    return recent_video

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
        most_recent_video = find_most_recent_video(usb)
        if most_recent_video:
            print(f"Most recent video found: {most_recent_video}")
            play_video(most_recent_video)
        else:
            print("No video files found.")

if __name__ == "__main__":
    main()
