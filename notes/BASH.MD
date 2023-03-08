# Bash Scripting:

<center><img src="../img/tux.png" width=20%></center>

The Bourne Again Shell - wraps around the linux kernel and is a command-line interpreter or Unix Shell widely used in GNU/Linux Operating System written by Brian Jhan Fox. It is used as a default login shell for most Linux distributions. Scripting is used to automate the execution of the tasks so that humans do not need to perform them individually.

`#!/bin/bash` tells the system to use Bash for execution. You can also check with : `$ which $SHELL (/bin/bash/)` and to write a bash script : ` $ nano file.sh`. To run the script after writing the script : ` $ bash file.sh` ( run the bash script) or  `$ chmod +x file.sh` and  `$ ./file.sh`:
 
```bash

#!/bin/bash

echo "hi 2_2"
sleep 3

echo "uh uh"
sleep 3

echo "oh wow"
sleep 3

echo "bye"
     
Age=17
if [ "$Age" -ge 18 ]; then
    echo "You can vote"
else
    echo "You cannot vote"    
fi

var=$((3+9))
echo $var

```


<table style="width:100%" >

<tr>
<th>file2sh</th>
<th>file3.sh</th>
<th>file4.sh<br /></th>
</tr>

<tr>
<td>

```bash

    #!/bin/bash

    name="skk"

    echo "hi $name"
    echo "lets take on this challenge $name"

```
<br /></td>
<td>


```bash
#!/bin/bash

echo "What is your name ?"
read name

echo "hello $name!! good to see you."

```
<br /></td>


<td>


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
<br /></td>
`$1` is the first argument: `$ ./file4.sh saikia moinmoin`


If a variable, is declared inside a function then it is generally a local variable and if it is declared outside then it is a global variable. The > notation is used to redirect stdout to a file. On the other hand, we can use  2> notation to redirect stderr, and &>  to redirect both stdout and stderr. 

resources : [bash cheatsheet](https://devhints.io/bash), [tldp](https://tldp.org/LDP/abs/html/)

### Basic Conditional Statements & Loops :

<tr>
<th>if else</th>
<th>loop</th><br /></th>
</tr>

<tr>
<td>

```bash

    if [[ condition ]]
    then
        statement
    elif [[ condition ]]; then
        statement 
    else
        do this by default
    fi

```

<br /></td>

<td>

```bash

    #!/bin/bash

    for X in cyan magenta yellow  
    do
        echo $X
    done

```

<br /></td>

</tr>
</table>


<table style="width:100%" >

<tr>
<th>file5.sh</th>
<th>file6.sh</th>
<th>file7.sh<br /></th>
</tr>

<tr>
<td>

```bash

        #!/bin/bash

        var1="Apple" #global variable
        myfun(){
            local var2="Banana" #local variable
            var3="Cherry" #global variable
            echo "The name of first fruit is $var1"
            echo "The name of second fruit is $var2"
        }
        myfun #calling function


        Name="Saikia"
        if [ "$Name" = "Saikia" ]; then
        echo "His name is Saikia. It is true."
        fi

```
<br /></td>
<td>

```bash

    echo "Enter filename"
    read filename

    if [ -e $filename ]
    then
    echo "$filename is exits on the directory"
    cat $filename

    else
        cat > $filename
        echo "File created"
    fi


    if [ 10 -eq 10 ];then
    echo "Equal"
    fi

    if [ 'Geeks' == 'Geeks' ];
    then
        echo "same" #output
    else
        echo "not same"
    fi
```
<br /></td>

<td>

```bash

Name="Saikia"
case "$Name" in
    #case 1
    "Saikia") echo "Profession : Software Engineer" ;;
    
    #case 2
    "skk") echo "Profession : Web Developer" ;;
    
    #case 3
    "florist_notes") echo "Profession : Technical Content Writer" ;;
esac

```
<br /></td>
</tr>

</table>

#### String and Numeric Comparisons :


<table style="width:100%" >

<tr>
<th>Operator</th>
<th>Description</th>
<th>Operator</th>
<th>Description</th><br />
</tr>

<tr>
<td>
==
<br /></td>
<td>
 Returns true if the strings are equal
<br /></td>

<td>
!=
<br /></td>
<td>
 Returns true if the strings are not equal
<br /></td>
</tr>


<tr>
<td>
-n
<br /></td>
<td>
Returns true if the string to be tested is not null
<br /></td>
<td>
-z
<br /></td>
<td>
Returns true if the string to be tested is null
<br /></td>
</tr>

<tr>
<td>
-eq
<br /></td>
<td>
Equal
<br /></td>

<td>
-ge
<br /></td>
<td>
Greater Than or Equal
<br /></td>
</tr>

<tr>
<td>
-gt
<br /></td>
<td>
Greater Than
<br /></td>

<td>
-le
<br /></td>
<td>
Less Than or Equal
<br /></td>
</tr>
<tr>
<td>
-lt
<br /></td>
<td>
Less Than
<br /></td>

<td>
-ne
<br /></td>
<td>
Not Equal
<br /></td>
</tr>


<tr>
<td>
-a
<br /></td>
<td>
AND statement
<br /></td>

<td>
-o
<br /></td>
<td>
OR statement
<br /></td>
</tr>

</table>

### .bashrc
The .bashrc file is a hidden script file containing various terminal session configurations. The file executes automatically in both interactive and non-interactive non-login shells.

When running a non-login shell (subshell), the primary read configuration file is the `/etc/bash.bashrc`. The file contains system-wide configurations for non-login shells.

### .bash_profile
The .bash_profile file is a hidden script file with custom configurations for a user terminal session. The file automatically executes in Bash interactive login shells.

When running an interactive login shell, the system reads the following configuration file first:

`/etc/profile` - Stores global configurations for login shells. The configurations apply to all users.
Next, the Bash shell searches for specific user configuration files in the following order:

`~/.bash_profile` <br />
`~/.bash_login` <br />
`~/.profile` <br />

<b>.bashrc</b> defines the settings for a user when running a <b>subshell</b>. Add custom configurations to this file to make parameters available in subshells for a specific user. <br />

<b>.bash_profile</b> defines the settings for a user when running a <b>login shell</b>. Add custom configurations to this file to make parameters available to a specific user when running a login shell.