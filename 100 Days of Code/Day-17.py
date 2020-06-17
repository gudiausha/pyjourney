#Task-1: Restricting the commit if invalid commit message is present
#Logic used:
    #if  commit message has the word ‘banglore’ in it :
        #then output “Your commit is successful”
    #else :
        #output “Invalid commit”


#!/usr/bin/env python
import sys
import os
import re

name = 'banglore'
message_file = open(sys.argv[1],'r')
commit_msg = message_file.read()

def check_msg(commit_msg):
    print("name variable :" , name)
    print("commit msg : ", commit_msg)
    
    if bool(re.search(name,commit_msg))==True:
        print('into if statement')
        print("Your commit is successful")
        sys.exit(0)
    else:
        print('into else statement')
        print("Invalid commit")
        sys.exit(1)

if __name__ == '__main__':
    check_msg(commit_msg)
