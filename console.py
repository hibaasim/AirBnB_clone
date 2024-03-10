#!/usr/bin/python3
'''Module for command line interpreter'''
import cmd

class HBNBCommand(cmd.Cmd):
    '''Defines the console'''
    prompt = '(hbnb) '

    def do_quit(self, args):
        '''Exits the program'''
        return True

    def do_EOF(self, args):
        '''Exits the program'''
        return True

    def emptyline(self):
        '''Passes an empty line and doesn't do anything'''
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
