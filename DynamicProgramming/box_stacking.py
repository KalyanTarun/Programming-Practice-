def get_areas(box):
    return (
        (box[2], box[0], box[1], box[0] * box[1]),
        (box[1], box[0], box[2], box[0] * box[2]),
        (box[0], box[1], box[2], box[1] * box[2])
    )


def get_all_areas(boxes):
    areas = []
    for box in boxes:
        areas.extend(get_areas(box))
    return sorted(areas, key=lambda element: element[3], reverse=True)


def find_height(boxes):
    areas = get_all_areas(boxes)
    for area in areas:
        print(area)




def main():
    boxes = (4, 6, 7), (1, 2, 3), (4, 5, 6), (10, 12, 32)
    find_height(boxes)


main()
