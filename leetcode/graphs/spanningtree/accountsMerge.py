# Merging various accounts 

class Person:
    def __init__(self, account):
        self.name = account[0]
        self.emails = account[1:]
        self.adj = set()
    
def mergeAccountsBruteForce(accounts):
    Persons = dict()
    for account in accounts:
        p1 = Person(account)
        for mail in p1.emails:
            for p in Persons:
                if mail in p.emails:
                    p1.adj.add(p)
                    p.adj.add(p1)
        Persons[p1] = 0
    # Now we have connected all common identities
    def dfs(node, parent):
        nonlocal mails
        Persons[node] = 1
        for mail in node.emails:
            mails.add(mail)
        
        adjnodes = node.adj
        for nextnode in adjnodes:
            if nextnode == parent or Persons[nextnode] == 1:
                continue
            else:
                dfs(nextnode, node)
        


    final = []
    for p1 in Persons:
        if Persons[p1] == 0:
            acc = [p1.name]
            # Not yet visited
            mails = set()
            dfs(p1, None)
            acc.extend(list(mails))
            final.append(acc)
    
    return final


def mergeAccountsUnionFind(accounts):
    # Here, we will use union-find by rank to determine the number of accounts
    n = len(accounts)
    parents = {i: i for i in range(n)}
    emails = dict(); cnt = 0
    for account in accounts:
        mails = account[1:]; imparents = []
        for mail in mails:
            if mail in emails:
                imparents.append(emails[mail])
            else:
                emails[mail] = cnt
            
        # We have all the parents for a node
        if imparents != []:
            p = min(imparents)
            parents[cnt] = p

            for pp in imparents[1:]:
                parents[pp] = p
    
    final = []
    def find(node):
        if parents[node] == node:
            return node
        else:
            parents[node] = find(parents[node])
            return parents[node]
    
    
    
            


accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
res = mergeAccountsBruteForce(accounts)
print(res)