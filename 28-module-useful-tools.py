import random

feet_in_mile = 5280
metres_in_km = 1000
beatles = ["John Lennon", "Paul McCartney", "Geroge Harrison", "Ringo Starr"]


def get_file_ext(filename):
    return filename[filename.index(".") + 1 :]


def roll_die(num):
    return random.randint(1, num)
