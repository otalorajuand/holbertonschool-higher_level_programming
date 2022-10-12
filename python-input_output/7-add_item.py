#!/usr/bin/python3
"""
This module imports two functions and executes with them
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

json_file_name = "add_item.json"

try:
    lista = load_from_json_file(json_file_name)
except FileNotFoundError:
    lista = []

for elem in sys.argv[1:]:
    lista.append(elem)

save_to_json_file(lista, json_file_name)
