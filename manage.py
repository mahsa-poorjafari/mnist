#!/home/mahsa/work/DFKI_hiwi/Baumbach_hiwi/mnist/venv/bin/python2.7

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mnist.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
