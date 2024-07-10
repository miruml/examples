# standard library imports
from datetime import datetime
import time

# 3rd party libraries
import pytz
import torch


def main():

    while True:
        print("Hello Zenus. We build things you love!")

        # check if cuda is available
        print("Is cuda available? :", end="")
        if torch.cuda.is_available():
            print("Yes")
        else:
            print("No")

        # print the current time
        timezone = pytz.timezone("America/Los_Angeles")
        print("The current time is: ", datetime.now(timezone))

        # wait for 5 seconds
        print("Sleeping for 5 seconds")
        time.sleep(5)


if __name__ == '__main__':
    main()