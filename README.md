# ASCII-Image-Generator
### Image to ASCII generator following Robert Heaton's project idea

## Usage
The interface is command line based. The program will prompt for an image in it's repository, then map the brightness using the user's selected method of mapping. The methods available are as follows:

#### Average of RGB values
Will sum the values for the red, green and blue components of each pixel, then divide by three to find the average brightness.

#### Brighness
Will average the brightest and dimmest of the RGB components for each pixel

#### Luminosity - Default
Humans percieve more green light than red or blue. This mode corrects the luminosity for this, using the sum of (0.21 * Red) + (0.72 * Green) + (0.07 * Blue)

After the mode is selected, an ASCII representation of the image will apear!

## Limitations
But alas, there are of course limitations. The main one is size: A puny command line cannot handle the amount of ASCII characters required to display large images in their original glory, so resizing the images is a must. Because of this, detail of the image is lost. To fix this, I would like to add .txt file output. 

## Updates & Upgrades
a simple list of things I would like to add:
* .txt file output for a little more size.
* video support
* a color output mode 

## Credits
I followed the guidlines set down by Robert Heaton in his guide for this project, which can [be found here](https://robertheaton.com/2018/06/12/programming-projects-for-advanced-beginners-ascii-art/)
