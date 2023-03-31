from abc import ABC, abstractmethod
from PIL import Image, ImageTk
import cv2
import time
import tkinter as tk


class MediaHandler(ABC):
    @abstractmethod
    def show(self, file_path, canvas, window, window_width, window_height):
        pass


class ImageHandler:
    def __init__(self, resize_image_func):
        self.resize_image_func = resize_image_func

    def show(self, file_path, canvas, window, width, height):

        try:
            if window is None or not isinstance(window, tk.Tk) or not window.winfo_exists():
                return

            image = Image.open(file_path)
            image = self.resize_image_func(image, width, height)
            img_object = ImageTk.PhotoImage(image)

            if hasattr(window, 'image'):
                del window.image

            canvas.delete("all")
            canvas.create_image(width // 2, height // 2, image=img_object)
            canvas.image = img_object
            window.update()
        except:
            print("Execution canceled by user")
            exit()


class VideoHandler:
    def __init__(self, resize_image_func):
        self.resize_image_func = resize_image_func

    def show(self, file_path, canvas, window, width, height):

        try:
            if window is None or not isinstance(window, tk.Tk) or not window.winfo_exists():
                return

            cap = cv2.VideoCapture(file_path)

            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                image = self.resize_image_func(image, width, height)

                if window.winfo_exists() == 0:  # Añade esta línea
                    break  # Añade esta línea

                img_object = ImageTk.PhotoImage(image)

                if hasattr(window, 'image'):
                    del window.image

                canvas.delete("all")
                canvas.create_image(width // 2, height // 2, image=img_object)
                canvas.image = img_object
                window.update()

            cap.release()

        except:
            print("Execution canceled by user")
            exit()
