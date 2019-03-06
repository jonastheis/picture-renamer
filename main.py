#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import listdir, rename
from os.path import isfile, join
import PIL.Image

MY_PATH = "/Users/jonastheis/Desktop/Cambodia"

# find all wrong named images
#files = filter(lambda x: "iOS" in x and x.endswith(".jpg"), [f for f in listdir(MY_PATH) if isfile(join(MY_PATH, f))])
files = filter(lambda x: x.endswith(".jpg") or x.endswith(".JPG"), [f for f in listdir(MY_PATH) if isfile(join(MY_PATH, f))])


print files

for n in files:
    try:

        img = PIL.Image.open(join(MY_PATH, n))
        date_total = img._getexif()[306]

        date_string, time_string = date_total.split()

        time_string = time_string.replace(":", ".")
        date_string = date_string.replace(":", "-")

        # optional: add hours to time
        if False:
            to_add = 9  # change to time shift
            hour = int(time_string.split(".")[0])
            hour += to_add

            time_string = "" + str(hour) + time_string[2:]


        date_total = date_string + " " + time_string + ".jpg"

        rename(join(MY_PATH, n), join(MY_PATH, date_total))
        print date_total

    except KeyError:
        pass
