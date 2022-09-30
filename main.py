import array_tools
import sorts
import time
import matplotlib as mpl
import matplotlib.pyplot as plt
import os
import sys
sys.setrecursionlimit(5000)



#random
length = 10
l_border = -1000000000
r_border = 1000000000

init_array = array_tools.make_simple_array(length, l_border, r_border)

h_time = []
q_time = []
b_time = []
s_time = []

size_arr = []
size_arr_b = []

while length <= 4000:
	heapsort_array = init_array[:]
	quicksort_array = init_array[:]
	bubblesort_array = init_array[:]
	shellsort_array = init_array[:]
	
	sum_time = 0
	for i in range(50):
		start_heapsort = time.time()
		sorts.heapSort(heapsort_array, length)
		time_heapsort = time.time() - start_heapsort
		sum_time += time_heapsort
		print("Heap--", time_heapsort)
		heapsort_array = init_array[:]
		#print(heapsort_array)
	print("Av_Heap--", sum_time/50)
	h_time.append(sum_time/50)

	sum_time = 0
	for i in range(50):
		start_quicksort = time.time()
		sorts.quickSort(0, length-1, quicksort_array)
		time_quicksort = time.time() - start_quicksort
		sum_time += time_quicksort
		print("Quick--", time_quicksort)
		quicksort_array = init_array[:]
		#print(quicksort_array)
	print("Av_Quick--", sum_time/50)
	q_time.append(sum_time/50)

	if length < 1000:
		sum_time = 0
		for i in range(50):
			start_bubblesort = time.time()
			sorts.bubbleSort(bubblesort_array)
			time_bubblesort = time.time() - start_bubblesort
			sum_time += time_bubblesort
			print("Bubble--", time_bubblesort)
			bubblesort_array = init_array[:]
			#print(bubblesort_array)
		print("Av_Bubble--", sum_time/50)
		b_time.append(sum_time/50)
	elif length <=1500:
		sum_time = 0
		for i in range(2):
			start_bubblesort = time.time()
			sorts.bubbleSort(bubblesort_array)
			time_bubblesort = time.time() - start_bubblesort
			sum_time += time_bubblesort
			print("Bubble--", time_bubblesort)
			bubblesort_array = init_array[:]
			#print(bubblesort_array)
		print("Av_Bubble--", sum_time/2)
		b_time.append(sum_time/2)
	else:
		pass
		
	sum_time = 0
	for i in range(50):
		start_shellsort = time.time()
		sorts.shellSort(shellsort_array)
		time_shellsort = time.time() - start_shellsort
		sum_time += time_shellsort
		print("Shell--", time_shellsort)
		shellsort_array = init_array[:]
		#print(shellsort_array)
	print("Av_Shell--", sum_time/50)
	s_time.append(sum_time/50)
	
	if length <= 1500:
		size_arr_b.append(length)
	size_arr.append(length)
	print(length)
	for i in range(5):
		init_array = array_tools.add_simple_element(init_array, l_border, r_border)
	length+=5


plt.figure(figsize=(10, 6), layout='constrained')
plt.plot(size_arr, h_time, label='Heapsort')  
plt.plot(size_arr, q_time, label='Quicksort')   
plt.plot(size_arr_b, b_time, label='Bubblesort')
plt.plot(size_arr, s_time, label='Shellsort') 
plt.xlabel('size') 
plt.ylabel('time (s)') 
plt.title("Время от размера не отсортированного массива до 4000 (bubble до 1500)")
plt.legend()
plt.savefig(os.path.join('random4000.png'))



#halfsort
length = 10
l_border = -1000000000
r_border = 1000000000

init_array = array_tools.make_simple_array(length, l_border, r_border)
init_array = array_tools.half_sort_simple_array(init_array)

h_time = []
q_time = []
b_time = []
s_time = []

size_arr = []
size_arr_b = []

