import json
import numpy as np

class Rule:
    def __init__(self, key, rules, probs=[1]):
        self.key = key
        self.rules = rules
        self.probs = probs

    def expand(self):
        return np.random.choice(self.rules, p=self.probs)

    def __repr__(self):
        return f'Rule(key={self.key}, rules={self.rules}, probs={self.probs})'

def parse(filename):
    data = None
    with open(filename) as json_file:
        data = json.load(json_file)

    if data is None:
        return None

    rules = dict()
    start = data['axiom']

    for rule in data['rules']:
        if rule['key'] in rules:
            rules[rule['key']].rules.append(rule['rule'])
            try:
                rules[rule['key']].probs.append(rule['prob'])
            except:
                continue
        else:
            if 'prob' in rule:
                rules[rule['key']] = Rule(rule['key'], [rule['rule']], [rule['prob']])
            else:
                rules[rule['key']] = Rule(rule['key'], [rule['rule']])

    return start, rules


def expand_rule(rule, rules, step=0):
    """ Expand the axiom to the step N """
    def expand(current):
        new_rule = ''
        for ele in current:
            if ele in rules:
                new_rule += rules[ele].expand()
            else:
                new_rule += ele

        return new_rule

    expanded = rule
    for _ in range(step):
        expanded = expand(expanded)

    return expanded
