import os
import os.path
import tkinter as tk
from PIL import Image, ImageTk
import time
from lib.media_handler import ImageHandler, VideoHandler
from extensions import ImageExtensions, VideoExtensions

class MediaViewer:
    def __init__(self, media_folder, image_time=2):
        self.media_folder = media_folder
        self.image_time = image_time
        self.window = tk.Tk()
        self.window.title("Visor de imágenes y videos")
        self.window.attributes("-fullscreen", True)
        self.window_width = self.window.winfo_screenwidth()
        self.window_height = self.window.winfo_screenheight()

        self.canvas = tk.Canvas(self.window, width=self.window_width, height=self.window_height, bg="black")
        self.canvas.pack()

        self.image_handler = ImageHandler(self.resize_image)
        self.video_handler = VideoHandler(self.resize_image)

        self.window.bind("<Escape>", self.exit_program)
        self.window.after(0, self.show_media)
        #self.window.after(self.image_time * 1000, self.show_media)
        self.window_open = True 
        self.window.mainloop()
        
    def get_file_extension(self, file_path):
        _, file_extension = os.path.splitext(file_path)
        return file_extension

    def resize_image(self, image, max_width, max_height):
        width_ratio = max_width / image.width
        height_ratio = max_height / image.height
        min_ratio = min(width_ratio, height_ratio)

        new_width = int(image.width * min_ratio)
        new_height = int(image.height * min_ratio)

        return image.resize((new_width, new_height), Image.ANTIALIAS)

    def show_image(self, image_path):
        image = Image.open(image_path)
        image = self.resize_image(image, self.window_width, self.window_height)
        img_object = ImageTk.PhotoImage(image)

        self.canvas.delete("all")
        self.canvas.create_image(self.window_width // 2, self.window_height // 2, image=img_object, anchor=tk.CENTER)
        self.window.update()

    def show_video(self, video_path):
        video = cv2.VideoCapture(video_path)

        while True:
            ret, frame = video.read()
            if not ret:
                break

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            image = Image.fromarray(frame)
            image = self.resize_image(image, self.winfolder_pathdow_width, self.window_height)
            img_object = ImageTk.PhotoImage(image)

            self.canvas.delete("all")
            self.canvas.create_image(self.window_width // 2, self.window_height // 2, image=img_object, anchor=tk.CENTER)
            self.window.update()

            time.sleep(0.03)

        video.release()

    def exit_program(self, event):
        self.window.destroy()

    def get_media_files(self):
        media_files = []

        for root, _, files in os.walk(self.media_folder):
            for file in files:
                file_path = os.path.join(root, file)
                file_extension = self.get_file_extension(file_path)

                if ImageExtensions.contains(file_extension) or VideoExtensions.contains(file_extension):
                    media_files.append(file_path)

        return media_files

    def show_media(self):
        media_files = self.get_media_files()
        self.index = 0
        self.window_open = True

        while self.window_open:
            if self.index >= len(media_files):
                self.index = 0

            file_path = media_files[self.index]
            file_extension = self.get_file_extension(file_path)

            if ImageExtensions.contains(file_extension):
                self.image_handler.show(file_path, self.canvas, self.window, self.window_width, self.window_height)
            elif VideoExtensions.contains(file_extension):
                self.video_handler.show(file_path, self.canvas, self.window, self.window_width, self.window_height, self.window_open)

            self.index += 1
            
            self.window.after(self.image_time * 1000, self.window.update())