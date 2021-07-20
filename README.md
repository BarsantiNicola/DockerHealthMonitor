Docker Health Monitor Service
========

The repository contains all the files used to deploy a docker container health monitor service which can run on a cloud infrastructure.
The service is in charge of protect the containers functionalities by restarting them in case of external attacks(packet loss attack/shutdown attack) 

Installation
-----

To install the service you can use the installation.sh file

 ```bash
	./DockerHealthMonitorService/installer.sh 
 ```

It will require an ip address and the root password for the remote machine in which install the service.
The installer will install all the elements needed by the service however there could be some problem during the libraries installation(in the case, problems will be reported by the installer). 
In case the required python libraries will collide with some used by other services we will not change them to not compromize the system functionalities. 
In the case it's your duty to see how to resolve the conflict in order to make the service functional

Usage
-----

You can interact with the service by a rest interface deployed on 8080 port of the machine in which the service is installed. 
From the interface you can add more machines inside the system to be managed by our system. A complete description of the rest
interface can be found at:

 ```html
	http://172.16.3.167:800   [UNIPI VPN Connection required]
 ```

Uninstall
-----

To uninstall the service you can use the uninstall file present into the repository.

```bash
	./DockerHealthMonitorService/uninstaller.sh 
 ```
 
 It will ask you for the ip address of the installation machine and its
root password. The uninstall will delete also all the service components deployed on all the managed cloud machines but it will not uninstall the python libraries
and the elements used(rabbitMQ, python3) in order to not risk to eventually compromise other system application
