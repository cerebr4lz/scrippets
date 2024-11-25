

fstab_mnt=($(awk '/^UUID/{print $2}' /etc/fstab))
curr_mnt=($(grep -P '/^dev/(?!.*snap)' /proc/mounts | awk '{print $2}'))
for i in ${fstab_mnt[@]}
do
if [[ ${curr_mnt[@]} != *"$i"* ]]
then
echo "Not Mounted!"
grep "$i" /etc/fstab | awk '{print $2}'
out='fail'
fi
done
if [ -z $out ]
then
echo "All disks mounted correctly!"
fi

