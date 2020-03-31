import json
import numpy as np

from typing import List, Union, Dict

class Rule:
    def __init__(self, key : str, rules : str, probs : List[float] = [1]):
        self.key = key
        self.rules = rules
        self.probs = probs

    def expand(self) -> str:
        return np.random.choice(self.rules, p=self.probs)

    def __repr__(self) -> str:
        return f'Rule(key={self.key}, rules={self.rules}, probs={self.probs})'

def parse(filename : str) -> Union[str, Dict[str, Rule]]:
    """ Parse the config file """
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


def expand_rule(rule : str, rules : Dict[str, Rule], step : int = 0) -> str:
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
