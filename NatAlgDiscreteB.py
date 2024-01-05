#############################################################################################################
############################## DO NOT TOUCH ANYTHING UNTIL I TELL YOU TO DO SO ##############################
#############################################################################################################

# This is the skeleton program NatAlgDiscreteA.py around which you should build your implementation.
#
# On input GCGraphA.txt, say, the output is a witness set that is in the file WitnessA_<timestamp>.txt where
# <timestamp> is a timestamp so that you do not overwrite previously produced witnesses. You can always
# rename these files. The witness file is placed in a folder called "abcd12" (or whatever your username is)
# which is assumed to exist.
#
# It is assumed that all graph files are in a folder called GraphFiles that lies in the same folder as
# NatAlgDiscreteA.py. So, there is a folder that looks like {NatAlgDiscreteA.py, GraphFiles, abcd12}.

##############################
#### ENTER YOUR USER-NAME ####
##############################

username = "zgcs95"

###############################################################
#### ENTER THE CODE FOR THE ALGORITHM YOU ARE IMPLEMENTING ####
###############################################################

alg_code = "AB"

#################################################################
#### ENTER THE CODE FOR THE GRAPH PROBLEM YOU ARE OPTIMIZING ####
#################################################################

problem_code = "CL"

#############################################################
#### ENTER THE DIGIT OF THE INPUT GRAPH FILE (A, B OR C) ####
#############################################################

graph_digit = "B"

#############################################################################################################
############################## DO NOT TOUCH ANYTHING UNTIL I TELL YOU TO DO SO ##############################
#############################################################################################################

import time
import os
import random
import math

def get_a_timestamp_for_an_output_file():
    local_time = time.asctime(time.localtime(time.time()))
    timestamp = local_time[4:7] + local_time[8:10] + local_time[11:13] + local_time[14:16] + local_time[17:19]
    timestamp = timestamp.replace(" ", "0") 
    return timestamp

def read_the_graph_file(problem_code, graph_digit):
    vertices_tag = "number of vertices = "
    len_vertices_tag = len(vertices_tag)
    edges_tag = "number of edges = "
    len_edges_tag = len(edges_tag)
    if problem_code == "GC":
        colours_tag = "number of colours to use = "
        len_colours_tag = len(colours_tag)
    if problem_code == "GP":
        sets_in_partition_tag = "number of partition sets = "
        len_sets_in_partition_tag = len(sets_in_partition_tag)
    input_file = "GraphFiles/" + problem_code + "Graph" + graph_digit + ".txt"
    
    f = open(input_file, 'r')
    whole_line = f.readline()
    vertices = whole_line[len_vertices_tag:len(whole_line) - 1]
    v = int(vertices)
    whole_line = f.readline()
    edges = whole_line[len_edges_tag:len(whole_line) - 1]
    if problem_code == "GC":
        whole_line = f.readline()
        colours = whole_line[len_colours_tag:len(whole_line) - 1]
        colours = int(colours)
    if problem_code == "GP":
        whole_line = f.readline()
        sets_in_partition = whole_line[len_sets_in_partition_tag:len(whole_line) - 1]
        sets_in_partition = int(sets_in_partition)
    matrix = []
    for i in range(0, v - 1):
        whole_line = f.readline()
        splitline = whole_line.split(',')
        splitline.pop(v - 1 - i)
        splitline.insert(0, 0)
        matrix.append(splitline[:])
    matrix.append([0])
    for i in range(0, v):
        for j in range(0, i):
            matrix[j][i] = int(matrix[j][i])
            matrix[i].insert(j, matrix[j][i])
    f.close()

    edges = []
    for i in range(0, v):
        for j in range(i + 1, v):
            if matrix[i][j] == 1:
                edges.append([i, j])

    if problem_code == "GC":
        return v, edges, matrix, colours
    elif problem_code == "GP":
        return v, edges, matrix, sets_in_partition
    else:
        return v, edges, matrix
 
if problem_code == "GC":
    v, edges, matrix, colours = read_the_graph_file(problem_code, graph_digit)
elif problem_code == "GP":
    v, edges, matrix, sets_in_partition = read_the_graph_file(problem_code, graph_digit)
else:
    v, edges, matrix = read_the_graph_file(problem_code, graph_digit)

#######################################
#### READ THE FOLLOWING CAREFULLY! ####
#######################################

# For the problem GC, the graph data has now been read into the following reserved variables:
#   - 'v' = the number of vertices of the graph
#   - 'edges' = a list of the edges of the graph (just in case you need them)
#   - 'matrix' = the full adjacency matrix of the graph
#   - 'colours' = the maximum number of colours to be used when colouring

