class Solution:
    def maxDiff(self, num: int) -> int:
        num_str = str(num)

        for d in num_str:
            if d != '9':
                max_num = int(num_str.replace(d, '9'))
                break
        else:
            max_num = num 

        first_digit = num_str[0]
        if first_digit != '1':
            min_num = int(num_str.replace(first_digit, '1'))
        else:
            for d in num_str[1:]:
                if d != '0' and d != '1':
                    min_num = int(num_str.replace(d, '0'))
                    break
            else:
                min_num = num  

        return max_num - min_num
