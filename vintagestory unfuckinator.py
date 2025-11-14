from time import sleep
import psutil

for proc in psutil.process_iter():
    if proc.name() == "Vintagestory":
        print('Vintage Story found! Killing')
        proc.kill()
        break
else: print('Vintage Story not found, check python permissions')

sleep(3) # give user time to read output
