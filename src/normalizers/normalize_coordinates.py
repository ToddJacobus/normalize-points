from src.validators.validate_coordinates import coordinates_are_valid

def normalize_point(coordinates):
    if not coordinates_are_valid(coordinates):
        x, y = coordinates
        
        num_circles_x = int(x / 360)
        degs_x = num_circles_x * 360
        norm_degs_x = x - degs_x
        if norm_degs_x > 180: norm_degs_x = norm_degs_x - 360
        if norm_degs_x < -180: norm_degs_x = norm_degs_x + 360
        
        # num_circles_y = int(y / 90)
        # degs_y = num_circles_y * 90
        # norm_degs_y = y - degs_y
        # if 90 < norm_degs_y <= 270: norm_degs_y = 180 - norm_degs_y
        # if norm_degs_y > 270: norm_degs_y = 360 - norm_degs_y

        num_circles_y = int(y / 360)
        degs_y = num_circles_y * 360
        norm_degs_y = y - degs_y
        quadrant = int(norm_degs_y / 90)
        
        if 90 < norm_degs_y <= 180: norm_degs_y = 180 - norm_degs_y
        if 180 < norm_degs_y <= 270: norm_degs_y = 180 - norm_degs_y
        if 270 < norm_degs_y <= 360: norm_degs_y = norm_degs_y - 360

        if -180 < norm_degs_y <= -90: norm_degs_y = -180 - norm_degs_y
        if -270 < norm_degs_y <= -180: norm_degs_y = -180 - norm_degs_y
        if -360 < norm_degs_y <= -270: norm_degs_y = norm_degs_y + 360

        return (norm_degs_x, norm_degs_y)