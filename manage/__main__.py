import argparse
from lib.manage_lab import mklab, rmlab

# top-level parser
parser = argparse.ArgumentParser(prog="python manage", description="Managament programs for lazy people")
subparsers = parser.add_subparsers(title="commands", dest="command")

# create parser for "mklab" command
mklab_parser = subparsers.add_parser("mklab", help="Create new lab folder")
mklab_parser.add_argument("Name", type=str, help="Name of the lab")

# create parser for "rmlab" command
rmlab_parser = subparsers.add_parser("rmlab", help="Delete lab folder")
rmlab_parser.add_argument("Name", type=str, help="Name of the lab")

args = parser.parse_args()

if args.command == "mklab":
    mklab(args.Name)
elif args.command == "rmlab":
    rmlab(args.Name)
else:
    parser.print_help()