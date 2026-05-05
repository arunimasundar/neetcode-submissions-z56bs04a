class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m=len(matrix)
        n=len(matrix[0])

        l=0
        r=m*n-1
        # print("l,r",l,r)

        while l<=r:
            mid=(l+r)//2
            # print("mid",mid)
            mid_r=mid//n
            mid_c=mid%n
            # print("mid_r,mid_c",mid_r,mid_c)
            num=matrix[mid_r][mid_c]

            if num==target:
                return True
            elif num<target:
                l=mid+1
            else:
                r=mid-1
        return False


