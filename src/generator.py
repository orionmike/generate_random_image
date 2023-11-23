
import time
from config import FILE_NAME_TEMPLATE
from libs.image import generate_random_image
from libs.utils import get_execute_time


def main():

    start = time.time()

    for index in range(200):

        filename = f"{FILE_NAME_TEMPLATE}-{str(index).zfill(3)}.webp"
        generate_random_image(filename)

    get_execute_time(start)


if __name__ == "__main__":
    main()
