#!/usr/bin/python

import argparse
import sys
import serial

def display_help():
    print('Usage: rbsetup [options]')
    print('Options:')
    print('-h or --help \t\t\t Displays help')
    print('-d or --display_setup \t\t Displays current setup for Remote Board.')
    print('-p or --powerbuttonled \t\t Sets intensity of Powerbutton LED (RED/WHITE).\
    \n\t\t\t\t Valid values must be between 10 and 100 (%). Default is 50. Step 10.')
    print('-i or --infoleds \t\t Sets intensity of Status LEDs.\
    Valid values must be between 10 and 100 (%). \n\t\t\t\t Default is 50. Step 10.')
    print('-a or --autostart \t\t Power-on state when power is re/connected to Power Board. \
    \n\t\t\t\t Valid values are 0 for OFF or 1 (or more than 1) for ON. Default is 0.')
    print('-n or --switch_on_timer \t Sets the time interval [in seconds] after its expiration the automatic power on occurs.\
    \n\t\t\t\t Valid values must be between 0 (for inactive timer) and 604800 (for 1 week). Default is 0.')
    print('-f or --switch_off_timer \t Sets the time interval [in seconds] after its expiration the automatic power off occurs.\
    \n\t\t\t\t Valid values must be between 0 (for inactive timer) and 604800 (for 1 week). Default is 0.')
    print('-r or --reset \t\t\t Reset to default setup. To perform reset set value to 1111\n')

    print('Example:')
    print('rbsetup -p 20 -i 60 --autostart 1')
    print('Command performs setup for Power Board which configures Powerbutton\'s illumination intensity to 20%,\
    \ninfoleds il. intensity to 60% and autostart feature responsible for automatic switch on after\
    \npower re/connection\n')

# Zacatek skriptu
print('Remote board setup tool v.0.0.1')
print('For display additional informations type rbsetup -h/--help\n')

# Parsovani vstupu
parser = argparse.ArgumentParser(add_help=False, formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument('--help', '-h', action='store_true', help=argparse.SUPPRESS)
parser.add_argument('--display_setup', '-d', action='store_true', help=argparse.SUPPRESS)
parser.add_argument('--powerbuttonled', '-p', action='store', choices=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], default='50', type=int, help=argparse.SUPPRESS)
parser.add_argument('--infoleds', '-i', action='store', choices=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], default='50', type=int, help=argparse.SUPPRESS)
parser.add_argument('--autostart', '-a', action='store', choices=[0, 1], default='0', type=int, help=argparse.SUPPRESS)
parser.add_argument('--switch_on_timer', '-n', action='store', type=int, default='0', help=argparse.SUPPRESS)
parser.add_argument('--switch_off_timer', '-f', action='store', type=int, default='0', help=argparse.SUPPRESS)
parser.add_argument('--reset', '-r', action='store', choices='1111', help=argparse.SUPPRESS)

args = parser.parse_args()

# Rucni osetreni vyjimek  
try:
    assert (args.switch_on_timer > -1)
except Exception:
    print('usage: ' + str(sys.argv[0]))
    print('rbsetup.py: error: argument --switch_on_timer/-n: invalid int value: ' + str(args.switch_on_timer))
    sys.exit(1)
    
# Rucni osetreni vyjimek  
try:
    assert (args.switch_off_timer > -1)
except Exception:
    print('usage: ' + str(sys.argv[0]))
    print('rbsetup.py: error: argument --switch_off_timer/-f: invalid int value: ' + str(args.switch_off_timer))
    sys.exit(1)
      
# Reakce na vysledek parsovani
if len(sys.argv) < 2:
    display_help()
    #sys.exit(0)

if args.help:
    display_help()

print('Settings performed as follows:')
print('display_setup (odstranit): ' + str(args.display_setup))
print('powerbuttonled: ' + str(args.powerbuttonled))
print('infoleds: ' + str(args.infoleds))
print('autostart: ' + str(args.autostart))
print('switch_on_timer: ' + str(args.switch_on_timer))
print('switch_off_timer: ' + str(args.switch_off_timer))
print('reset (odstranit): ' + str(args.reset))

# Datovy proud
datovy_proud = str(args.powerbuttonled) + ';' + str(args.infoleds) + ';' + str(args.autostart) + ';' \
+ str(args.switch_on_timer) + ';' + str(args.switch_off_timer) + '*'
print('\nDatovy proud: ' + datovy_proud)

port = serial.Serial("/dev/ttyAMA0", baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=3.0)
print(port.name)         # check which port was really used
port.write('hello')     # write a string
port.close()             # close port