while length <= 4000:
	heapsort_array = init_array[:]
	quicksort_array = init_array[:]
	bubblesort_array = init_array[:]
	shellsort_array = init_array[:]
	
	sum_time = 0
	for i in range(50):
		start_heapsort = time.time()
		sorts.heapSort(heapsort_array, length)
		time_heapsort = time.time() - start_heapsort
		sum_time += time_heapsort
		print("Heap--", time_heapsort)
		heapsort_array = init_array[:]
		#print(heapsort_array)
	print("Av_Heap--", sum_time/50)
	h_time.append(sum_time/50)

	sum_time = 0
	for i in range(50):
		start_quicksort = time.time()
		sorts.quickSort(0, length-1, quicksort_array)
		time_quicksort = time.time() - start_quicksort
		sum_time += time_quicksort
		print("Quick--", time_quicksort)
		quicksort_array = init_array[:]
		#print(quicksort_array)
	print("Av_Quick--", sum_time/50)
	q_time.append(sum_time/50)

	if length < 1000:
		sum_time = 0
		for i in range(50):
			start_bubblesort = time.time()
			sorts.bubbleSort(bubblesort_array)
			time_bubblesort = time.time() - start_bubblesort
			sum_time += time_bubblesort
			print("Bubble--", time_bubblesort)
			bubblesort_array = init_array[:]
			#print(bubblesort_array)
		print("Av_Bubble--", sum_time/50)
		b_time.append(sum_time/50)
	elif length <=1500:
		sum_time = 0
		for i in range(2):
			start_bubblesort = time.time()
			sorts.bubbleSort(bubblesort_array)
			time_bubblesort = time.time() - start_bubblesort
			sum_time += time_bubblesort
			print("Bubble--", time_bubblesort)
			bubblesort_array = init_array[:]
			#print(bubblesort_array)
		print("Av_Bubble--", sum_time/2)
		b_time.append(sum_time/2)
	else:
		pass
		
	sum_time = 0
	for i in range(50):
		start_shellsort = time.time()
		sorts.shellSort(shellsort_array)
		time_shellsort = time.time() - start_shellsort
		sum_time += time_shellsort
		print("Shell--", time_shellsort)
		shellsort_array = init_array[:]
		#print(shellsort_array)
	print("Av_Shell--", sum_time/50)
	s_time.append(sum_time/50)
	
	if length <= 1500:
		size_arr_b.append(length)
	size_arr.append(length)
	print(length)
	for i in range(5):
		init_array = array_tools.add_simple_element(init_array, l_border, r_border)
	length+=5
	init_array = array_tools.half_sort_simple_array(init_array)


plt.figure(figsize=(10, 6), layout='constrained')
plt.plot(size_arr, h_time, label='Heapsort')  
plt.plot(size_arr, q_time, label='Quicksort')   
plt.plot(size_arr_b, b_time, label='Bubblesort')
plt.plot(size_arr, s_time, label='Shellsort') 
plt.xlabel('size') 
plt.ylabel('time (s)') 
plt.title("Время от размера частично отсортированного массива до 4000 (bubble до 1500)")
plt.legend()
plt.savefig(os.path.join('half4000.png'))



#fullreverse
length = 10
l_border = -1000000000
r_border = 1000000000

init_array = array_tools.make_simple_array(length, l_border, r_border)
sorts.shellSort(init_array)

h_time = []
q_time = []
b_time = []
s_time = []

size_arr = []
size_arr_b = []

while length <= 4000:
	heapsort_array = init_array[::-1]
	quicksort_array = init_array[::-1]
	bubblesort_array = init_array[::-1]
	shellsort_array = init_array[::-1]
	
	sum_time = 0
	for i in range(50):
		start_heapsort = time.time()
		sorts.heapSort(heapsort_array, length)
		time_heapsort = time.time() - start_heapsort
		sum_time += time_heapsort
		print("Heap--", time_heapsort)
		heapsort_array = init_array[:]
		#print(heapsort_array)
	print("Av_Heap--", sum_time/50)
	h_time.append(sum_time/50)
	
	if length < 1000:
		sum_time = 0
		for i in range(50):
			start_quicksort = time.time()
			sorts.quickSort(0, length-1, quicksort_array)
			time_quicksort = time.time() - start_quicksort
			sum_time += time_quicksort
			print("Quick--", time_quicksort)
			quicksort_array = init_array[:]
			#print(quicksort_array)
		print("Av_Quick--", sum_time/50)
		q_time.append(sum_time/50)
	elif length <=1500:
		sum_time = 0
		for i in range(10):
			start_quicksort = time.time()
			sorts.quickSort(0, length-1, quicksort_array)
			time_quicksort = time.time() - start_quicksort
			sum_time += time_quicksort
			print("Quick--", time_quicksort)
			quicksort_array = init_array[:]
			#print(quicksort_array)
		print("Av_Quick--", sum_time/10)
		q_time.append(sum_time/10)
	else:
		pass
		
	if length < 1000:
		sum_time = 0
		for i in range(50):
			start_bubblesort = time.time()
			sorts.bubbleSort(bubblesort_array)
			time_bubblesort = time.time() - start_bubblesort
			sum_time += time_bubblesort
			print("Bubble--", time_bubblesort)
			bubblesort_array = init_array[:]
			#print(bubblesort_array)
		print("Av_Bubble--", sum_time/50)
		b_time.append(sum_time/50)
	elif length <=1500:
		sum_time = 0
		for i in range(10):
			start_bubblesort = time.time()
			sorts.bubbleSort(bubblesort_array)
			time_bubblesort = time.time() - start_bubblesort
			sum_time += time_bubblesort
			print("Bubble--", time_bubblesort)
			bubblesort_array = init_array[:]
			#print(bubblesort_array)
		print("Av_Bubble--", sum_time/10)
		b_time.append(sum_time/10)
	else:
		pass	
		
	sum_time = 0
	for i in range(50):
		start_shellsort = time.time()
		sorts.shellSort(shellsort_array)
		time_shellsort = time.time() - start_shellsort
		sum_time += time_shellsort
		print("Shell--", time_shellsort)
		shellsort_array = init_array[:]
		#print(shellsort_array)
	print("Av_Shell--", sum_time/50)
	s_time.append(sum_time/50)
	
	if length <= 1500:
		size_arr_b.append(length)
	size_arr.append(length)
	print(length)
	for i in range(5):
		init_array = array_tools.add_simple_element(init_array, l_border, r_border)
	length+=5
	sorts.shellSort(init_array)


