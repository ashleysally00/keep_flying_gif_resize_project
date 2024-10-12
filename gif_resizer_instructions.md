# GIF Resizer Instructions<h1>🦋</h1>

This Python script allows you to resize GIF images while preserving their animated properties. Follow these steps to use the GIF resizer on your own images like I did on the example butterfly gif. If you have any problems, let me know! 

## Prerequisites

- Python 3.x (Python 3.6 or higher recommended)
- Pillow library

## Installation

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Install the Pillow library using pip:

   ```
   pip install Pillow
   ```

   Note: If you have multiple Python versions installed or if your system uses `python3` command, you might need to use `pip3` instead:

   ```
   pip3 install Pillow
   ```

   If you're unsure, try `pip --version` or `pip3 --version` to check which version of pip is associated with your Python 3 installation.

## Usage

1. Download the `gif_resizer.py` file from this repository.

2. Place the GIF you want to resize in the same directory as the `gif_resizer.py` file.

3. Open a terminal or command prompt and navigate to the directory containing the script and your GIF.

4. Run the script using the following command:

   ```
   python gif_resizer.py
   ```

   Note: If your system uses `python3` command for Python 3, use:

   ```
   python3 gif_resizer.py
   ```

5. The script will prompt you for the following information:
   - Input GIF filename
   - Output GIF filename
   - Desired width in pixels

6. After providing the required information, the script will resize your GIF and save it with the specified output filename.

## Example

```
$ python gif_resizer.py
Enter the input GIF filename: my_animation.gif
Enter the output GIF filename: resized_animation.gif
Enter the desired width in pixels: 300

Resized GIF saved as resized_animation.gif
New dimensions: 300x225
Original GIF size: 1024.50 KB
Resized GIF size: 512.25 KB
```

## Notes

- The script maintains the aspect ratio of the original GIF.
- The resized GIF will preserve the animation, including frame durations and disposal methods.
- Transparent GIFs are supported.
- There is no limit on the input GIF size, but larger GIFs will take longer to process.
- The script works with standard GIF color modes (typically RGB or indexed color).
- CMYK images are not supported, as GIFs don't typically use CMYK color mode.
- The script does not perform color mode conversions. It preserves the original color mode of the input GIF.

## Troubleshooting

If you encounter any issues:

1. Ensure you have the latest version of Pillow installed:
   ```
   pip install --upgrade Pillow
   ```
   or
   ```
   pip3 install --upgrade Pillow
   ```

2. Check that your input GIF is not corrupted and can be opened by other image viewers.

3. If you get a "file not found" error, make sure the input GIF is in the same directory as the script.

4. If your GIF appears in an unexpected color mode after resizing, check the color mode of your original GIF. This script does not convert between color modes.

For any other issues, please open an issue in this GitHub repository.

Happy GIF resizing! We hope this tool helps you create perfectly sized animated GIFs for all your projects.

