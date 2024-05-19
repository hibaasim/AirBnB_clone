#!/usr/bin/python3
'''The console module'''
import cmd


class HBNBCommand(cmd.Cmd):
    '''Defines the console

    Args
        prompt: the prompt to be displayed
    '''
    prompt = '(hbnb) '

    def do_quit(self, args):
        '''Exits the console'''
        return True

    def do_EOF(self, args):
        '''Exits the console'''
        return True

    def emptyline(self):
        '''Does not exectue anything when enter is pressed in an empty line'''
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