plt.figure(figsize=(10, 6), layout='constrained')
plt.plot(size_arr, h_time, label='Heapsort')  
plt.plot(size_arr_b, q_time, label='Quicksort')   
plt.plot(size_arr_b, b_time, label='Bubblesort')
plt.plot(size_arr, s_time, label='Shellsort') 
plt.xlabel('size') 
plt.ylabel('time (s)') 
plt.title("Время от размера обратно отсортированного массива до 4000 (bubble и quick до 1500)")
plt.legend()
plt.savefig(os.path.join('fullreverse4000.png'))



#onedigit
length = 10
l_border = 1
r_border = 1

init_array = array_tools.make_simple_array(length, l_border, r_border)

h_time = []
q_time = []
b_time = []
s_time = []

size_arr = []
size_arr_b = []

while length <= 4000:
	heapsort_array = init_array[::-1]
	quicksort_array = init_array[::-1]
	bubblesort_array = init_array[::-1]
	shellsort_array = init_array[::-1]
	
	sum_time = 0
	for i in range(50):
		start_heapsort = time.time()
		sorts.heapSort(heapsort_array, length)
		time_heapsort = time.time() - start_heapsort
		sum_time += time_heapsort
		print("Heap--", time_heapsort)
		heapsort_array = init_array[:]
		#print(heapsort_array)
	print("Av_Heap--", sum_time/50)
	h_time.append(sum_time/50)

	if length < 1000:
		sum_time = 0
		for i in range(50):
			start_quicksort = time.time()
			sorts.quickSort(0, length-1, quicksort_array)
			time_quicksort = time.time() - start_quicksort
			sum_time += time_quicksort
			print("Quick--", time_quicksort)
			quicksort_array = init_array[:]
			#print(quicksort_array)
		print("Av_Quick--", sum_time/50)
		q_time.append(sum_time/50)
	elif length <=1500:
		sum_time = 0
		for i in range(10):
			start_quicksort = time.time()
			sorts.quickSort(0, length-1, quicksort_array)
			time_quicksort = time.time() - start_quicksort
			sum_time += time_quicksort
			print("Quick--", time_quicksort)
			quicksort_array = init_array[:]
			#print(quicksort_array)
		print("Av_Quick--", sum_time/10)
		q_time.append(sum_time/10)
	else:
		pass

	if length < 1000:
		sum_time = 0
		for i in range(50):
			start_bubblesort = time.time()
			sorts.bubbleSort(bubblesort_array)
			time_bubblesort = time.time() - start_bubblesort
			sum_time += time_bubblesort
			print("Bubble--", time_bubblesort)
			bubblesort_array = init_array[:]
			#print(bubblesort_array)
		print("Av_Bubble--", sum_time/50)
		b_time.append(sum_time/50)
	elif length <=1500:
		sum_time = 0
		for i in range(10):
			start_bubblesort = time.time()
			sorts.bubbleSort(bubblesort_array)
			time_bubblesort = time.time() - start_bubblesort
			sum_time += time_bubblesort
			print("Bubble--", time_bubblesort)
			bubblesort_array = init_array[:]
			#print(bubblesort_array)
		print("Av_Bubble--", sum_time/10)
		b_time.append(sum_time/10)
	else:
		pass
			
	sum_time = 0
	for i in range(50):
		start_shellsort = time.time()
		sorts.shellSort(shellsort_array)
		time_shellsort = time.time() - start_shellsort
		sum_time += time_shellsort
		print("Shell--", time_shellsort)
		shellsort_array = init_array[:]
		#print(shellsort_array)
	print("Av_Shell--", sum_time/50)
	s_time.append(sum_time/50)
	
	if length <= 1500:
		size_arr_b.append(length)
	size_arr.append(length)
	print(length)
	for i in range(5):
		init_array = array_tools.add_simple_element(init_array, l_border, r_border)
	length+=5


