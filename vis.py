import os
import argparse
import streamlit as st

# pass params as args
# https://gist.github.com/markopy/ff82a054de47612f748fb6e388bf5588
# streamlit run visualisation/vis.py -- --animal cat

parser = argparse.ArgumentParser(description='test app')

parser.add_argument('--namespace', default="",help='namespace')
parser.add_argument('--logdir', default="",help='log dir')
parser.add_argument('--datadir', default="s3://data/path",help='data dir')
parser.add_argument('--var1', default="val1",help='var1')
parser.add_argument('--var2', default="val2",help='var2')

try:
    args = parser.parse_args()
except SystemExit as e:
    # This exception will be raised if --help or invalid command line arguments
    # are used. Currently streamlit prevents the program from exiting normally
    # so we have to do a hard exit.
    # os._exit(e.code)
    pass

st.write("""
# Params \n
datadir = {datadir}\n
var1 = {var1}\n
var2 = {var2}\n
""".format(datadir=args.datadir, var1=args.var1, var2=args.var2))
