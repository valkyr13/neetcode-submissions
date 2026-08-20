class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        universal_hm = {}
        nodes = len(accounts)

        self.parent = [i for i in range(nodes)]

        def find(i):
            if self.parent[i] == i:
                return i
            self.parent[i] = find(self.parent[i])
            # 0 -> 1 , 1 -> 2 case - transitive case
            return self.parent[i]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                self.parent[root_i] = root_j

        for j in range(nodes):
            row = accounts[j]            
            for i in range(1,len(row)):
                if row[i] not in universal_hm:
                    universal_hm[row[i]] = j
                else:
                    union(j, universal_hm[row[i]])

        ans = defaultdict(list)

        for email, person in universal_hm.items():
            parent = find(person)
            ans[parent].append(email)

        
        return [[accounts[person_idx][0]] + sorted(emails) for person_idx, emails in ans.items()]