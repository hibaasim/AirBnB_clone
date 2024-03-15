#!/usr/bin/python3
'''Module for command line interpreter'''
import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    '''Defines the console

    Attributes:
        prompt: the command line prompt
    '''
    prompt = '(hbnb) '
    argument_list = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']

    def do_quit(self, args):
        '''Exits the program'''
        return True

    def do_EOF(self, args):
        '''Exits the program'''
        return True

    def emptyline(self):
        '''Passes an empty line and doesn't do anything'''
        pass

    def do_create(self, args):
        '''Creates new instance of BaseModel,
            saves it (to the JSON file) and prints the id
        '''
        argument = shlex.split(args)

        if len(argument) == 0:
            print('** class name missing **')
        elif argument[0] not in self.argument_list:
            print("** class doesn't exist **")
        else:
            new_inst = eval(f'{argument[0]}()')
            storage.save()
            print(new_inst.id)

    def do_show(self, args):
        argument = shlex.split(args)

        if len(argument) == 0:
            print('** class name missing **')
        elif argument[0] not in self.argument_list:
            print("** class doesn't exist **")
        elif len(argument) < 2:
            print('** instance id missing **')
        else:
            instance = storage.all()

            key = f'{argument[0]}.{argument[1]}'
            if key in instance:
                print(instance[key])
            else:
                print('** no instance found **')

    def do_destroy(self, args):
        '''Deletes an instance based on the class name and id
        '''
        argument = shlex.split(args)

        if len(argument) == 0:
            print('** class name missing **')
        elif argument[0] not in self.argument_list:
            print("** class doesn't exist **")
        elif len(argument) < 2:
            print('** instance id missing **')
        else:
            instance = storage.all()

            key = f'{argument[0]}.{argument[1]}'
            if key in instance:
                del instance[key]
                storage.save()
            else:
                print('** no instance found **')

    def do_all(self, args):
        '''Prints all string representation of all instances'''
        instance = storage.all()
        argument = shlex.split(args)

        if len(argument) == 0:
            for key, value in instance.items():
                print(str(value))
        elif argument[0] not in self.argument_list:
            print("** class doesn't exist **")
        else:
            for key, value in instance.items():
                if key.split('.')[0] == argument[0]:
                    print(str(value))

    def do_update(self, args):
        '''Updates an instance based on the class name and id
            by adding or updating attribute

        Usage:
            update <class name> <id> <attribute name> "<attribute value>"
        '''
        argument = shlex.split(args)

        if len(argument) == 0:
            print('** class name missing **')
        elif argument[0] not in self.argument_list:
            print("** class doesn't exist **")
        elif len(argument) < 2:
            print('** instance id missing **')
        else:
            instance = storage.all()
            
            key = f'{argument[0]}.{argument[1]}'
            if key not in instance:
                print('** no instance found **')
            elif len(argument) < 3:
                print('** attribute name missing **')
            elif len(argument) < 4:
                print('** value missing **')
            else:
                obj = instance[key]
                attr_name = argument[2]
                attr_val = argument[3]

                try:
                    attr_val = eval(attr_val)
                except Exception:
                    pass
                setattr(obj, attr_name, attr_val)
                obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
