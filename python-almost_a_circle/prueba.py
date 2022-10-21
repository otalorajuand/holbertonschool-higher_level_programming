#!/usr/bin/python3
""" Doc """
import os, sys
import subprocess


def run_command(cmd):
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return "{}{}".format(output, error)


def run_unittest():
    nb_tests = 0
    is_success = False
    try:
        res = run_command("python3 -m unittest discover tests")
        for line in res.split("\\n"):
            if "Ran " in line:
                nb_tests = int(res.split("Ran ")[-1].split(" tests")[0])
            if nb_tests > 0 and "OK" in line:
                is_success = True
    except:
        nb_tests = 0
        is_success = False
    return nb_tests, is_success


# validate tests are passing by default
nb_tests, passing = run_unittest()

if nb_tests <= 0:
    print("No test found")
    exit(1)
if not passing:
    print("Regular tests are not passing")
    exit(1),
