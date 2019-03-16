def can_stack(larger_box, smaller_box):
    """
    1. if smaller box area >= larger box area, return false
    2. Find smallest of larger area and largest of smaller area
    3. If Smallest of larger area >= largest of smaller area.
        a. if sm of la == la of sm and sm x == sm y: return false
            else: return true.
    :param larger_box: dict
    :param smaller_box: dict
    :return: True or False
    """
    if larger_box['area'] <= smaller_box['area']:
        return False
    largest_of_smaller = max(smaller_box['x'], smaller_box['y'], )
    smallest_of_larger = min(larger_box['x'], larger_box['y'], )
    if smallest_of_larger >= largest_of_smaller:
        if smallest_of_larger == largest_of_smaller and smaller_box['x'] == smaller_box['y']:
            return False
        return True
    return False


def get_areas(boxes):
    areas = []
    for box in boxes:
        for i in range(3):
            x, y, h = ((i + j) % 3 for j in range(3))
            areas.append({
                'x': box[x],
                'y': box[y],
                'height': box[h],
                'area': box[x] * box[y],
                'max_height': 0,
                'id': len(areas),
                'child': None
            })
    return sorted(areas, key=lambda element: element['area'], reverse=True)


def compute_heights(current_box_index, boxes):
    if boxes[current_box_index]['max_height'] != 0:
        return
    for i in range(current_box_index + 1, len(boxes)):
        stackable = can_stack(boxes[current_box_index], boxes[i])
        if stackable:
            compute_heights(i, boxes)
            if boxes[current_box_index]['max_height'] <= boxes[i]['max_height']:
                boxes[current_box_index]['max_height'] = boxes[i]['max_height'] + boxes[i]['height']
                boxes[current_box_index]['child'] = boxes[i]['id']


def find_height(boxes):
    areas = get_areas(boxes)

    for i in range(len(areas)):
        compute_heights(i, areas)

    for area in areas:
        print(area)

    root = max(areas, key=lambda box: box['max_height'])
    return root['height'] + root['max_height']


def main():
    inputs = [
        ((4, 6, 7), (1, 2, 3), (4, 5, 6), (10, 12, 32)),
        ((1, 2, 3), (4, 5, 6), (3, 4, 1))
    ]
    for boxes in inputs:
        max_height = find_height(boxes)
        print(max_height)


if __name__ == '__main__':
    main()
