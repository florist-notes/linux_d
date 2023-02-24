Linux Command Pallette:

<table style="width:100%" >

<tr>
<th>command</th>
<th>description <br /></th>
<th>reference <br /></th>
</tr>

<tr>
<th>uname -r</th>
<td>Show system information via uname command<br /></td>
<td>$uname -r<br /></td>
</tr>

<tr>
<th>uname -a</th>
<td>See kernel release information<br /></td>
<td>$uname -a<br /></td>
</tr>

<tr>
<th>uptime</th>
<td>Display how long the system has been running, including load average<br /></td>
<td>$uptime<br /></td>
</tr>

<tr>
<th>hostname</th>
<td>See system hostname<br /></td>
<td>$hostname<br />
$hostname -i (Show the IP address of the system)<br />

</td>
</tr>

<tr>
<th>last reboot </th>
<td>List system reboot history<br /></td>
<td>$last reboot<br /></td>
</tr>

<tr>
<th>scp</th>
<td>Copy a file to a server directory securely<br /></td>
<td>$scp [file_name.txt] [server/tmp]<br /></td>
</tr>

<tr>
<th>ulimit</th>
<td>View or limit system resource amounts<br /></td>
<td>$ulimit [flags] [limit]<br /></td>
</tr>

<tr>
<th>last </th>
<td>Show last system logins:<br /></td>
<td>$last<br /></td>
</tr>

<tr>
<th>who </th>
<td>Display who is currently logged into the system<br /></td>
<td>$who<br /></td>
</tr>

<tr>
<th>w</th>
<td>Show which users are logged in and their activity<br /></td>
<td>$w<br /></td>
</tr>

<tr>
<th>pstree </th>
<td>Process in a tree like diagram<br /></td>
<td>$pstree<br /></td>
</tr>

<tr>
<th>pmap</th>
<td>Display a memory usage map of processes<br /></td>
<td>$pmap<br /></td>
</tr>

<tr>
<th>pidof</th>
<td>Gives the Process ID (PID) of a process<br /></td>
<td>$pidof<br /></td>
</tr>

<tr>
<th>nice</th>
<td>Starts a process with a given priority<br /></td>
<td>$nice<br /></td>
</tr>

<tr>
<th>renice</th>
<td>Changes priority of an already running process<br /></td>
<td>$renice<br /></td>
</tr>

<tr>
<th>sudo passwd -l 'username'</th>
<td>To change the password of a user<br /></td>
<td>$sudo passwd -l 'username'<br /></td>
</tr>

<tr>
<th>sudo userdel -r 'username'</th>
<td>To remove a newly created user<br /></td>
<td>$sudo userdel -r 'username'<br /></td>
</tr>

<tr>
<th>sudo usermod -a -G GROUPNAME USERNAME</th>
<td>To add a user to a group<br /></td>
<td>$sudo usermod -a -G GROUPNAME USERNAME<br /></td>
</tr>

<tr>
<th>dmesg</th>
<td>Display messages in kernel ring buffer<br /></td>
<td>$dmesg<br /></td>
</tr>

<tr>
<th>cat /proc/cpuinfo</th>
<td>Display CPU information<br /></td>
<td>$cat /proc/cpuinfo<br /></td>
</tr>

<tr>
<th>cat /proc/meminfo</th>
<td>Display memory information<br /></td>
<td>$cat /proc/meminfo<br /></td>
</tr>

<tr>
<th>mpstat 1 / vmstat 1 / iostat 1</th>
<td>Display processor, virtual memory and I/O related statistics<br /></td>
<td>-<br /></td>
</tr>

<tr>
<th>tcpdump -i eth0</th>
<td>Capture and display all packets on interface eth0<br /></td>
<td>$tcpdump -i eth0<br /></td>
</tr>

<tr>
<th>tcpdump -i eth0 'port 80'</th>
<td>Monitor all traffic on port 80 ( HTTP )<br /></td>
<td>$tcpdump -i eth0 'port 80'<br /></td>
</tr>

<tr>
<th>lsof</th>
<td>List all open files on the system<br /></td>
<td>$lsof -u user (List files opened by user)<br /></td>
</tr>

<tr>
<th>last</th>
<td>Display the last users who have logged onto the system.<br /></td>
<td>$last<br /></td>
</tr>

<tr>
<th>netstat -pnltu</th>
<td>See active (listening) ports with the netstat command<br /></td>
<td>$netstat -pnltu<br /></td>
</tr>

<tr>
<th>netstat -nutlp</th>
<td>Show tcp and udp ports and their programs<br /></td>
<td>$netstat -nutlp<br /></td>
</tr>

<tr>
<th>dig [domain] </th>
<td>Show DNS information about a domain using the dig command<br /></td>
<td>$dig [domain] <br /></td>
</tr>

<tr>
<th>dig -x [ip_address]</th>
<td>Do reverse lookup of an IP address<br /></td>
<td>$dig -x [ip_address]<br /></td>
</tr>

</table>