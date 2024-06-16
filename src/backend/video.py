"""
@file: video.py
@directory: /Automated-Dashcam-Montages/src/backend/

The purpose of this file is to navigate through dashcam video backup
directories and retrieve all videos corresponding to a particular trip.
These clips will be stitched together to send to the frontend for display.

Further functionality includes video resolution scaling and compression to
create a more efficient automation experience.
"""

# Imports
import os
import sys
import moviepy.editor as moviepy


# Constants
BITRATE = "800k"                  # Bitrate used in compression and scaling functions
SCALING_RESOLUTION = (1280, 720)  # Downscaling resolution for compressiong and scaling functions


def list_subdirectories(base_directory):
    """
    Print out all folders available for access in Dascham Backup directory

    @params:
        base_directory      : reference to 'Dashcam Backup' directory
    """

    # Error handling for non existent base directory
    if not os.path.exists(base_directory):
        print(f"Base directory at {base_directory} does not exist.")
        return []

    # subdirectories = [directory for directory in os.listdir(base_directory) if os.path.isdir(os.path.join(base_directory, directory))]

    subdirectories = []

    for directory in os.listdir(base_directory):
        if os.path.isdir(os.path.join(base_directory, directory)):
            subdirectories.append(directory)

    print(f"Subdirectories available for selection in {base_directory}: {subdirectories}")

    return subdirectories


def navigate_to_folder(base_directory):
    """
    Navigate to the directory containing backups of dashcam footage

    @params:
        base_directory    : reference to 'Dashcam Backup' directory

    @returns:
        target_directory  : desired directory to pull video footage from
    """

    # Collect desired date stamp of folder
    user_directory_selection = input("Enter the date of the desired footage from: ")

    target_directory = os.path.join(base_directory, user_directory_selection)

    # Error Handling for invalid date stamp input
    if not os.path.exists(target_directory):
        print(f"Directory for date {user_directory_selection} does not exist.")
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

    # Accepted file extensions for compilation
    video_extensions = ('.mp4', '.MP4', '.avi', '.mov')

    video_files = [os.path.join(target_directory, file) for file in os.listdir(target_directory) if file.lower().endswith(video_extensions)]
    print("Extracted the following video files: " + str(video_files))

    all_files = [os.path.join(target_directory, file_generic) for file_generic in os.listdir(target_directory)]
    print("Extracted the following miscenallenous files: " + str(all_files))

    # # Retrieve all videos at the desired folder
    # file_list = os.listdir(target_directory)

    # # Iterate through file list and return list of all video files
    # for file in file_list:
    #     if file.endswith(video_extensions):
    #         video_files = [os.path.join(target_directory, file)]

    # Check for pre-existing compilation in target directory.
    if "stitched_video.mp4" in [os.path.basename(file) for file in video_files]:
        print("Montage video already exists in target directory.")
        return None

    # Empty directory or directory with no acceptable file extensions
    if not video_files:
        print(f"No video files found in directory: {target_directory}")
        return None

    return sorted(video_files)


def compress_and_scale_video(input_path, output_path):
    """
    Performs scaling and compression of individual video file for greater script efficiency

    @params:
        input_path      :  path to the original video file
        output_path     :  path to save the compressed and scaled video

    @returns:
        NONE
    """

    clip = moviepy.VideoFileClip(input_path)
    clip_resized = clip.resize(newsize=SCALING_RESOLUTION)

    clip_resized.write_videofile(output_path, codec='libx264', bitrate=BITRATE, preset='fast')


def compress_and_scale_wrapper(video_files):
    """
    Handler to manage scaling and compression of all retreived video files in extracted list

    @params:
        video_files         : list of all files found at target date stamped directory

    @returns:
        compressed_files    : list of paths to the compressed video files
    """

    compressed_files = []

    for video in video_files:
        input_path = video
        output_path = os.path.splitext(video)[0] + "_compressed.mp4"

        # Send indivual files to subfunction that performs scaling and compression
        compress_and_scale_video(input_path, output_path)
        compressed_files.append(output_path)

    return compressed_files


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

    # Use codec='libx264' and preset='ultrafast'
    compilation.write_videofile(output_path, codec='libx264', preset='ultrafast')


def main():
    """main()"""

    # Raw string references base directory of all backup dashcam footage
    base_directory = r"d:\Dashcam Backup"
    list_subdirectories(base_directory)

    target_directory = navigate_to_folder(base_directory)

    if target_directory:
        video_files = retrieve_video_files(target_directory)

        # User confirmation
        if video_files:
            user_stitch_confirmation = input("Please enter your confirmation to proceed. [y/n]")

            if user_stitch_confirmation.lower() == 'y':
                # Initiate scaling and compression procedure for all relevant video files
                compressed_files = compress_and_scale_wrapper(video_files)

                # Stitched video will be placed in same directory as utilized video files
                output_path = os.path.join(target_directory, "stitched_video.mp4")

                # Stitch all compressed files
                stitch_video_clips(compressed_files, output_path)
                print(f"Stitched video saved to: {output_path}")
            else:
                print("Terminating program.")
                sys.exit()


if __name__ == "__main__":
    main()
