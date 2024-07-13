# Spot Painting Recreation with Python Turtle

This project recreates Damien Hirst's famous Spot Paintings using Python's Turtle module. The recreation process involves extracting colors from an image of one of Hirst's paintings and then using those colors to create a similar spot painting programmatically.

## Project Structure

The project consists of two main files:

1. **color_extract.py**: Extracts colors from the reference painting image.
2. **main.py**: Uses the extracted colors to create a spot painting using the Turtle module.

## Dependencies

To run this project, you need the following Python libraries:
- `turtle`
- `colorgram.py`

You can install `colorgram.py` using pip:
```bash
pip install colorgram.py

# color_extract.py

This script extracts all colors from an image and prepares them for use in the spot painting. The script uses the colorgram module to achieve this.

## Usage

1. Ensure you have an image of Damien Hirst's Spot Painting saved locally.
2. The script will extract the colors from this image and save them in a format suitable for the `main.py` script.

# main.py

This script uses the Turtle module to draw spots on the canvas using the colors extracted by `color_extract.py`.

## Usage

1. Ensure you have the colors extracted and available in a list format.
2. The script will use the Turtle module to create a spot painting with these colors.

# How to Run

1. First, run the `color_extract.py` script to extract colors from your chosen image.
2. Use the extracted colors in `main.py` to draw the spots.
3. Execute `main.py` to see the recreated spot painting.

# References

- [Damien Hirst](https://www.damienhirst.com/) - Original Spot Painting Artist

# License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Feel free to adjust the paths, number of colors, and other parameters as needed for your specific use case.


