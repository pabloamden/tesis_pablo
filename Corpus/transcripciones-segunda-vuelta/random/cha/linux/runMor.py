#!/bin/env python
import os
from glob import glob
from subprocess import run
from subprocess import STDOUT
from os.path import expanduser

HOME = expanduser("~")
CLAN_BIN_PATH = f"{HOME}/Apps/unix-clan/unix/bin"
CLAN_LIB_PATH = f"{HOME}/Apps/unix-clan/lib"
LANGUAGE = "spa"

pipeline = [
	[f"{CLAN_BIN_PATH}/mor",f"-L{CLAN_LIB_PATH}/{LANGUAGE}"],
	[f"{CLAN_BIN_PATH}/post", f"+d{CLAN_LIB_PATH}/{LANGUAGE}/post.db"],
	[f"{CLAN_BIN_PATH}/postmortem", f"-L{CLAN_LIB_PATH}/{LANGUAGE}"],
	[f"{CLAN_BIN_PATH}/megrasp", f"+L{CLAN_LIB_PATH}/{LANGUAGE}"],
]

chaFiles = glob("./*.cha")
print(chaFiles)

for f in chaFiles:
	print("")
	print("Processing file: ", f)
	print("")
	
	for process in pipeline:
		print("")
		print("---------------")
		print(f"Running {process[0]}")
		print("---------------")
		print("")
		run( process + [f], stderr=STDOUT )
