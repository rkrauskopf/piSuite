from subprocess import check_call, STDOUT
import os

# installing pip3
print('Installing python3-setuptools...')
check_call(['sudo', 'apt-get', 'install', '-y', 'python3-setuptools'], stdout=open(os.devnull, 'wb'), stderr=STDOUT)

print('Installing easy_install3...')
check_call(['sudo', 'easy_install3', 'pip'], stdout=open(os.devnull, 'wb'), stderr=STDOUT)

# install git
print('Installing git...')
check_call(['sudo', 'apt-get', 'install', '-y', 'arduino'], stdout=open(os.devnull, 'wb'), stderr=STDOUT)

# install python couchdb and arduino IDE
print('Installing couchdb...')
check_call(['sudo', 'apt-get', 'install', '-y', 'couchdb'], stdout=open(os.devnull, 'wb'), stderr=STDOUT)

print('Installing arduino IDE...')
check_call(['sudo', 'apt-get', 'install', '-y', 'arduino'], stdout=open(os.devnull, 'wb'), stderr=STDOUT)

# install necessary python libraries
print('Installing python couchdb library...')
check_call(['pip3', 'install', 'couchdb'], stdout=open(os.devnull, 'wb'), stderr=STDOUT)

print('Installing python pyserial library...')
check_call(['pip3', 'install', 'pyserial'], stdout=open(os.devnull, 'wb'), stderr=STDOUT)

print('Installing python bottle library...')
check_call(['pip3', 'install', 'bottle'], stdout=open(os.devnull, 'wb'), stderr=STDOUT)