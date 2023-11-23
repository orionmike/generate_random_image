
import time
from config import FILE_NAME_TEMPLATE
from libs.image import generate_random_image
from libs.utils import get_execute_time

import multiprocessing as mp


def main():
    start = time.time()
    
    active_core = round(mp.cpu_count()/2)

    print(active_core)

    file_list = [f'image-{f}.webp' for f in range(200)]
    # print(file_list)

    with mp.Pool(active_core) as pool:
        pool.map(generate_random_image, file_list)

    get_execute_time(start)


if __name__ == "__main__":
    main()
