from os import listdir, rename
from os.path import isfile, join
import PIL.Image
from datetime import datetime, timedelta

INPUT_DATE_FORMAT = '%Y:%m:%d %H:%M:%S'
OUTPUT_DATE_FORMAT = '%Y-%m-%d %H.%M.%S'


class Renamer:
    def __init__(self, path, time_shift):
        self.path = path
        self.time_shift = time_shift
        self.count = 0

    def start(self):
        # get all files in folder
        all_files = [f for f in listdir(self.path) if isfile(join(self.path, f))]
        # filter out only .jpgs
        picture_paths = filter(lambda x: x.endswith(".jpg") or x.endswith(".JPG"), all_files)

        for p in picture_paths:
            # catch all errors, e.g. no time in image encoded
            try:
                img = PIL.Image.open(join(self.path, p))
                date_total = img._getexif()[306]

                img_datetime = datetime.strptime(date_total, INPUT_DATE_FORMAT)

                # add timedelta if set
                if self.time_shift is not 0:
                    img_datetime = img_datetime + timedelta(hours=self.time_shift)

                img_datetime_string = img_datetime.strftime(OUTPUT_DATE_FORMAT) + ".jpg"
                rename(join(self.path, p), join(self.path, img_datetime_string))

                self.count += 1

            except KeyError:
                pass

        return self.count
