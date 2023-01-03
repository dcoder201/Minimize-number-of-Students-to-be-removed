#User function Template for python3
from bisect import bisect_left
class Solution:
    def removeStudents(self, H, N):
        # code here
        ans=[H[0]]
        for i in range(1, N):
            if H[i]>ans[-1]:
                ans.append(H[i])
            else:
                ans[bisect_left(ans, H[i])]=H[i]
        return N-len(ans)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        H=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.removeStudents(H,N))
# } Driver Code Ends
