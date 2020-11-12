import os
import socket
import multiprocessing,subprocess
import subprocess
import time


print("Bot is starting.")
process3 = subprocess.Popen(["python", "message.py"])
time.sleep(15)
process2 = subprocess.Popen(["python", "command.py"])
time.sleep(15)
process1 = subprocess.Popen(["python", "backgroundTasks.py"])


