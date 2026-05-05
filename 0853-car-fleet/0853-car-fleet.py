class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for i in range(len(position)):
            pairs.append((position[i], speed[i]))
        
        pairs.sort(reverse=True, key=lambda x: x[0])

        fleets = 1
        prev_time = (target - pairs[0][0]) / pairs[0][1]
        for i in range(1, len(pairs)):
            curr_car = pairs[i]
            curr_time = (target - curr_car[0]) / curr_car[1]
            if curr_time > prev_time:
                fleets += 1
                prev_time = curr_time
        
        return fleets     