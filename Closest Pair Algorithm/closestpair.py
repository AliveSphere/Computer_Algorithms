# Charles Buyas, cjb8qf, HW02, 9/17/17
# My version is Python 3
# I didn't use any website sources, but I collaborated with Brady Zhang, bxz3kt
import math

filename = "garden.txt"
num_tomatoes = open(filename).readlines()[0]
print(str(num_tomatoes))

coord_list = []
with open(filename) as file:                # opens the garden text file
    for item in file:
        if len(item.strip('\n').split(" ")) == 2:
            coord_list.append(tuple(map(float, item.split(' '))))
#print(coord_list)


def distance(point1, point2):               # writing a distance equation
    return math.hypot(point2[0]-point1[0], point2[1]-point1[1])


def base_case_compare(curList):             # it will only hit base case with 3 or fewer points in a list
    min_distance = float("inf")                      # set arbitrary min dist
    for i in range(len(curList)):                       # comparing points
        for x in range(len(curList)):
            if i != x:                      # making sure we aren't comparing a point to itself
            #if curList[i] != curList[x]:
                cur = abs(distance(curList[i], curList[x]))   # uses distance formula above
                #if min_distance == -4:
                 #   min_distance = cur      # if this is the first time we're calculating
                if cur < min_distance:
                    min_distance = cur      # if cur is the new min dist
    return abs(min_distance)                # returns the result


def strip(list, min_distance):              # compares over the split between divide and conquer steps
    sorted_y_list = sorted(list, key = lambda tuple2: tuple2[1])
    mindist = min_distance
    new_mindist = 10                        # sets base case for comparing

    for i in range(len(sorted_y_list)):
        j= i + 1                            # makes sure that you're only checking numbers beyond your current value, and only 15 below it
        while j < len(sorted_y_list) and abs((sorted_y_list[i])[1] - (sorted_y_list[j])[1]) < mindist and j <= i+15:
            new_mindist = abs(distance(sorted_y_list[i], sorted_y_list[j]))
            j+=1
    return new_mindist


def closest_point(curList):                 # main function
    if len(curList) <= 3:
        return base_case_compare(curList)   # having 3 points it what I chose would be a base case size
    sorted_x_list = sorted(curList, key = lambda tuple1: tuple1[0])
    leftList = sorted_x_list[:int(len(sorted_x_list)/2)]
    rightList = sorted_x_list[int(len(sorted_x_list)/2):]
    final_minimum_dist = min(closest_point(leftList), closest_point(rightList))
    middle_points = []
    for n in curList:
        if abs(n[0]-sorted_x_list[int(len(sorted_x_list)/2)][0]) < final_minimum_dist:
            middle_points.append(n)
    return min(final_minimum_dist, strip(middle_points, final_minimum_dist))

print(closest_point(coord_list))