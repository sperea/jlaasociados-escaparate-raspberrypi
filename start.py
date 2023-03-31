import os
import sys
import argparse
from application.gui.media_viewer_gui import MediaViewerGUI 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Showcase Media Viewer. version 1.0. Run: %(prog)s. Written by Sergio Perea (https://sperea.es)")
    parser.add_argument("--t", type=int, default=2, help="Image viewing time expressed in seconds")
    parser.add_argument("--p", type=str, default="media", help="Specifies the path of the media files")
    parser.add_argument("--v", action='version', version='%(prog)s 1.0')
    parser.add_argument("--h", action='help', help="Show available options")

    args = parser.parse_args()

    script_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    media_folder = os.path.join(script_path, args.p)

    if os.path.exists(media_folder):
        print("Running with the following parameters:")
        print(f"Media folder: {args.p}")
        print(f"Image time: {args.t}")
        print("Press ESC to finish")
        viewer = MediaViewerGUI(args.p, image_time=args.t)
    else:
        print("The 'media' folder is not in the same directory as the script.")