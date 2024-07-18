## Tile Tinkerer
I saw an interesting image and decided to re-create it, and then added some extra functionality.
### TileArt creates art by repeating a set mask a number of iterations and averaging the mask's color with the existing image's color.
## Usage
```sh
python ./main.py # Will output the help menu
# python ./main.py <mask1> <mask2> ...
python ./main.py \(0x0000ff,0xff0000\) \(0x0000ff,0xff0000\) # Example of how the program takes in hex color values
```

![Sample TileArt](https://raw.githubusercontent.com/Somebody32x2/TileArt/master/tileart_%5B000000%2C000080%2C0000ff%5D%2C%5B008000%2Cffffff%2C0080ff%5D%2C%5B00ff00%2C00ff80%2C00ffff%5D_x6.png)
