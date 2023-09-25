from collections import defaultdict
class Solution(object):
    
    def convertToadjacency(self, numCourses, prerequisites):
        courseAdjacencylist = defaultdict(list)
        for each_course, pr_course in prerequisites:
            courseAdjacencylist[each_course].append(pr_course)
            
        courseAdjacencycount = {}
        for each_course, pr_course_list in courseAdjacencylist.items():
            courseAdjacencycount[each_course] = len(pr_course_list)
            
        courseAdjacencyrevlist = defaultdict(list)
        for each_course, pr_course in prerequisites:
            courseAdjacencyrevlist[pr_course].append(each_course)
            
        zero_list = []
        for i in range(numCourses):
            if(i not in courseAdjacencycount):
                zero_list.append(i)
                courseAdjacencycount[i] = 0
            
        return courseAdjacencylist, courseAdjacencyrevlist, courseAdjacencycount, zero_list
    
        
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        courseAdjacencylist, courseAdjacencyrevlist, courseAdjacencycount, zero_list = self.convertToadjacency(numCourses, prerequisites)
        print(courseAdjacencylist, courseAdjacencycount, zero_list)
        seen_dict = {}
        while(zero_list):
            each_node = zero_list.pop()
            seen_dict[each_node] = True
            adv_course_list = courseAdjacencyrevlist[each_node]
            
            for each_course in adv_course_list:
                courseAdjacencycount[each_course] -= 1
                if(courseAdjacencycount[each_course]==0):
                    zero_list.append(each_course)
        print(seen_dict)
        if(len(seen_dict)==numCourses):
            return True
        else:
            return False
        