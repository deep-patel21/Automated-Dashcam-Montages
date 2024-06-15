"""
@file: video.py
@directory: /Automated-Dashcam-Montages/src/backend/

The purpose of this file is to navigate through dashcam video backup
directories and retrieve all videos corresponding to a particular trip.
These clips will be stitched together to send to the frontend for display.
"""

# Imports
import os
import moviepy.editor as moviepy


def navigate_to_folder(base_directory):
    """
    Navigate to the directory containing backups of dashcam footage

    @params:
        base_directory    : reference to 'Dashcam Backup' directory     - Required

    @returns:
        target_directory  : desired directory to pull video footage from
    """

    # Collect desired date stamp of folder
    user_date = input("Enter the date of the desired footage from: ")

    target_directory = os.path.join(base_directory, user_date)

    # Error Handling for invalid date stamp input
    if not os.path.exists(target_directory):
        print(f"Directory for date {user_date} does not exist.")
        return None

    return target_directory


def retrieve_video_files(target_directory):
    """
    Parse all video files in the target directory and return in a list

    @params:
        target_directory    : desired directory to pull video footage from

    @returns:
        video_files         : list of all videos at the desired directory
    """

    video_extensions = ('.mp4', '.MP4' '.avi', '.mov')

    video_files = [os.path.join(target_directory, file) for file in os.listdir(target_directory) if file.endswith(video_extensions)]

    print("Extracted the following files: " + str(video_files))

    # # Retrieve all videos at the desired folder
    # file_list = os.listdir(target_directory)

    # # Iterate through file list and return list of all video files
    # for file in file_list:
    #     if file.endswith(video_extensions):
    #         video_files = [os.path.join(target_directory, file)]

    if "stitched_video.mp4" in [os.path.basename(file) for file in video_files]:
        print("Montage video already exists in target directory.")
        return None

    if not video_files:
        print(f"No video files found in directory: {target_directory}")
        return None

    return sorted(video_files)


def stitch_video_clips(video_files, output_path):
    """
    Write a single video file as a compilation of all extracted video files

    @params:
        video_files     : list of all files found at target date stamped directory
        output_path     : location to store concatenated compilation video

    @returns:
        NONE
    """

    clips = [moviepy.VideoFileClip(file) for file in video_files]

    # for file in video_files:
    #     clips = moviepy.VideoFileClip(file)

    compilation = moviepy.concatenate_videoclips(clips)

    compilation.write_videofile(output_path, codec='libx264', preset='ultrafast')


def main():
    """main()"""

    base_directory = r"d:\Dashcam Backup"
    target_directory = navigate_to_folder(base_directory)

    if target_directory:
        video_files = retrieve_video_files(target_directory)

        if video_files:
            output_path = os.path.join(target_directory, "stitched_video.mp4")
            stitch_video_clips(video_files, output_path)
            print(f"Stitched video saved to: {output_path}")


if __name__ == "__main__":
    main()
