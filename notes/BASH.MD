# Bash Scripting:

<center><img src="../img/tux.png" width=20%></center>

The Bourne Again Shell - wraps around the linux kernel and is a command-line interpreter or unix shell widely used in GNU/Linux Operating System written by Brian Jhan Fox. It is used as a default login shell for most Linux distributions. Scripting is used to automate the execution of the tasks so that humans do not need to perform them individually.

`#!/bin/bash` tells the system to use Bash for execution. You can also check with : `$ which $SHELL` (/bin/bash/) and to write a bash script, start with : ` $ nano file.sh`. To run the script after writing the script : ` $ bash file.sh` ( run the bash script) or  `$ chmod +x file.sh` and  `$ ./file.sh`:
 
```bash

#!/bin/bash

echo "hi 2_2"
sleep 3

name = "skk"
echo "uh uh"
sleep 3

echo "oh wow $name!"
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


### Conditional statements & loops :

<table style="width:100%" >
<tr>
<th>if else</th>
<th>for loop</th>
<th>while loop<br /></th>
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

<td>

```bash
    #!/bin/bash
    i=1
    while [[ $i -le 10 ]] ; do
    echo "$i"
    (( i += 1 ))
    done
```
<br />
</td>

</tr>
</table>

Some bash scripting examples:


<table style="width:100%" >

<tr>
<th>file3.sh</th>
<th>file4.sh<br /></th>
</tr>

<tr>

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
</tr>
</table>


`$1` is the first argument: `$ ./file4.sh saikia moinmoin`


If a variable, is declared inside a function then it is generally a local variable and if it is declared outside then it is a global variable. The > notation is used to redirect stdout to a file. On the other hand, we can use  2> notation to redirect stderr, and &>  to redirect both stdout and stderr. 

resources : [bash cheatsheet](https://devhints.io/bash), [tldp](https://tldp.org/LDP/abs/html/), [utility-bash-script](https://github.com/aviaryan/utility-bash-scripts), [Packt Publishing](https://github.com/PacktPublishing/Complete-Bash-Shell-Scripting-), [awesome-bash](https://github.com/awesome-lists/awesome-bash), [simple-bash-scripts](https://github.com/ruanyf/simple-bash-scripts), [crontab.guru](https://crontab.guru/#*_*_*_*_*)


Counting lines of code in a project : `$ alias sloc="git ls-files \"*.js*\" \"*.scss\" | xargs wc -l"`

View list of aliases in your source file : ` $ alias lsalias="grep -in --color -e '^alias\s+*' ~/mymacrc | sed 's/alias //' | grep --color -e ':[a-z][a-z0-9]*'"`

Remove Dangling Docker images : `$ alias dcdangling="docker rmi \$(docker images -f \"dangling=true\" -q)" `

Currency - Currency Converter : ` $ currency INR USD 10`

Stocks - Display stock price details : ` $ stocks Intel`

Check weather : `$ weather moon` or `$ weather hamburg`

Shorten given URL : `$ short <URL>`

Check which ciphers are enabled / disabled for a given https site : `$ siteciphers google.com`

Lyrics of a song : `$ lyrics -a michael jackson -s who is it`

YouTube from terminal : `$ ytview Ed Sheeran`


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

## .bashrc , .bash_profile, .bash_history

`.bash_profile` is read and executed when Bash is invoked as an interactive login shell, while .bashrc is executed for an interactive non-login shell.

Use .bash_profile to run commands that should run only once, such as customizing the $PATH environment variable .
Put the commands that should run every time you launch a new shell in the .bashrc file. This include your aliases and functions , custom prompts, history customizations , and so on.
Typically, `~/.bash_profile` contains lines like below that source the `.bashrc` file. This means each time you log in to the terminal, both files are read and executed.

```bash
if [ -f ~/.bashrc ]; then
	. ~/.bashrc
fi
```

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

## VARIABLES in linux :

$SHELL, $USER, $PWD, $HOSTNAME, $RANDOM

`$RANDOM`  variable  `$ echo $RANDOM` returns a random number.

We can create our own system variables: `$ twitter="florist_notes"` and ` $ echo twitter` to print variable value. Tomake it an environment variable : `$ export twitter`. To make it permanent : `$ nano .bashrc`

export twitter = "florist_notes"

save `.bashrc` and the variable will stay. For arithmetic : `$(())`, so `$ echo $(( 2 * 3 ))`


To read from a file `sample_file.txt` :

```bash
#!/bin/bash

    LINE=1

    while read -r CURRENT_LINE
        do
            echo "$LINE: $CURRENT_LINE"
        ((LINE++))
    done < "sample_file.txt"
```

If you need to include the output of a complex command in your script, you can write the statement inside back ticks.

```bash

    #!/bin/bash

    var = `df -h | grep tmpfs`
    echo $var

```
Some useful bash scripts:

Search for Files Recursively To Find an Expression : `$ find . -type f -exec grep -l "nltk" {} \;`

Print the Elapsed Time of Code Execution :

```bash

#!/bin/bash

start_time=$(date +%s)

# your code here

end_time=$(date +%s)

echo "Time elapsed: $(($end_time - $start_time)) seconds"

