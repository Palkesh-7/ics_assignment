# 14.Write a function to change permission of file or directories.

import os
import stat
pwd=os.getcwd()
file_name = input("Enter file name :")
path = os.path.join(pwd,file_name)
os.chmod(path, stat.S_IREAD)
print("The file can only be ready by owner")





# Os.chmod() modes
# Following are the different mode arguments of os.chmod() −

# stat.S_ISUID − On execution, set the group ID.
# stat.S_ENFMT − Records must be locked.
# stat.S_ISVTX − after execution, saves the text image
# stat.S_IREAD − Reading by owner.
# stat.S_IWRITE − Writing by owner.
# stat.S_IEXEC − Execution by owner.
# stat.S_IRWXU − Reading, writing, and execution by owner
# stat.S_IRUSR − Reading by owner
# stat.S_IWUSR − Writing by owner.
# stat.S_IXUSR − Execution by owner.
# stat.S_IRWXG − Reading, writing, and execution by group
# stat.S_IRGRP − Reading by group
# stat.S_IWGRP − Writing by group
# stat.S_IXGRP − Execution by group
# stat.S_IRWXO − Reading, writing, and execution by others.
# stat.S_IROTH − Reading by others
# stat.S_IWOTH − Writing by others
# stat.S_IXOTH − Execution by others