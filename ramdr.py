import json
import os
import socket
import string
import sys
def create(name, size):
  os.mkdir(f'/mnt/{name}')
  mib_in_mb = 0.95367431640625
  size_mebibytes = int(int(size)*mib_in_mb)+1
  fstab_entry=f'{name} /mnt/{name} ramfs nodev,nosuid,noexec,nodiratime,size={size_mebibytes}M,x-gvfs-show 0 0'
  with open('/etc/fstab','a') as f:
    f.write(fstab_entry+'\n')
  os.system(f'mount /mnt/{name}')
