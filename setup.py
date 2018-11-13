#!/usr/bin/env python
from setuptools import setup, find_packages
from subprocess import Popen, PIPE

Version = "8.0"
p = Popen(
    ("git",
     "describe",
     "--tags"),
    stdin=PIPE,
    stdout=PIPE,
    stderr=PIPE)
try:
    descr = p.stdout.readlines()[0].strip().decode("utf-8")
    Version = "-".join(descr.split("-")[:-2])
    if Version == "":
        Version = descr
except:
    descr = Version

setup (name = "thermo",
       version=descr,
       packages = find_packages(),
       description = "Package to draw Thermodynamic diagrams with VCS",
       url = "https://github.com/cdat/thermo",
       data_files = [("share/thermo",["share/test_data_files.txt"])],
      )
