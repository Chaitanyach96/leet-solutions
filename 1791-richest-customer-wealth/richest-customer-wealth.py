class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        maximum = 0

        for i in range(len(accounts)):

            total = 0
            
            for j in range(len(accounts[i])):
                total = total + accounts[i][j]
                
                if total > maximum:
                    maximum = total

        return maximum
