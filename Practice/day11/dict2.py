import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
 
i = response.json()

for ele in range(len(i)): 
 print(i[ele]["user"]["login"])


