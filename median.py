class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        array= sorted(nums1 + nums2)
        print(array)
        le = len(array)
        print(le)
        if len(array)%2==1:
            return array[int((le+1)/2)-1]
        else:
            return (array[int(le/2)] + array[(int(le/2-1))])/2
