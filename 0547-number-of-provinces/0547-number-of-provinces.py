class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        num_rows = len(isConnected)
        num_cols = len(isConnected[0])
        
        list_counter = 0
        row_check_dict = {}
        list_provinces = []
        
        one_checker_dict = {}
        for row_index in range(0, num_rows):
            for col_index in range(0, num_cols):
                
                if(row_index!=col_index):
                    if((isConnected[row_index][col_index]==1) and (str(row_index)+"_"+str(col_index) not in one_checker_dict) and (str(col_index)+"_"+str(row_index) not in one_checker_dict)):
                        
                        one_checker_dict[str(row_index)+"_"+str(col_index)] = 1
                        one_checker_dict[str(col_index)+"_"+str(row_index)] = 1
                        
                        if(row_index in row_check_dict):
                            row_check_dict[col_index] = row_check_dict[row_index]
                            list_provinces[row_check_dict[row_index]].append(col_index)
                            
                        else:
                            row_check_dict[row_index] = list_counter
                            row_check_dict[col_index] = list_counter
                            list_provinces.append([row_index,col_index])
                            list_counter += 1
        print(list_provinces)
        new_list_provinces = []
        new_list_provinces_dict = {}
        list_counter = 0
        for each_province in list_provinces:
            print(new_list_provinces_dict)
            counter = 0
            for each_city in each_province:
                if(each_city in new_list_provinces_dict):
                    counter += 1
                    new_province_index = new_list_provinces_dict[each_city]

            
            if(counter>0):
                new_list_provinces[new_province_index].extend(each_province)
                for each_city in each_province:
                    new_list_provinces_dict[each_city] = new_province_index
                
            else:
                for each_city in each_province:
                    new_list_provinces_dict[each_city] = list_counter
                new_list_provinces.append(each_province)
                list_counter += 1

        list_provinces = new_list_provinces
        new_list_provinces = []
         
        new_list_provinces_dict = {}
        list_counter = 0
        for each_province in list_provinces:
            print(new_list_provinces_dict)
            counter = 0
            for each_city in each_province:
                if(each_city in new_list_provinces_dict):
                    counter += 1
                    new_province_index = new_list_provinces_dict[each_city]

            
            if(counter>0):
                new_list_provinces[new_province_index].extend(each_province)
                for each_city in each_province:
                    new_list_provinces_dict[each_city] = new_province_index
                
            else:
                for each_city in each_province:
                    new_list_provinces_dict[each_city] = list_counter
                new_list_provinces.append(each_province)
                list_counter += 1        
        
        print(new_list_provinces)
        print(num_rows)
        new_list_provinces_flat_list = list(set([x for xs in new_list_provinces for x in xs]))
        counter_add_city = 0
        for each_city in range(num_rows):
            if(each_city not in new_list_provinces_flat_list):
                counter_add_city += 1
                print(each_city)
            
        return counter_add_city+len(new_list_provinces)