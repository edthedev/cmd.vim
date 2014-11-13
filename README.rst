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
    ---------------
    >task list project:example

    ID Proj    Age Description
    -- ------- --- ----------------------------
     5 example 2m  This is a thing to do.
     6 example 2m  Here is another thing to do.
     7 example 2m  And a third thing to do.

     3 tasks

During the day, I might complete a couple of tasks::

    >task 5 done
    >task 7 done

To update my week plan file, I delete the previous list, and then move the cursor to the line::

    >task list project:example

And run <Leader>cc::

    >task list project:example

    ID Proj    Age Description
    -- ------- --- ----------------------------
     5 example 3m  Here is another thing to do.

    1 task

.. _minion: http://github.com/edthedev/minion
.. _TaskWarrior: http://taskwarrior.org/docs/tutorials/30second.html

Install 
-----------------------------
This plugin is packaged for use with Vundle_, and requires Vim_ compiled with Python_ support.
(Vim_ is typically packaged with Python_ support, this plugin will warn you if it is not.)

.. _Vim: http://vim.org/about.php
.. _Python: http://python.org
.. _Vundle: https://github.com/gmarik/vundle/blob/master/README.md 

Install and configure Vundle_ and then add 'edthedev/cmd.vim' to your .vimrc.::

    Bundle 'edthedev/cmd.vim'

Then, from within Vim, run BundleInstall.::

    :BundleInstall


