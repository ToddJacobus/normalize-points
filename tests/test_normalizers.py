from unittest import TestCase

from src.normalizers.normalize_coordinates import normalize_point
from src.validators.validate_coordinates import coordinates_are_valid

class NormalizerTests(TestCase):
    """Tests for evaluating return values for normalization and validation
    functions"""

    def setUp(self):
        # "Raw" and normalized latitude and longitude values predetermined
        # to be the correct result of normalization.
        self.sample_points = {
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

    def test_valid_points(self):
        """Test that each point is a valid, lat/lon pair"""

        for coords in self.sample_points.values():
            normalized_point = normalize_point(coords['raw'])
            self.assertTrue(
                    coordinates_are_valid(normalized_point)
                )
    
    def test_correct_points(self):
        """Test that the normalization function calculates the correct,
        normalized values based on a collection of sample points"""

        for coords in self.sample_points.values():
            self.assertEqual(
                normalize_point(coords['raw']),
                coords['norm']
            )
