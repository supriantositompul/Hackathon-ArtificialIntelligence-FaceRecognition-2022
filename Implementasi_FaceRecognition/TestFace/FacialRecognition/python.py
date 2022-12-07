import numpy as np
import math
import time


# start = np.array([1,2,3,5,6,0,7,8,4]).reshape(3,3) #--->>> Hard array to solve
start = np.array([1,2,3,0,4,6,7,5,8]).reshape(3,3) #--->>> Easy array than above one to solve

goal = np.array([1,2,3,4,5,6,7,8,0]).reshape(3,3) #--->>> Goal state to achieve


def actions_array(array):
	goal = np.array([1,2,3,4,5,6,7,8,0]).reshape(3,3)
	possible_actions = []
	new_arrays = {}
	for i in range(len(array)):
		for j in range(len(array)):
			if array[i][j] == 0:

				#for moving up
				if i > 0:
					up_array = array.copy()
					up_array[i][j], up_array[i-1][j] = up_array[i-1][j], up_array[i][j]
					if not np.array_equal(up_array, start):
						new_arrays["up"] = up_array


				#for moving down
				if i < len(array) - 1:
					down_array = array.copy()
					down_array[i][j], down_array[i+1][j] = down_array[i+1][j], down_array[i][j]
					if not np.array_equal(down_array, start):
						new_arrays["down"] = down_array


				#for moving right
				if j < len(array) - 1:
					right_array = array.copy()
					right_array[i][j], right_array[i][j+1] = right_array[i][j+1], right_array[i][j]
					if not np.array_equal(right_array, start):
						new_arrays["right"] = right_array


				#for moving left
				if j > 0 :
					left_array = array.copy()
					left_array[i][j], left_array[i][j-1] = left_array[i][j-1], left_array[i][j]
					if not np.array_equal(left_array, start):
						new_arrays["left"] = left_array


	return new_arrays



#H value by calculating number of misplaced tiles
def h_value(array):

	s = sum(abs((val-1)%3 - i%3) + abs((val-1)//3 - i//3)
        for i, val in enumerate(array.reshape(1,9)[0]) if val)

	return s


def main():
	run = True
	prev_step = []
	array = start.copy()
	ola = None
	count = 0

	tic = time.time()
	while run:

		h={}

		if ola is not None:
			array = ola


		act = actions_array(array)

		for keys, values in act.items():
			h[keys]=h_value(values)


		#find the smallest h value and its key in the dict
		new_dic =  dict(sorted(h.items(), key=lambda item: item[1]))
		res = list(new_dic.items())[0]
		r, v = res[0], res[1]

		if not prev_step:
			prev_step.append(['start_array', array])

		else:
			for i in range(len(prev_step)):
					if np.array_equal(act[r], prev_step[i][1]):
					#check if the 2nd value in dic is = to the lowest or not
					#we are taking only the top two smallest
						new_h = list(new_dic.items())[1]
						r, v = new_h[0], new_h[1]


		if np.array_equal(act[r], goal):
			print("\n")
			print('''Problem Solved !. Steps included are : \n''')

			prev_step.append([res[0], act[r]])
			for i in prev_step:
				print(i[0])
				print(i[1])
				print("\n")
			run = False
			toc = time.time()
			print("Total number of steps: " + str(count))
			print("Total amount of time in search: " + str(toc - tic) + " second(s)")

		else:
			prev_step.append([r, act[r]])
			ola = act[r]
			# prev_step[res[0]] = act[res[0]]
			count+=1




main()
