"""
leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/subdomain-visit-count/description/?envType=problem-list-v2&envId=hash-table&difficulty=MEDIUM
"""

from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_count = {}
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count = int(count)
            domain = domain.split(".")
            for i in range(len(domain)):
                subdomain = ".".join(domain[i:])
                domain_count[subdomain] = domain_count.get(subdomain, 0) + count
        return [f"{count} {domain}" for domain, count in domain_count.items()]


solution = Solution()
print(
    solution.subdomainVisits(["9001 discuss.leetcode.com"])
)  # ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
