#Task2: Restricting push to the master

#Logic used:
    #if push to master:
        #output  “You are not allowed to push to master branch” 
    #else:
        #output “ push to remote successful”
        
        
   
#!/usr/bin/env python
import sys
import re
import os
from subprocess import check_output

protected = 'refs/heads/master'
inp_command = sys.stdin.read()
branch_name = inp_command.split()
print("remote branch name :", branch_name[2])

if (protected != branch_name[2]):
    print('into if clause')
    print('push to remote successful')
    sys.exit(0)

else :
    print('into else clause')
    print('you are not allowed to push to the master branch')
    sys.exit(1)







