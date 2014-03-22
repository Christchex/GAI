

def agent(self, start, goal):
    closed = []
    openset = [start]
    came_from =  []
    gscore = 0
    while(openset != []):
        current = getClosest()
        if current = goal:
            return reconstruct_path(came_from, goal)
        openset.remove(current)
        closed.append(current)
        neighbors[] = get_neighbors(current)
        for(s in neighbors):
            if(s in closed):
                continue
            temp_gscore = gscore + dist(current, s)
            elif(!s in openset or temp_gscore < gscore):
                gscore = temp_gscore
                came_from.append(current)
                if(!s in openset):
                    openset.append(s)
    print("Did it work?")
    return came_from

                
                
        
        
        
#returns the Fscore of the given point    
def getF(point):
    return gscore + dist(point, goal)


#Returns the point with the lowest F score in Openset
def getClosest():
    
    lowest = openset[0]
    value = getF(lowest)
    for(s in openset):
        if(dist(s,goal) < value):
            lowest = s
            value = getF(lowest)
    return lowest



#returns the distance between two points
def dist(point, goal):
    return (goal - point)
    
def reachable(node):
    return True
    #

def get_neighbors(point):
    #returns list of neighbors
    
    
                            
def main(self):


    
    
if __name__ == "__main__":
    main()

