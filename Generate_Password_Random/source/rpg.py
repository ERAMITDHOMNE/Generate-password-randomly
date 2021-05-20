#!/usr/bin/env python
# -*- coding:utf-8 -*-

import string
import random

def random_password_generator():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    size = 8
    return ''.join(random.choice(chars) for x in range(size, 20))

def random_password_generator_ico():
	random_password_generator_ico = """
	#####################################################################
	#Password Generetor Randomly -Lectures By Mr.Dhomne YOutube Channel #
	#####################################################################
	#                                                           #########
	#####################################################################
	#               DEVELOPER : AMIT DHOMNE                     #########
	#          Mail Address : amit.dhomne@yahoo.com             #########
	#          LINKEDIN : https://github.com/ERAMITDHOMNE       #########
	#   YouTube Channel : Lectures by Mr.Dhomne                 #########
	#####################################################################
	"""
	print(random_password_generator_ico)
