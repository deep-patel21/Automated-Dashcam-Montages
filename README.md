# Automated Dashcam Montages
Automation project to simplify the process of creating road trip timelapse montages and dashcam footage organization.

## Workflow Summary

### video.py
1. **List Subdirectories:** Lists all available subdirectories selectable for compilation in my base Dashcam Backup folder.
2. **Navigate to Folder:** Sets the target folder as selected by the user for a particular date of Dashcam footage.
3. **Retrieve Video Files:** Extract all video files in the target folder and return them as a list.
4. **Compress and Scale Videos:** Iterate through the video file list, compressing and scaling each video file for efficiency.
5. **Stitch Video Clips:** Stitch the compressed video files into one stiched_video.mp4 file for timelapse viewing.

### update_html.py
1. **Generate Video List:** Scans the directory for available stitched videos and generates a list of compilation videos.
2. **Update HTML Content:** Updates the HTML template with the list of available videos, including video thumbnails and links. (Coming Soon...)

### index.html
1. **Speed Adjustment:** Adds a field to manipulate video speed. Will later be changed to button presets.
2. **Account Management:** Allows users to create and manage a personal library of their road trip timelapses. (Coming soon...)

## Upcoming Improvements 
- **Error Handling:** Adding additional error handling to manage unexpected situations.
- **Graphical User Interface:** Creating a webpage for users to utilize functionality by uploading their own video clips.
- **Command-Line Interface:** Incorporating 'argparse' argument parser for higher degree of control on script executions.
- **Audio Processing:** Enabling users to handle footage audio, including muting, or replacing audio with copyright-free music.
- **Automated Script Processing:** Executing script automatically when new road trip footage files are uploaded to base directory.

