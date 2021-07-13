class Solution:
    def maximumWealth(self, accounts) -> int:
        """
        U
        given a list of lists for each item in the inner list add up the sum and return the largest total of the inner lists

        P
        loop throught the outer most list
        for each element in the inner list add them all up
        and return the largest total of the inner list items

        """
        total = 0
        for bank in accounts:
            bankSum = 0
            for i in bank:
                bankSum += i
            if bankSum > total:
                total = bankSum
        return total