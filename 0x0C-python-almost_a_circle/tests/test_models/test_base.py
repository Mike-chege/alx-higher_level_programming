#!/usr/bin/python3
# Test for base.py
"""Test for Base class"""


import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_start(unittest.TestCase):
    """
    Class definition for testing Base class
    """

    def test_func(self):
        """
        testing base functionality
        """
        b = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b2.id + 1, b3.id)

    def test_id(self):
        """
        testing the given id
        """
        b = Base()
        b2 = Base(24)
        b3 = Base(45)
        b4 = Base()
        self.assertEqual(45, b3.id)
        self.assertEqual(b.id + 1, b4.id)

    def test_json_string(self):
        """
        testing Class Base to json string method
        """
        r1 = Rectangle(4, 5, 6, 7, 8)
        r2 = Rectangle(10, 11, 12, 13, 14)
        dictionary = r1.to_dictionary()
        d2 = r2.to_dictionary()
        json_dict = Base.to_json_string([dictionary, d2])
        j_d = eval(json_dict)
        self.assertEqual(j_d[0]['id'], 8)
        self.assertEqual(j_d[1]['x'], 12)

    def test_write_file_functionality(self):
        """
        testing the write file functionality
        """
        s = Square(3, 1, 1, 10)
        s2 = Square(4, 2, 2, 20)
        r1 = Rectangle(5, 6, 3, 3, 30)
        r2 = Rectangle(7, 8, 4, 4, 40)
        Base.save_to_file([s, s2])
        with open('Square.json', 'r', encoding='utf-8') as myFile:
            text = myFile.read()
        list_of_dicts = eval(text)
        self.assertEqual(list_of_dicts[0]['id'], 10)
        self.assertEqual(list_of_dicts[1]['x'], 2)

        Base.save_to_file([r1, r2])
        with open('Rectangle.json', 'r', encoding='utf-8') as myFile:
            text = myFile.read()
        list_of_dicts = eval(text)
        self.assertEqual(list_of_dicts[0]['id'], 30)
        self.assertEqual(list_of_dicts[1]['x'], 4)

    def test_write_file_comp_input(self):
        """
        testing writing a file with more harder inputs
        """
        s = Square(3, 1, 1, 10)
        s2 = Square(4, 2, 2, 20)
        r1 = Rectangle(5, 6, 3, 3, 30)
        r2 = Rectangle(7, 8, 4, 4, 40)
        Base.save_to_file(["hello", 42, "more garb", True, s, s2])
        with open('Square.json', 'r', encoding='utf-8') as myFile:
            text = myFile.read()
        list_of_dicts = eval(text)
        self.assertEqual(list_of_dicts[0]['id'], 10)
        self.assertEqual(list_of_dicts[1]['x'], 2)

        Base.save_to_file([s, 89, r1, "garb", 42, s2, r2])
        with open('Rectangle.json', 'r', encoding='utf-8') as myFile:
            text = myFile.read()
        list_of_dicts = eval(text)
        self.assertEqual(list_of_dicts[1]['id'], 30)
        self.assertEqual(list_of_dicts[3]['x'], 4)

    def test_write_file_empty_list_d(self):
        """
        testing if empty list is written to the correct required
        destination file
        """
        Base.save_to_file([])
        with open('Rectangle.json', 'r', encoding='utf-8') as myFile:
            text = myFile.read()
        self.assertEqual(text, "[]")

    def test_from_json_(self):
        """
        testing bases from_json_string (method) to convert string to
        lists of dictionaries
        """
        s = Square(4, 8, 9, 2)
        r = Rectangle(9, 2, 3, 4)
        r_d = r.to_dictionary()
        s_d = s.to_dictionary()
        json_d = Base.to_json_string([s_d, r_d])
        d_list = Base.from_json_string(json_d)
        self.assertEqual(d_list[0]['id'], 2)
        self.assertEqual(d_list[1]['width'], 9)
        self.assertEqual(len(d_list), 2)

    def test_from_json_empty(self):
        """
        testsing class base from_json_string method with some
        empty inputs
        """
        d_list = Base.from_json_string("")
        self.assertEqual(len(d_list), 0)
        d_list = Base.from_json_string(None)
        self.assertEqual(len(d_list), 0)

    def test_create_inst_dictionary(self):
        r = Rectangle(9, 2, 3, 4, 45)
        s = Square(4, 8, 9, 2)
        r_d = r.to_dictionary()
        s_d = s.to_dictionary()
        r2 = Rectangle.create(**r_d)
        s2 = Square.create(**s_d)
        self.assertEqual(s.id, s2.id)
        self.assertEqual(r.id, r2.id)
        self.assertEqual(s.y, s2.y)
        self.assertEqual(s.x, s2.x)
        self.assertEqual(r.width, r2.width)
        self.assertEqual(s.size, s2.size)

    def test_read_from_file_rec_sqr(self):
        """
        testing base class ability to read from file to be used
        by Rectangle and Square
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(list_rectangles_output[0].y, 8)
        self.assertEqual(list_rectangles_output[1].height, 4)

    def test_read_from_file_json(self):
        """
        testing base class ability to read from json files
        """
        r1 = Rectangle(10, 7, 8, 3, 44)
        r2 = Rectangle(24, 23, 5, 1, 99)
        Rectangle.save_to_file([r1, r2])
        with open('Rectangle.json', 'r', encoding='utf-8') as myFile:
            text = myFile.read()
        rects = Rectangle.load_from_file()
        self.assertEqual(rects[0].width, 10)
        self.assertEqual(rects[1].id, 99)
        self.assertEqual(rects[1].x, 5)

    def test_read_from_file_empty_json(self):
        """
        testing base class (method) ability to read from json files when
        they are empty
        """
        try:
            os.remove('Square.json')
        except:
            pass
        list_output = Square.load_from_file()
        self.assertEqual(len(list_output), 0)
        self.assertEqual(list, type(list_output))

    def test_write_csv_instance(self):
        """
        testing base class ability to write instances as csv
        """
        r1 = Rectangle(10, 7, 2, 8, 33)
        r2 = Rectangle(10, 8, 4, 9, 44)
        Rectangle.save_to_file_csv([r1, r2])
        with open('Rectangle.csv', 'r', encoding='utf-8') as myFile:
            text = myFile.readlines()
        self.assertEqual(text[0][0] + text[0][1], "33")
        self.assertEqual(text[1][0] + text[1][1], "44")

    def test_write_csv_wrong_input(self):
        """
        testing base class ability to write instances as csv
        with wrong input
        """
        r1 = Rectangle(10, 7, 2, 4, 33)
        r2 = Rectangle(10, 8, 4, 9, 44)
        s1 = Square(10, 8, 4, 109)
        s2 = Square(11, 4, 3, 120)
        bs = ["bs", 42, True]
        more_bs = 45.34
        Rectangle.save_to_file_csv([bs, s1, s2, more_bs, r2, r1])
        with open('Rectangle.csv', 'r', encoding='utf-8') as myFile:
            text = myFile.readlines()
        self.assertEqual(text[0][0] + text[0][1] + text[0][2], "109")
        self.assertEqual(text[3][0] + text[3][1], "33")

    def test_read_csv_input(self):
        """
        testing base class ability to read csv input
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_output = Rectangle.load_from_file_csv()
        self.assertEqual(8, list_output[0].y)
        self.assertEqual(4, list_output[1].height)

    def test_read_csv_wrong(self):
        """tests base class to read from csv"""
        r1 = Rectangle(10, 7, 2, 8)
        s1 = Square(2, 4)
        list_rectangles_input = [r1, s1]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_output = Rectangle.load_from_file_csv()
        self.assertEqual(8, list_output[0].y)
        self.assertEqual(4, list_output[1].height)

    def test_read_csv_empty_sqr(self):
        try:
            os.remove('Square.csv')
        except:
            pass
        list_output = Square.load_from_file_csv()
        self.assertEqual(0, len(list_output))
        self.assertEqual(list, type(list_output))
