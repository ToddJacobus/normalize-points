from src.validators.validate_coordinates import coordinates_are_valid

def normalize_point(coordinates):
    if not coordinates_are_valid(coordinates):
        x, y = coordinates

        norm_degs_x = x - (int(x / 360) * 360)

        if norm_degs_x > 180: norm_degs_x = norm_degs_x - 360
        if norm_degs_x < -180: norm_degs_x = norm_degs_x + 360

        norm_degs_y = y - (int(y / 360) * 360)
        
        if 90< norm_degs_y <= 270: norm_degs_y = 180 - norm_degs_y
        if 270 < norm_degs_y <= 360: norm_degs_y = norm_degs_y - 360

        if -270 < norm_degs_y <= -90: norm_degs_y = -180 - norm_degs_y
        if -360 < norm_degs_y <= -270: norm_degs_y = norm_degs_y + 360

        return (norm_degs_x, norm_degs_y)