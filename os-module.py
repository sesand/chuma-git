                            # OS MOUDLE

"""
                            
import os
print(dir(os))

"""
#output
"""
['DirEntry', 'F_OK', 'GenericAlias', 'Mapping', 'MutableMapping', 'O_APPEND', 'O_BINARY', 'O_CREAT', 'O_EXCL',
 'O_NOINHERIT', 'O_RANDOM', 'O_RDONLY', 'O_RDWR', 'O_SEQUENTIAL', 'O_SHORT_LIVED', 'O_TEMPORARY', 'O_TEXT', 
 'O_TRUNC', 'O_WRONLY', 'P_DETACH', 'P_NOWAIT', 'P_NOWAITO', 'P_OVERLAY', 'P_WAIT', 'PathLike', 'R_OK', 'SEEK_CUR',
 'SEEK_END', 'SEEK_SET', 'TMP_MAX', 'W_OK', 'X_OK', '_AddedDllDirectory', '_Environ', '__all__', '__builtins__', 
 '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_check_methods', 
 '_execvpe', '_exists', '_exit', '_fspath', '_get_exports_list', '_walk', '_wrap_close', 'abc', 'abort', 'access',
 'add_dll_directory', 'altsep', 'chdir', 'chmod', 'close', 'closerange', 'cpu_count', 'curdir', 'defpath',
 'device_encoding', 'devnull', 'dup', 'dup2', 'environ', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv',
 'execve', 'execvp', 'execvpe', 'extsep', 'fdopen', 
'fsdecode', 'fsencode', 'fspath', 'fstat', 'fsync', 'ftruncate', 'get_exec_path', 'get_handle_inheritable', 
'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 'getenv', 'getlogin', 'getpid', 'getppid', 
'isatty', 'kill', 'linesep', 'link', 'listdir', 'lseek', 'lstat', 'makedirs', 'mkdir', 'name', 'open', 'pardir',
'path', 'pathsep', 'pipe', 'popen', 'putenv', 'read', 'readlink', 'remove', 'removedirs', 'rename', 'renames',
'replace', 'rmdir', 'scandir', 'sep', 'set_handle_inheritable', 'set_inheritable', 'spawnl', 'spawnle', 'spawnv', 
'spawnve', 'st', 'startfile', 'stat', 'stat_result', 'statvfs_result', 'strerror', 'supports_bytes_environ',
'supports_dir_fd', 'supports_effective_ids', 'supports_fd', 'supports_follow_symlinks', 'symlink', 'sys', 'system',
'terminal_size', 'times', 'times_result', 'truncate', 'umask', 'uname_result', 'unlink', 'unsetenv', 'urandom', 
'utime', 'waitpid', 'waitstatus_to_exitcode', 'walk', 'write']

"""


import os

# directory information
"""
print(os.getcwd())      # current working directory
"""
#output

#C:\Users\admin\Desktop\html\python


# modify our path (directory)
"""

print(os.chdir("C:\\Users\\admin\\Desktop\\html\\python\\MODULES"))  # change directory

"""
# elements are presented in directory
"""
print(os.listdir())

"""
# make to create a new directory
"""
print(os.mkdir("builtin-modules"))

"""

"""
print(os.listdir())

"""
"""
print(os.makedirs("MODULES1/BUILTIN-MODULES"))

"""

"""
print(os.rmdir("BUILTIN-MODULES"))

"""

"""
print(os.removedirs("MODULES1/BUILTIN-MODULES"))

"""


# rename file

"""
print(os.rename("filereading.txt","file-reading.txt"))

"""

# file inoformation(view all infromation)

"""
print(os.stat("gowtham1.txt"))

"""
#output
"""
os.stat_result(st_mode=33206, st_ino=1125899907646396, st_dev=4264735422,
st_nlink=1, st_uid=0, st_gid=0, st_size=1439, st_atime=1686743186, st_mtime=1669900497, st_ctime=1686459457)
"""
#atime-->access time, mtime--->modify time, ctime--->last created time


# view particular information only (but not readable form)
"""
print(os.stat('gowtham1.txt').st_atime)
print(os.stat('gowtham1.txt').st_ctime)
print(os.stat('gowtham1.txt').st_mtime)
print(os.stat('gowtham1.txt').st_mode)

"""     
#output

#1686743186.7658486
#1686459457.2307143
#1669900497.8464565
#33206

# to access data and time to readable format

"""
from datetime import datetime
mtime=os.stat('gowtham1.txt').st_mtime
print(datetime.fromtimestamp(mtime))

"""
#output
#2022-12-01 05:14:57.846457



# walk()--> information get current working files
# its a generator which gives a 3 tuple of values. 

#print(os.getcwd())

"""
for dirpath,dirs,files in os.walk('C:\\Users\\admin\\Desktop\\html\\python'):
    print("directory path",dirpath)
    print('directories',dirs)
    print("files",files)

"""    
#output

#directory path C:\Users\admin\Desktop\html\python\exmployee complaint management
#directories ['__pycache__']
#files ['db.py', 'main.py']
#directory path C:\Users\admin\Desktop\html\python\exmployee complaint management\__pycache__
#directories []
#files ['db.cpython-310.pyc']
#directory path C:\Users\admin\Desktop\html\python\MODULES
#directories ['builtin-modules']
#files []
#directory path C:\Users\admin\Desktop\html\python\MODULES\builtin-modules
#directories []
#files []
#directory path C:\Users\admin\Desktop\html\python\__pycache__
#directories []
#files ['functions.cpython-310.pyc', 'modules.cpython-310.pyc']

"""
print(os.walk("C:\\Users\\admin\\Desktop\\html\\python"))

"""



