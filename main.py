'''

Exercise 3

Write a function ( run_timing ) that asks how long it took for you to run 10 km.
The function continues to ask how long (in minutes) it took for additional runs, until
the user presses Enter. At that point, the function exits—but only after calculating and
displaying the average time that the 10 km runs took.
For example, here is what the output would look like if the user entered three data
points:
Enter 10 km run time: 15
Enter 10 km run time: 20
Enter 10 km run time: 10
Enter 10 km run time: <enter> 

Average of 15.0, over 3 runs

'''
def run_timing():
    numbers_of_runs = 0
    total_time = 0
    while True:
        one_run = input('Enter 10k run time: ')
        
        if one_run == '':
            break
        
        numbers_of_runs += 1
        total_time += float(one_run)
        average_time = total_time / numbers_of_runs
    print('<enter>')
    if numbers_of_runs != 0:
        print(f'Average of {average_time:.1f}, over {numbers_of_runs} runs')
    
run_timing()