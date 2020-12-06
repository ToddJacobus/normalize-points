
def coordinates_are_valid(coordinates):
    """Simple validation function.  Returns True if both x and y values
    of the coordinate pair are within acceptable ranges of geographic
    latitude and longitude"""

    x, y = coordinates
    x_is_valid = -180 <= x <= 180
    y_is_valid = -90 <= y <= 90

    return x_is_valid and y_is_valid