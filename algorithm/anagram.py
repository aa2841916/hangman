# def anagram(w1,w2):
#     """
#     变为词算法
#     :param w1: string或int类型常量
#     :param w2: string或int类型常量
#     :return: 返回W1 = W2
#     """
#     w1 = w1.lower()
#     w2 = w2.lower()
#     return sorted(w1) == sorted(w2)
#
# print(anagram('ic','ci'))
# print(anagram('112','121'))
#
#
# class leijia:
#     """
#     自己写的累加逻辑，类
#     """
#     def __init__(self):
#         self.add = 0
#         while self.add < 100:
#             self.add += 10
#             print(self.add)
#
#     def bu(self,max,y):
#         max = self
#
#
# leijia().bu()
#
#
# def count_characthers(string):
#     """
#     计算字母频数
#     """
#     count_dict = {}
#     for c in string:
#         if c in count_dict:
#             count_dict[c] += 1
#         else:
#             count_dict[c] = 1
#     print(count_dict)
#
# count_characthers('Dssscuubye')


def bottles_of_beer(bob):
    """
    递归,使用函数递归，牛逼
    :param bob: 瓶酒瓶数
    :return: 歌词
    """
    if bob < 1:
        print('没有啤酒了')
        return
    tmp = bob
    bob -= 1
    print('{} 瓶啤酒，还剩 {} 瓶啤酒'
          .format(tmp,bob))
    bottles_of_beer(bob)


bottles_of_beer(99)