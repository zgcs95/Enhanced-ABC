#############################################################################################################
############################## DO NOT TOUCH ANYTHING UNTIL I TELL YOU TO DO SO ##############################
#############################################################################################################

# This is the skeleton program NatAlgReal.py around which you should build your implementation.
# Read all comments below carefully.

##############################
#### ENTER YOUR USER-NAME ####
##############################

username = "zgcs95"

###############################################################
#### ENTER THE CODE FOR THE ALGORITHM YOU ARE IMPLEMENTING ####
###############################################################

alg_code = "AB"

#############################################################################################################
############################## DO NOT TOUCH ANYTHING UNTIL I TELL YOU TO DO SO ##############################
#############################################################################################################

import time
import random
import math

#
# The function f is 3-dimensional and you are attempting to MINIMIZE it.
# To compute the value f(a, b, c), call the function 'compute_f(a, b, c)'.
# The variables 'f', 'a', 'b' and 'c' are reserved.
# On termination your algorithm should be such that:
#   - the reserved variable 'min_f' holds the minimum value that you have computed for the function f 
#   - the reserved variable 'minimum' is a list of length 3 holding the minimum point that you have found.
#

def compute_f(a, b, c):
    f = a**2/4000 + b**2/4000 + c**2/4000 - (math.sin(math.pi/2 + a) * math.sin(math.pi/2 + b/math.sqrt(2)) \
                                          * math.sin(math.pi/2 + c/math.sqrt(3))) + 1
    return f

#
# The ranges for the values for a, b and c are [-500, 500]. The lists below hold the minimum and maximum
# values for each a, b and c, respectively, and you should use these list variables in your code.
#

min_range = [-500, -500, -500]
max_range = [500, 500, 500]

start_time = time.time()

#############################################################################################################
########################################### ENTER YOUR CODE BELOW ###########################################
#############################################################################################################


#fitness function
def fitness(x):
    if x>0:
        return 1/(1+x)
    else:
        return 1 + abs(x)

#generate random food source
def ran_source():
    a = random.uniform(-500, 500)
    b = random.uniform(-500, 500)
    c = random.uniform(-500, 500)
    result = compute_f(a, b, c)
    return [fitness(result), a, b, c, result, 0]

#near-neighbour function for vanilla version
def new(current, partner):
    variable = random.randint(1, 3)
    result = current.copy()
    result[variable] = current[variable] + random.uniform(-1, 1)*(current[variable] - partner[variable])
    result[0] = fitness(compute_f(result[1], result[2], result[3]))
    result[4] = compute_f(result[1], result[2], result[3])
    result[-1] = 0
    return result


#roulette wheel selection
def wheel(sources):
    sum = 0
    for i in range(len(sources)):
        sum = sum + sources[i][0]
    point = random.uniform(0, 1)
    sum2 = 0
    for j in range(len(sources)):
        sum2 = sum2 + sources[j][0]
        if sum2/sum >= point:
            return j

#near-neighbour function for enhanced version
def enhance_new(index, current, sources, number):
    result = current.copy()
    bin_num = bin(number)
    for i in range(1, 4):
        if bin_num[-i] == "1":
            partner = random.randint(0, len(sources)-1)
            while partner == index:
                partner = random.randint(0, len(sources)-1)
            result[i] = current[i] + random.uniform(-1, 1)*(current[i] - sources[partner][i])
    result[0] = fitness(compute_f(result[1], result[2], result[3]))
    result[4] = compute_f(result[1], result[2], result[3])
    return result

#tournament selection
def tournament(sources):
    number = random.randint(1, len(sources))
    result = sources.copy()
    random.shuffle(result)
    result = result[:number]
    result.sort(reverse=True)
    for i in range(len(sources)):
        if sources[i]==result[0]:
            return i

