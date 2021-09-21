# fp-afm
Move around an atomic force microscopy scan in first person.
Unfortunately, only editor control work currently.
I am unsure if collisions are possible with the images from [http://gwyddion.net/](Gwyddion).
Probably it is possible by exporting from [http://gwyddion.net/](Gwyddion) to STL and then importing into Blender to create a scene.
Alternatively, collisions can be detected manually based on the image itself.

![Editor view of AFM height map.] Screenshot_01.png "Editor view of AFM height map."

## Prepare data
Export your data as a PNG from [http://gwyddion.net/](Gwyddion).
It is import that you do *not* check the `export as grayscale option`.
Instead just select all the options such that no scale bars are displayed.
I recommend working with the height data from contact mode as that will provide the smoothest surface to move on.

## Colored height maps
If you want colored height maps, you can export two files from [http://gwyddion.net/](Gwyddion).
The first is the default image as described above which will be grayscale.
Then you can change to another color scale and export again.
This time save the file identically except append *-color.png* to whatever your original stem was.
The script will detect this automatically and color the terrain appropriately.

## Installation
This is a very simple Python script that only depends on the [https://www.ursinaengine.org/](Ursina game engine).
You can use `pip3 -r requirements.txt` to install required packages.