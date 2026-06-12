class Solution(object):
    def merge(nums1, m, nums2, n):
        i,j,k=m-1,n-1,m+n-1
        while i>=0 and j>=0:
            if nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                i-=1
            else:
                nums1[k]=nums2[j]
                j-=1
            k-=1
        while j>=0:
            nums1[k]=nums2[j]
            j-=1
            k-=1
        return nums1 #*optional return (JUST TO SEETHAT WE ARE JETTING THE RIGHT ANSWER)*

print(Solution.merge([1,2,3,0,0,0],3,[2,5,6],3))
print(Solution.merge([1],1,[],0))
print(Solution.merge([0],0,[1],1))


