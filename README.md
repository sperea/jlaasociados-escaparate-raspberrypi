## Showcase Media Viewer

Showcase Media Viewer is a Python application for displaying images and videos in a loop. It has been developed as part of a digital signage solution for a retail store, but it can be used in any other context where you need to display media files continuously.

### Features
- Display images and videos in a loop.
- Resize images and videos to fit a window.
- Support for JPEG, PNG, and BMP images.
- Support for MP4 videos (H.264 codec).
- Configurable time for displaying each media file.

### Installation

Media Viewer requires Python 3.11.2.

To install the Showcase Media Viewer for Raspberry Pi, you can follow these steps:

- Make sure your Raspberry Pi is up to date by running sudo apt-get update and sudo apt-get upgrade.

- Install Python 3 if it is not already installed by running sudo apt-get install python3.

- Clone the repository by running git clone https://github.com/sperea/showcase-media-viewer-raspberrypi.git.

- Change into the cloned directory by running cd showcase-media-viewer-raspberrypi.

- Install the required Python packages by running sudo pip3 install -r requirements.txt.

- Run the program by running python3 start.py.

Note that you may need to modify the media_folder variable in start.py to point to the location of your media files. You can also use the --t flag to adjust the amount of time each image is displayed. Use the --h flag for more information on available options.

### Usage

To start Media Viewer, run the following command:

``
python start.py --p /path/to/media --t 5 
``

* `--p`: the path to the directory containing the media files.
* `--t`: the time (in seconds) for displaying each image. Default is 5 seconds.
* `--h`: show help
* `--h`: show version

*Press Esc to exit the application.*

### To start the Showcase Media Viewer on a Raspberry Pi connected to a TV 

To start the Showcase Media Viewer on a Raspberry Pi connected to a TV when the Pi boots up, you can use the following steps:

1. Copy the start.py file and the media_viewer folder to a desired location on the Raspberry Pi.
2. Open the terminal and navigate to the location where you saved the files.
3. Type sudo nano /etc/xdg/lxsession/LXDE-pi/autostart to open the autostart file for editing.
4. Add the following line to the end of the file:

``
@lxterminal --command="python3 /path/to/start.py"
``

Be sure to replace /path/to/start.py with the actual path to the start.py file on your Raspberry Pi.

5. Press Ctrl + O to save the file, then press Ctrl + X to exit the editor.

6. Reboot the Raspberry Pi, and the Showcase Media Viewer should start automatically.

With these steps, the Showcase Media Viewer will be launched automatically every time the Raspberry Pi starts up, allowing it to display images and videos on the connected TV without requiring any manual intervention.

## License

Media Viewer is licensed under the GNU General Public License v3.0. See the LICENSE file for more information.