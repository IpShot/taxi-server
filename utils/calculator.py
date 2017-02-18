from math import pi, cos, sin, sqrt, pow, atan, atan2, degrees, floor

# Radius of The Earth
radius = 6372795

def deg_to_rad(point):
	return {
		'lat': point['lat'] * pi / 180,
		'lon': point['lon'] * pi / 180,
	}

##
# Calculate distance between points with
# lattitude and longtitude coordinates
# @params:
#   point1 - { 'lat': float, 'lon': float } in degrees
#   point2 - { 'lat': float, 'lon': float } in degrees
# @return:
#   distance between point1 and point2 in meters
#   
def distance(point1, point2):
	p1 = deg_to_rad(point1)
	p2 = deg_to_rad(point2)

	cos_lp1 = cos(p1['lat'])
	cos_lp2 = cos(p2['lat'])
	sin_lp1 = sin(p1['lat'])
	sin_lp2 = sin(p2['lat'])
	delta = p2['lon'] - p1['lon']
	cos_delta = cos(delta)
	sin_delta = sin(delta)

	y = sqrt( 
		pow(cos_lp2 * sin_delta, 2) + 
		pow(cos_lp1 * sin_lp2 - sin_lp1 * cos_lp2 * cos_delta, 2) 
	)
	x = sin_lp1 * sin_lp2 + cos_lp1 * cos_lp2 * cos_delta
	ad = atan2(y, x)
	dist = ad * radius

	return dist