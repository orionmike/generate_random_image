
from config import FILE_NAME_TEMPLATE
from libs.image import generate_random_image


def main():

    for index in range(10):

        filename = f"{FILE_NAME_TEMPLATE}-{str(index).zfill(3)}.webp"
        generate_random_image(filename)


if __name__ == "__main__":
    main()
