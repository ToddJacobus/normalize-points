# Project Description

This application was developed as part of a coding exercise posed by GISinc.  The key requirement was to normalize coordinates from a hypothetical mathematical result, which may be outside of normal, geographic ranges, and convert them to the acceptable format for latitude and longitude.  For example, this application can accept the tuple `(190, 240)` as an input, and outputs `(-170, -60)`.

Albeit it’s a bit overkill for this exercise, I organized this application in the same way I would organize a much larger application.  This means I included unit tests and separated out each functional API into their own, importable, python modules.  This way, the application is much more extensible and much more easily developed by a team.

There are two unit tests and each demonstrates the solution to the challenge.  The first is a validation test, which tests the validity of the input coordinates.  The second tests that the normalization function transforms the inputs into the acceptable outputs.  These outputs are derived from examples of correct normalizations passed along with the exercise description.

I have also included a Dockerfile and docker-compose.yml file which describes a very simple container.  Again, this is overkill for such a simple application, but this represents standard procedure for when I develop more complex applications.  By running the unit tests within the Docker container, you can see that the results of the normalization function match the desired output.

The application uses only standard Python libraries and has no dependencies.  The `requirements.txt` file is there only to demonstrate how I manage and share dependencies for a given environment.

# Usage

To convert a point from a mathmatical result to an acceptable value for Latitude and Longitude:
```
from src.normalizers.normalize_coordinates import normalize_point
from src.validators.validate_coordinates import coordinates_are_valid

normalized_point = normalize_point((190, 240))
coordinates_are_valid(normalized_point)

>>> True

```