
def longestPalindrome(self, s):
    l = len(s)
    primary = 0
    secondary = 0
    l_edge = 0
    r_edge = 0
    flag = 0
    ans = ""
    for i in range(2*l-1):
        l_edge = primary
        r_edge = secondary
        while s[l_edge] == s[r_edge]:
            if l_edge == 0 or r_edge == (l-1):
                if s[l_edge] == s[r_edge]:
                    break
            else:
                l_edge -= 1
                r_edge += 1
        if s[l_edge] == s[r_edge]:
            curr = s[l_edge:r_edge+1]
        else:
            curr = s[l_edge+1:r_edge]
        if i%2 == 1:
            primary +=1
        else:
            secondary +=1
        if len(curr) >= len(ans):
            ans = curr
    return ans
