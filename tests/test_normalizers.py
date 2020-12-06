from unittest import TestCase

from src.normalizers.normalize_coordinates import normalize_point
from src.validators.validate_coordinates import coordinates_are_valid

class NormalizerTests(TestCase):
    def test_valid_points(self):
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
    
    def test_correct_points(self):
        sample_points = {
            "point_A": {
                "raw": (190, 240),
                "norm": (-170, -60),
                },
            "point_B": {
                "raw": (-210, 120),
                "norm": (150, 60)
                },
            "point_C": {
                "raw": (720, -10),
                "norm": (0, -10),
                },
            "point_D": {
                "raw": (-750, 0),
                "norm": (-30, 0),
                },
            "point_E": { 
                "raw": (-890, -100),
                "norm": (-170, -80)
                },
            "point_F": {
                "raw": (920, 180),
                "norm": (-160, 0),
                },
        }

        for point, coords in sample_points.items():
            self.assertEqual(
                normalize_point(coords['raw']),
                coords['norm']
            )
