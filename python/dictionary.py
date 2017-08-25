import collections
import random
import datetime
import sys

DataPoint = collections.namedtuple("DataPoint", "id x y temp quality")


# List function
def find_point_by_id_in_list(data_list, i):
    for record in data_list:
        if record.id == i:
            return i

    return None


def main():
    print("Creating data...", end=' ')
    sys.stdout.flush()

    data_list = []
    random.seed(0)
    for d_id in range(500000):
        x = random.randint(0, 1000)
        y = random.randint(0, 1000)
        temp = random.randint(-10, 50)
        quality = random.random()
        data_list.append(DataPoint(d_id, x, y, temp, quality))

    print('done')
    sys.stdout.flush()

    # reorder the list
    print("Reordering list...", end=' ')
    sys.stdout.flush()

    # randomly sort the list

    data_list.sort(key=lambda l: l.quality)

    print('done')
    sys.stdout.flush()

    # print(*data_list, sep='\n')
    print("Creating interesting Id's...", end=' ')

    interesting_ids = {random.randint(0, len(data_list)) for _ in range(0, 100)}
    print('done')
    sys.stdout.flush()


# ****** List

    print("Locating data in LIST...", end=' ')
    sys.stdout.flush()
    t0 = datetime.datetime.now()

    interesting_points = []
    for i in interesting_ids:
        pt = find_point_by_id_in_list(data_list, i)
        interesting_points.append(pt)

    t1 = datetime.datetime.now()
    print('done')
    sys.stdout.flush()
    dt_list = (t1 - t0).total_seconds()

    print('List time {}'.format(dt_list))


# ****** Dictionary

    print("Locating data in Dictionary...", end=' ')
    sys.stdout.flush()
    t3 = datetime.datetime.now()

    interesting_points.clear()
    print(data_list[0])
    data_dict = {d.id: d for d in data_list}


    print(data_dict[0])

    for d_id in interesting_ids:
        d = data_dict[d_id]
        interesting_points.append(d)

    t4 = datetime.datetime.now()
    print('done')
    sys.stdout.flush()
    dt_dict = (t4 - t3).total_seconds()

    print('Dictionary time {}'.format(dt_dict))


if __name__ == '__main__':
    main()