```

Execute Command on Each File if a Condition Is Met :

```bash

for file in *; do
    if [[ $file =~ ^[a-zA-Z] ]]; then
        # execute command on the file
        echo $file
    fi
done

```

Weather : `weather(){ curl -s "wttr.in/$1?m1"} `

`.bashrc` is read only once, when bash starts. It is just so by design (and has always been). If you make any subsequent changes to `.bashrc`, they won't be applied until `.bashrc` is re-read. By running `source .bashrc`, you make exactly this - you tell bash to re-read that file.

```bash


    $ echo " # # #             🌸  # #  "
    $ echo " * * * *                    "
    $ echo " * * * * *                  "
    $ echo " * * * * * *                "
    $ echo " * * * * * * *              "
    $ echo " * * * * * * * *            "
    $ echo " * * * * * * * * *          "
    $ echo " * * * * * * * * * *        "
    $ echo " * * * s k k * * * * *      "
    $ echo " * * * * * @ * * * * * *    "
    $ echo " * * * / b i n / b a s h /  "
    $ echo " * * * * * * * * * * * * *  "
    $ echo " * * * * * * * * * * * *    "
    $ echo " * * * * * * * * * * *      "
    $ echo " # * * * * * * * * *        "
    $ echo " * * * * * * * * *          "
    $ echo " * * * * * * * *            "
    $ echo " * * * * * * *              "
    $ echo " * * * * * *                "
    $ echo " * * * * *                  "
    $ echo " * * * *                    "
    $ echo " # # #             🌸  # #  "

```

## How to Automate Scripts by Scheduling via cron Jobs

Cron is a job scheduling utility present in Unix like systems. You can schedule jobs to execute daily, weekly, monthly or in a specific time of the day. Automation in Linux heavily relies on cron jobs. For individual users, the cron service checks the following file: `/var/spool/cron/crontabs`. In order to use cron jobs, an admin needs to allow cron jobs to be added for users in the `/etc/cron.allow` file.

To allow skk to use crons, include his name in `/etc/cron.allow`. This will allow skk to create and edit cron jobs. Users can also be denied access to cron job access by entering their usernames in the file `/etc/cron.d/cron.deny`.



To add cron Jobs in Linux : `$ sudo systemctl status cron.service` ( check running cron services ). Further cron commands :


` $ crontab -e` : edits crontab entries to add, delete, or edit cron jobs.

` $ crontab -l` : list all the cron jobs for the current user.

` $ crontab -u username -l` : list another user's crons.

` $ crontab -u username -e` : edit another user's crons.

` $ crontab -r ` : delete all scheduled tasks.

Alternatively, a root user can move their scripts into the following directories to schedule their execution:

`/etc/cron.hourly/` – Run all scripts once an hour

`/etc/cron.daily/` – Run once a day.

`/etc/cron.weekly/` – Run once a week.

`/etc/cron.monthly/` – Run once a month.


Below is the syntax to schedule crons:

```bash

# Cron job example


