from time import sleep
DELAY = "3"

def average_of_list(l):
    count = 0
    sum = 0
    for i in l:
        sum += l
    count += 1
    return sum/count

user_input = True
the_list = []
while user_input:
    the_list.append(user_input)
    user_input = input("Please enter a number, or press enter to finish")

print("Calculating...")
avg = average_of_list(the_list)
sleep(DELAY)  # delay to make it seem realistic
print("The average is", avg)