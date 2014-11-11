#!/usr/bin/env python2
"""
This is a line.
    >echo Hello World and all that.

"""
import subprocess

def find_cmd(line):
    return line.lstrip('\t').lstrip(' ').lstrip('>')

def cmd(line):
    # output = subprocess.check_output("echo Hello")
    command = find_cmd(line)
    output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()
    return output
