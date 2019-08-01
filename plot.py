from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt
import numpy as np
import sys
import re

np.random.seed(19680801)

def main():

	points = [1, 1, 1]

	file = open("magn_data.txt", "r")

	fig = plt.figure(figsize=(15,9))
	ax = fig.add_subplot(111, projection='3d')

	x = []
	y = []
	z = []

	for line in file.readlines():
		points =  re.findall(r'[0-9]+', line)
		x.append(int(points[0]));
		y.append(int(points[1]));
		z.append(int(points[2]));


	ax.scatter(x, y, z, c='b', marker='o')

	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	ax.set_zlabel('Z')

	# Full screen
	# figManager = plt.get_current_fig_manager() 
	# figManager.full_screen_toggle() 

	plt.show()

    

if __name__ == "__main__":
	main()