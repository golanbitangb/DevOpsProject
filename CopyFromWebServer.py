
import subprocess
import sys
import os
from shutil import copyfile

HOST="buildnode"
#COMMAND="scp /home/ec2-user/workspace/WebProject/target/courseProject.war ec2-user@webserver:/home/ec2-user/dest/"

COMMAND="scp"
DEST=" /var/lib/tomcat/webapps"
REMOTEWEBSERVER="ec2-user@webserver:/home/ec2-user/dest/"
SOURCE="/home/ec2-user/workspace/WebProject/target/courseProject.war"
LOCALWEBSERVER="/home/ec2-user/dest/courseProject.war"
ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND, SOURCE, REMOTEWEBSERVER],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
result = ssh.stdout.readlines()
if result == []:
	cmd = "sudo cp -r " + LOCALWEBSERVER + DEST
	os.system(cmd)
else:
    print("golan2")
	
#copyfile('/home/ec2-user/dest/courseProject.war', '/home/ec2-user/dest/courseProject2.war' )