#main function of the vanilla version
def AB(N, M, num_cyc, pi):
    t = 1
    sources = []
    for i in range(N):
        sources.append(ran_source())
    sources.sort(reverse=True)
    best = sources[0]
    while t <= num_cyc:
        for j in range(N+M):
            if j < N:
                k = j
                partner = random.randint(0, N-1)
                neighbour = new(sources[k], sources[partner])
                if neighbour[0] >= sources[k][0]:
                    sources[k] = neighbour
                else:
                    sources[k][-1] = sources[k][-1] + 1
            else:
                k = wheel(sources)
                partner = random.randint(0, N - 1)
                neighbour = new(sources[k], sources[partner])
                if neighbour[0] >= sources[k][0]:
                    sources[k] = neighbour
                else:
                    sources[k][-1] = sources[k][-1] + 1
        sources.sort(reverse=True)
        if sources[0][0] >= best[0]:
            best = sources[0]
        for x in range(len(sources)):
            if sources[x][-1] >= pi:
                sources[x] = ran_source()
        if (time.time() - start_time) >= 60:
            break
        t = t + 1
    return [best[-2], [best[1], best[2], best[3]]]

#main function of the enhanced version
def enhanced_AB(N, M, num_cyc, pi):
    t = 1
    sources = []
    for i in range(N):
        sources.append(ran_source())
    sources.sort(reverse=True)
    best = sources[0]
    while t <= num_cyc:
        for j in range(N+M):
            #employed bee phase
            if j < N:
                k = j
                neighbours = []
                for a in range(sources[k][-1]+1):
                    if a > 7:
                        break
                    neighbours.append(enhance_new(k, sources[k], sources, a))
                neighbours.sort(reverse=True)
                if neighbours[0][0] > sources[k][0]:
                    sources[k] = neighbours[0]
                    sources[k][-1] = 0
                else:
                    sources[k][-1] = sources[k][-1] + 1
            #onlooker bee phase
            else:
                k = tournament(sources)
                partner = random.randint(0, N - 1)
                while partner == k:
                    partner = random.randint(0, N - 1)
                neighbour = new(sources[k], sources[partner])
                if neighbour[0] > sources[k][0]:
                    sources[k] = neighbour
                else:
                    sources[k][-1] = sources[k][-1] + 1
        sources.sort(reverse=True)
        #updata the best food source
        if sources[0][0] >= best[0]:
            best = sources[0]
        #scout bee phase
        for x in range(len(sources)):
            if sources[x][-1] >= pi:
                random_source = ran_source()
                if random_source[0] > sources[x][0]:
                    sources[x] = random_source
        if (time.time() - start_time) >= 60:
            break
        t = t + 1
    return [best[-2], [best[1], best[2], best[3]]]

N = 30
M = 10
num_cyc = 300000
lambbda = 8


result = enhanced_AB(N, M, num_cyc, lambbda)

min_f = result[0]
minimum = result[1]



#############################################################################################################
################################## DO NOT TOUCH ANYTHING BELOW THIS COMMENT #################################
#############################################################################################################

# You should now have computed your minimum value for the function f in the variable 'min_f' and the reserved
# variable 'minimum' should hold a list containing the values a, b and c for which function f is such that
# f(a, b, c) achieves its minimum; that is, your minimum point.

now_time = time.time()
elapsed_time = round(now_time - start_time, 1)
    
error_flag = False
if type(min_f) != float and type(min_f) != int:
    print("\n*** error: you don't have a real-valued variable 'min_f'")
    error_flag = True
if type(minimum) != list:
    print("\n*** error: you don't have a tuple 'minimum' giving the minimum point")
    error_flag = True
elif len(minimum) != 3:
    print("\n*** error: you don't have a 3-tuple 'minimum' giving the minimum point; you have a {0}-tuple".format(len(minimum)))
    error_flag = True
else:
    var_names = ['a', 'b', 'c']
    for i in range(0, 3):
        if type(minimum[i]) != float and type(minimum[i]) != int:
            print("\n*** error: the value for {0} in your minimum point (a, b, c) is not numeric".format(var_names[i]))
            error_flag = True

if error_flag == False:
    print("\nYou have found a minimum value of {0} and a minimum point of [{1}, {2}, {3}].".format(min_f, minimum[0], minimum[1], minimum[2]))
    print("Your elapsed time was {0} seconds.".format(elapsed_time))


    

















    
