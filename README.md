# Guide on how to build a simple Docker container from Flask API

## Introduction
This repository is an example on how to create a docker image and run in on your localhost with Flask API.
I have taken one of my codes and build a docker from it.
Do the steps below to build your own Docker Image.

## Dependencies
First of all you have to install Docker engine on your machine , if you don't have one. You can check it with this command
	
	docker --version
	docker-compose --version

If this both commands print your docker version , you can pass this part up to git clone part.
If you are using Ubuntu 20.04, you can simply run the instalation file , and all will be done on your behalf.
	
	sh install_docker.sh

In case of any error , or if you use other operation system rather than Ubuntu 20.04, install Docker and Docker-compose from the official website.

	https://docs.docker.com/compose/install/

## Configuration and Usage
Clone the repo in your local machine

	git clone git clone https://github.com/inDATAside/docker_template.git

Put the Python and all the necessary files into the **app** folder.
Your main python file should be a module. It means you should have a function which can be imported in other file, which 
will do all calculations and return some output. For example **app/ofcom_internet.py** is a module and its 
**run(...)** function is imported into the **sever.py** file.

In **server.py** change to import line to yours.
	
	from your_module import your_function

If your function accepts any parameters from outside such as dataframe , object, list, etc, which you have to read from a file
and pass them to the function, you can do that in "server.py" after the imports. Take a look on lines 7-19, where I read a dataframe ,
drop the duplicates, and define a new list.
If no parameters are needed delete this lines and also the parameters to function call on line 26.
The **req.data** variable is a dictionary , with **your_function** parameters. Example
	if your function gets for instance 2 parameters, input_dataframe and a input_string, you have to pass them as follows
	
	function_params = req.data
	result = run(function_params['input_dataframe'], function_params['input_string'])

In the**server.py** change the parameters in your function call.

Decide on which port you will run your application and change it on the last line.

The **server.py** file is ready !!! Huraaaaaaaaay :D

Next step is to change a couple of things in **docker-compose.yml**.
	- set the port on line 12 to the port you decided to use
	- change the docker container names on line 4 and 5 to your container name
		internet_compresed --> some_name

Docker-compose.yml is also ready

The last change is needed in **Dockerfile**
- on line 3 you can add your info (The Docker creator name and email). This step is optional , You can change it or remove the line.
- on line 9 add the libraries needed for your program to run

Example

	&& pip3 install pandas tensorflow sqlalchemy==1.4.44

You can specify a version of the lib or install the latest version
If you have many libraries to install , you can write in on multiple lines
Example

	&& pip3 install pandas tensorflow sqlalchemy==1.4.44 \
	&& pip3 install numpy torch==1.8.0

**NOTE: The space+slash at the end of each line except the last is mandatory**

- Change the port on line 14

	EXPOSE your_port

Now you can build and run the docker container with the command

	docker-compose up --build

## ATTENTION , IMPPORTANT NOTE!!!!!!

If you are building the docker for the FIRST time, use the command above.
For the further you can use the command without the build parameter,
even if you do some changes in the code.

	docker-compose up

BUT, if you want to add a new package , or change an existing package version in Dockerfile
you have to run the container with --build parameter for the first time after the changes.
In other words, if any changes are made to Dockerfile, run with --build, else, without --build

After the instalations are done you can send requests to your machine 

## Example

	import requests
	import json

	# Change the your-machine-ip and your-port, example
	# 'http://192.168.1.100:5000/api/process'
	test_url = 'http://your-machine-ip:your-port/api/process'
    headers = {'content-type': 'application/json'}
    # input_dict variable is the input to your_function in a dictionary
    input_dict = {
    				'input_dataframe' : some_data_frame,
					'input_string' : some_string
				}
    response = requests.post(test_url, data=input_dict, headers=headers)
    your_function_output = json.loads(response.content)["message"]


You are done , enjoy your Docker container with Flask API !!!!!							

## Citation
Author - Arsen Arijanyan
Email  - arsen.aridjanyan@gmail.com
