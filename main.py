"""main.py"""

import sys
import turtle

from lsystem import actions
from lsystem import rules_conf


def run(rule):
    """ Run the rule  """
    for ele in rule:
        try:
            actions.ACTIONS[ele]()
        except:
            # Dummy command
            continue


def main():
    turtle.speed(20)

    axiom, rules = rules_conf.parse(sys.argv[1])
    rule = rules_conf.expand_rule(axiom, rules, step=4)

    run(rule)

if __name__ == '__main__':
    main()
    turtle.done()
