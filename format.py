import re
import os
import sys

rstr1 = r'''([\\\[\{\(\)\]\},\.\_\^\*\~\&\+\-\|])\s+(\w)|(\w)\s+([\\\[\{\(\)\]\},\.\_\^\*\~\&\+\-\|])'''
rstr2 = r'''([\{\}\|\)\(+-\^\_])\s+([\\\}\{\-\+\^])'''

targets = [n for n in os.listdir('./') if n.endswith('.md')]

print(targets)

for n in targets:
    with open(n, 'r') as f:
        ctx = f.read()
    ctx = re.sub(rstr1, r'\1\2', ctx)
    ctx = re.sub(rstr2, r'\1\2', ctx)
    with open(n, 'w') as f:
        f.write(ctx)
