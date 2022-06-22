'''
    lis[][0]:Petrol
    lis[][1]:Distance
'''
#https://practice.geeksforgeeks.org/problems/circular-tour/

class Solution:
    
    #Function to find starting point where the truck can start to get through
    #the complete circle without exhausting its petrol in between.
    def tour(self,lis, n):
        balance, deficit = 0,0
        start = 0
        for i in range(n):
            balance += lis[i][0] - lis[i][1]
            if balance < 0:
                start = i+1
                deficit += balance
                balance = 0
        if balance + deficit >= 0:
            return start
        else:
            return -1
        #Code here

#{ 
#  Driver Code Starts
if __name__ == '__main__': 
    t = int(input())
    for i in range(t):
        n = int(input())
        arr=list(map(int, input().strip().split()))
        lis=[]
        for i in range(1, 2*n, 2):
            lis.append([ arr[i-1], arr[i] ])
        print(Solution().tour(lis, n))
# } Driver Code Ends