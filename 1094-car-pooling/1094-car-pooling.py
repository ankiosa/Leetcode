class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        travel_dict = {}
        for each_trip in trips:
            if(each_trip[1] in travel_dict):
                travel_dict[each_trip[1]] += each_trip[0]
            else:
                travel_dict[each_trip[1]] = each_trip[0]
            if(each_trip[2] in travel_dict):
                travel_dict[each_trip[2]] -= each_trip[0]
            else:
                travel_dict[each_trip[2]] = -each_trip[0]
        print(travel_dict)

        total_pos = sorted(travel_dict.keys())
        for each_pos in total_pos:
            capacity = capacity-travel_dict[each_pos]
            if(capacity<0):
                return False
        return True

            
