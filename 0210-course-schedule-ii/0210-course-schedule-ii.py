class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_map = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)

        res = []
        visited = set() # Store verified courses
        cycle = set() # Track courses in branch to check for cycles

        def dfs(course: int) -> bool:
            # Cycle detected, i.e. course invalid
            if course in cycle:
                return False
            
            # Already verified course
            if course in visited:
                return True

            cycle.add(course)
            for prereq in prereq_map[course]:
                if not dfs(prereq):
                    return False

            cycle.remove(course)
            visited.add(course)
            res.append(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return res