# Item Catalog Project

## Overview



### Requirements

* Python 2 - version 2.7.12
* Vagrant
* VirtualBox
* Git

### Project Objectives

The project has three objectives,
* Most popular article of all time
* Most popular article author of all time
* Day on which more than 1% requests led to error

### To run the Project
* Install Vagrant and VirtualBox
* Vagrant can be installed using configurations provided by Udacity from <a href="">here</a>
* Clone this repo
> `git clone https://github.com/prkksh/item-catalog/`
* Open terminal and cd in to the folder vagrant is installed and run 'vagrant up' to launch the linux VM. Then, Login using 'vagrant ssh' command.
* The files are inside the vagrant folder. To access the files, run
>`cd /vagrant`

* Setup the database with
>`python database_setup.py`
* Populate the database with
>`python restaurant_menu.py`
* After populating, run the module with
>`python project.py`
* Go to <a href="">http://localhost:5000</a>
