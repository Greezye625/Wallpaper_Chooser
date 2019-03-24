# Wallpaper_Chooser
App that chooses a random Wallpaper for you

1. Pack it into an "*.exe" file (e.g. pyinstaller --onefile main.py), it needs to be just a single file
2. Drop it in the folder with your wallpapers (make sure there are just images, and app in the folder)
3. Create a shortcut

After launching, app will randomly choose a wallpaper for you, from images inside the folder. If you like it - hit [Enter] and it will
copy the file to your Desktop, from which you can easily set it as a wallpaper. If not, write "n" and hit[Enter] and it will choose another one.

I wrote this app for myself, to help in picking wallpaper from >1,5k images (as i don't want to use windows slideshow to cycle through them, 
just set one, use it, and then change it to another when i get bored)

future versions will include smaller executable (pyinstaller packs it into a 300mb file currently :/ ) and some form of setup, and configuration (so you can choose folder with images during config, and not have to drop "*.exe" into it and create a shortcut)
