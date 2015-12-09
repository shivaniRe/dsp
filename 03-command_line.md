# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > rm -rf : Command removes directory with files in it.
* (asterisk): symbol is to say "anything". Wherever you put *, the shell will build a list of all the files that match the non-asterisk part.
find: command is used to search for all the files.
grep: is used to search for different words in all the files in the directory. e.g.: grep <word> *.txt (find all the .txt files with the word) or grep "<list of words/ a sentence>" *.txt
man: command is used to find information about commands. e.g.: man find, man less etc
apropos: This command looks through all the help files and finds the relevant help even if you forget the name of a command and know what it does.
chown: utility changes the user ID and/or the group ID of the specified files.
chmod: utility modifies the file mode bits of the listed files as specified by the mode operand. It may also be used to modify the Access Control Lists (ACLs) associated with the listed files.
xargs: is used to construct srgument list and execute utility.
sudo: allows a permitted user to execute a command as the superuser or another user, as specified in the sudoers file.



What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

> > 'ls' is used to list the contents of a directory. 
'ls -a' lists all the directory entries whose names begin with a dot (.). 
'ls -l' forces the output to be one entry per line.
'ls -lh' List files in the long format with unit suffixes like Byte, Kilobyte, Megabyte, Gigabyte, Terabyte and Petabyte in order	to reduce the number of digits to four or fewer.

---


---

What does `xargs` do? Give an example of how to use it.

> > xargs reads the standard input stream data and converts it into arguments to the command.
e.g.: $ echo a b c d e f| xargs
a b c d e f

---

