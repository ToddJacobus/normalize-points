
def coordinates_are_valid(coordinates, srid=4326):
    x, y = coordinates
    x_is_valid = -180 <= x <= 180
    y_is_valid = -90 <= y <= 90

    return x_is_valid and y_is_valid