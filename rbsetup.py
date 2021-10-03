#!/usr/bin/python

import argparse
import sys

def display_help():
    print('Usage: rbsetup [options]')
    print('Options:')
    print('-h or --help \t\t\t Displays help')
    print('-d or --display_setup \t\t Displays current setup for Remote Board.')
    print('-p or --powerbuttonled \t\t Sets intensity of Powerbutton LED (RED/WHITE).\
    \n\t\t\t\t Valid values must be between 10 and 100 (%). Default is 50.')
    print('-i or --infoleds \t\t Sets intensity of Status LEDs.\
    Valid values must be between 10 and 100 (%). \n\t\t\t\t Default is 50.')
    print('-a or --autostart \t\t Power-on state when power is re/connected to Power Board. \
    \n\t\t\t\t Valid values are 0 for OFF or 1 (or more than 1) for ON. Default is 0.')
    print('-n or --switch_on_timer \t Sets the time interval [in seconds] after its expiration the automatic power on occurs.\
    \n\t\t\t\t Valid values must be between 10 and 100 (%). Default is 0.')
    print('-f or --switch_off_timer \t Sets the time interval [in seconds] after its expiration the automatic power off occurs.\
    \n\t\t\t\t Valid values must be between 10 and 100 (%). Default is 0.')
    print('-r or --reset \t\t\t Reset to default setup. \
    \n\t\t\t\t To perform reset set value to 1111\n')

    print('Example:')
    print('rbsetup -p 25 -i 33 --autostart 1')
    print('Command performs setup for Power Board which configures Powerbutton\'s illumination intensity to 25%,\
    \ninfoleds il. intensity to 33% and autostart feature responsible for automatic switch on after\
    \npower re/connection\n')

# Zacatek skriptu
print('Remote board setup tool v.0.0.1')
print('For display additional informations type rbsetup -h/--help\n')

parser = argparse.ArgumentParser(add_help=False)

parser.add_argument('--help', '-h', action='store_true')
parser.add_argument('--display_setup', '-d', action='store', default='0', type=int)
parser.add_argument('--powerbuttonled', '-p', action='store', default='50', type=int)
parser.add_argument('--infoleds', '-i', action='store', default='50', type=int)
parser.add_argument('--autostart', '-a', action='store', default='0', type=int)
parser.add_argument('--switch_on_timer', '-n', action='store', default='0', type=int)
parser.add_argument('--switch_off_timer', '-f', action='store', default='0', type=int)

# Osetreni vstupu
try:
    args = parser.parse_args()
    if args.powerbuttonled > 100 or args.powerbuttonled < 10:
        raise Exception('powerbutton value must be between 10 and 100')
    if args.infoleds > 100 or args.infoleds < 10:
        raise Exception('infoleds value must be between 10 and 100')
    if args.switch_on_timer > 100 or args.switch_on_timer < 0:
        raise Exception('switch_on_timer value must be between 0 and 100')
    if args.switch_off_timer > 100 or args.switch_off_timer < 0:
        raise Exception('switch_off_timer value must be between 0 and 100')
except SystemExit:
    print('Input error. The input must be only an integer (whole number) in the given range.')

if len(sys.argv)<2 or args.help:
    display_help()
    sys.exit(1)
    
print('display_setup: ' + str(args.display_setup))
print('powerbuttonled: ' + str(args.powerbuttonled))
print('infoleds: ' + str(args.infoleds))
print('autostart: ' + str(args.autostart))
print('switch_on_timer: ' + str(args.switch_on_timer))
print('switch_off_timer: ' + str(args.switch_off_timer))

datovy_proud = str(args.powerbuttonled) + str(args.infoleds) + str(args.autostart) + str(args.switch_on_timer) + str(args.switch_off_timer)

print('\nDatovy proud: ' + datovy_proud)
