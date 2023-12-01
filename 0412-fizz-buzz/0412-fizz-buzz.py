class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        anslist = []
        for i in range(1, n+1):
            if i % 15 == 0:
                anslist.append('FizzBuzz')
            elif i % 3 == 0:
                anslist.append('Fizz')
            elif i % 5 == 0:
                anslist.append('Buzz')
            else:
                anslist.append(str(i))
        return anslist