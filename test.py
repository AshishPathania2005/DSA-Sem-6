class Solution:
    def mySqrt(self, x: int) -> int:
        s = 0
        e = x+1
        m = (s+e)/2
        if(m>x/m):
            e = m-1
        else:
            s = m+1
        return s

        