#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cmath
from decimal import *

class vec3:
    x = 0.0
    y = 0.0
    z = 0.0

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def normalize(self):
        x = self.x
        y = self.y
        z = self.z

        n = Decimal(x) * Decimal(x) + Decimal(y) * Decimal(y) + Decimal(z) * Decimal(z);
        # Already normalized.
        if n == 1.0:
            return

        n = Decimal(n).sqrt()

        # Too close to zero.
        if (n.real < 2e-37):
            return

        n = Decimal(1.0) / n
        self.x *= float(n)
        self.y *= float(n)
        self.z *= float(n)

    def __add__(self, other):
        n = vec3()
        if isinstance(other, vec3):
            n.x = self.x + other.x
            n.y = self.y + other.y
            n.z = self.z + other.z
            n.ok = True
        if isinstance(other, float):
            n.x = self.x + other
            n.y = self.y + other
            n.z = self.z + other
            n.ok = True

        return n

    def __sub__(self, other):
        n = vec3()
        if isinstance(other, vec3):
            n.x = self.x - other.x
            n.y = self.y - other.y
            n.z = self.z - other.z
            n.ok = True
        if isinstance(other, float):
            n.x = self.x - other
            n.y = self.y - other
            n.z = self.z - other
            n.ok = True

        return n

    def __mul__(self, other):
        n = vec3()
        if isinstance(other, vec3):
            n.x = self.x * other.x
            n.y = self.y * other.y
            n.z = self.z * other.z
            n.ok = True
        if isinstance(other, float):
            n.x = self.x * other
            n.y = self.y * other
            n.z = self.z * other
            n.ok = True

        return n

    def __str__(self):
        return "[" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + "]"

def __num_trim__(str):
    numstr = "01234567890."
    tmp = str
    while len(tmp) > 0:
        char = tmp[0]
        if char in numstr:
            break
        else:
            tmp = tmp[1:]

    while len(tmp) > 0:
        char = tmp[len(tmp) - 1]
        if char in numstr:
            break
        else:
            tmp = tmp[:len(tmp) - 1]

    return tmp

def read_vector3(tip_str):
    success = False
    center = vec3()
    while not success:
        center_str = raw_input(tip_str)

        if center_str == "q":
            return center, success

        center_str = __num_trim__(center_str)

        str_list = center_str.split(",")
        if len(str_list) == 3:
            try:
                center.x = float( __num_trim__(str_list[0]))
                center.y = float( __num_trim__(str_list[1]))
                center.z = float( __num_trim__(str_list[2]))
                center.ok = True
                success = True
            except:
                success = False
                pass


    return center, success

def read_radius(tip_str):

    radius = 0
    success = False
    while not success:

        radius_str = raw_input(tip_str)

        if radius_str == "q":
            return radius, success

        radius_str = __num_trim__(radius_str)

        if len(radius_str) > 0:
            try:
                radius = float(radius_str)
                success = True
            except:
                success = False
                pass

    return radius, success

def calculate_circle(center, radius, top_point, left_point):
    print("\ncalculated circle: ")
    magic_number = 0.55228475

    vec_top = top_point - center
    vec_top.normalize()

    point_top = center + (vec_top * radius)
    point_bottom = center - (vec_top * radius)

    vec_left = left_point - center
    vec_left.normalize()

    point_left = center + (vec_left * radius)
    point_right = center - (vec_left * radius)

    # from top to draw
    ret = []
    ret.append(point_top)

    # go left
    cp = point_top + (vec_left * radius * magic_number)
    ret.append(cp)

    # go down
    cp = point_left + (vec_top * radius * magic_number)
    ret.append(cp)

    # to left
    ret.append(point_left)

    # go down
    cp = point_left - (vec_top * radius * magic_number)
    ret.append(cp)

    cp = point_bottom + (vec_left * radius * magic_number)
    ret.append(cp)

    # down
    ret.append(point_bottom)

    # go right
    cp = point_bottom - (vec_left * radius * magic_number)
    ret.append(cp)

    cp = point_right - (vec_top * radius * magic_number)
    ret.append(cp)

    # right
    ret.append(point_right)

    # go up
    cp = point_right + (vec_top * radius * magic_number)
    ret.append(cp)

    cp = point_top - (vec_left * radius * magic_number)
    ret.append(cp)

    # back
    ret.append(point_top)


    # print
    print("[")
    for i in xrange(0, len(ret)):
        print(str(ret[i]) + ",")
    print("]")

def __main__():

    print('\nInput "q" to quit')

    center, success = read_vector3('\nInput the center Vector3 (x, y, z): \n')
    if not success:
        return
    print('get center ' + str(center))

    radius, success = read_radius('\nInput the radius: \n')
    if not success:
        return
    print('get radius ' + str(radius))

    top_point, success = read_vector3('\nInput the top point Vector3 (x, y, z): \n')
    if not success:
        return
    print('get top point ' + str(top_point))

    left_point, success = read_vector3('\nInput the left point Vector3 (x, y, z): \n')
    if not success:
        return
    print('get left point ' + str(left_point))

    calculate_circle(center, radius, top_point, left_point)

__main__()