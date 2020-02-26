import time,logging
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return x
        left = 1
        right = x // 2
        while left < right:
           time.sleep(1)
           print('调试代码，观察区间左右端点、中位数，和进入的分之：left = {},right = {},'.format(left,right),end = '')
           mid = (left + right + 1) >> 1
           print('mid = {}'.format(mid),end = '')
           squre = mid * mid

           if squre > x:
               print('进入right = mid - 1 这个分支。')
               right = mid - 1
           else:
               print('进入left = mid 这个分支。')
               left = mid
        return left

# logging.debug(msg, *args, **kwargs)








if __name__ == '__main__':
    test = Solution()
    print(test.mySqrt(17))