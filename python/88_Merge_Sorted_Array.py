class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        aux = []
        ii, jj = 0, 0
        while ii < len(nums1) - len(nums2) or jj < len(nums2):
            if ii == len(nums1) - len(nums2):
                aux.append(nums2[jj])
                jj += 1
            elif jj == len(nums2):
                aux.append(nums1[ii])
                ii += 1
            else:
                if nums1[ii] < nums2[jj]:
                    aux.append(nums1[ii])
                    ii += 1
                else:
                    aux.append(nums2[jj])
                    jj += 1
        for ii in range(len(nums1)):
            nums1[ii] = aux[ii]

# order reversed, need not aux, space O(1)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ii, jj, kk = m - 1, n - 1, m + n - 1
        while ii >= 0 or jj >= 0:
            if ii < 0:
                nums1[kk] = nums2[jj]
                jj -= 1
            elif jj < 0:
                nums1[kk] = nums1[ii]
                ii -= 1
            else:
                if nums1[ii] > nums2[jj]:
                    nums1[kk] = nums1[ii]
                    ii -= 1
                else:
                    nums1[kk] = nums2[jj]
                    jj -= 1
            kk -= 1