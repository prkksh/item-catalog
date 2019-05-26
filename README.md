# Item Catalog Project

## Overview
This is a catalog app which the user can view, edit, create and delete entries. The app is a basic restaurant app with menus. The code follows PEP8 guidelines and has login features using google oauth2. (This project is for Item Catalog from Udacity Full Stack Developer Nanodegree)


### Requirements

* Python 2 - version 2.7.12
* Vagrant
* VirtualBox
* Git

### Project Objectives

The project has following objectives,
*API endpoints
*CRUD operations
*Authentication and Authorization

### To run the Project
* Install Vagrant and VirtualBox
* Vagrant can be installed using configurations provided by Udacity from <a href="https://classroom.udacity.com/nanodegrees/nd004/parts/4dcefa2a-fb54-4909-9708-9ef2839e5340/modules/349fd477-16d6-44ae-b33a-2b8521735718/lessons/3621198668/concepts/35960790720923">here</a>
* Clone this repo
> `git clone https://github.com/prkksh/item-catalog`
* Open terminal and cd in to the folder vagrant is installed and run 'vagrant up' to launch the linux VM. Then, Login using 'vagrant ssh' command.
* The files are inside the vagrant folder. To access the files, run
>`cd /vagrant`

* Setup the database with
>`python database_setup.py`
* Populate the database with
>`python restaurant_menu.py`
* After populating, run the module with
>`python project.py`
* Go to <a href="">http://localhost:9090</a>
