from collections import defaultdict

class Solution(object):
    def accountsMerge(self, accounts):
        parent = {}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)
        
        # Har email ko uske parent se initialize karo
        email_to_name = {}
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                email_to_name[email] = name
                # Pehle email se baaki sab merge karo
                union(account[1], email)
        
        # Root email ke around group karo
        groups = defaultdict(list)
        for email in parent:
            groups[find(email)].append(email)
        
        return [[email_to_name[root]] + sorted(emails)
                for root, emails in groups.items()]

#----Testing----
solver = Solution()
print(solver.accountsMerge([
    ["John","johnsmith@mail.com","john_newyork@mail.com"],
    ["John","johnsmith@mail.com","john00@mail.com"],
    ["Mary","mary@mail.com"],
    ["John","johnnybravo@mail.com"]
]))