## Showcase Media Viewer

Showcase Media Viewer is a Python application for displaying images and videos in a loop. It has been developed as part of a digital signage solution for a retail store, but it can be used in any other context where you need to display media files continuously.

### Features
- Display images and videos in a loop.
- Resize images and videos to fit a window.
- Support for JPEG, PNG, and BMP images.
- Support for MP4 videos (H.264 codec).
- Configurable time for displaying each media file.

### Installation

Media Viewer requires Python 3.11.2 or higher and the following Python packages:

pillow
opencv-python-headless
numpy

You can install these dependencies with the following command:

``
pip install -r requirements.txt
``

### Usage

To start Media Viewer, run the following command:

``
python start.py --media-dir /path/to/media --image-time 5 --video-time 10


* `--media-dir`: the path to the directory containing the media files.
* `--image-time`: the time (in seconds) for displaying each image. Default is 5 seconds.
/help: show help

*Press Esc to exit the application.*

## License

Media Viewer is licensed under the GNU General Public License v3.0. See the LICENSE file for more information.