# git ssh setup:

### Check if SSH Key is Added to Your GitHub Account:
First, make sure you have an SSH key on your local machine. You can check by running:
```bash
    $ ls -al ~/.ssh
```
Look for files named `id_rsa` and `id_rsa.pub`. If they don’t exist, you’ll need to create a new SSH key.

### Generate a New SSH Key (If Necessary):
If you don’t have an SSH key, generate one by running:
```bash
    $ ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```
Press Enter to accept the default file location, and optionally, enter a passphrase.

### Add Your SSH Key to the SSH Agent:
Start the SSH agent:
```bash
    $ eval "$(ssh-agent -s)"
```
Add your SSH private key to the agent:
```bash
    $ ssh-add ~/.ssh/id_rsa
```

### Add the SSH Key to Your GitHub Account:
Copy the SSH key to your clipboard:
```bash
    $ cat ~/.ssh/id_rsa.pub | xclip -selection clipboard 
```
Go to your GitHub SSH settings and click New SSH Key. Paste your key and give it a title.

### Test Your Connection:
Test your SSH connection to GitHub:
```bash
    $ ssh -T git@github.com
```

You should see a message like: `Hi username! You've successfully authenticated, but GitHub does not provide shell access.`.

### Verify Remote URL in Git:
Make sure your repository’s remote URL is set to use SSH, not HTTPS:
```bash
    $ git remote -v
```
If it shows an HTTPS URL, you can change it to SSH:
```bash
    $ git remote set-url origin git@github.com:username/repository.git
```

If you prefer not to install xclip, you can also manually copy the SSH key by displaying it in the terminal and copying it: ` $ cat ~/.ssh/id_rsa.pub`.