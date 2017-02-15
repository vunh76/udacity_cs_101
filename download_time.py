# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

# print 2 ** 10      # one kilobit, kb
# print 2 ** 10 * 8  # one kilobyte, kB

# print 2 ** 20      # one megabit, Mb
# print 2 ** 20 * 8  # one megabyte, MB

# print 2 ** 30      # one gigabit, Gb
# print 2 ** 30 * 8  # one gigabyte, GB

# print 2 ** 40      # one terabit, Tb
# print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size
# is given in megabytes (MB).

def convert_seconds(seconds):
    round_seconds = int(seconds)
    fractions = seconds - round_seconds
    hours = round_seconds / 3600
    round_seconds = round_seconds - hours * 3600
    minutes = round_seconds / 60
    seconds = round_seconds - minutes * 60
    if fractions > 0:
        seconds = seconds + fractions
    result = ""
    if hours == 1:
        result = str(hours) + " hour"
    else:
        result = str(hours) + " hours"
    result = result + ", "
    if minutes == 1:
        result = result + str(minutes) + " minute"
    else:
        result = result + str(minutes) + " minutes"
    result = result + ", "
    if seconds == 1:
        result = result + str(seconds) + " second"
    else:
        result = result + str(seconds) + " seconds"
    return result


def download_time(file_size, file_unit, bandwidth, bandwidth_unit):
    units = 'kMGT'
    c = file_unit[0]
    index = units.find(c)
    file_size = file_size * 2 ** ((index + 1) * 10)
    c = file_unit[1]
    if c == "B":
        file_size = file_size * 8

    c = bandwidth_unit[0]
    index = units.find(c)
    bandwidth = bandwidth * 2 ** ((index + 1) * 10)
    c = bandwidth_unit[1]
    if c == "B":
        bandwidth = bandwidth * 8

    seconds = 1.0 * file_size / bandwidth
    return convert_seconds(seconds)


print download_time(1024, 'kB', 1, 'MB')
# >>> 0 hours, 0 minutes, 1 second

print download_time(1024, 'kB', 1, 'Mb')
# >>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13, 'GB', 5.6, 'MB')
# >>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13, 'GB', 5.6, 'Mb')
# >>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10, 'MB', 2, 'kB')
# >>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10, 'MB', 2, 'kb')
# >>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable


