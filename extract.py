import datetime
import json
start_date = datetime.date(2016, 8, 1)
end_date = datetime.date(2017, 02, 12)

base_dir = "/Users/vunh/devel/tmp/"

while start_date < end_date:
    filename = "ActivityLog_" + start_date.strftime("%b_%d_%Y") + ".txt"
    filename = base_dir + filename
    f = open(filename, "r")
    for line in f:
        parts = line.split("\t")
        if parts[6] == "sorted_tutors":
            data = json.loads(parts[7])
            if "ranking" in data:
                print parts[4], ",".join(data["ranking"].keys())
            elif "routing_score" in data:
                print parts[4], ",".join(data["routing_score"].keys())

    f.close()
    start_date = start_date + datetime.timedelta(days=1)
