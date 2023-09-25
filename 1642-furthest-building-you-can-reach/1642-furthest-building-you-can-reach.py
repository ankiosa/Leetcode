import bisect
class Solution(object):
    def __init__(self):
        # Initialize class variables
        self.bricks_heap = []
        self.bricks_sum = 0
        self.ladders_heap = []
        self.ladder_size = 0

    def add_elem_into_sorted_new_heap(self, elem, new_heap):
        #new_heap.append(elem)
        # Sort the list
        #new_heap.sort()

        indexval = bisect.bisect_left(new_heap, elem)
        new_heap.insert(indexval, elem)

    def rearrangement_heaps(self, elem, bricks, ladders):
        if self.ladder_size == ladders:
            if ladders == 0:
                self.bricks_heap.append(elem)
                self.bricks_sum += elem
            elif elem < self.ladders_heap[0]:
                self.bricks_heap.append(elem)
                self.bricks_sum += elem
            else:
                new_elem = self.ladders_heap.pop(0)
                self.bricks_heap.append(new_elem)
                self.bricks_sum += new_elem
                self.add_elem_into_sorted_new_heap(elem, self.ladders_heap)
        else:
            self.add_elem_into_sorted_new_heap(elem, self.ladders_heap)
            self.ladder_size += 1

    def furthestBuilding(self, heights, bricks, ladders):
        
        heights_diff = [heights[i + 1] - heights[i] for i in range(len(heights) - 1)]
        if(bricks==0 and ladders==0):
            if(len(heights)==1):
                return 0
            else:
                for i in range(len(heights_diff)):
                    if(heights_diff[i]>0):
                        return i
        for i in range(len(heights_diff)):
            if heights_diff[i] < 0:
                pass
            else:
                self.rearrangement_heaps(heights_diff[i],bricks, ladders)
                if self.bricks_sum > bricks:
                    break

        if self.bricks_sum <= bricks:
            return i + 1
        else:
            return i