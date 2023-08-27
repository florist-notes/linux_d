<table style="width:100%" >

# Linux Networking

In order to do networking with linux, having computer networks knowledge is imperative.  I studied networking (CCNA syllabus) (2015-2016) and did lot of packet tracking with [GNS 3](https://www.gns3.com/) (CISCO IOS).

<img src="net/img/hat.jpg" width=38%><a></a><img src="net/img/lab1.PNG" width=51%>

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

<tr>
<th>ip addr</th>
<td>Show IP addresses and network interfaces (modern replacement for ifconfig).<br /></td>
<td>$ ip addr<br /></td>
</tr>

<tr>
<th>ip link</th>
<td>Display and manage network device attributes.<br /></td>
<td>$ ip link<br /></td>
</tr>

<tr>
<th>traceroute <hostname or IP>	</th>
<td>Trace the route packets take to reach a destination host.<br /></td>
<td>$ traceroute &lt;hostname or IP&gt;<br /></td>
</tr>

<tr>
<th>netstat -nr</th>
<td>Show routing table (deprecated, use ip route instead).<br /></td>
<td>$ netstat -nr<br /></td>
</tr>

<tr>
<th>nslookup  &lt;hostname&gt;</th>
<td>Query DNS servers for DNS information about a domain.<br /></td>
<td>$ nslookup &lt;hostname&gt; <br /></td>
</tr>

<tr>
<th>ss or netstat -tuln </th>
<td>Display information about open network sockets.<br /></td>
<td>$ ss or netstat -tuln <br /></td>
</tr>

<tr>
<th>lsof -i</th>
<td>List open files associated with network connections.<br /></td>
<td>$ lsof -i <br /></td>
</tr>

<tr>
<th>ifup &lt;interface&gt; <hostname></th>
<td>Bring a network interface up.<br /></td>
<td>$ ifup &lt;interface&gt; <br /></td>
</tr>

<tr>
<th>ifdown &lt;interface&gt;</th>
<td>Bring a network interface down.<br /></td>
<td>$ ifdown &lt;interface&gt; <br /></td>
</tr>

<tr>
<th>vnstat</th>
<td>Monitor network traffic and bandwidth usage.<br /></td>
<td>$ vnstat<br /></td>
</tr>

</table>

I have some CISCO IOS [here](net/GNS3IOS) and CCNA [labs](net/Labs/).

<img src="net/img/net.png" width=100%>

## Socket Programming in Python :

Sockets and the socket API are used to send messages across a network. They provide a form of inter-process communication (IPC). The network can be a logical, local network to the computer, or one that’s physically connected to an external network, with its own connections to other networks. The obvious example is the Internet, which we connect to via your ISP.

```python

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

```
Here we made a socket instance and passed it two parameters. The first parameter is AF_INET and the second one is SOCK_STREAM. AF_INET refers to the address-family ipv4. The SOCK_STREAM means connection-oriented TCP protocol. The primary socket API functions and methods in this module are:

```

socket()
.bind()
.listen()
.accept()
.connect()
.connect_ex()
.send()
.recv()
.close()

```

<table width=100%>
<tr>
<th>Echo Server</th>
<th>Echo Client</th>
</tr>

<tr>
<td>

```py

import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)
print("Server is listening on port 12345")

while True:
    # Wait for a connection
    print("Waiting for a connection...")
    client_socket, client_address = server_socket.accept()

    try:
        print(f"Connection from {client_address}")
        data = client_socket.recv(1024)
        print(f"Received: {data.decode()}")

        # Send the received data back to the client
        client_socket.sendall(data)
    finally:
        # Clean up the connection
        client_socket.close()


```
</td>
<td>

```py

import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server's address and port
server_address = ('localhost', 12345)
client_socket.connect(server_address)

try:
    # Send data to the server
    message = "Hello, server!"
    client_socket.sendall(message.encode())

    # Receive the response from the server
    data = client_socket.recv(1024)
    print(f"Received: {data.decode()}")
finally:
    # Clean up the connection
    client_socket.close()


```
</td>
</tr>
</table>


resources : [socket programming](https://realpython.com/python-sockets/), [Socket Programming HOWTO](https://docs.python.org/3/howto/sockets.html)