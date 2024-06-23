# Oklahoma Cooling Centers Python

[Oklahoma Cooling Centers](https://alex-code4okc.github.io/oklahoma_cooling_centers_python/)

Python project to generate webpage map of Oklahoma Cooling centers. 

Cool zones are taken from [OG&E's public PDF](https://www.oge.com/wps/wcm/connect/5fff4221-6696-4166-9129-f431fc5a424f/OGE-Website+updates+2024-Cool+Zones-v2.pdf?MOD=AJPERES&CVID=p0Yt3kc).

## Dependencies
* [Folium](https://github.com/python-visualization/folium)
* [Pandas](https://github.com/pandas-dev/pandas)

## Quickstart
```bash
# create virtual environment
python3 -m venv .venv

# activate virtual environment
source .venv/bin/activate

# install dependencies
python3 -m pip install -r requirements.txt

# run script
./make_map.py

# open map in browser
open ./docs/index.html

# deactivate virtual environment
deactivate
```

## Development
### Read PDF
* ImageMagick is a problem child for `pdftotree` on macOS. Run the following to use `gen_csv.py`:
```bash
# install imagemagick v6
brew uninstall imagemagick
brew install imagemagick@6
brew unlink imagemagick
brew link imagemagick@6 --force

# ~/.bashrc
export BREW_PREFIX=$(brew --prefix)
export MAGICK_HOME="$BREW_PREFIX/opt/imagemagick@6"
```
* Run `gen_csv.py` to generate `./csv/cooling_centers_2024.csv`

### Geocoding
* Setup a free Google Cloud Platform account and [setup the Geocoding API](https://developers.google.com/maps/documentation/geocoding/overview)
* Fill out `.env` with your API key
* Run `geocode.py` append `latitude` and `longitude` to `./csv/cooling_centers_2024.csv`

## TODO
* [Issues](https://github.com/alex-code4okc/oklahoma_cooling_centers_python/issues)
* Remove OG&E's Arkansas locations
  * Maybe keep Fort Smith as that's close to the border at least
* Open locations on map in [new tab](https://www.freecodecamp.org/news/how-to-open-a-link-in-a-new-tab/)
