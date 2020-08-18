import time
import subprocess as sup
import rcon
import runpy

config_dict = runpy.run_module("config")

outfilename = config_dict['bakfoldername'] + time.strftime(
    '%Y%m%d%H%M%S', time.localtime(time.time())) + '.tar.gz'

with rcon.MCRcon('127.0.0.1', config_dict['pwd'], config_dict['port']) as mcr:
    resp = mcr.command('save-all')
    print(resp)
    time.sleep(1)
    resp = mcr.command('save-off')
    print(resp)

cmd = 'tar -zcvf ' + config_dict['outfilename'] + ' ' + config_dict[
    'srcfoldername']
sup.run(cmd, shell=True)
time.sleep(1)

with rcon.MCRcon('127.0.0.1', config_dict['pwd'], config_dict['port']) as mcr:
    resp = mcr.command('save-on')
    print(resp)

print('Backuped: ' + outfilename)
