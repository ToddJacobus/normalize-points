from unittest import TestCase

from src.normalizers.normalize_coordinates import normalize_point
from src.validators.validate_coordinates import coordinates_are_valid

class NormalizerTests(TestCase):
    def test_normalize_point_text_coords(self):
        sample_points = {
            "point_A": (190, 240),
            "point_B": (-210, 120),
            "point_C": (720, -10),
            "point_D": (-750, 0),
            "point_E": (-890, -100),
            "point_F": (920, 180),
        }

        for point, coords in sample_points.items():
            normalized_point = normalize_point(coords)
            self.assertTrue(
                coordinates_are_valid(normalized_point)
                )

    

# normalizePoint(new Point(190, 240))  ->  Point(-170, -60)

# normalizePoint(new Point(-210, 120)) ->  Point(150, 60)

# normalizePoint(new Point(720, -10))  ->  Point(0, -10)

# normalizePoint(new Point(-750, 0)) -> Point(-30, 0)

# normalizePoint(new Point(-890, -100)) -> Point(-170, -80)

# normalizePoint(new Point(920, 180))   -> Point(-160, 0
