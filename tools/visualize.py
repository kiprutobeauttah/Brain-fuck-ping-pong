def run(code, steps=500):
    tape = [0] * 64
    ptr = 0
    pc = 0
    stack = []

    for i, c in enumerate(code):
        if c == "[":
            stack.append(i)
        elif c == "]":
            j = stack.pop()
            stack.append((j, i))

    loops = dict(stack)

    step = 0
    while pc < len(code) and step < steps:
        c = code[pc]

        if c == ">": ptr += 1
        elif c == "<": ptr -= 1
        elif c == "+": tape[ptr] += 1
        elif c == "-": tape[ptr] -= 1
        elif c == ".":
            print(chr(tape[ptr] % 256), end="")
        elif c == ",":
            tape[ptr] = 0
        elif c == "[" and tape[ptr] == 0:
            pc = loops[pc]
        elif c == "]" and tape[ptr] != 0:
            pc = loops[pc]

        pc += 1
        step += 1

        if step % 50 == 0:
            print(f"\n[step {step}] ptr={ptr} tape={tape[:10]}")

with open("build/game.bf") as f:
    run(f.read())
