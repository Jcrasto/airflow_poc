from datetime import datetime
import numpy


if __name__ == "__main__":
    now = datetime.now()
    current_date = now.strftime("%Y%m%d%H%M%S")
    file = open("../files/normal_dist_sample_{}.csv".format(current_date), "w")
    for i in range(100):
        file.write(str(numpy.random.normal(0,1)) + "," + str(numpy.random.normal(0,1)) + "\n")

    file.close()
    exit(99)