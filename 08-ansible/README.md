Steps to Create and Use a Custom Ansible Module
1. Set Up EC2 and Install Ansible
Make sure that you have Ansible installed on your EC2 instance. You can install it by running:

sudo apt update
sudo apt install ansible -y
pip install --upgrade ansible jinja2
----------------------
2. Create the Custom Module
Custom modules in Ansible are written in Python and follow a specific structure. Create a simple module that checks if a file exists on the target EC2 instance and returns a success message if found.
----------------------
3. Make the Module Executable
To run the custom module, make sure it has executable permissions:

chmod +x check_file.py
----------------------
4. Create an Ansible Playbook to Use the Custom Module
Create a playbook that uses the custom module to check for the existence of a file on your EC2 instance.

check_file_playbook.yml
----------------------

5. Set Up Ansible Configuration to Use Custom Modules
You need to tell Ansible where to find your custom modules. Create or modify ansible.cfg:

----------------------
6. Run the Playbook
Now that everything is set up, run the playbook to use the custom module.

To check file on EC2 instance:
ansible-playbook check_file_playbook.yml -i <ec2-ip>, --private-key /path/to/private-key.pem
----------------------------
