Cmd.vim
========

Cmd.vim is a convenient way to run command line commands from within a Vim buffer, and (optionally) paste the results.

Bash Examples
--------------
Use Leader-cc to run the command on the current line, and paste it's contents below.::

    >ls
    <Leader>cc

Becomes::

    >ls
    README.rst
    bin
    plugin

If you want to just grab the results, a shortcut is <Leader>cs::

    >cat README.rst | wc -l
    <Leader>cs
The results are also are always copied into buffer 1. <Leader>cp is setup by default as a shortcut to paste from buffer 1.::

    <Leader>cp
    37

TaskWarrior Example
--------------------
I wrote this plugin to integrate my daily morning meeting notes, between Minion_ and TaskWarrior_.

Within a file named Weekly Plan for 2014-11-10.txt, I keep track of notes and tasks planned for the week.
I print this file for my morning meeting.

This file might look a bit like::

    Example Project



.. _minion: http://github.com/edthedev/minion
.. _TaskWarrior: http://taskwarrior.org/docs/tutorials/30second.html

