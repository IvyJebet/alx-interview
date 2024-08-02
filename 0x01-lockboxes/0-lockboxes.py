#!/usr/bin/python3
"""Solves the puzzle involving unlocking all the boxes."""


def look_next_opened_box(opened_boxes):
    """Searches for the next box that has been opened.
    
    Args:
        opened_boxes (dict): A dictionary tracking the status of opened boxes.
        
    Returns:
        list: The keys contained in the next opened box, or None if no such box exists.
    """
    for index, box in opened_boxes.items():
        if box.get('status') == 'opened':
            box['status'] = 'opened/checked'
            return box.get('keys')
    return None


def canUnlockAll(boxes):
    """Determines if it is possible to open all the boxes.
    
    Args:
        boxes (list): A list where each element is a list of keys for other boxes.
        
    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if len(boxes) <= 1 or boxes == [[]]:
        return True

    aux = {}
    while True:
        if len(aux) == 0:
            aux[0] = {
                'status': 'opened',
                'keys': boxes[0],
            }
        keys = look_next_opened_box(aux)
        if keys:
            for key in keys:
                if aux.get(key) and aux.get(key).get('status') == 'opened/checked':
                    continue
                aux[key] = {
                    'status': 'opened',
                    'keys': boxes[key]
                }
        elif 'opened' in [box.get('status') for box in aux.values()]:
            continue
        elif len(aux) == len(boxes):
            break
        else:
            return False

    return len(aux) == len(boxes)


def main():
    """Main function to test the ability to unlock all boxes."""
    canUnlockAll([[]])


if __name__ == '__main__':
    main()
