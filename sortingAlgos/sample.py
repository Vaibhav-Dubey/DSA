def maximum_networks(speed, n, min_comps, speed_threshold):
    count = 0
    total_speed = 0
    comps = 0

    for i in range(n):
        total_speed += speed[i]
        comps += 1

        if comps >= min_comps and total_speed >= speed_threshold:
            count += 1
            total_speed = 0
            comps = 0

    return count

n = 6
speed = [5, 7, 9, 12, 10, 13]
speed_threshold = 15
min_comps = 2

print(maximum_networks(speed, n, min_comps, speed_threshold))