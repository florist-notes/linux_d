<table style="width:100%" >

# Linux Networking

I studied networking (CCNA syllabus) (2015-2016) and did lot of packet tracking with GNS3 (CISCO IOS).

<center><img src="net/img/hat.jpg" width=40%><a></a><img src="net/img/lab1.PNG" width=54%></center>

Linux Networking Command Pallette🌸:

<table style="width:100%" >

<tr>
<th>command</th>
<th>description <br /></th>
<th>reference <br /></th>
</tr>

<tr>
<th>ifconfig</th>
<td>Display and manipulate route and network interfaces.<br /></td>
<td>$ ifconfig<br /></td>
</tr>

<tr>
<th>ip</th>
<td>It is a replacement of ifconfig command. Use ip link show command to display all network interfaces on the system.<br /></td>
<td>$ ip link show<br /></td>
</tr>

<tr>
<th>ip route show</th>
<td>Use the IP route to print or display the routing table.<br /></td>
<td>$ ip route show<br /></td>
</tr>

<tr>
<th>ping -c 3 google.com </th>
<td>By default, ping runs in an infinite loop. To send a defined number of packets, use -c flag<br /></td>
<td>$ ping -c 3 google.com <br /></td>
</tr>

<tr>
<th>ss -t -a</th>
<td> ss command with -t and -a flags to list all TCP sockets. This displays both listening and non-listening sockets. ss gets details about network sockets.<br /></td>
<td>$ ss -t -a<br /></td>
</tr>

<tr>
<th>iftop</th>
<td>Monitors stats related to bandwidth.<br /></td>
<td>$ iftop<br /></td>
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

<tr>
<th>lastlog </th>
<td> The lastlog command is used to find the details of a recent login of all users or of a given user.<br /></td>
<td>$lastlog <br /></td>
</tr>

<tr>
<th>firewalld</th>
<td>CLI tool to configure rules of Firewall.<br /></td>
<td>$ firewalld<br /></td>
</tr>

<tr>
<th>tcpdump</th>
<td>Packet sniffing and analyzing utility used to capture, analyze and filter network traffic.<br /></td>
<td>$ tcpdump<br /></td>
</tr>

</table>

I have some CISCO IOS [here](net/GNS3IOS) and CCNA [labs](net/Labs/).

<img src="net/img/net.png" width=100%>

