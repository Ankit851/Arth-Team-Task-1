import os
import getpass

print("""-------------------------------------------------------------  Password Protected !! -----------------------------------------------------------------
""")


apass = "neeraj"
count=0


def yum_configure():
	os.system("cp epel.repo dock.repo  epel-playground.repo epel-testing.repo root.repo rpmfusion-free-updates.repo rpmfusion-free-updates-testing.repo /etc/yum.repos.d/ ")
	print("Your yum is configured now check it by 'yum repolist' command.")
	x=input("Enter to continue...")

def docker_install():
	os.system("yum install docker-ce --nobest -y")
	os.system("systemctl start docker")
	os.system("systemctl enable docker")
	os.system("firewall-cmd --zone=public --add-masquerade --permanent")
	os.system("firewall-cmd --zone=public --add-port=80/tcp")
	os.system("firewall-cmd --zone=public --add-port=443/tcp")
	os.system("firewall-cmd --reload")
	os.system("systemctl restart docker")
	os.system("yum install httpd")
	os.system("systemctl enable httpd")
	print("Docker-CE successfully installed.")
	x=input("Enter to continue...")

def docker_pull():
	imgname=input("Enter image with version. for ex- centos:7 : ")
	os.system("docker pull {}".format(imgname))
	print("{} image downloaded successfully.".format(imgname))
	x=input("Enter to continue...")

def docker_images():
	print("""
								Available Images
""")
	os.system("docker images")
	x=input("Enter to continue...")

def docker_create_image():
	print("""
								Available Containers
""")
	os.system("docker ps -a")
	own_image = input("Give name to your own image with version. for ex- myimage:v1 : ")
	which_image = input("Container Name : ")
	os.system("docker commit {0}{1}".format(which_image,own_image))	
	x=input("Enter to continue...")

def docker_remove_image():
	print("""
								Available Images
""")
	os.system("docker images")
	rimage = input("Image name with version. for ex- myimage:v1 : ")
	os.system("docker rmi {}".format(rimage))
	print("{} image successfully removed.".format(rimage))
	x=input("Enter to continue...")

def docker_running_con():
	os.system("docker ps")
	x=input("Enter to continue...")

def docker_all_con():
	print("""
								All Containers
""")
	os.system("docker ps -a")
	x=input("Enter to continue...")

def docker_start():
	print("""
								Available Containers
""")
	os.system("docker ps -a")
	start = input("Container Name : ")
	os.system("docker start {}".format(start))
	print("{} container start successfully.".format(start))
	x=input("Enter to continue...")

def docker_stop():
	print("""
								Running Containers
""")
	os.system("docker ps")
	stop = input("Container Name : ")
	os.system("docker stop {}".format(stop))
	print("{} container stopped successfully.".format(stop))
	x=input("Enter to continue...")

def docker_terminate():
	print("""
								All Containers
""")
	os.system("docker ps -a")
	terminate = input("Container Name : ")
	os.system("docker stop {}".format(terminate))
	print("{} container terminated successfully.".format(terminate))
	x=input("Enter to continue...")

def new_con():
	print("""
								Available Images
""")
	os.system("docker images")
	cname=input('Container Name : ')
	iname = input('Enter image name with version. for ex- centos:7 : ')
	os.system("docker run -dit --name {} {}".format(cname,iname))
	print("{} container created successfully.".format(cname))
	print("press 'left ctrl' and hold 'p' and 'q' to detech.")
	x=input("Enter to continue...")

def docker_attach():
	print("""
								Available Containers
Note : You can only attach to the running container.
""")
	os.system("docker ps")
	attach = input("Container name to attach.")
	os.system("docker attach {}".format(attach))
	print("press 'left ctrl' and hold 'p' and 'q' to detach.")
	x=input("Enter to continue...")

def remove_con():
	print("""
								Available Containers
""")
	os.system("docker ps -a")
	remove = input("Container Name or ID : ")
	os.system("docker rm -f {}".format(remove))
	print("{} container removed successfully.".format(remove))
	x=input("Enter to continue...")

def remove_all_con():
	print("""
								Available Containers
""")
	os.system("docker ps -a")
	print("Warning not recommended.")
	os.system("docker rm -f $(docker ps -a)")
	print("successfully removed all containers.")
	x=input("Enter to continue...")

def show_vol():
	os.system("docker volume ls")
	x=input("Enter to continue...")

def create_vol():
	vol=input("volume name.")
	os.system("docker create volume {}".format(vol))
	print("successfully created volume. {}".format(vol))
	x=input("Enter to continue...")

