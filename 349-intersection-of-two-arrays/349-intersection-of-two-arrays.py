class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def myMin(l1, l2):
            if len(l1) < len(l2):
                return l1
            else:
                return l2
        # print(myMin(nums1, nums2)) 
    
        def myMax(l1, l2):
            if len(l1) > len(l2):
                return l1
            else:
                return l2
        
        output = []
        for elem in myMin(nums1,nums2):
            if elem in myMax(nums1, nums2):
                if elem not in output:
                    output.append(elem)
        return(output)