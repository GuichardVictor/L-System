""" actions.py maps a vocabulary to a turtle action """

import turtle

# STATE_STACK will store the state of the turtle when saving it
STATE_STACK = []

def _pipe() -> None:
    """ `|` correspond to a complete turn """
    turtle.left(180)

def _save_state() -> None:
    """ Save the turtle state to the stack """
    global STATE_STACK
    STATE_STACK.append({'pos': turtle.pos(), 'dir': turtle.heading()})

def _load_state() -> None:
    """ Pop the stack to reload the previous state """
    global STATE_STACK
    state = STATE_STACK.pop()
    turtle.setpos(state['pos'])
    turtle.setheading(state['dir'])


# Vocab to action directory
ACTIONS = {
        'F': lambda: turtle.forward(5),
        '+': lambda: turtle.right(25),
        '-': lambda: turtle.left(25),
        '|': _pipe,
        '[': _save_state,
        ']': _load_state
}
