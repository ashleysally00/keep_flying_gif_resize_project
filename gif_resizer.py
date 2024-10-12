from PIL import Image
import os

def resize_gif_with_pillow(input_path, output_path, new_width):
    """Resizes a GIF to a new width while maintaining the aspect ratio."""
    with Image.open(input_path) as img:
        # Calculate new dimensions
        original_width, original_height = img.size
        aspect_ratio = original_width / original_height
        new_height = int(new_width / aspect_ratio)
        
        # Prepare for processing frames
        frames = []
        durations = []
        disposals = []

        # Process each frame in the GIF
        try:
            while True:
                # Store disposal method if available (if not, assume default of 2)
                disposal_method = img.info.get('disposal', 2)
                disposals.append(disposal_method)
                
                # Resize the frame
                frame = img.copy()
                frame = frame.resize((new_width, new_height), Image.LANCZOS)
                
                # Handle transparency if present
                if disposal_method == 2:  # Disposal method 2: clear to background
                    frame = frame.convert("RGBA")
                    if "transparency" in img.info:
                        transparency = img.info["transparency"]
                        frame.putalpha(frame.getchannel("A").point(lambda x: 0 if x == transparency else x))
                
                frames.append(frame)
                durations.append(img.info.get('duration', 100))  # Default to 100ms if duration not found
                
                # Move to next frame
                img.seek(img.tell() + 1)
        except EOFError:
            pass  # End of frames reached

        # Save the resized GIF with the correct parameters
        frames[0].save(
            output_path,
            save_all=True,
            append_images=frames[1:],
            optimize=False,
            duration=durations,
            disposal=disposals,
            loop=0  # Set to 0 for infinite loop
        )
    
    print(f"Resized GIF saved as {output_path}")
    print(f"New dimensions: {new_width}x{new_height}")

# Usage
input_gif = "Gif_Keep_Flying.gif"
output_gif = "improved_resized_Gif_Keep_Flying.gif"
new_width = 200  # Adjust this value to change the width

resize_gif_with_pillow(input_gif, output_gif, new_width)

# Print file sizes for comparison
original_size = os.path.getsize(input_gif) / 1024  # Size in KB
resized_size = os.path.getsize(output_gif) / 1024  # Size in KB
print(f"Original GIF size: {original_size:.2f} KB")
print(f"Resized GIF size: {resized_size:.2f} KB")

