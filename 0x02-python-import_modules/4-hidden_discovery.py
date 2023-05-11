#!/usr/bin/python3

if __name__ == "__main__":
    """Output is the names in hidden_4 module."""
    import hidden_4 as hidden

    for name in dir(hidden):
        if name[:2] != "__":
            print(name)
