

from pathlib import Path
from re import search, sub

fstabread = Path('/etc/fstab').read_text().splitlines()
fstab = {x.split()[1] for x in fstabread if x.startswith('UUID')}
mountread = Path('/proc/mounts').read_text().splitlines()
mounts = {y.split()[1] for y in mountread if search(r'^/dev/(?!.*snap)', y)}
out = fstab - mounts

if not out:
    print("All disks mounted correctly.")
else:
    print('These were not mounted: ', *out, sep='\n')
