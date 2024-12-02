class Module:
    def __init__(self, line):
        name, dests = line.split(" -> ")
        if name == "broadcaster":
            self.name = name
            self.type = "B"
        else:
            self.name = name[1:]
            self.type = name[0]
        self.state = False
        self.dests = dests.split(", ")
        self.inputs = {}


class System:
    def __init__(self, input):
        self.modules = {m.name: m for m in map(Module, input.splitlines())}
        for empty in ("output", "rx"):
            self.modules[empty] = Module(f"{empty} -> ")
            self.modules[empty].dests = []
        for m in self.modules.values():
            for d in m.dests:
                self.modules[d].inputs[m.name] = False

        self.Q = []
        self.pulses = [0, 0]
        self.buttonPresses = 0

    def buttonPress(self):
        self.buttonPresses += 1
        self.Q = [("button", "broadcaster", False)]
        while self.Q:
            self.process(*self.Q.pop(0))

    def process(self, source, name, level):
        self.pulses[level] += 1
        mod = self.modules[name]
        if mod.type == "%":
            if level:
                return
            mod.state = not mod.state
        elif mod.type == "&":
            mod.inputs[source] = level
            mod.state = not all(mod.inputs.values())
        for d in mod.dests:
            self.Q.append((name, d, mod.state))

    def score(self):
        return self.pulses[0] * self.pulses[1]


s = System(open("input.txt").read())
for _ in range(1000):
    s.buttonPress()
print(s.score())