# For the problem CL, the graph data has now been read into the following reserved variables:
#   - 'v' = the number of vertices of the graph
#   - 'edges' = a list of the edges of the graph (just in case you need them)
#   - 'matrix' = the full adjacency matrix of the graph

# For the problem GP, the graph data has now been read into the following reserved variables:
#   - 'v' = the number of vertices of the graph
#   - 'edges' = a list of the edges of the graph (just in case you need them)
#   - 'matrix' = the full adjacency matrix of the graph
#   - 'sets_in_partition' = the number of sets in any partition

# These are reserved variables and need to be treated as such, i.e., use these names for these
# concepts and don't re-use the names.

# For the problem GC, you will produce a colouring in the form of a list of n integers called
# 'colouring' where the entries range from 1 to 'colours'. Note! 0 is disallowed as a colour!
# You will also produce an integer in the variable 'conflicts' which denotes how many edges
# are such that the two incident vertices are identically coloured (of course, your aim is to
# minimize the value of 'conflicts').

# For the problem CL, you will produce a clique in the form of a list of n integers called
# 'clique' where the entries are either 0 or 1. If 'clique[i]' = 1 then this denotes that the
# vertex i is in the clique.
# You will also produce an integer in the variable 'clique_size' which denotes how many vertices
# are in your clique (of course, your aim is to maximize the value of 'clique_size').

# For the problem GP, you will produce a partition in the form of a list of n integers called
# 'partition' where the entries are in {1, 2, ..., 'sets_in_partition'}. Note! 0 is not the
# name of a partition set! If 'partition[i]' = j then this denotes that the vertex i is in the
# partition set j.
# You will also produce an integer in the variable 'conflicts' which denotes how many edges are
# incident with vertices in different partition sets (of course, your aim is to minimize the
# value of 'conflicts').

# In consequence, the following additional variables are reserved:
#   - 'colouring'
#   - 'conflicts'
#   - 'clique'
#   - 'clique_size'
#   - 'partition'

# The various algorithms all have additional parameters (see the lectures). These parameters
# are detailed below and are referred to using the following reserved variables.
#
# AB (Artificial bee colony)
#   - 'n' = dimension of the optimization problem
#   - 'num_cyc' = number of cycles to iterate
#   - 'N' = number of employed bees / food sources
#   - 'M' = number of onlooker bees
#   - 'lambbda' = limit threshold

if alg_code == 'AB':
    n = None
    num_cyc = None
    N = None
    M = None
    lambbda = None

# FF (Firefly)
#   - 'n' = dimension of the optimization problem
#   - 'num_cyc' = number of cycles to iterate
#   - 'N' = number of fireflies
#   - 'lambbda' = light absorption coefficient
#   - 'alpha' = scaling parameter

if alg_code == 'FF':
    n = None
    num_cyc = None
    N = None
    lambbda = None
    alpha = None

# CS (Cuckoo search)
#   - 'n' = dimension of optimization problem
#   - 'num_cyc' = number of cycles to iterate
#   - 'N' = number of nests
#   - 'p' = fraction of local flights to undertake
#   - 'q' = fraction of nests to abandon
#   - 'alpha' = scaling factor for Levy flights
#   - 'beta' = parameter for Mantegna's algorithm

if alg_code == 'CS':
    n = None
    num_cyc = None
    N = None
    p = None
    q = None
    alpha = None
    beta = None

# WO (Whale optimization)
#   - 'n' = dimension of optimization problem
#   - 'num_cyc' = number of cycles to iterate
#   - 'N' = number of whales
#   - 'b' = spiral constant

if alg_code == 'WO':
    n = None
    num_cyc = None
    N = None
    b = None

# BA (Bat)
#   - 'n' = dimension of optimization problem
#   - 'num_cyc' = number of cycles to iterate
#   - 'N' = number of fireflies
#   - 'sigma' = scaling factor
#   - 'f_min' = minimum frequency
#   - 'f_max' = maximum frequency

if alg_code == 'BA':
    n = None
    num_cyc = None
    N = None
    sigma = None
    f_min = None
    f_max = None

# These are reserved variables and need to be treated as such, i.e., use these names for these
# parameters and don't re-use the names! Note that I have initialized them as I write them in the
# output file even if you don't actually use them. If you use the parameters then don't touch anything
# above but initialize them for yourself below. Also, you may introduce additional parameters if you
# wish (below) but they won't get written to the output file.

start_time = time.time()

