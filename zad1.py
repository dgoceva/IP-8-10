import functools
import math


def input_number(prompt, error_msg, is_possitive=True):
    while True:
        try:
            x = int(input(prompt))
            if is_possitive and x <= 0:
                raise Exception('Number must be possitive')
            return x
        except ValueError:
            print(error_msg)
        except Exception as e:
            print(e)


n = input_number('N=', 'Invalid number N')
k = input_number('K=', 'Invalid number K')
nums = [input_number('X=', 'Invalid number X', False) for _ in range(n)]
print(nums)

nums1 = [x for x in nums if x > k]
print(nums1)

print(functools.reduce(lambda x, y: x*y,
      [nums1[i] for i in range(1, len(nums1), 2)]))
print(math.prod([nums1[i] for i in range(1, len(nums1), 2)]))

if len(nums1) > 0:
    print(nums1.index(min(nums1)))
else:
    print('No such data...')

nums2 = [x for x in nums if x <= k and x > 0]
print(nums2)

if len(nums2) > 0:
    print(max(nums2)-min(nums2))
else:
    print('No such data...')
