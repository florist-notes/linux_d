Linux Command Pallette:

<table style="width:100%" >

<tr>
<th>command</th>
<th>description <br /></th>
<th>reference <br /></th>
</tr>

<tr>
<th>pwd</th>
<td>present working directory <br /></td>
<td>- <br /></td>
</tr>

<tr>
<th>cd</th>
<td>change directory <br /></td>
<td>- <br /></td>
</tr>

<tr>
<th>ls</th>
<td>lists everything in current directory<br /></td>
<td>$ ls -la : show all files <br /></td>
</tr>

<tr>
<th>mkdir / rmdir</th>
<td>make directory or remove directory <br /></td>
<td>- <br /></td>
</tr>

<tr>
<th>echo, cp, rm, mv, touch, locate</th>
<td>basic commands <br /></td>
<td>
$echo "Hi!" > test.txt <br />
$touch test.txt <br />
$cp test.txt Downloads/ <br />
$rm Downloads/text.txt <br />
$rm -r Downloads/ <br />
$mv test.txt Downloads/ <br />
$locate golaghat.py <br />

</td>
</tr>

<tr>
<th>updatedb</th>
<td>updates the database <br /></td>
<td>- <br /></td>
</tr>

<tr>
<th>passwd</th>
<td>change system password <br /></td>
<td>- <br /></td>
</tr>

<tr>
<th>man / whatis</th>
<td>$man ls : manual of ls <br /></td>
<td>$whatis ls (faster man) <br /></td>
</tr>

<tr>
<th>chmod</th>
<td>change mode - change permission of files and directory <br /></td>
<td>- is file, d is directory, rwx is read, write & execute. 3 groups - 1 (owner), 2 (group) and 3 (users).<br />
$ chmod +x (give execute permission).<br />
$ chmod 777 hello.txt (all group rwx access).<br /></td>
</tr>

<tr>
<th>adduser</th>
<td>add new users <br /></td>
<td>$adduser skk <br />
$cat /etc/passwd <br />
$cat /etc/shadow <br />
</td>
</tr>

<tr>
<th>/etc/passwd , /etc/shadow</th>
<td>user passwords are stored in /shadow in hash and can be cracked with hashcat. <br /></td>
<td>$sudo passwd root <br /></td>
</tr>

<tr>
<th>su</th>
<td>switch user <br /></td>
<td>$su skk <br /></td>
</tr>

<tr>
<th>sudo</th>
<td>root priviledges <br /></td>
<td>- <br /></td>
</tr>

<tr>
<th>ifconfig</th>
<td>information on ipv4, v6, mac address, subnet mask etc <br /></td>
<td>- <br /></td>
</tr>

<tr>
<th>iwconfig</th>
<td>- <br /></td>
<td>- <br /></td>
</tr>

<tr>
<th>ping</th>
<td>- <br /></td>
<td>- <br /></td>
</tr>

<tr>
<th>arp</th>
<td>maps ip addresses to mac addresses <br /></td>
<td>- <br /></td>
</tr>

<tr>
<th>netstat</th>
<td>display all connections <br /></td>
<td>- <br /></td>
</tr>

<tr>
<th>route</th>
<td>displays routing table <br /></td>
<td>- <br /></td>
</tr>

<tr>
<th>echo</th>
<td>echoes in terminal <br /></td>
<td>$echo "hello" <br />
$echo "hey" > hey.txt  (to append)<br />
</td>
</tr>

<tr>
<th>cat / shred</th>
<td>prints out what's in a file or block/shred <br /></td>
<td>$cat hey.txt <br />
$shred hey.txt <br /></td>
</tr>

<tr>
<th>replacing vs appending (> vs >>)</th>
<td>- <br /></td>
<td>
$echo "hey again" >> hey.txt <br /></td>
</tr>

<tr>
<th>touch</th>
<td>create a file <br /></td>
<td>$touch newfile.txt <br /></td>
</tr>

<tr>
<th>nano / vim</th>
<td>text editor built in terminal <br /></td>
<td>$nano newfile.txt <br />
$vim newfile.txt <br /></td>
</tr>

<tr>
<th>gedit</th>
<td>gui text editor <br /></td>
<td>$gedit newfile.txt <br /></td>
</tr>

<tr>
<th>ssh user@ip</th>
<td>remote access <br /></td>
<td>- <br /></td>
</tr>

<tr>
<th>ln -s</th>
<td>create soft links <br /></td>
<td>$ln -s abc.txt xyz.txt <br /></td>
</tr>

<tr>
<th>clear</th>
<td>clear the terminal <br /></td>
<td>- <br /></td>
</tr>

<tr>
<th>whoami</th>
<td>get username <br /></td>
<td>- <br /></td>
</tr>

<tr>
<th>sudo apt update <br />
sudo apt install packagename</th>
<td>apt is the package manager <br /></td>
<td>- <br /></td>
</tr>

<tr>
<th>finger</th>
<td>inspect a user <br /></td>
<td>$sudo apt install finger <br />
$finger username <br /></td>
</tr>

<tr>
<th>which / whereis</th>
<td>finds address or location of package <br /></td>
<td>$which finger <br />
$whereis finger <br /></td>
</tr>

<tr>
<th>wget/ curl addresslink</th>
<td>download content from internet <br /></td>
<td>- <br /></td>
</tr>

<tr>
<th>zip</th>
<td>zip files <br /></td>
<td>$zip filename.zip allfiles.txt <br />
$unzip filename.zip<br /></td>
</tr>

<tr>
<th>less, head, tail</th>
<td>check sections of a file <br /></td>
<td>- <br /></td>
</tr>

<tr>
<th>cmp/ diff file1 file2</th>
<td>compare or find differences in two files <br /></td>
<td>- <br /></td>
</tr>

<tr>
<th>cat file.txt | sort</th>
<td>the whole text file sorted <br /></td>
<td>- <br /></td>
</tr>

<tr>
<th>find</th>
<td>find patterns in files with regrex <br /></td>
<td>$sudo find / -name "thebible*" <br />
$sudo find . -type f -name "*.*"   (find all hidden files) <br />
$sudo find . -type f -empty   (empty directories) <br />
$sudo find . perm /a=x   (executible files) <br />
</td>
</tr>

<tr>
<th>ssh user@ip</th>
<td>remote access <br /></td>
<td>- <br /></td>
</tr>

<tr>
<th>ssh user@ip</th>
<td>remote access <br /></td>
<td>- <br /></td>
</tr>

<tr>
<th>ssh user@ip</th>
<td>remote access <br /></td>
<td>- <br /></td>
</tr>

<tr>
<th>ssh user@ip</th>
<td>remote access <br /></td>
<td>- <br /></td>
</tr>

<tr>
<th>ssh user@ip</th>
<td>remote access <br /></td>
<td>- <br /></td>
</tr>

<tr>
<th>ssh user@ip</th>
<td>remote access <br /></td>
<td>- <br /></td>
</tr>

<tr>
<th>ssh user@ip</th>
<td>remote access <br /></td>
<td>- <br /></td>
</tr>

<tr>
<th>ssh user@ip</th>
<td>remote access <br /></td>
<td>- <br /></td>
</tr>

<tr>
<th>ssh user@ip</th>
<td>remote access <br /></td>
<td>- <br /></td>
</tr>

<tr>
<th>ssh user@ip</th>
<td>remote access <br /></td>
<td>- <br /></td>
</tr>

</table>