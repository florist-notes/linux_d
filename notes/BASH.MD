# Bash Scripting:

Bourne Again Shell - wraps around the linux kernel.


```bash
 :~# which $SHELL (/bin/bash/)
 :~# echo "Hi 2_2" ( #! is called shebang )
 :~# nano file.sh

#!/bin/bash

echo "hi 2_2"

 :~# bash file.sh ( run the bash script) or  :~# chmod +x file.sh and  :~# ./file.sh
 :~# nano file.sh

#!/bin/bash

echo "hi 2_2"
sleep 3

echo "uh uh"
sleep 3

echo "oh wow"
sleep 3

echo "bye"

 :~# 

```
file2.sh :

```bash
#!/bin/bash

name="skk"

echo "hi $name"
echo "lets take on this challenge $name"
```
file3.sh :

```bash
#!/bin/bash

echo "What is your name ?"
read name

echo "hello $name!! good to see you."

```
`$1` is the first argument: `$ ./file4.sh saikia moinmoin`

file4.sh:
```bash
#!/bin/bash

name=$1
compliment=$2

user=$(whoami)
date2=$(date)
whereami=$(pwd)

echo "hello $name!! good to see you."
echo "message foor you: $compliment."

sleep 2

echo "You are currently logged in as $user and you are in the $whereami. Today: $date2"

```

[bash cheatsheet](https://devhints.io/bash)