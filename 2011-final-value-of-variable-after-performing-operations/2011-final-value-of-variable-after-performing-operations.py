class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        val = 0
        for operation in operations:
            operator = ""
            if operation[0] == "X":
                operator = operation[-1]
            else:
                operator = operation[0]

            if operator == "-":
                val -= 1
            else:
                val += 1

        return val