#inserted data: "0 8 6 8 0 7 9 6 75"
#increasing peaks
#0 8 4 12 2 10 6 14 1 9 5 13 3 11 7 15

def route_planner(peaks):
    peaks_list = peaks.split(" ") #splitting peaks
    final_route = [] #defines final route as list
    for peak in peaks_list:
        if len(final_route) ==0: 
            final_route.append(peak) #appends lowest peak as 0 
        elif int(peak) > int(final_route[len(final_route) - 1]):
            final_route.append(peak) #appends each next lowest peak
    return final_route
        
print(route_planner("0 2 6 3 5 9 8 4 9 5"))