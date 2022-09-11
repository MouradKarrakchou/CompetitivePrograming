class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        number=n
        setStore=set()
        while number!=1 and number not in setStore:
            sum=0
            setStore.add(number)
            for k in str(number):
                sum+=int(k)**2
            number=sum
        return number==1

print(Solution.isHappy(Solution,19))