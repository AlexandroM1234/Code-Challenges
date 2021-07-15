class Solution:
    def diagonalSum(self, mat):
        """
        using a low and high pointer on the first and last values in the inner lists
        using those values add them to the total
        once they equal eachother make sure it only add the value to the total once
        after the low and high equal eachother their values replace to the end of the loop
        """
        if len(mat) == 1:
            return mat[0][0]
        total = 0
        low = 0
        high = len(mat) - 1

        for i in range(len(mat)):
            if low != high:
                total += mat[i][low] + mat[i][high]
            else:
                total += mat[i][low]
            low += 1
            high -= 1
        return total