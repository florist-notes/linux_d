









<img src="../img/fs2.png" width=100%>


resources : [Linux Directories Explained in 100 Seconds](https://youtu.be/42iQKuQodW4), [Navigating the Linux Filesystem](https://youtu.be/BNL3qBN9pP0), [the Linux File System explained in 1,233 seconds](https://youtu.be/A3G-3hp88mo), [Linux File System/Structure Explained!](https://youtu.be/HbgzrKJvDRw), [Introduction to Linux – Full Course for Beginners](https://youtu.be/sWbUDq4S6Y8)

Everything in linux is a "file" - "On a UNIX system, everything is a file; if something is not a file, it is a process.".

### Linux Filesystem

<table style="width:100%" >

<tr>
<th>distro</th>
<th>description <br /></th>
</tr>

<tr>
<th>/bin</th>
<td>Common programs, shared by the system, the system administrator and the users.<br /></td>
</tr>


<tr>
<th>/boot</th>
<td>The startup files and the kernel, vmlinuz. In some recent distributions also grub data. Grub is the GRand Unified Boot loader and is an attempt to get rid of the many different boot-loaders we know today.<br /></td>
</tr>


<tr>
<th>/dev</th>
<td>Contains references to all the CPU peripheral hardware, which are represented as files with special properties.<br /></td>
</tr>


<tr>
<th>/etc</th>
<td>Most important system configuration files are in /etc, this directory contains data similar to those in the Control Panel in Windows<br /></td>
</tr>


<tr>
<th>/home</th>
<td>Home directories of the common users.<br /></td>
</tr>


<tr>
<th>/lib</th>
<td>Library files, includes files for all kinds of programs needed by the system and the users.<br /></td>
</tr>


<tr>
<th>/net</th>
<td>Standard mount point for entire remote file systems<br /></td>
</tr>


<tr>
<th>/proc</th>
<td>A virtual file system containing information about system resources. More information about the meaning of the files in proc is obtained by entering the command man proc in a terminal window. The file proc.txt discusses the virtual file system in detail.<br /></td>
</tr>


<tr>
<th>/root</th>
<td>The administrative user's home directory. Mind the difference between /, the root directory and /root, the home directory of the root user.<br /></td>
</tr>


<tr>
<th>/sbin</th>
<td>Programs for use by the system and the system administrator.<br /></td>
</tr>


<tr>
<th>/tmp</th>
<td>Temporary space for use by the system, cleaned upon reboot, so don't use this for saving any work!<br /></td>
</tr>


<tr>
<th>/usr</th>
<td>Programs, libraries, documentation etc. for all user-related programs.<br /></td>
</tr>


<tr>
<th>/var</th>
<td>Storage for all variable files and temporary files created by users, such as log files, the mail queue, the print spooler area, space for temporary storage of files downloaded from the Internet, or to keep an image of a CD before burning it.<br /></td>
</tr>


<tr>
<th>/opt</th>
<td>Typically contains extra and third party software.<br /></td>
</tr>


<tr>
<th>/mnt</th>
<td>Standard mount point for external file systems, e.g. a CD-ROM or a digital camera.<br /></td>
</tr>

<tr>
<th>/misc</th>
<td>For miscellaneous purposes.<br /></td>
</tr>

<tr>
<th>/initrd</th>
<td>(on some distributions) Information for booting. Do not remove!<br /></td>
</tr>

<tr>
<th>/lost+found</th>
<td>Every partition has a lost+found in its upper directory. Files that were saved during failures are here.<br /></td>
</tr>
</table>
