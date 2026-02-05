class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = {}
        for cpdomain in cpdomains:
            count,domains = cpdomain.split()
            domains = domains.split(".")
            last = ""
            for i in range(len(domains)-1,-1,-1):
                domain = domains[i]
                last = domain + "." + last if last else domain
                d[last] = d.get(last,0) + int(count)
                
        res = []
        for domain in d:
            entry = str(d[domain]) +" "+domain
            res.append(entry)
        return res