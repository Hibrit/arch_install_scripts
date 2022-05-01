#!/usr/bin/python3

#! we can still use dialog instead of curses through a connector api
#! see pythondialog on pypi

#! we will run commands in background and track their stdouts stdinps in order to control them (Threading)

#! remember to track error logs to a proper file

#! at the end of the process give user to opportunity to save their installation for sharing!
#! remember we have a system that we can share our installations with it

# import subprocess


# subprocess.call('echo test'.split())
# print(subprocess.STDIN)
# subprocess.call('ls -l'.split())
# print(subprocess.STDIN)


# print(subprocess.PIPE)

# process = subprocess.Popen(
#     'echo test'.split(), stdout=subprocess.PIPE, stdin=subprocess.PIPE)

# process.stdin.write(b'date > /tmp/test.txt')
#output = process.stdout.read()

# output, error = process.communicate()
# print(output)
# print(error)


# process.stdin.write('date && zsh -c "date >> /tmp/test.txt"')
# output, error = process.communicate()
# print(output)
# print(error)
