class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Always binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        left = (m + n + 1) // 2

        low = 0
        high = m

        while low <= high:

            cut1 = (low + high) // 2
            cut2 = left - cut1

            # Left and right values around the partition
            l1 = float("-inf") if cut1 == 0 else nums1[cut1 - 1]
            r1 = float("inf") if cut1 == m else nums1[cut1]

            l2 = float("-inf") if cut2 == 0 else nums2[cut2 - 1]
            r2 = float("inf") if cut2 == n else nums2[cut2]

            # Correct partition found
            if l1 <= r2 and l2 <= r1:

                if (m + n) % 2 == 1:
                    return max(l1, l2)

                return (max(l1, l2) + min(r1, r2)) / 2

            # Move left
            elif l1 > r2:
                high = cut1 - 1

            # Move right
            else:
                low = cut1 + 1
