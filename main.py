import getpass
import os
import random
import imageio
# import pyautogui
from PIL import ImageTk, Image
import tkinter as tk


def cls():
    """
    Commented out - bootleg "clear console" for Pycharm,
    use while writing, and switch to "os.system..." line when
    packing into .exe

    for getting coordinates:
    time.sleep(2)
    print(pyautogui.position())

    launch program, and move cursor to the simulated console window,
    after 2s you'll get coordinates to put as pyautogui.click() arguments
    :return:
    """

    # time.sleep(0.1)
    # pyautogui.click(x=778, y=832)
    # pyautogui.hotkey('ctrl', 'l')

    os.system('cls' if os.name == 'nt' else 'clear')


def choose_wallpaper():
    wallpaper_list = os.listdir()

    size = 960, 540

    while True:
        while True:
            img_name = random.choice(wallpaper_list)
            if img_name.endswith('.exe'):
                continue
            else:
                break

        # img_name = 'test.jpg'
        imgfile = imageio.imread(img_name)
        filename, file_extension = os.path.splitext(img_name)

        img_to_display = Image.open(img_name)
        Image.Image.thumbnail(img_to_display, size, Image.ANTIALIAS)

        root = tk.Tk()
        img_to_display_tk = ImageTk.PhotoImage(img_to_display)
        panel = tk.Label(root, image=img_to_display_tk)
        panel.pack()
        root.update()

        while True:
            decision = input("Do you like this wallpaper? (Enter - Yes/N - No)")
            if decision.casefold() == 'n':
                root.update()
                root.destroy()
                break
            elif decision.casefold() == '':
                imageio.imwrite(r'C:\Users\\' + getpass.getuser() + r'\Desktop\\WALLPAPER' + file_extension, imgfile)
                return
            cls()
        cls()


def main():
    choose_wallpaper()


if __name__ == '__main__':
    main()
