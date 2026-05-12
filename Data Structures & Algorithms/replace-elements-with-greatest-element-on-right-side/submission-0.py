class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        for i in range(len(arr)-1):
            maxi=float('-inf')
            for j in range(i+1, len(arr)):
                maxi=max(arr[j] , maxi)
            arr[i]=maxi
        arr[-1]=-1
        return arr