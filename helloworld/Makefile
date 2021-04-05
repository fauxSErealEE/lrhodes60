# A simple example Makefile

# A simple Make Macro
LINK_TARGET = helloworld.exe

# A Make Macro that uses backslash to extend the line
OBJ = \
helloworld.o

# Make Macro defined by two Macro Expansions
# Macro expansions are introduced with a $ and enclosed in (parantheses)
REBUILDABLES = $(OBJ) $(LINK_TARGET)

#There are two standard Targets a Makefile should have:
# "all" and "clean" because they are often command-line goals.

# The rule for "all" is used to incrementally build your system
# It does this by expressing a dependecy on the results of that system, 
#which in turn have their own rules and dependencies.

all:  $(LINK_TARGET)
	echo all done

# A simple Rule (used for 'cleaning' the build env)
# It has a target named "clean" (left of colon)
# no dependencies (right of colon)
# and two commands (indented by tabs on the lines that follow)
.PHONY: clean
clean:
	del -f $(REBUILDABLES)
	echo Clean done

#There is no required order to the list of rules as they appear in the Makefile.
# Make will build its own dependcy tree and only execute each rule only once
# its dependecies' rules have been executed successfuly.

#Rule that uses built-in Make Macros
# $@ expands to the rule's target
# $^ expands to the rule's dependencies
$(LINK_TARGET) : $(OBJ)
	gcc -g -o $@ $^

# A Pattern rule, used for compile-line.
# Says how to create a .o file, given a .c file
# $@ for pattern-matched target
# $< for pattern-matched dependency
%.o : %.c
	gcc -g -o $@ -c $<

#Dependecy Rules, used without commands
#indicates that if any file to the right is out of date, so is the left
#often used to catch header file dependencies

helloworld.o : helloworld.c helloworld.h

#helloworld.exe: helloworld.o 
#	gcc -o helloworld.exe helloworld.o

#helloworld.o: helloworld.c
#	gcc -c helloworld.c

#clean:
#	rm helloworld.o helloworld.exe