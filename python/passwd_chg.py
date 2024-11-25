# jsteeleiv 2023

# Automatically change password for a user.

# USAGE: `sudo passwd_ch.py <username> <password>`
# TEST}: `sudo chage -l {user} | head -1`

import sys
import subprocess as sp
user, passwd = sys.argv[1:]
passwd = passwd.encode() + b'\n'
subk = dict(stdout=sp.PIPE, stdin=sp.PIPE, stderr=sp.PIPE)
change=sp.Popen(['passwd', user], **subk)
for i in range(2):
    change.stdin.write(passwd)