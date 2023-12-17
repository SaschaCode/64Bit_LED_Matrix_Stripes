from PIL import Image

def transform_to_colored_bitmap(input_image_path, output_image_path):
    # Open the input image
    original_image = Image.open(input_image_path)

    # Resize the image to 64x64 pixels
    resized_image = original_image.resize((64, 64))

    # Convert the image to RGB mode
    rgb_image = resized_image.convert('RGB')

    # Save the colored bitmap image
    rgb_image.save(output_image_path)

def transform_to_pixel_art(input_image_path, output_image_path):
    # Open the input image
    original_image = Image.open(input_image_path)

    # Resize the image to 64x64 pixels using nearest-neighbor interpolation
    pixel_art_image = original_image.resize((64, 64), Image.NEAREST)

    # Save the pixel art image
    pixel_art_image.save(output_image_path)

if __name__ == "__main__":
    input_path = "D:/Github/64Bit_LED_Matrix_Stripes/Pics/sr256b49a296aaws3.png"  # Change this to the path of your input image
    output_path_orig = "D:/Github/64Bit_LED_Matrix_Stripes/Pics/output_colored_bitmap_orig.bmp"  # Change this to the desired output path
    output_path_pixel = "D:/Github/64Bit_LED_Matrix_Stripes/Pics/output_colored_bitmap_pixel.bmp"  # Change this to the desired output path

    transform_to_colored_bitmap(input_path, output_path_orig)
    transform_to_pixel_art(input_path, output_path_pixel)
