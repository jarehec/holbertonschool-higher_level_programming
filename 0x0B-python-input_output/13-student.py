#!/usr/bin/python3
class Student:
    'Student class'
    def __init__(self, first_name, last_name, age):
        'initialization'
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (isinstance(attrs, list)):
            return dict((k, self.__dict__[k])
                        for k in attrs if k in self.__dict__)
        return self.__dict__

    def reload_from_json(self, json):
        for k in json:
            self.__dict__[k] = json[k]
