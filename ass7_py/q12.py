# 12.Write a function to copy data from one machine to another machine.

import os
import paramiko

def copy_data_one_machine_to_another(hostname,username,password,scr_dir,dest_dir):
    ssh_client=paramiko.SSHClient()  
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=hostname,username=username,password=password)
    sftp = ssh_client.open_sftp() 

    sftp.put(scr_dir,dest_dir)
    sftp.close()


if __name__ == "__main__":
    hostname  = "ubuntu2004"
    username='ubuntu'
    password='palkesh@02'
    scr_dir  = os.getcwd()
    file_name = input("Enter file name :")
    scr_dir = os.path.join(file_name)
    dest_dir = "/home/ubuntu/folder1/file_name.py"
    copy_data_one_machine_to_another(hostname,username,password,scr_dir,dest_dir)
