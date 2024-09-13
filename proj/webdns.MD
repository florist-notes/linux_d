# 1 Web server with [NGINX](https://www.nginx.com/)

#### [Install and configure Nginx](https://ubuntu.com/tutorials/install-and-configure-nginx#1-overview), [linuxserver.io](https://www.linuxserver.io/)

<center><img src="un.jpg" width=80%></center><br />

NGINX is a high-performance web server, reverse proxy server, and load balancer known for its speed, scalability, and low resource consumption. It is widely used in both small-scale websites and large-scale enterprise environments.

```bash
    $ sudo apt install nginx
```

Once NGINX is installed, you need to start the service and enable it to start automatically at boot.

```bash
    $ sudo systemctl start nginx
    $ sudo systemctl status nginx
```

+ Configure the Firewall : If you have a firewall enabled, you’ll need to allow HTTP and HTTPS traffic to pass through. ` $ sudo ufw allow 'Nginx Full'`.

At this point, NGINX is running. You can verify it by visiting your server's IP address in a browser (e.g., `http://your-server-ip`). You should see the default NGINX welcome page.

Configure NGINX Server Block (Virtual Host) : NGINX uses server blocks to host multiple websites on the same server. Here's how to create a new server block.
+ Create a directory for your website content: ` $ sudo mkdir -p /var/www/example.com/html`.
+ Set ownership of the directory to your user: ` $ sudo chown -R $USER:$USER /var/www/example.com/html`.
+ Set appropriate permissions: ` $ sudo chmod -R 755 /var/www/example.com`.
+ Create a sample index.html file: ` $ nano /var/www/example.com/html/index.html`.
+ Create a new server block configuration file: ` $ sudo nano /etc/nginx/sites-available/example.com`.

```
server {
    listen 80;
    server_name example.com www.example.com;

    root /var/www/example.com/html;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}
```
+ Enable the server block: ` $ sudo ln -s /etc/nginx/sites-available/example.com /etc/nginx/sites-enabled/`.
+ Test the configuration for syntax errors: ` $ sudo nginx -t`.
+ Reload NGINX to apply the changes: ` $ sudo systemctl reload nginx`.

`Main Configuration File`: Located at `/etc/nginx/nginx.conf`. This file contains the global settings for NGINX.

`Site-Specific Configuration`: Located in `/etc/nginx/sites-available/` and `/etc/nginx/sites-enabled/`. By default, NGINX serves sites from `/var/www/html`.

+ To secure your website with HTTPS, you can use Let's Encrypt for free SSL certificates. Install CertBlock : ` $ sudo apt install certbot python3-certbot-nginx`.
+ Obtain an SSL certificate: ` $ sudo certbot --nginx -d example.com -d www.example.com`.
+ Test automatic renewal: ` $ sudo certbot renew --dry-run`.
+ Access logs: ` $ sudo tail -f /var/log/nginx/access.log`.
+ Error logs: ` $ sudo tail -f /var/log/nginx/error.log `.


Resources : [Install a webserver on Linux in 15 minutes
](https://youtu.be/7GTYB8RVYBc), [Reverse proxy nginx letsencrypt tutorial](https://youtu.be/DyXl4c2XN-o), [How To Install Nginx on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-20-04), [Linux Server Course - System Configuration and Operation](https://youtu.be/WMy3OzvBWc0), [How to Install and Configure NGINX Web Server in Ubuntu 22.04 LTS](https://youtu.be/7YqlP7HYU1g), [The NGINX Crash Course](https://youtu.be/7VAI73roXaY), [Nginx Server | Install on Ubuntu 20.04](https://youtu.be/JD2Hm8tymgY), [Flask Load Balancing Using Nginx and Docker](https://youtu.be/42Q65H8ch7U), [Python Flask Tutorial: Deploying Your Application (Option #1) - Deploy to a Linux Server](https://youtu.be/goToXTC96Co), [Python Flask Tutorial: How to Use a Custom Domain Name for Our Application](https://youtu.be/LUFn-QVcmB8), [Deploy Flask Application on Ubuntu VPS using Nginx](https://youtu.be/BpcK5jON6Cg), [How to Deploy a Flask App to a Linux Server](https://youtu.be/YFBRVJPhDGY).