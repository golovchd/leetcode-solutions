class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        l = len(num)
        for n1_length_s in range(1, l // 2 + 1):
            for n2_length_s in range(1, l - 2 * n1_length_s + 1):
                s = 0
                n1_length = n1_length_s
                n2_length = n2_length_s
                while s < l and s + n1_length + n2_length <= l:
                    n3_start = s + n1_length + n2_length
                    if (n1_length > 1 and num[s:s + 1] == '0' or
                        n2_length > 1 and num[s + n1_length:s + n1_length + 1] == '0' or
                        max(n1_length, n2_length) > 1 and num[n3_start:n3_start + 1] == '0'):
                        break
                    n1 = int(num[s:s + n1_length])
                    n2 = int(num[s + n1_length:s + n1_length + n2_length])
                    n3 = n1 + n2
                    n3str = str(n3)
                    n3_length = len(n3str)
                    if n3_length > 1 and num[n3_start:n3_start + 1] == '0':
                        break
                    if num[n3_start:n3_start + n3_length] != n3str:
                        break
                    if n3_start + n3_length == l:
                        return True
                    n1 = n2
                    n2 = n3
                    s += n1_length
                    n1_length = n2_length
                    n2_length = n3_length
        return False
