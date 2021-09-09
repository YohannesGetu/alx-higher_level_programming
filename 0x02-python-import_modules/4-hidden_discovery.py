#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for i in range(0, len(dir(hidden_4))):
        if dir(hidden_4)[i][0:2] != '__':
            print(dir(hidden_4)[i])
