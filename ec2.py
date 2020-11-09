#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
def color(c):
    os.system('tput setaf {}'.format(c))
def clear():
    os.system('clear')
def ec2_func(ec2_arg,ip):
    while(1):
        clear()
        color(7)
        print('\n\t\t\t\t    EC2 Menu')
        print('\t\t\t==================================\n')
        color(3)
        ec2_menu=['Show all EC2 Instances','Start an EC2 Instance','Stop an EC2 Instance','Terminate an Instance','Create a New Key pair','Delete a Key Pair','Create a Security Group','Delete a Security Group','Launch New Instance','Create an EBS Volume','Delete an EBS Volume','Attach EBS Volume to an Instance','Detach an EBS Volume','List all EBS Volumes']
        for i in range(len(ec2_menu)):
            if i<9:
                print('\t\t\tEnter {}  : {}'.format(i+1,ec2_menu[i]))
            else:
                print('\t\t\tEnter {} : {}'.format(i+1,ec2_menu[i]))
        color(6)
        print('\t\t\tEnter 0  : Go Back')
        color(1)
        print('\t\t\tEnter e  : To Exit')
        color(5)
        choice=input('Enter your choice : ')
        color(7)
        if choice=='0':
            from aws import aws_func
            aws_func(ec2_arg,ip)
        elif choice=='1':
            os.system('{} {} aws ec2 describe-instances'.format(ec2_arg,ip))
        elif choice=='2':
            instance_id=input('Enter the Instance ID : ')
            os.system('{} {} aws ec2 start-instances --instance-ids {}'.format(ec2_arg,ip,instance_id))
        elif choice=='3':
            instance_id=input('Enter the Instance ID : ')
            os.system('{} {} aws ec2 stop-instances --instance-ids {}'.format(ec2_arg,ip,instance_id))
        elif choice=='4':
            instance_id=input('Enter the Instance ID : ')
            os.system('{} {} aws ec2 terminate-instances --instance-ids {}'.format(ec2_arg,ip,instance_id))
        elif choice=='5':
            key_name=input('Enter the name of the Key you want : ')
            os.system('{} {} aws ec2 create-key-pair --key-name {}'.format(ec2_arg,ip,key_name))
        elif choice=='6':
            key_name=input('Enter the name of the Key to delete : ')
            os.system('{} {} aws ec2 delete-key-pair --key-name {}'.format(ec2_arg,ip,key_name))
        elif choice=='7':
            group_name=input('Enter any name for your Security Group : ')
            description=input('Enter any description for your Security Group : ')
            os.system('{} {} aws ec2 create-security-group --group-name {} --description {}'.format(ec2_arg,ip,group_name,description))
        elif choice=='8':
            group_name=input('Enter the name of the Security Group : ')
            os.system('{} {} aws ec2 delete-security-group --group-name {}'.format(ec2_arg,ip,group_name))
        elif choice=='9':
            image_id=input('Enter the AMI Image ID : ')
            instance_type=input('Enter the Instance Type : ')
            count=int(input('Enter the Count : '))
            security_group_id=input('Enter the Security Group ID : ')
            key_name=input('Enter the Key Name : ')
            os.system('{} {} aws ec2 run-instances --image-id {} --instance-type {}  --count {} --security-group-ids {} --key-name {}'.format(ec2_arg,ip,image_id,instance_type,count,security_group_id,key_name))
        elif choice=='10':
            availability_zone=input('Enter the availability-zone : ')
            size=int(input('Enter the size in GiB : '))
            volume_type=input('Enter the Volume Type : ')
            os.system('{} {} aws ec2 create-volume --availability-zone {} --size {} --volume-type {}'.format(ec2_arg,ip,availability_zone,size,volume_type))
        elif choice=='11':
            volume_id=input('Enter the Volume ID : ')
            os.system('{} {} aws ec2 delete-volume --volume-id {}'.format(ec2_arg,ip,volume_id))
        elif choice=='12':
            volume_id=input('Enter the Volume ID : ')
            instance_id=input('Enter the Instance ID : ')
            device=input('Enter the Device Name where to attach the Volume : ')
            os.system('{} {} aws ec2 attach-volume --volume-id {} --instance-id {} --device {}'.format(ec2_arg,ip,volume_id,instance_id,device))
        elif choice=='13':
            volume_id=input('Enter the Volume ID : ')
            os.system('{} {} aws ec2 detach-volume --volume-id {}'.format(ec2_arg,ip,volume_id))
        elif choice=='14':
            os.system('{} {} aws ec2 describe-volumes'.format(ec2_arg,ip))
        elif choice=='e':
            color(7)
            clear()
            exit()
        else:
            print('Invalid Choice !')
        input('Press Enter to continue....')


# In[ ]:




