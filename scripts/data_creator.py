from datetime import datetime
import numpy
import logging


if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S')
    now = datetime.now()
    current_date = now.strftime("%Y%m%d%H%M%S")
    logging.info("Creating file: ../files/normal_dist_sample_{}.csv".format(current_date))
    file = open("../files/normal_dist_sample_{}.csv".format(current_date), "w")
    for i in range(100):
        file.write(str(numpy.random.normal(0,1)) + "," + str(numpy.random.normal(0,1)) + "\n")

    file.close()