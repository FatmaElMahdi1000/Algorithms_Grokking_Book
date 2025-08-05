class Solution(object):
    def fib_seq(self):
        my_fib_seq = [0, 1]
        while True:
            next_number = my_fib_seq[-1] + my_fib_seq[-2]
            if next_number > 832040:
                break
            my_fib_seq.append(next_number)
        return my_fib_seq

    def fib(self, n):
        if n < 0 or n > 30:
            print("Error: Out of range")
            return None
        our_seq = self.fib_seq()
        return our_seq[n]
fib = Solution()
print(fib.fib_seq())   # ✅ Full sequence
print(fib.fib(10))     # ✅ Prints: 89

print("***********SOLUTION NUMBER 2 ******************")
class Solution(object):
    def fib_recursive(self, n):
        if(n <= 0) or (n > 30):
            return 0
        elif (n == 1):
            return 1
        else:
            return self.fib_recursive(n - 1) + self.fib_recursive(n - 2)

fib = Solution()
print(fib.fib_recursive(10))
        


