#############################################################################################################
########################################### ENTER YOUR CODE BELOW ###########################################
#############################################################################################################

#check whether it is a proper clique by using matrix
def check_clique(set):
    x = set[1].copy()
    x.sort()
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            if matrix[x[i]-1][x[j]-1]==0:
                return False
    return True

#generate random food source
def ran_source(max):
    elements = []
    n = random.randint(1, max)
    for i in range(1, n+1):
        elements.append(i)
    random.shuffle(elements)
    result = random.sample(elements, n)
    return [len(result), result, 0]

#The function used to generate near-neighbour in the scout bee phase
def new(x, max, number):
    neighbour = x[1].copy()
    save_num = random.randint(len(x[1])//2, len(x[1]))
    result = random.sample(neighbour, save_num)
    missing = []
    for i in range(1, max+1):
        if i not in result:
            missing.append(i)
    added = random.sample(missing, number-save_num)
    new = result + added
    new.sort()
    return [len(new), new, 0]

#The function used to generate near-neighbour in the employee bee and onlooker bee phase
def entire(x, max):
    neighbour = x[1].copy()
    missing = []
    for i in range(1, max + 1):
        if i not in neighbour:
            missing.append(i)
    for j in range(len(missing)):
        if check_clique([len(neighbour+[missing[j]]), neighbour+[missing[j]], 0])==True:
            return [len(neighbour+[missing[j]]), neighbour+[missing[j]], 0]
    return False


#formatting the result into the required format
def formatting(source, num_v):
    result = []
    for i in range(num_v):
        result.append(0)
    for j in range(len(source[1])):
        result[source[1][j]-1] = 1
    return [source[0], result]

#tournament selection
def tournament(sources):
    number = random.randint(1, len(sources))
    result = sources[:number].copy()
    result.sort(reverse=True)
    for i in range(len(sources)):
        if sources[i]==result[0]:
            return i

#Main function of AB
def AB(N, M, num_cyc, pi, num_v):
    #generate food sources randomly
    sources = []
    for i in range(N):
        new_source = ran_source(num_v)
        while check_clique(new_source)==False:
            new_source = ran_source(num_v)
        sources.append(new_source)
    sources.sort(reverse=True)
    best = sources[0]
    t = 1
    while t < num_cyc:
        for k in range(N+M):
            #employed bee phase
            if k < N:
                neighbour = entire(sources[k], num_v)
                if neighbour!=False:
                    sources[k] = neighbour
                else:
                    sources[k][2] = sources[k][2] + 1
            #onlooker be phase
            else:
                k = tournament(sources)
                neighbour = entire(sources[k], num_v)
                if neighbour!=False:
                    sources[k] = neighbour
                else:
                    sources[k][2] = sources[k][2] + 1
        sources.sort(reverse=True)
        if sources[0][0] > best[0]:
            best = sources[0]
        #scout bee phase
        for j in range(1):
            if sources[j][2]>0:
                neighbour = new(sources[j], num_v, len(sources[j][1]) + 1)
                if check_clique(neighbour)==True:
                    sources[j] = neighbour
        if (time.time() - start_time) >= 60:
            break
        t = t + 1
    sources.sort(reverse=True)
    #formatting result
    result = formatting(sources[0], num_v)
    return result

num_cyc = 10
N = 10
M = 10
lambbda = 1

#v = 425
result = AB(N, M, num_cyc, lambbda, v)
clique = result[1]
clique_size = result[0]

#############################################################################################################
################################## DO NOT TOUCH ANYTHING BELOW THIS COMMENT #################################
#############################################################################################################

now_time = time.time()
elapsed_time = round(now_time - start_time, 1)

# You should now have computed the list 'colouring' and integer 'conflicts', if you are solving GC;
# the list 'clique' and the integer 'clique_size', if you are solving CL; or the list 'partition' and the
# integer 'conflicts', if you are solving GP.

timestamp = get_a_timestamp_for_an_output_file()
witness_set = username + "/Witness" + graph_digit + "_" + timestamp + ".txt"

f = open(witness_set, "w")

f.write("username = {0}\n".format(username))
f.write("graph = {0}Graph{1}.txt with (|V|,|E|) = ({2},{3})\n".format(problem_code, graph_digit, v, len(edges)))
if problem_code == "GC":
    f.write("colours-to-use = {0}\n".format(colours))
if problem_code == "GP":
    f.write("number of partition sets = {0}\n".format(sets_in_partition))
f.write("algorithm = {0}\n".format(alg_code))
if alg_code == "AB":
    f.write("associated parameters [n, num_cyc, N, M, lambbda] = ")
    f.write("[{0}, {1}, {2}, {3}, {4}]\n".format(n,num_cyc,N,M,lambbda))
elif alg_code == "FF":
    f.write("associated parameters [n, num_cyc, N, lambbda, alpha] = ")
    f.write("[{0}, {1}, {2}, {3}, {4}]\n".format(n,num_cyc,N,lambbda,alpha))
elif alg_code == "CS":
    f.write("associated parameters [n, num_cyc, N, p, q, alpha, beta] = ")
    f.write("[{0}, {1}, {2}, {3}, {4}, {5}, {6}]\n".format(n,num_cyc,N,p,q,alpha,beta))
elif alg_code == "WO":
    f.write("associated parameters [n, num_cyc, N, b] = ")
    f.write("[{0}, {1}, {2}, {3}]\n".format(n,num_cyc,N,b))
elif alg_code == "BA":
    f.write("associated parameters [n, num_cyc, sigma, f_max, f_min] = ")
    f.write("[{0}, {1}, {2}, {3}, {4}]\n".format(n,num_cyc,sigma,f_max,f_min))
if problem_code == "GC" or problem_code == "GP":
    f.write("conflicts = {0}\n".format(conflicts))
else:
    f.write("clique size = {0}\n".format(clique_size))
f.write("elapsed time = {0}\n".format(elapsed_time))

if problem_code == "GC":
    error = []
    length = len(colouring)
    if length != v:
        error.append("*** error: 'colouring' has length " + str(length) + " but should have length " + str(v) + "\n")
    bad_colouring = False
    for i in range(0, length):
        if colouring[i] < 1 or colouring[i] > colours:
            bad_colouring = True
            break
    if bad_colouring == True:
        error.append("*** error: 'colouring' uses illegal colours \n")
    true_conflicts = 0
    for i in range(0, length):
        for j in range(i + 1, length):
            if matrix[i][j] == 1 and colouring[i] == colouring[j]:
                true_conflicts = true_conflicts + 1
    if conflicts != true_conflicts:
        error.append("*** error: you claim " + str(conflicts) + " but there are actually " + str(true_conflicts) + " conflicts\n")
    if error != []:
        print("I am saving your colouring into a witness file but there are errors:")
        for item in error:
            print(item)
    for i in range(0, length):
        f.write("{0},".format(colouring[i]))
        if (i + 1) % 40 == 0:
            f.write("\n")
    if length % 40 != 0:
        f.write("\n")
elif problem_code == "GP":
    error = []
    length = len(partition)
    if length != v:
        error.append("*** error: 'partition' has length " + str(length) + " but should have length " + str(v) + "\n")
    bad_partition = False
    for i in range(0, length):
        if partition[i] < 1 or partition[i] > sets_in_partition:
            bad_partition = True
            break
    if bad_partition == True:
        error.append("*** error: 'partition' uses illegal set numbers \n")
    true_conflicts = 0
    for i in range(0, length):
        for j in range(i + 1, length):
            if matrix[i][j] == 1 and partition[i] != partition[j]:
                true_conflicts = true_conflicts + 1
    if conflicts != true_conflicts:
        error.append("*** error: you claim " + str(conflicts) + " but there are actually " + str(true_conflicts) + " conflicts\n")
    if error != []:
        print("I am saving your partition into a witness file but there are errors:")
        for item in error:
            print(item)
    for i in range(0, length):
        f.write("{0},".format(partition[i]))
        if (i + 1) % 40 == 0:
            f.write("\n")
    if length % 40 != 0:
        f.write("\n")
else:
    error = []
    length = len(clique)
    if length != v:
        error.append("*** error: 'clique' has length " + str(length) + " but should have length " + str(v) + "\n")
    bad_clique = False
    for i in range(0, length):
        if clique[i] != 0 and clique[i] != 1:
            bad_clique = True
            break
    if bad_clique == True:
        error.append("*** error: 'clique' is not a list of 0s and 1s\n")
    true_size = 0
    for i in range(0, length):
        if clique[i] == 1:
            true_size = true_size + 1
    if clique_size != true_size:
        error.append("*** error: you claim a clique of size " + str(clique_size) + " but it actually has size " + str(true_size) + "\n")
    if error != []:
        print("I am saving your clique into a witness file but there are errors:")
        for item in error:
            print(item)
    for i in range(0, length):
        f.write("{0},".format(clique[i]))
        if (i + 1) % 40 == 0:
            f.write("\n")
    if length % 40 != 0:
        f.write("\n")

f.close()
    
print("witness file saved")


















    
