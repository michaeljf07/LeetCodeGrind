class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_map = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)

        visited = set()

        def dfs(course: int):
            # Cycle detected
            if course in visited:
                return False

            # Course has no prereqs
            if len(prereq_map[course]) == 0:
                return True

            visited.add(course)
            for prereq in prereq_map[course]:
                if not dfs(prereq):
                    return False

            visited.remove(course)
            prereq_map[course] = [] # marks course as "safe" to avoid redundant work
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
 