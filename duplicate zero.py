class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        i=0
        N=len(arr)
        while i<len(arr):
            if arr[i]!=0:
                i+=1
            else:
                Q=arr[i+1:N-1]
                #print ("Q=", Q)
                arr[i+1]=0
                i+=2
                #print("arr[0:i]", arr[0:i])
                arr=arr[0:i]+Q
                print("arr=", arr, i, len(arr))
                if i==N-1:
                    return
o=Solution()
nums=[1,0,2,3,0,4,5,0]
o.duplicateZeros(nums)
print ("nums=", nums)