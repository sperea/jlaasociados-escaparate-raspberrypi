import os
import sys
import argparse
from media_viewer import MediaViewer

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Showcase Media Viewer. version 1.0. Run: %(prog)s. Written by Sergio Perea (https://sperea.es)")
    parser.add_argument("--t", type=int, default=5, help="Image viewing time expressed in seconds")
    parser.add_argument("--p", type=str, default="media", help="Specifies the path of the media files")
    parser.add_argument("--v", action='version', version='%(prog)s 1.0')
    parser.add_argument("--h", action='help', help="Show available options")

    args = parser.parse_args()

    script_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    media_folder = os.path.join(script_path, args.media_folder)

    if os.path.exists(media_folder):
        viewer = MediaViewer(media_folder, image_time=args.image_time)
    else:
        print("The 'media' folder is not in the same directory as the script.")