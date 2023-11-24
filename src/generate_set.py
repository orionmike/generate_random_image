
import time
from config import FILE_NAME_TEMPLATE
from libs.image import generate_random_image
from libs.utils import get_execute_time


def main():

    start = time.time()

    for index in range(24):
        ind = str(index+1).zfill(2)
        file_path = f"result_image/catalog/product-{ind}/product-{ind}.webp"

        generate_random_image(file_path, num=index+1)

    for index in range(24):
        ind = str(index+1).zfill(2)
        file_path = f"result_image/blog/post-{ind}/product-{ind}.webp"

        generate_random_image(file_path, num=index+1)

    get_execute_time(start)


if __name__ == "__main__":
    main()
