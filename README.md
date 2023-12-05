## General
____________

### Author
* Josh McIntyre

### Website
* jmcintyre.net

### Overview
* TurtleTumbler is a visual demo of brute-force password cracking with the Raspberry Pi

## Development
________________

### Git Workflow
* master for releases (merge development)
* development for bugfixes and new features

### Building
* make build
Build the application
* make clean
Clean the build directory

### Features
* Generate a PIN hash
* Brute-force PIN attempts until a matching hash is found
* Display information about attempts and password hashes on an LCD screen

### Requirements
* Requires a Raspberry Pi
* Requires Python
* Requires I2C character LCD

### Platforms
* Raspberry Pi

## Usage
____________

### Raspberry Pi Usage
* From the command line, run `python3 turtletumbler.py`
