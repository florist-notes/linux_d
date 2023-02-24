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
<th>bc</th>
<td>high precision calculator <br /></td>
<td>$bc <br /></td>
</tr>

<tr>
<th>cd</th>
<td>change directory <br /></td>
<td>$cd - (return to previous directory) <br />
$cd ~ (Navigate to HOME directory) <br />
$cd .. (Move one level up) <br />
$cd / (Move to the root directory) <br /></td>
</tr>

<tr>
<th>ls</th>
<td>lists everything in current directory<br /></td>
<td>$ ls -la : show all files <br />
$ ls *.txt <br />
$ ls -R (Lists files in sub-directories as well)<br /></td>
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
$rm -rf Downloads/ <br />
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
<th>man / whatis / tldr</th>
<td>$man ls : manual of ls <br /></td>
<td>$whatis ls (faster man) <br />
$tldr tar <br /></td>
</tr>

<tr>
<th>chmod</th>
<td>change mode - change permission of files and directory <br /></td>
<td>- is file, d is directory, rwx is read, write & execute, -= is no permission. 3 groups - 1 (owner), 2 (group) and 3 (users).<br />
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
$echo "hey" > hey.txt  <br />
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
$echo "hey again" >> hey.txt (to append) <br /></td>
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
<th>whoami / uname -a / neofetch</th>
<td>get username <br /></td>
<td>$neofetch <br /></td>
</tr>

<tr>
<th>sudo apt update <br />
sudo apt install packagename</th>
<td>apt is the package manager <br /></td>
<td>apt-get <br /></td>
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
<th>zip / tar</th>
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
<td>find patterns in files with regex <br /></td>
<td>$sudo find / -name "thebible*" <br />
$sudo find . -type f -name "*.*"   (find all hidden files) <br />
$sudo find . -type f -empty   (empty directories) <br />
$sudo find . perm /a=x   (executible files) <br />
</td>
</tr>

<tr>
<th>chown username filename</th>
<td>change ownership of file <br /></td>
<td>- <br /></td>
</tr>

<tr>
<th>grep</th>
<td>grab particular info : grep [pattern] [file_name]<br /></td>
<td>$ip address | grep eth0 <br />
$ip address | grep eth0 | inet <br /></td>
</tr>

<tr>
<th>cmatrix -a</th>
<td>code matrix -a (asynchronous) <br /></td>
<td>- <br /></td>
</tr>

<tr>
<th>trash-list / trash-restore</th>
<td>find all files in trash can <br /></td>
<td>$sudo apt install trash-cli <br /></td>
</tr>

<tr>
<th>awk</th>
<td>filter for output commands using '{}'  <br /></td>
<td>$who | awk '{print $1,$4}' <br /></td>
</tr>

<tr>
<th>cat /etc/resolv.conf</th>
<td>DNS info <br /></td>
<td>$resolvectl status <br /></td>
</tr>

<tr>
<th>traceroute google.co.in</th>
<td>trace route to destination ip <br /></td>
<td>- <br /></td>
</tr>

<tr>
<th>ufw</th>
<td>firewall <br /></td>
<td>
$sudo ufw enable <br />
$sudo ufw status <br />
$sudo ufw allow 80 (allow port 80) <br /></td>
</tr>

<tr>
<th>cal>
<td>system calendar <br /></td>
<td>- <br /></td>
</tr>

<tr>
<th>free</th>
<td>free memory <br /></td>
<td>- <br /></td>
</tr>

<tr>
<th>ps / service</th>
<td>processes running<br /></td>
<td>$ps -aux<br />
$ps -aux | grep processname <br /></td>
</tr>

<tr>
<th>kill / pkill</th>
<td>kill process with pid <br /></td>
<td>$kill pid <br />
$kill -9 pid (-9 is force kill)<br />
$pkill -f nameofprocess<br />  </td>
</tr>

<tr>
<th>systemctl</th>
<td>systemctl <br /></td>
<td>$sudo systemctl start apache2 <br />
$sudo systemctl status apache2 <br />
$sudo systemctl restart apache2 <br />
$sudo systemctl stop apache2 <br /></td>
</tr>

<tr>
<th>history, reboot, shutdown</th>
<td>basic commands <br /></td>
<td> - <br /></td>
</tr>

<tr>
<th>progress</th>
<td>check progress of processes <br /></td>
<td>$sudo progress<br /></td>
</tr>

<tr>
<th>autojump</th>
<td>jump to directories on the fly <br /></td>
<td>$j github <br />
$j .config <br /></td>
</tr>

<tr>
<th>sudo !!</th>
<td>reruns the previous command with a sudo prefix <br /></td>
<td>$sudo !!<br /></td>
</tr>


<tr>
<th>dd</th>
<td>Majorly used for creating bootable USB sticks <br /></td>
<td>-<br /></td>
</tr>

<tr>
<th>wc</th>
<td>Word count <br /></td>
<td>$wc file.txt<br /></td>
</tr>

<tr>
<th>alias / unalias wr</th>
<td>Create custom shortcuts for your regularly used commands <br /></td>
<td>$ alias wr=”cd /var/www/html”<br /></td>
</tr>

<tr>
<th>gpg</th>
<td>Encrypt a file <br /></td>
<td>$ gpg -c [file_name]<br /></td>
</tr>

<tr>
<th>source</th>
<td>Read and execute the file content in the current shell <br /></td>
<td>$ source [filename]<br /></td>
</tr>

</table>

<table style="width:100%" >
<tr>
<th>FILESYSTEM <a href="commands/fs.MD">NOTES</a> 🔗</th>
<th>DEVOPS <a href="commands/devops.MD">NOTES</a> 🔗</th>
<th>SERVER <a href="commands/server.MD">NOTES</a> 🔗</th>
<th>SECURITY <a href="commands/security.MD">NOTES</a> 🔗</th>
</tr>


</table>