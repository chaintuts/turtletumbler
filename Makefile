# This file contains a make script for the TurtleTumbler application
#
# Author: Josh McIntyre
#

# This block defines makefile variables
SRC_FILES=src/*.py

BUILD_DIR=bin/turtletumbler

# This rule builds the application
build: $(SRC_FILES) $(TEST_FILES)
	mkdir -p $(BUILD_DIR)
	cp $(SRC_FILES) $(BUILD_DIR)

# This rule cleans the build directory
clean: $(BUILD_DIR)
	rm -r $(BUILD_DIR)/*
	rmdir $(BUILD_DIR)
