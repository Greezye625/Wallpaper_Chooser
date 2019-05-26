import os
import random
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
    wallpaper_list = os.listdir(os.path.expanduser('~') + r'/Pictures/Wallpapers/')

    size = 960, 540

    cycled_throug_list = []

    while True:
        while True:
            img_name = random.choice(wallpaper_list)
            if img_name not in cycled_throug_list:
                break

        cycled_throug_list.append(img_name)

        img_to_display = Image.open(os.path.expanduser('~') + r'/Pictures/Wallpapers/' + img_name)
        Image.Image.thumbnail(img_to_display, size, Image.ANTIALIAS)

        root = tk.Tk()
        img_to_display_tk = ImageTk.PhotoImage(img_to_display)
        panel = tk.Label(root, image=img_to_display_tk)
        panel.pack()
        root.update()
        while True:
            decision = input("Do you like this wallpaper? (Y - Yes/Enter - No): ")
            if decision.casefold() == '':
                root.update()
                root.destroy()
                break
            elif decision.casefold() == 'y':
                os.system(r'''dconf write /org/cinnamon/desktop/background/picture-uri "'file:///home/greezye/Pictures/Wallpapers/{}'"'''.format(img_name))

                final_check = input("Is the wallpaper looking ok? (Y/n): ")

                if final_check.casefold() == 'y':
                    return
                else:
                    root.update()
                    root.destroy()
                    break
            cls()
        cls()


def main():
    choose_wallpaper()


if __name__ == '__main__':
    main()
