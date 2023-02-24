Linux Command Pallette:

<table style="width:100%" >

<tr>
<th>command</th>
<th>description <br /></th>
<th>reference <br /></th>
</tr>

<tr>
<th>nohup skk.py</th>
<td>run skk.py immune to hangup signal <br /></td>
<td>$sudo nohup ./mn.sh > myscipt.sh & <br /></td>
</tr>

<tr>
<th>command &</th>
<td>run < command> and send task to background <br /></td>
<td>$nohup command &<br /></td>
</tr>

<tr>
<th>fg %N</th>
<td>go to task N <br /></td>
<td>$fg %N<br /></td>
</tr>

<tr>
<th>chgrp -c -R</th>
<td>change file group permission <br /></td>
<td>$chgrp -c -R<br /></td>
</tr>

<tr>
<th>du -s</th>
<td>disk usage <br /></td>
<td>$du -s<br /></td>
</tr>

<tr>
<th>file -b -</th>
<td>identify the file type<br /></td>
<td>$file -b -<br /></td>
</tr>

<tr>
<th>free -m</th>
<td>display free and used system memory<br /></td>
<td>$free -m<br /></td>
</tr>

<tr>
<th>sensors</th>
<td>CPU temperature <br /></td>
<td>-<br /></td>
</tr>

<tr>
<th>dmesg -k</th>
<td>display system messages<br /></td>
<td>$dmesg -k<br /></td>
</tr>

<tr>
<th>mount / unmount</th>
<td>mount a filesystem<br /></td>
<td>$mount -a -t<br />
$umount -f -v<br /></td>
</tr>

<tr>
<th>df -h, -</th>
<td>File system usage<br /></td>
<td>$df -h, -<br /></td>
</tr>

<tr>
<th>mkfs -t -V</th>
<td>create file system<br /></td>
<td>$mkfs -t -V<br /></td>
</tr>

<tr>
<th>fsck -A -N</th>
<td>file system check & repair<br /></td>
<td>$fsck -A -N<br /></td>
</tr>

<tr>
<th>fdisk -l</th>
<td>edit disk partition<br /></td>
<td>$fdisk -l<br /></td>
</tr>

<tr>
<th>pvcreate / lvcreate</th>
<td>create physical / logical volume<br /></td>
<td>-<br /></td>
</tr>

<tr>
<th>cat /proc/cpuinfo</th>
<td>see CPU information<br /></td>
<td>$cat /proc/cpuinfo<br /></td>
</tr>

<tr>
<th>lshw</th>
<td>list hardware configuration information<br /></td>
<td>$lshw<br /></td>
</tr>

<tr>
<th>lspci -tv</th>
<td>show PCI devices in a tree like diagram<br /></td>
<td>$lspci -tv<br /></td>
</tr>

<tr>
<th>lsusb -tv</th>
<td>display USB devices in a tree like diagram<br /></td>
<td>$lsusb -tvbr /></td>
</tr>

<tr>
<th>dmidecode</th>
<td>display hardware information from the BIOS<br /></td>
<td>$dmidecode<br /></td>
</tr>

<tr>
<th>hdparm -i /dev/disk</th>
<td>display disk data information<br /></td>
<td>$hdparm -i /dev/disk<br /></td>
</tr>

<tr>
<th>hdparm </th>
<td>Conduct a read-speed test on device/disk:<br /></td>
<td>$hdparm -tT /dev/[device]<br /></td>
</tr>


</table>