*   *   *   *   *  sh /path/to/script/script.sh
|   |   |   |   |              |
|   |   |   |   |      Command or Script to Execute        
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |
|   |   |   | Day of the Week(0-6)
|   |   |   |
|   |   | Month of the Year(1-12)
|   |   |
|   | Day of the Month(1-31)  
|   |
| Hour(0-23)  
|
Min(0-59)
```

Here, * represent represents minute(s) hour(s) day(s) month(s) weekday(s), respectively. Below are some examples of scheduling cron jobs.

If, for example, you want to set up a cron job to run root/backup.sh every Friday at 5:37 pm, here’s what your cron command should look like: ` $ 37 17 * * 5 root/backup.sh`.

<b>Example </b>: `5 0 * 8 *` for `At 00:05 in August.` , `5 4 * * 6` for `At 04:05 on Sunday.` and `0 22 * * 1-5` for `At 22:00 on every day-of-week from Monday through Friday`. The command `crontab -l` lists the already scheduled scripts for a particular user. To find scripts : `$ find . -type f -name "*.sh"`.

<b> L </b>: writing 3<b>L</b> in the day-of-week field means the last Wednesday of a month. (#hash) For example, 1#2 means the second Monday of the month.

Keep in mind that the cron output will be automatically sent to your local email account. If you want to stop receiving emails, you can add `>/dev/null 2>&1` to a command as in the following example: `$ 0 5 * * * /root/backup.sh >/dev/null 2>&1`.

If you want to send the output to a specific email account, add MAILTO followed by an email address. Here is an example: 

```bash
MAILTO="inbox@domain.tld"
0 3 * * * /root/backup.sh >/dev/null 2>&1
```
` * * * * *` : runs every minute

Here are some useful special strings that you can use in commands:<br /><br />

<b>@hourly.</b> The job will run once an hour. <br />
<b>@daily</b> or <b>@midnight.</b> These strings will run the task every day at midnight.<br />
<b>@weekly.</b> Use this to run jobs once a week at midnight on Sunday.<br />
<b>@monthly.</b> This special string runs a command once on the first day of every month.<br />
<b>@yearly.</b> Use this to run a task once a year at midnight on January 1st.<br />
<b>@reboot.</b> With this string, the job will run only once at startup.<br />

`@reboot /root/clearcache.sh` :	Clear cache every time you turn on the system.

`@hourly /scripts/monitor.sh` :	Perform monitoring every hour.

`0 0 * * 0 /root/backup.sh` :	Perform a backup every Sunday at midnight.

`0 * * * 1 /root/clearcache.sh` :	Clear the cache every hour on Mondays.

`0 6,18 * * * /root/backup.sh` :	Backup data twice a day at 6am and 6pm.

`*/10 * * * * /scripts/monitor.sh` :	Perform monitoring every 10 minutes.

`* * 20 7 * /root/backup.sh` :	Perform a backup every minute on July 20.

`0 22 * * 1-5 /root/clearcache.sh` :	Clear the cache every weekday (Monday to Friday) at 10pm.

`* * * 1,2,5 * /scripts/monitor.sh` :	Perform monitoring every minute during January, February, and May.

`10-59/10 5 * * * /root/clearcache.sh` :	Clear the cache every 10 minutes at 5am, starting from 5:10am.

`0 8 1 */3 * /home/user/script.sh` :	Make the task run quarterly on the first day of the month at 8am.

`0 * * * * /root/backup.sh` :	Create a backup every hour.

`* * * * * /scripts/script.sh; /scripts/scrit2.sh` :	Include multiple tasks on a single cron job. Useful for scheduling multiple tasks to run at the same time.

`@reboot /root/clearcache.sh` :	Clear cache every time you turn on the system.

`0 8 1-7 * 1 /scripts/script.sh` :	Run a script on the first Monday of each month, at 8 am.

`15 9 1,20 * * /scripts/monitor.sh` :	Perform monitoring at 9:15 pm on the 1st and 20th of every month.

`0 0 1,15 * 3 /scripts/script.sh` :	Run a script at midnight every Wednesday between the 1st and 15th of every month.

`00 08-17 * * 1-5 bin/check-db-status` :	Check database status every day from Monday to Friday every hour from 8 to 5 pm.

## How to schedule a Python script using cron job

<b>Scheduling a cron job when you have root or sudo privileges</b> :

With administrator-level access to a linux instance, the best practice for scheduling a cron job for your scripts is to create an application-specific crontab file in the server's `cron.d` directory, usually located at `/etc/cron.d/`. This "drop in" directory is scanned every minute by cron and all you need to do is copy a crontab file into place and wait for the scheduled time for your jobs to run.

The crontab file itself has a very simple format. It may include comments, environment variables, and the jobs to be run. Each job must fit on a single line that begins with a valid cron schedule expression, the user the job should run as, and finally the command string to be run

```bash

# Run the data archiver once a day as the skk user
5 4 * * * skk /etc/scripts/run_archiver.py

```

<b>Scheduling a cron job without root privileges</b>
If your system administrator allows it, cron jobs can also be scheduled by users in a private user crontab file. These user crontabs can only run commands as yourself. To interact with your user crontab, use the crontab command.

View your crontab file:

`$ crontab -l`
Open your crontab in a text editor to make updates:

`$ crontab -e`
From the text editor, add your new cron entry:

```bash
# Run the data archiver once a day
5 4 * * * /etc/scripts/run_archiver.py
```

Even though cron runs your cron jobs using a real user account, it does not trigger an interactive session, so any environment variables you may be loading in `.bash_profile` or `.bashrc` will not be available. If your script expects certain environment variables, you can either set them within the crontab file itself, or have each line of your crontab source your `.bash_profile` before invoking your script. 


`$ 5 4 * * * source ~/.bash_profile ; python /etc/scripts/run_archiver.py`


If you are using a tool like virtualenv to isolate your Python dependencies, you will need to activate that virtual environment when invoking your script. The easiest way to do this is to use the python binary symlinked in the environment:

`$ 5 4 * * * /etc/virtualenvs/example/bin/python /etc/scripts/run_archiver.py`


## Running a cron job using Celery with the beat scheduler.

Celery is a popular Python library for running background tasks with asynchronous task queues that trigger commands in a separate worker process. The most common use case is to add jobs to a celery task queue from your application code when a user does things like ask for a password reset email. When you use the celery-beat package, you can also add scheduled jobs alongside these event-driven tasks. Note: This guide assumes that you are already running Celery in your app.

First, locate your Celery initialization code and add a task for your new cron job. This is usually in a file called `tasks.py`:


```python

from celery import Celery
from celery.schedules import crontab
app = Celery()

# ... existing celery tasks here

@app.task
def run_archiver():
    from application import archiver
    archiver.run()

```

Define a beat schedule that will be read by Celery on start-up:

```json
app.conf.beat_schedule = {
    'run-archiver': {
        'task': 'tasks.run_archiver',
        'schedule': '5 4 * * *'
    },
}
app.conf.timezone = 'UTC'
```

Bonus: Automatically monitor your Celery cron jobs with Cronitor

```python

import cronitor.celery
# Discover all of your celery tasks and automatically add monitoring.
cronitor.celery.initialize(app, api_key="<cronitor api key here>")

```