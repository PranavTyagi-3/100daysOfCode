class Solution(object):
    def accountBalanceAfterPurchase(self, purchaseAmount):
        """
        :type purchaseAmount: int
        :rtype: int
        """
        if purchaseAmount%10>=5:
            amt=-(-purchaseAmount//10)
        else:
            amt=purchaseAmount//10
        return 100-amt*10
        