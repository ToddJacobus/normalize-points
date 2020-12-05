from src.validators.validate_coordinates import coordinates_are_valid

def normalize_point(coordinates):
    if not coordinates_are_valid(coordinates):
        x, y = coordinates
        
        num_circles = int(x / 360)
        degs = num_circles * 360
        norm_degs = x - degs
        if norm_degs > 180: norm_degs = norm_degs - 360
        if norm_degs < -180: norm_degs = norm_degs + 360
        
        return norm_degs