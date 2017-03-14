
import subprocess
import sys
import os
from shutil import copyfile

HOST="webserver"
#COMMAND="scp /home/ec2-user/workspace/WebProject/target/courseProject.war ec2-user@webserver:/home/ec2-user/dest/"

COMMAND="scp"
DEST=" /var/lib/tomcat/webapps"
SOURCE="ec2-user@buildnode:/home/ec2-user/workspace/WebProject/target/courseProject.war"
LOCALWEBSERVER="/home/ec2-user/dest/courseProject.war"
#REMOTEWEBSERVER="/home/ec2-user/dest/"

ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND, SOURCE, LOCALWEBSERVER],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
result = ssh.stdout.readlines()
if result == []:
	cmd = "ssh webserver sudo  cp " + LOCALWEBSERVER + DEST
	os.system(cmd)
	#error = ssh.stderr.readlines()
    #print >>sys.stderr, "ERROR: %s" % error
else:
    print("Success2")
	
#copyfile('/home/ec2-user/dest/courseProject.war', '/home/ec2-user/dest/courseProject2.war' )


