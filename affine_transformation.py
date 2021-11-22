from PIL import Image, ImageDraw
from math import cos, sin, pi

# Read txt file
with open('DS0.txt') as f:
    lines = f.readlines()

coordinates = []

for line in lines:
    # Delete '\n' symbol from every dot and split by space
    formatted_line = line[:-1].split(' ')
    # Create single coordinate as tuple
    single_coordinate = (int(formatted_line[0]), int(formatted_line[1]))
    coordinates.append(single_coordinate)

# Create new image
out = Image.new("RGB", (960, 960), (255, 255, 255))
draw = ImageDraw.Draw(out)
# Fill canvas with prepared coordinates
draw.point(coordinates, fill='red')

angle = 10 * (0 + 1)
# Angle in radians
angle_rad = angle * pi/180
# Center of rotation
ox, oy = 480, 480

rotated_coordinates = []

for coordinate in coordinates:
    x = coordinate[0]
    y = coordinate[1]
    # Affine formulas to perform rotation for every dot
    new_x = ox + (x - ox) * cos(angle_rad) - (y - oy) * sin(angle_rad)
    new_y = oy + (x - ox) * sin(angle_rad) + (y - oy) * cos(angle_rad)
    single_coordinate = (new_x, new_y)
    rotated_coordinates.append(single_coordinate)

# Fill canvas with prepared rotated coordinates
draw.point(rotated_coordinates, fill='blue')

# Show picture
out.show()

# Save picture
out.save("output_affine.jpg")
