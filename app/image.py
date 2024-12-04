import PIL
import streamlit as st
from PIL import Image, ImageDraw, ImageFont


def load_image(image_path):
    return Image.open(image_path).convert("RGBA")


def resize_image(image, max_width, max_height):
    """Resize an image to fit within max_width and max_height while maintaining aspect ratio."""
    aspect_ratio = image.width / image.height
    if aspect_ratio > max_width / max_height:
        new_width = max_width
        new_height = int(max_width / aspect_ratio)
    else:
        new_height = max_height
        new_width = int(max_height * aspect_ratio)
    return image.resize((new_width, new_height), Image.LANCZOS)


def center_image(image, canvas_width, canvas_height, x_offset=0, y_offset=0):
    """Center the image on the canvas with optional offsets."""
    centered_x = (canvas_width - image.width) // 2 + x_offset
    centered_y = (canvas_height - image.height) // 2 + y_offset
    return centered_x, centered_y


def generate_action(character1, character2, world, action):
    char1_img = load_image(f'library/characters/{character1}.jpg')
    char2_img = load_image(f'library/characters/{character2}.jpg')
    world_img = load_image(f'library/world/{world}.jpg')

    canvas_width, canvas_height = 800, 600
    canvas = Image.new('RGBA', (canvas_width, canvas_height), (255, 255, 255, 255))

    # Resize and center the environment
    resized_world = resize_image(world_img, canvas_width, canvas_height)
    canvas.paste(resized_world, (0, 0))

    # Resize characters
    char1_img = resize_image(char1_img, 200, 300)
    char2_img = resize_image(char2_img, 200, 300)

    if action == 'fight':
        char2_img_flipped = char2_img.transpose(Image.FLIP_LEFT_RIGHT)

        # Place characters facing each other
        x1, y1 = 100, canvas_height - char1_img.height - 50
        x2, y2 = canvas_width - char2_img_flipped.width - 100, canvas_height - char2_img_flipped.height - 50
        canvas.paste(char1_img, (x1, y1), char1_img)
        canvas.paste(char2_img_flipped, (x2, y2), char2_img_flipped)

        # Add action labels
        baaam_img = load_image('library/action/baaam.png')
        ouuuchh_img = load_image('library/action/pow.png')
        baaam_img = resize_image(baaam_img, 100, 50)
        ouuuchh_img = resize_image(ouuuchh_img, 100, 50)

        canvas.paste(baaam_img, (x1 + char1_img.width // 2 - 50, y1 - 70), baaam_img)
        canvas.paste(ouuuchh_img, (x2 + char2_img_flipped.width // 2 - 50, y2 - 70), ouuuchh_img)

    elif action == 'treasure_hunt':
        # Place characters side by side facing right
        x1, y1 = 100, canvas_height - char1_img.height - 50
        x2, y2 = x1 + char1_img.width + 50, canvas_height - char2_img.height - 50
        canvas.paste(char1_img, (x1, y1), char1_img)
        canvas.paste(char2_img, (x2, y2), char2_img)

        # Add treasure icon
        treasure_img = load_image('library/ending/treasure.png')
        treasure_img = resize_image(treasure_img, 100, 100)
        canvas.paste(treasure_img, (canvas_width - treasure_img.width - 50, canvas_height - treasure_img.height - 50), treasure_img)

    return canvas


def generate_end_image(character1, character2, environment, ending):
    char1_img = load_image(f'library/characters/{character1}.jpg')
    char2_img = load_image(f'library/characters/{character2}.jpg')
    env_img = load_image(f'library/world/{environment}.jpg')
    ending_img = load_image(f'library/ending/{ending}.jpg')

    canvas_width, canvas_height = 800, 600
    canvas = Image.new('RGBA', (canvas_width, canvas_height), (255, 255, 255, 255))

    # Resize and center the environment
    resized_env = resize_image(env_img, canvas_width, canvas_height)
    canvas.paste(resized_env, (0, 0))

    # Resize characters
    char1_img = resize_image(char1_img, 200, 300)
    char2_img = resize_image(char2_img, 200, 300)

    # Place characters facing each other
    x1, y1 = 100, canvas_height - char1_img.height - 50
    x2, y2 = canvas_width - char2_img.width - 100, canvas_height - char2_img.height - 50
    canvas.paste(char1_img, (x1, y1), char1_img)
    canvas.paste(char2_img, (x2, y2), char2_img)

    # Add "The End" icon
    ending_img = resize_image(ending_img, 200, 100)
    x_end, y_end = center_image(ending_img, canvas_width, canvas_height, y_offset=-200)
    canvas.paste(ending_img, (x_end, y_end), ending_img)

    return canvas


if __name__ == "__main__":
    char1 = 'Nael'
    char2 = 'Naim'
    world = 'Space'
    action = 'fight'
    ending = 'end'

    action_image = generate_action(char1, char2, world, action)
    end_image = generate_end_image(char1, char2, world, ending)

    action_image.show()
    end_image.show()
