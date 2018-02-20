# Video Demonstrating how it works:

https://www.youtube.com/watch?v=d8ANItKGWzg 


# FAQ:

1) What it does?

It will identify users with SYSDBA and DBA rights in a given list of Oracle Servers. It will show the results on the screen and also will generate a report /tmp/PrivilegedAccounts.xls


2) Why this name "ronaldo"? 

Ronaldo was very good goalkeeper and he played for Corinthians for several years - https://www.youtube.com/watch?v=iGj2TQFSWK8 .


3) Why I wrote this tool?

The goal is to assist sysadmins, IT auditors and other people to identify the most powerful privileged accounts on Oracle Databases.


4) Can I modify this tool?

Sure, it's a free and open-source tool.


5) How to install it?

Just download the tool (ronaldo.py) and copy it to a folder in your Linux system with python installed. You might need to update python with the following libraries: cx_Oracle, getpass, sys, os,  xlwt, termcolor.
I developed this tool using the Kali Linux, since all python libraries where already installed.
Note: This is the version that I used: Linux kali 4.13.0-kali1-amd64 #1 SMP Debian 4.13.10-1kali2 (2017-11-08) x86_64 GNU/Linux


6) How do I run this tool?

Type: "python ronaldo.py -h" for more information.

Usage..: 

Usage   --> python ronaldo.py <<username>> <<path+filename>>

Example --> python ronaldo.py bcaseiro /tmp/serverlist.txt

Note: Oracle servers should be listed with its instance name, like the list below:

oracleserver01/xe

oracleserver02/dev

oracleserver03/production