plt.figure(figsize=(10, 6), layout='constrained')
plt.plot(size_arr, h_time, label='Heapsort')  
plt.plot(size_arr_b, q_time, label='Quicksort')   
plt.plot(size_arr_b, b_time, label='Bubblesort')
plt.plot(size_arr, s_time, label='Shellsort') 
plt.xlabel('size') 
plt.ylabel('time (s)') 
plt.title("Время от размера массива с одним значением до 4000 (bubble и quick до 1500)")
plt.legend()
plt.savefig(os.path.join('onedigit4000.png'))



#threedigit
length = 10
l_border = 0
r_border = 2

init_array = array_tools.make_simple_array(length, l_border, r_border)

h_time = []
q_time = []
b_time = []
s_time = []

size_arr = []
size_arr_b = []

while length <= 4000:
	heapsort_array = init_array[::-1]
	quicksort_array = init_array[::-1]
	bubblesort_array = init_array[::-1]
	shellsort_array = init_array[::-1]
	
	sum_time = 0
	for i in range(50):
		start_heapsort = time.time()
		sorts.heapSort(heapsort_array, length)
		time_heapsort = time.time() - start_heapsort
		sum_time += time_heapsort
		print("Heap--", time_heapsort)
		heapsort_array = init_array[:]
		#print(heapsort_array)
	print("Av_Heap--", sum_time/50)
	h_time.append(sum_time/50)

	if length < 1000:
		sum_time = 0
		for i in range(50):
			start_quicksort = time.time()
			sorts.quickSort(0, length-1, quicksort_array)
			time_quicksort = time.time() - start_quicksort
			sum_time += time_quicksort
			print("Quick--", time_quicksort)
			quicksort_array = init_array[:]
			#print(quicksort_array)
		print("Av_Quick--", sum_time/50)
		q_time.append(sum_time/50)
	elif length <=1500:
		sum_time = 0
		for i in range(10):
			start_quicksort = time.time()
			sorts.quickSort(0, length-1, quicksort_array)
			time_quicksort = time.time() - start_quicksort
			sum_time += time_quicksort
			print("Quick--", time_quicksort)
			quicksort_array = init_array[:]
			#print(quicksort_array)
		print("Av_Quick--", sum_time/10)
		q_time.append(sum_time/10)
	else:
		pass

	if length < 1000:
		sum_time = 0
		for i in range(50):
			start_bubblesort = time.time()
			sorts.bubbleSort(bubblesort_array)
			time_bubblesort = time.time() - start_bubblesort
			sum_time += time_bubblesort
			print("Bubble--", time_bubblesort)
			bubblesort_array = init_array[:]
			#print(bubblesort_array)
		print("Av_Bubble--", sum_time/50)
		b_time.append(sum_time/50)
	elif length <=1500:
		sum_time = 0
		for i in range(10):
			start_bubblesort = time.time()
			sorts.bubbleSort(bubblesort_array)
			time_bubblesort = time.time() - start_bubblesort
			sum_time += time_bubblesort
			print("Bubble--", time_bubblesort)
			bubblesort_array = init_array[:]
			#print(bubblesort_array)
		print("Av_Bubble--", sum_time/10)
		b_time.append(sum_time/10)
	else:
		pass
				
	sum_time = 0
	for i in range(50):
		start_shellsort = time.time()
		sorts.shellSort(shellsort_array)
		time_shellsort = time.time() - start_shellsort
		sum_time += time_shellsort
		print("Shell--", time_shellsort)
		shellsort_array = init_array[:]
		#print(shellsort_array)
	print("Av_Shell--", sum_time/50)
	s_time.append(sum_time/50)
	
	if length <= 1500:
		size_arr_b.append(length)
	size_arr.append(length)
	print(length)
	for i in range(5):
		init_array = array_tools.add_simple_element(init_array, l_border, r_border)
	length+=5


