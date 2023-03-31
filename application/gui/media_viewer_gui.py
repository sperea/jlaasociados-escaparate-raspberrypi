import tkinter as tk
from PIL import ImageTk
from PIL import Image
import time
import cv2
from application.controller.media_controller import MediaController
from application.controller.media_controller import VideoExtensions
from application.controller.media_controller import ImageExtensions

class MediaViewerGUI:
    def __init__(self, media_folder, image_time=2):
        self.controller = MediaController(media_folder, image_time)
        self.window = tk.Tk()
        self.window.title("Visor de imágenes y videos")
        self.window.attributes("-fullscreen", True)
        self.window_width = self.window.winfo_screenwidth()
        self.window_height = self.window.winfo_screenheight()

        self.canvas = tk.Canvas(self.window, width=self.window_width, height=self.window_height, bg="black")
        self.canvas.pack()

        self.window.bind("<Escape>", self.on_escape_key_pressed)
        self.window.after(0, self.show_media)
        self.window_open = True
        self.window.mainloop()

    def exit_program(self, event):
            self.window_open = False
            self.window.destroy()

    def on_escape_key_pressed(self, event):
        self.exit_program(event)

    def show_media(self):
        media_files = self.controller.get_media_files()
        self.index = 0
        self.window_open = True

        while self.window_open:
            if self.index >= len(media_files):
                self.index = 0

            file_path = media_files[self.index]
            file_extension = self.controller.get_file_extension(file_path)

            if ImageExtensions.contains(file_extension):
                self.show_image(file_path)
            elif VideoExtensions.contains(file_extension):
                self.show_video(file_path)

            self.index += 1
            if self.window_open:
                self.window.after(self.controller.image_time * 1000, self.window.update())

    def resize_image(self, image, max_width, max_height):
        width_ratio = max_width / image.width
        height_ratio = max_height / image.height
        min_ratio = min(width_ratio, height_ratio)

        new_width = int(image.width * min_ratio)
        new_height = int(image.height * min_ratio)

        return image.resize((new_width, new_height), Image.LANCZOS)

    def show_image(self, image_path):
        image = Image.open(image_path)
        image = self.controller.resize_image(image, self.window_width, self.window_height)
        self.img_object = ImageTk.PhotoImage(image)
        self.canvas.delete("all")
        
        x_position = (self.window_width - image.width) // 2
        y_position = (self.window_height - image.height) // 2

        self.canvas.create_image(x_position, y_position, image=self.img_object, anchor=tk.NW)
        self.window.update()


    def show_video(self, video_path):
        video = cv2.VideoCapture(video_path)

        while True:
            ret, frame = video.read()
            if not ret:
                break

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            image = Image.fromarray(frame)
            image = self.controller.resize_image(image, self.window_width, self.window_height)
            self.img_object = ImageTk.PhotoImage(image)

            self.canvas.delete("all")

            x_position = (self.window_width - image.width) // 2
            y_position = (self.window_height - image.height) // 2

            self.canvas.create_image(x_position, y_position, image=self.img_object, anchor=tk.NW)
            self.window.update()

            time.sleep(0.03)

        video.release()