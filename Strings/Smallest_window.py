#https://practice.geeksforgeeks.org/problems/smallest-window-in-a-string-containing-all-the-characters-of-another-string-1587115621
#sliding window problem
#https://leetcode.com/problems/minimum-window-substring/
def smallestWindow(s, p):
    n = len(s)
    if n < len(p):
        return -1
    mp = [0]*256
     
    # Starting index of ans
    start = 0
     
    # Answer
    # Length of ans
    ans = n + 1
    cnt = 0
     
    # creating map
    for i in p:
        mp[ord(i)] += 1
        if mp[ord(i)] == 1:
            cnt += 1
             
     # References of Window       
    j = 0
    i = 0
     
    # Traversing the window
    while(j < n):
       
      # Calculating
        mp[ord(s[j])] -= 1
        if mp[ord(s[j])] == 0:
            cnt -= 1
             
            # Condition matching
            while cnt == 0:
                if ans > j - i + 1:
                   
                  # calculating answer.
                    ans = j - i + 1
                    start = i
                     
                 # Sliding I
                # Calculation for removing I
                mp[ord(s[i])] += 1
                if mp[ord(s[i])] > 0:
                    cnt += 1
                i += 1
        j += 1
    if ans > n:
        return "-1"
    return s[start:start+ans]
 
# Driver code
if __name__ == "__main__":
    s = "ADOBECODEBANC"
    p = "ABC"
    result = smallestWindow(s, p)
    print("-->Smallest window that contain all character :", result)
     