plt.figure(figsize=(10, 6), layout='constrained')
plt.plot(size_arr, h_time, label='Heapsort')  
plt.plot(size_arr_b, q_time, label='Quicksort')   
plt.plot(size_arr_b, b_time, label='Bubblesort')
plt.plot(size_arr, s_time, label='Shellsort') 
plt.xlabel('size') 
plt.ylabel('time (s)') 
plt.title("Время от размера массива с тремя значениями до 4000 (bubble и quick до 1500)")
plt.legend()
plt.savefig(os.path.join('threedigit4000.png'))



#full
length = 10
l_border = -1000000000
r_border = 1000000000

init_array = array_tools.make_simple_array(length, l_border, r_border)
sorts.shellSort(init_array)

h_time = []
q_time = []
b_time = []
s_time = []

size_arr = []
size_arr_b = []

while length <= 4000:
	heapsort_array = init_array[::-1]
	quicksort_array = init_array[::-1]
	bubblesort_array = init_array[::-1]
	shellsort_array = init_array[::-1]
	
	sum_time = 0
	for i in range(50):
		start_heapsort = time.time()
		sorts.heapSort(heapsort_array, length)
		time_heapsort = time.time() - start_heapsort
		sum_time += time_heapsort
		print("Heap--", time_heapsort)
		heapsort_array = init_array[:]
		#print(heapsort_array)
	print("Av_Heap--", sum_time/50)
	h_time.append(sum_time/50)

	if length < 1000:
		sum_time = 0
		for i in range(50):
			start_quicksort = time.time()
			sorts.quickSort(0, length-1, quicksort_array)
			time_quicksort = time.time() - start_quicksort
			sum_time += time_quicksort
			print("Quick--", time_quicksort)
			quicksort_array = init_array[:]
			#print(quicksort_array)
		print("Av_Quick--", sum_time/50)
		q_time.append(sum_time/50)
	elif length <=1500:
		sum_time = 0
		for i in range(10):
			start_quicksort = time.time()
			sorts.quickSort(0, length-1, quicksort_array)
			time_quicksort = time.time() - start_quicksort
			sum_time += time_quicksort
			print("Quick--", time_quicksort)
			quicksort_array = init_array[:]
			#print(quicksort_array)
		print("Av_Quick--", sum_time/10)
		q_time.append(sum_time/10)
	else:
		pass

	if length < 1000:
		sum_time = 0
		for i in range(50):
			start_bubblesort = time.time()
			sorts.bubbleSort(bubblesort_array)
			time_bubblesort = time.time() - start_bubblesort
			sum_time += time_bubblesort
			print("Bubble--", time_bubblesort)
			bubblesort_array = init_array[:]
			#print(bubblesort_array)
		print("Av_Bubble--", sum_time/50)
		b_time.append(sum_time/50)
	elif length <=1500:
		sum_time = 0
		for i in range(10):
			start_bubblesort = time.time()
			sorts.bubbleSort(bubblesort_array)
			time_bubblesort = time.time() - start_bubblesort
			sum_time += time_bubblesort
			print("Bubble--", time_bubblesort)
			bubblesort_array = init_array[:]
			#print(bubblesort_array)
		print("Av_Bubble--", sum_time/10)
		b_time.append(sum_time/10)
	else:
		pass
			
	sum_time = 0
	for i in range(50):
		start_shellsort = time.time()
		sorts.shellSort(shellsort_array)
		time_shellsort = time.time() - start_shellsort
		sum_time += time_shellsort
		print("Shell--", time_shellsort)
		shellsort_array = init_array[:]
		#print(shellsort_array)
	print("Av_Shell--", sum_time/50)
	s_time.append(sum_time/50)
	
	if length <= 1500:
		size_arr_b.append(length)
	size_arr.append(length)
	print(length)
	for i in range(5):
		init_array = array_tools.add_simple_element(init_array, l_border, r_border)
	length+=5
	sorts.shellSort(init_array)


plt.figure(figsize=(10, 6), layout='constrained')
plt.plot(size_arr, h_time, label='Heapsort')  
plt.plot(size_arr_b, q_time, label='Quicksort')   
plt.plot(size_arr_b, b_time, label='Bubblesort')
plt.plot(size_arr, s_time, label='Shellsort') 
plt.xlabel('size') 
plt.ylabel('time (s)') 
plt.title("Время от размера отсортированного массива до 4000 (bubble и quick до 1500)")
plt.legend()
plt.savefig(os.path.join('fullsort4000.png'))
