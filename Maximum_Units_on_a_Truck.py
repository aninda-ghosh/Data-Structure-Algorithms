!Maximum Units on a Truck


import heapq

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        MaxUnit = 0
        boxlist = []
        for box in boxTypes:
            heapq.heappush(boxlist, (-box[1], box[0]))   #Making a max heap out of the box list out all the lists
        
        # We'll keep a track of the remaining truck size
        availabletrucksize = truckSize
               
        for i in range(len(boxlist)):
            
            if(availabletrucksize):
                (unitperbox, noofboxes) = heapq.heappop(boxlist)
                
                # If we can fit one kind of boxtype in the truck
                if(noofboxes <= availabletrucksize):
                    MaxUnit += ((-1)*unitperbox*noofboxes)
                    availabletrucksize -= noofboxes
                else:
                # Else we will fill it up with some fractions of the units of a different type
                    print((availabletrucksize%truckSize))
                    MaxUnit += ((-1)*unitperbox*(availabletrucksize%truckSize))
                    availabletrucksize -= (availabletrucksize%truckSize)
        
        return MaxUnit
                
