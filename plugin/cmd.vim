" ---------------
"
"		Command line helper
"
" ---------------
if !has('python')
    echo "Error: cmd.vim requires vim compiled with +python"
        finish
    endif

let s:path = expand('<sfile>:p:h')

" Setup for Python library imports.
python << endpython
import sys
import os
import vim
script_path = vim.eval('s:path')
# print script_path
lib_path = os.path.join(script_path, '../bin')
# print lib_path
sys.path.insert(0, lib_path)

# import brain_of_minion as brain
from cmd import cmd
endpython

" Archive the current open file.
" -------------------------------
function! DoCmd()
	let s:line = getline('.')

    let s:current_file = expand('%')
python << endpython
current_line = vim.eval("s:line")
output = cmd(current_line)
vim.command('let @1 = "' + output + '"')
# print output
endpython
endfunction

" Run the command and echo the output.
map <Leader>cs :call DoCmd()<cr>:echom @1<cr>
" Paste the last command output from the last run.
map <Leader>cp "1p
" Run and then paste immediately.
map <Leader>cc :call DoCmd()<cr>"1p

