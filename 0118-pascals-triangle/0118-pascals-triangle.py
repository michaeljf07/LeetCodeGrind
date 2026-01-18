class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def gen_row(prev_row: list[int]):
            new_row = [1]

            for i in range(1, len(prev_row)):
                new_row.append(prev_row[i-1] + prev_row[i])

            new_row.append(1)

            return new_row

        ans = [[1]]
        for i in range(1, numRows):
            ans.append(gen_row(ans[-1]))
        
        return ans