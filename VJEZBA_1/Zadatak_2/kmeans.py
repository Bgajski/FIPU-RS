MAX_ITERATIONS = 100

def distance_squared(point, center):
    dx = point[0] - center[0]
    dy = point[1] - center[1]
    return dx * dx + dy * dy

def nearest_center(point, centers):
    nearest_index = 0
    nearest_distance = distance_squared(point, centers[0])

    for index in range(1, len(centers)):
        distance = distance_squared(point, centers[index])
        if distance < nearest_distance:
            nearest_index = index
            nearest_distance = distance

    return nearest_index, nearest_distance

def choose_starting_centers(points, k):
    centers = [points[0]]

    while len(centers) < k:
        farthest_point = points[0]
        farthest_distance = 0

        for point in points:
            _, distance = nearest_center(point, centers)
            if distance > farthest_distance:
                farthest_point = point
                farthest_distance = distance

        centers.append(farthest_point)

    return centers

def kmeans(points, k):
    centers = choose_starting_centers(points, k)

    for _ in range(MAX_ITERATIONS):
        groups = [[] for _ in centers]

        for point in points:
            index, _ = nearest_center(point, centers)
            groups[index].append(point)

        new_centers = []
        for index, group in enumerate(groups):
            if not group:
                new_centers.append(centers[index])
                continue

            sum_x = 0
            sum_y = 0
            for x, y in group:
                sum_x += x
                sum_y += y

            new_centers.append((sum_x / len(group), sum_y / len(group)))

        if new_centers == centers:
            break

        centers = new_centers

    labels = []
    for point in points:
        index, _ = nearest_center(point, centers)
        labels.append(index)

    return labels, centers