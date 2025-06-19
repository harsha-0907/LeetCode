class Solution:
    def myAtoi(self, string: str) -> int:
        string = string.lstrip()  # Fix: assign stripped result back to string
        length = len(string)
        if length == 0:
            return 0  # Edge case: empty string after stripping

        sign = '+'
        i = 0

        # Fix: prevent index error on empty or single character string
        if i < length and string[i] == '-':
            sign = '-'
            i += 1
        elif i < length and string[i] == '+':
            i += 1

        number = None

        for pos in range(i, length):
            if string[pos].isdigit():
                if number is None:
                    number = 0
                number = number * 10 + int(string[pos])
            else:
                break

        if number is None:
            return 0

        if sign == '-':
            number = -number

        # Clamp to 32-bit signed int range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if number < INT_MIN:
            return INT_MIN
        if number > INT_MAX:
            return INT_MAX

        return number
