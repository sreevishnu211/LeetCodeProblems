#https://leetcode.com/problems/palindromic-substrings/

class Solution(object):

     def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        isPalindroneMap = [ [ False for x in range( len( s ) ) ] for y in range( len( s ) ) ]
        count = 0

        for i in range( len( s ) ):
            isPalindroneMap[ i ][ i ] = True
            count += 1
        
        for i in range( len( s ) - 1 ):
            if s[ i ] == s[ i + 1 ]:
                isPalindroneMap[ i ][ i + 1 ] = True
                count += 1
        
        for i in range( 3, len( s ) + 1 ):
            for j in range( len( s ) - i + 1 ):
                isPalindroneMap[ j ][ j + i -1 ] = ( s[ j ] == s[ j + i -1 ] ) and isPalindroneMap[ j + 1 ][ j + i -2 ]
                if isPalindroneMap[ j ][ j + i -1 ]:
                    count += 1
        return count