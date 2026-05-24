class Solution(object):
    def merge(self, nums1, m, nums2, n):
        temp = []
        i = 0
        j = 0

        # compare and pick smaller element
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                temp.append(nums1[i])
                i += 1
            else:
                temp.append(nums2[j])
                j += 1

        # remaining elements of nums1
        while i < m:
            temp.append(nums1[i])
            i += 1

        # remaining elements of nums2
        while j < n:
            temp.append(nums2[j])
            j += 1

        # copy temp back into nums1
        for k in range(m + n):
            nums1[k] = temp[k]