def remove_vol():
	print("""
								Available Volumes
""")
	os.system("docker volume ls")
	rvol=input("volume name.")
	os.system("docker volume rm {}".format(rvol))
	print("successfully removed volume. {}".format(rvol))
	x=input("Enter to continue...")
	
def con_ip():
	con_name=input("Container name.")
	os.system("docker inspect --format {{.NetworkSteetings.IPAddress}} {}".format(con_name))
	x=input("Enter to continue...")

def docker_cpu():
	print("If you struck in between press 'left ctrl' + 'c' + os.system('watch -n 1 free -m')")
	os.system("watch -n 1 free -m")
	x=input("Enter to continue...")

def active_port():
	os.system("netstat -tnlp")
	x=input("Enter to continue...")

def wordpress():
	os.system(' curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose')
	os.system("chmod +x /usr/local/bin/docker-compose")
	os.system("cp docker-compose.yml /") 
	os.system("cd / ")
	os.system("mkdir /infrastructure")
	os.system("cd /infrastructure/")
	os.system("pwd")
	os.system("mv ../docker-compose.yml .")
	os.system("docker-compose up -d")
	print("Wordpress is ready to use. Run Wordpress in browser with Base OS IP and port no. : 8080. for ex- 192.168.43.139:8080")
	x=input("""

Details :
	MYSQL_ROOT_PASSWORD : rootpass
	MYSQL_USER : neeraj
	MYSQL_PASSWORD : redhat
	MYSQL_DATABASE : db

	Container : neeraj
	Image : mysql:5.7

Press Enter to continue...""")

def docker_jenkin():
	print("""
								Available Images
""")
	os.system("docker images")
	jname=input('\nContainer Name : ')
	img_name = input('Enter image name with version. for ex- centos:7 : ')
	os.system("docker run -dit --name {} {}".format(jname,img_name))
	print("downloading jenkins....")
	os.system("sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat/jenkins.repo")
	os.system("sudo rpm --import https://pkg.jenkins.io/redhat/jenkins.io.key")
	os.system("yum install jenkins")
	print("Jenkins is ready to use. Run Jenkins in browser with Container IP and port no. : 8080. for ex- 192.168.43.139:8080")
	print("""

Details :
	Container : {0}
	Image : {1}	""".format(jname,img_name))

	print("{} container created successfully.".format(jname))
	x=input("Enter to continue...")
	



while count < 3:
	passwd = getpass.getpass("								Enter Password : ")
	if apass != passwd:
		print("Try Again!!")
		count+=1
	else:
		while True:	
			os.system("clear")

			print("""
							   Welcome to Docker Menu
							  ________________________

								  Images
								  ------
			1 Docker Install		2 Available Docker Images	3 Download Docker Image
			4 Create Image			5 Remove Image

								 Containers
								 ----------
 			6 Show Running Containers	7 Attach Container 		8 All Containers
			9 Launch Container		10 Stop Container Service	11 Start Container Service
			12 Delete Container 		13 Delete All Containers	14 Show Container IP

								Infrastructure
								--------------
			15 Launch Wordpress		16 Launch Jenkins			

								   Volume
								   ------
			17 Create Volume		18 See Volumes			19 Remove Volume
								
								  Settings
								  --------
			20 Yum Configuration 		21 Monitor Docker CPU		22 Active Ports
			
			23 Exit""")

			ch=int(input("Enter your choice. "))


			if ch == 1:
				docker_install()
				continue
			elif ch == 2:
				docker_images()
				continue				
			elif ch == 3:
				docker_pull()
				continue
			elif ch == 4:
				docker_create_image()
				continue
			elif ch == 5:
				docker_remove_image()
				continue
			elif ch == 6:
				docker_running_con()
				continue			
			elif ch == 7:
				docker_attach()
				continue
			elif ch == 8:
				docker_all_con()
				continue
			elif ch == 9:
				new_con()
				continue
			elif ch == 10:
				docker_stop()
				continue
			elif ch == 11:
				docker_start()
				continue
			elif ch == 12:
				remove_con()
				continue			
			elif ch == 13:
				remove_all_con()
				continue
			elif ch == 14:
				con_ip()
				continue
			elif ch == 15:
				wordpress()
				continue
			elif ch == 16:
				docker_jenkin()
				continue
			elif ch == 17:
				create_vol()
				continue
			elif ch == 18:				
				show_vol()
				continue
			elif ch == 19:
				remove_vol()
				continue
			elif ch == 20:
				yum_configure()
				continue
			elif ch == 21:
				docker_cpu()
				continue			
			elif ch == 22:
				active_port()
				continue
			elif ch == 23:
				exit()
		else:
			print("Not Found.")
			x=input("Retry...")
else:
	print("Try again !", end="")
	x=input("Enter to exit...")







