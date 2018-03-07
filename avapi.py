#!/usr/bin/env python

import argparse
import json

from pprint import pprint

import avapi

parser = argparse.ArgumentParser()
parser.add_argument('-g', '--get', nargs='+', action='store')
parser.add_argument('-k', '--key', type=str)
parser.add_argument('-v', '--verbose', action='store_true')

args = parser.parse_args()

av = avapi.Avapi(
                 key=args.key,
                 verbose=args.verbose
                )

get_functions = {
    'intraday'        : av.intraday,
    'daily'           : av.daily,
    'daily-adjusted'  : av.daily_adjusted,
    'weekly'          : av.weekly,
    'weekly-adjusted' : av.weekly_adjusted,
    'monthly'         : av.monthly_adjusted,
    'batch'           : av.batch
}

if args.get is not None:
    pprint(get_functions[args.get[0]](*args.get[1:]))
