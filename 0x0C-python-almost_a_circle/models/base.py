#!/usr/bin/python3
# Task 1 base.py
"""This class will be the “base” of all other classes"""


import turtle


class Base:
    """
    class Base definition
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        instantializing the base class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns JSON string representation
        of list_dictionaries
        """
        return str(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns a list of dictionary objects
        from json string
        """
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return eval(json_string)

    @staticmethod
    def to_csv_lines(list_csv):
        """
        Returnng CSV string representation
        from list of child class
        """
        builder = ""
        for csv in list_csv:
            for i, ele in enumerate(csv):
                builder += str(ele)
                if i != len(csv) - 1:
                    builder += ','
            builder += '\n'
        return builder

    @staticmethod
    def from_csv_lines(list_csv):
        """
        returning the list of
        CSV instance objects
        """
        if list_csv is None or len(list_csv) == 0:
            return []

        csv_data = []
        for line in list_csv:
            raw_data = line.strip('\n').split(',')
            csv_data.append([int(ele) for ele in raw_data])
        return csv_data

    @staticmethod
    def get_cname_from_sublist(list_objs):
        """
        geting the appropiate cname
        to use when saving objects
        """
        cname = None
        for i, obj in enumerate(list_objs):
            if not issubclass(type(obj), Base):
                continue
            elif cname is None or cname != "Rectangle":
                cname = obj.__class__.__name__
        if cname is None:
            cname = "Rectangle"
        return cname

    @classmethod
    def save_to_file(cls, list_objs):
        """
        saveing a list of objects to a file as a JSON string
        """
        new_list = None
        list_obj_copy = list_objs.copy()
        cname = cls.get_cname_from_sublist(list_obj_copy)

        super_list = []
        for ele in list_obj_copy:
            if issubclass(type(ele), Base):
                super_list.append(ele.to_dictionary())
        write_str = cls.to_json_string(super_list)
        with open(cname + '.json', 'w', encoding='utf-8') as myFile:
            myFile.write(write_str)

    @classmethod
    def create(cls, **dictionary):
        """
        creating a new instance of the child class
        """
        new_inst = cls(1, 1)
        if new_inst is not None:
            new_inst.update(**dictionary)
        return new_inst

    @classmethod
    def load_from_file(cls):
        """
        Returning a list of instances
        """
        cname = cls.__name__
        try:
            with open(cname + '.json', 'r', encoding='utf-8') as myFile:
                text = myFile.read()
        except:
            return []

        inst_list = []
        dict_list = cls.from_json_string(text)
        for ele in dict_list:
            inst_list.append(cls.create(**ele))
        return inst_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        serializes and deserializes in CSV
        """
        list_obj_copy = list_objs.copy()
        cname = cls.get_cname_from_sublist(list_obj_copy)
        super_list = []

        for ele in list_obj_copy:
            if issubclass(type(ele), Base):
                super_list.append(ele.to_csv())
        write_str = cls.to_csv_lines(super_list)
        with open(cname + '.csv', 'w', encoding='utf-8') as myFile:
            myFile.write(write_str)

    @classmethod
    def load_from_file_csv(cls):
        """
        loading the list
        of objects from their csv file
        """
        cname = cls.__name__
        try:
            with open(cname + '.csv', 'r', encoding='utf-8') as myFile:
                lines = myFile.readlines()
        except:
            return []

        inst_list = []
        csv_list_list = cls.from_csv_lines(lines)
        for csv_inst in csv_list_list:
            new_obj = cls(1, 1)
            new_obj.update(*csv_inst)
            inst_list.append(new_obj)
        return inst_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        drawing both the rectangles and squares using imported turtle
        """
        window = turtle.Screen()
        window.bgcolor("green")
        all_eles = list_rectangles.copy()
        all_eles.extend(list_squares)
        turtles = [turtle.Turtle() for ele in all_eles]
        for i, t in enumerate(turtles):
            if i < len(list_rectangles):
                t.color("blue")
                if i > 0:
                    prev_pos = turtles[i - 1].position()
                    prev_x = prev_pos[0] + list_rectangles[i - 1].width
                    pre_y = prev_pos[1]
                    if i % 6 == 0:
                        pre_y = prev_pos[1] + list_rectangles[i - 1].height
                    t.setpos(prev_x, pre_y)
                t.forward(list_rectangles[i].width)
                t.right(90)
                t.forward(list_rectangles[i].height)
                t.right(90)
                t.forward(list_rectangles[i].width)
                t.right(90)
                t.forward(list_rectangles[i].height)
            else:
                t.color("red")
                if i > 0:
                    cur_sq_i = i - len(list_rectangles)
                    prev_pos = turtles[i - 1].position()
                    prev_x = prev_pos[0] + list_squares[cur_sq_i - 1].size
                    prev_y = prev_pos[1]
                    if i % 6 == 0:
                        prev_y = prev_pos[1] + list_squares[cur_sq_i - 1].size
                    t.setpos(prev_x, prev_y)
                for s in range(0, 4):
                    t.forward(list_squares[cur_sq_i].size)
                    t.right(90)
