#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
def color(c):
    os.system('tput setaf {}'.format(c))
def clear():
    os.system('clear')
def main_men(arg,ip):
    while(1):
        clear()
        color(7)
        print('\n\t\t\t    Main Menu')
        print('\t\t==================================\n')
        color(45)
        menu=['Linux','Docker','Hadoop','AWS']
        for i in range(len(menu)):
            print('\t\t\tEnter {} : {}'.format(i+1,menu[i]))
        color(2)
        print('\t\t\tEnter 0 : Go Back')
        color(1)
        print('\t\t\tEnter e : To Exit')
        color(5)
        choice=input('Enter your choice : ')
        if choice=='0':
            from loc_rem import local_remote
            local_remote()
        elif choice=='1':
            from linux import linux_func
            linux_func(arg,ip)
        elif choice=='2':
            from docker import docker_menu
            docker_menu(arg,ip)
        elif choice=='3':
            from hadoop import hadoop_func
            hadoop_func(arg,ip)
        elif choice=='4':
            from aws import aws_func
            aws_func(arg,ip)
        elif choice=='e':
            clear()
            color(7)
            exit()
        else:
            print('Invalid choice !')


# In[ ]:




