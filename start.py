import os
import sys
import argparse
from media_viewer import MediaViewer

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Visor de imágenes y videos")
    parser.add_argument("--image-time", type=int, default=5, help="Tiempo de visualización de imágenes en segundos")
    args = parser.parse_args()

    script_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    media_folder = os.path.join(script_path, "media")

    if os.path.exists(media_folder):
        viewer = MediaViewer(media_folder, image_time=args.image_time)
    else:
        print("The 'media' folder is not in the same directory as the script.")