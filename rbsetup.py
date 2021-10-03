#!/usr/bin/python

import argparse

print('Remote board setup tool v.0.0.1\n')


parser = argparse.ArgumentParser(description='')

parser.add_argument('--powerbuttonled', '-p', action='store', default='50', type=int,
                    help='an integer for the accumulator')

parser.add_argument('--infoleds', '-i', action='store', default='50', type=int,
                    help='sum the integers (default: find the max)')

parser.add_argument('--autostart', '-a', action='store', default='0', type=int,
                    help='sum the integers (default: find the max)')

parser.add_argument('--switch_on_timer', '-n', action='store', default='0', type=int,
                    help='sum the integers (default: find the max)')

parser.add_argument('--switch_off_timer', '-f', action='store', default='0', type=int,
                    help='sum the integers (default: find the max)')

try:
    args = parser.parse_args()
except SystemExit:
    print('Input error. The input must be only an integer (whole number) in the given range.')
    
if args.powerbuttonled > 100 or args.powerbuttonled < 10:
    raise Exception('powerbutton value must be between 10 and 100')
if args.infoleds > 100 or args.infoleds < 10:
    raise Exception('infoleds value must be between 10 and 100')
if args.switch_on_timer > 100 or args.switch_on_timer < 0:
    raise Exception('switch_on_timer value must be between 0 and 100')
if args.switch_off_timer > 100 or args.switch_off_timer < 0:
    raise Exception('switch_off_timer value must be between 0 and 100')

print('powerbuttonled: ' + str(args.powerbuttonled))
print('infoleds: ' + str(args.infoleds))
print('autostart: ' + str(args.autostart))
print('switch_on_timer: ' + str(args.switch_on_timer))
print('switch_off_timer: ' + str(args.switch_off_timer))

datovy_proud = str(args.powerbuttonled) + str(args.infoleds) + str(args.autostart) + str(args.switch_on_timer) + str(args.switch_off_timer)

print('\nDatovy proud: ' + datovy_proud)
