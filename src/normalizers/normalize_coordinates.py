from src.validators.validate_coordinates import coordinates_are_valid

def normalize_point(coordinates):
    """Normalization function which converts degrees of a circle to 
    acceptable values for geographic, latitude and longitude."""
    
    if not coordinates_are_valid(coordinates):
        # Check if coordinates are valid.  If so, we can skip this step
        # and maybe save a little bit of time, especially if we need to
        # process many points.
        x, y = coordinates

        # Remove concentric, multiples of 360 degrees
        norm_degs_x = x - (int(x / 360) * 360)

        # Calculate geographic longitude based on hemisphere
        if norm_degs_x > 180: norm_degs_x = norm_degs_x - 360
        if norm_degs_x < -180: norm_degs_x = norm_degs_x + 360

        # Again, remove concentric, multiples of 360 degrees
        norm_degs_y = y - (int(y / 360) * 360)
        
        # Calculate geographic latitude based on quadrant
        if 90< norm_degs_y <= 270: norm_degs_y = 180 - norm_degs_y
        if 270 < norm_degs_y <= 360: norm_degs_y = norm_degs_y - 360

        if -270 < norm_degs_y <= -90: norm_degs_y = -180 - norm_degs_y
        if -360 < norm_degs_y <= -270: norm_degs_y = norm_degs_y + 360

        return (norm_degs_x, norm_degs_y)