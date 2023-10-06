process = int(input("ENTER THE NUM OF PROCESS => " ))
wait_time = 0
avg = 0
avg_t = 0
arrival = 0 #Could not figure out how to in coorperate correctly so i stopped this 
matrix = [[0 for j in range(4)] for i in range(process)]
'''#EVERYTHING ABOVE: These are the initializers that will be needed so num of processes, the wait times, average, then create a matrix that will 
used to set and move everything around '''



print("WHAT ARE THE BURST TIME => " )
for i in range(process):
    matrix[i][1] = int(input("P{} ".format(i+1)))
    matrix[i][0] = i + 1
''' Takes the input from user to set the burst time in the matrix'''

'''Below is the sort for the matrix that is basically setting them in order from what their burst times should be
and almost act like the Gantt Chart for the matrix by checking if the temp(burst) is greater than the one being compared to
and then will change positions depending on that'''
for i in range(process):
    temp = i
    for j in range(i + 1, process):
        if matrix[j][1] < matrix[temp][1]:
            temp = j
    new = matrix[i][1]
    matrix[i][1] = matrix[temp][1]
    matrix[temp][1] = new 
    new = matrix[i][0]
    matrix[i][0] = matrix[temp][0]
    matrix[temp][0] = new

matrix[0][2] = 0 

'''This will be used for the waiting time to add up and then find the average after they are out of the loop'''
for i in range(1, process):
    matrix[i][2] = 0
    for j in range(i):
        matrix[i][2] += matrix[j][1]
    wait_time += matrix[i][2]
avg = wait_time / process



'''Prints out the matrix and what we have will then be output as well as the wait time average '''
print("PROCESS   BURST     WAIT")
for i in range(process):
    matrix[i][3] = matrix[i][1] + matrix[i][2]
    wait_time += matrix[i][3]
    print("P{}          {}        {}".format(matrix[i][0],matrix[i][1],matrix[i][3]))

print("AVG WAIT TIME IS => {}".format(avg))


