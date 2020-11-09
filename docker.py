#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
def color(c):
    os.system('tput setaf {}'.format(c))
def clear():
    os.system('clear')

# Configure and Install Docker
def dockerConfig():
        print('yum should be configured before docker installation .')
        os.system('sudo yum config\-manager \-\-add\-repo\=https\:\/\download.docker.com\/linux\/centos\/docker\-ce\.repo')
        os.system('dnf install docker-ce --nobest -y')
        os.system('systemctl start docker')
        os.system('systemctl status docker')

# Configure Web Server
def dockerWeb():
	os.system('docker run -dit --name webOS -p 8080:80 centos')
	os.system('docker exec webOS yum install httpd -y')
	os.system('docker cp index.html webOS:/var/www/html/')
	os.system('docker exec webOS /usr/sbin/httpd')
	input()

# Launch Python
def dockerPython():
	os.system('docker run -dit --name pyOS centos')
	os.system('docker exec pyOS yum install python3 -y')
	os.system('docker cp hello.py pyOS:/')
	print()
	os.system('docker exec pyOS python3 /hello.py')
	input()

# Launch GUI
def dockerGUI():
	os.system('docker run -it --name gui --env="DISPLAY" --net=host firefox:v1')
	input()

# Docker Menu
def docker_menu(doc_arg,ip):
    while True:
        clear()
        color(7)
        print('\n\t\t\t\t     Docker Menu')
        print('\t\t\t==================================\n')
        color(6)
        print("""
                        Enter 1 : Configure Docker
                        Enter 2 : Search Docker Image
                        Enter 3 : Pull Docker Image
                        Enter 4 : List Container 
                        Enter 5 : Remove all the Container
                        Enter 6 : Configure Webserver on Docker
                                """)		
        color(45)
        print('\t\t\tEnter 0  : Go Back')
        color(1)
        print('\t\t\tEnter e  : To Exit')
        color(5)
        choice=input('Enter your choice : ')
        color(7)
        if choice=='0':
            from main_menu import main_men
            main_men(doc_arg,ip)

        if choice == '1':
            dockerConfig()

        elif choice == '2':
            image_name = input("\nEnter the OS Name : ")
            os.system("docker search {}".format(image_name))
            input()

        elif choice == '3':
            image_name = input("\nEnter the OS Name : ")

            os.system("docker pull {}".format(image_name))
            input()

        elif choice == '4':
            os.system("docker ps -a")
            input()

        elif choice == '5':
            os.system("docker rm -f $(docker ps -aq)")
            input()

        elif choice == '6':
            dockerWeb()

        elif choice=='e':
            clear()
            color(7)
            exit()
        else:
            print('Invalid choice !')


# In[ ]:




