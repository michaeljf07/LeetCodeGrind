class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        sym_to_val = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1,
        }

        cur_num = num
        while cur_num != 0:
            for sym in sym_to_val:
                if cur_num - sym_to_val[sym] >= 0:
                    res += sym
                    cur_num -= sym_to_val[sym]
                    break
        
        return res
                    

