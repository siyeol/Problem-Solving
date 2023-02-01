domains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]

subdomain = dict()

for domain in domains:
    cnt, url = domain.split()
    # print(cnt, url)
    url_split = url.split(sep=".")


    for us in url_split:
        if url not in subdomain:
            subdomain[url]=int(cnt)
        else:
            subdomain[url]+=int(cnt)
        url = url[len(us)+1:]

result_list = list()
for url, cnt in subdomain.items():
    result_list.append(str(cnt)+" "+url)

print(result_list)

"""
Example 1:
Input: 
["9001 discuss.leetcode.com"]
Output: 
["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]

Example 2:
Input: 
["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
Output: 
["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
"""