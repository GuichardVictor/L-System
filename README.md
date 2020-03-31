# L Systems

Simple 2D L-system algorithm made in python and turtle.

## Usage

```sh
$ python main.py config.json
```

## Config Example

```json
{
    "rules": [
        {
            "key": "F",
            "rule": "FF"
        },
        {
            "key": "X",
            "rule": "F+[-F-XF-X][+FF][--XF[+X]][++F-X]"
        }
    ],
    "axiom": "---X"
}
```

`axiom` is the starting point of the L system, then each rules will be applied.

If two or more rules have the same `key` a probability (`prob`) has to be given to each one and the sum must be equal to 1.

## Authors

Victor Guichard
