"""
@file: generate_page.py

Update an HTML page with a path to generated compilation video.
"""

# Imports
import os

def update_html(video_path, html_path):
    """
    Update the HTML file to reference the stitched video.

    @params:
        video_path : path to the stitched video
        html_path  : path to the HTML file

    @returns:
        NONE
    """

    with open(html_path, 'r') as html_file_r:
        html_content = html_file_r.read()

    # Set new video source tags to be replaced in target html file
    video_src_tag = f'<source src="{video_path}" type="video/mp4">'
    updated_html_content = html_content.replace('<source src="" type="video/mp4">', video_src_tag)

    # Write the updated content to target html file
    with open(html_path, 'w') as html_file_w:
        html_file_w.write(updated_html_content)
    
    print(f"Updated file at: {html_path}")


def main():
    """main()"""

    # File Paths 
    stitched_video_path = r"D:\Dashcam Backup\September 5, 2022 (MINE)\stitched_video.mp4"
    html_file_path = r"C:\Users\deeps\OneDrive\Desktop\video_speed_up\Automated-Dashcam-Montages\src\frontend\index.html"

    update_html(stitched_video_path, html_file_path)


if __name__ == "__main__":
    main()