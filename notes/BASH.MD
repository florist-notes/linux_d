# Bash Scripting:

Bourne Again Shell - wraps around the linux kernel. Bash is a command-line interpreter or Unix Shell and it is widely used in GNU/Linux Operating System.  It is written by Brian Jhan Fox. It is used as a default login shell for most Linux distributions. Scripting is used to automate the execution of the tasks so that humans do not need to perform them individually.

`#!/bin/bash` tells the system to use Bash for execution. 
 
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
     
Age=17
if [ "$Age" -ge 18 ]; then
    echo "You can vote"
else
    echo "You cannot vote"    
fi

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

If a variable, is declared inside a function then it is generally a local variable and if it is declared outside then it is a global variable. The > notation is used to redirect stdout to a file. On the other hand, we can use  2> notation to redirect stderr, and &>  to redirect both stdout and stderr. 

resources : [bash cheatsheet](https://devhints.io/bash)


<table style="width:100%" >

<tr>
<th>bash script 1</th>
<th>bash script 2 </th>
<th>bash script 3 <br /></th>
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

</table>