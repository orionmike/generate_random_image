import random

from PIL import Image, ImageDraw, ImageOps

from config import (BG_FINISH, BG_START, FG_FINISH, FG_START,
                    HEIGHT, PATH_DIR_RESULT, SEGMENT_SIZE,
                    WIDTH, IND, logger)
from libs.color import get_random_color


def generate_random_image(file_name: str) -> None:

    try:
        background_color = get_random_color(FG_START, FG_FINISH)
        foreground_color = get_random_color(BG_START, BG_FINISH)

        with Image.new('RGB', (SEGMENT_SIZE*WIDTH, SEGMENT_SIZE*HEIGHT), background_color) as img:

            # print(SEGMENT_SIZE*WIDTH, SEGMENT_SIZE*HEIGHT)

            draw_image = ImageDraw.Draw(img)
            part = random.randint(6, 12)

            for _ in range(part):

                kx = random.randint(0, 6)
                ky = random.randint(0, 6)

                x1 = kx * SEGMENT_SIZE
                y1 = ky * SEGMENT_SIZE

                x2 = x1+(SEGMENT_SIZE*random.randint(1, 3))
                y2 = y1+(SEGMENT_SIZE*random.randint(1, 3))

                draw_image.rectangle((x1, y1, x2, y2), fill=foreground_color)

            img = ImageOps.expand(img, SEGMENT_SIZE, get_random_color(BG_START, BG_FINISH))
            img.save(PATH_DIR_RESULT / file_name)

        print(f"{IND} image generate: {file_name}")
    except Exception as e:
        error = f'generate_random_image -> error: {e}'
        print(error)
        logger.error(error)
