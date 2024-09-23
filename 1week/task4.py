from collections import Counter, defaultdict


"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/sort-characters-by-frequency/description/
"""


class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join([char * count for char, count in Counter(s).most_common()])


# another solution
"""
class Solution:
    def frequencySort(self, s: str) -> str:
        result = []

        count = Counter(s)
        buckets = defaultdict(list)

        for char, freq in count.items():
            buckets[freq].append(char)

        for i in range(len(s), 0, - 1):
            for char in buckets[i]:
                result.append(char * i)
        return ''.join(result)
"""

solution = Solution()
print(solution.frequencySort("Aabb"))  # bbAa
