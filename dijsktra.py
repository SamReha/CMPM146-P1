from p1_support import load_level, show_level
from math import sqrt
from heapq import heappush, heappop

def dijk(src, dst, graph, adj):
	dist = {}
	prev = {}

	dist[src] = 0
	prev[src] = None

	for vert in graph['spaces']:
		print vert

 	return None	

def get_steps(level, cell):
	steps = []
	x, y = cell
	for dx in [-1,0,1]:
		for dy in [-1,0,1]:
			next_cell = (x + dx, y + dy)
			dist = sqrt(dx*dx+dy*dy)
			if dist > 0 and next_cell in level['spaces']:
				steps.append(next_cell)

	return steps


def test_route(filename, src_waypoint, dst_waypoint):
	level = load_level(filename)

	src = level['waypoints'][src_waypoint]
	dst = level['waypoints'][dst_waypoint]

	path = dijk(src, dst, level, get_steps)

	if path is not None:
		show_level(level, path)
	else:
		print("There is no path from " + src_waypoint + " to " + dst_waypoint + ".")

if __name__ ==  '__main__':
	import sys
	_, filename, src_waypoint, dst_waypoint = sys.argv
	test_route(filename, src_waypoint, dst_waypoint)
