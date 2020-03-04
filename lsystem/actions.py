import turtle

STATE_STACK = []

def _pipe():
    turtle.left(180)

def _save_state():
    global STATE_STACK
    STATE_STACK.append({'pos': turtle.pos(), 'dir': turtle.heading()})

def _load_state():
    global STATE_STACK
    state = STATE_STACK.pop()
    turtle.setpos(state['pos'])
    turtle.setheading(state['dir'])


ACTIONS = {
        'F': lambda: turtle.forward(5),
        '+': lambda: turtle.right(25),
        '-': lambda: turtle.left(25),
        '|': _pipe,
        '[': _save_state,
        ']': _load_state
}
