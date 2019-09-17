class Trigger:
    def __init__(self):
        self.calls = {}
        self.t = -1

    # Register an event
    def register(self, reg_t, fn, args = [], kwargs = {}):
        fns = self.calls.get(reg_t, [])
        fns.append((fn, args, kwargs))
        self.calls[reg_t] = fns

    def tick(self):
        self.t += 1
        fns = self.calls.get(self.t)
        for fn, args, kwargs in fns:
            fn(*args, **kwargs)

    def __str__(self):
        s = "Triggers\n"
        for t, fns in sorted(self.calls.items()):
            s += " " + str(t) + ":\n"
            for fnargs in fn:
                s += " -" + str(fnargs)
        return s


global_trigger = Trigger()

class Node:
    def __init__(self, name):
        self.routes = {}
        self.name = name

    def in(self, packet):
        print("Received packet")

    def add_route(self, destination, hop):
        self.routes[destination] = hop

    def out(self, packet):
        nextHop = self.routes[packet.dest.name]
        # Only send if we're not the destination
        if nextHope.name != self.name:
            nextHop.in(packet)


class Router(Node):
    def __init__(self, name, delay, buffer_size = 8):
        super(name, dest)
        self.buffer = []
        self.delay  = delay

    def in(self, packet):
        # Drop if we're full
        if self.buffer.size() >= buffer_size:
            print(name + ": drop")
            return

        self.buffer.append(packet)

        global global_trigger
        global_trigger.register(global_trigger.t + delay * self.buffer.size(), out)

    def out(self):
        packet = self.buffer.pop()
        super().out(packet)

class TCPNode(Node):
    def __init__(self, name):
        super(name)
        self.delay = delay
        self.n = 0

        global global_trigger
        global_trigger.register(global_trigger.t + delay, out)

    def in(self, packet):
        print("ack?")

    def out(self):
        packet = Packet(self, final_dest, self.n)
        dest.in(packet)


class Packet:
    def __init__(self, sender, receiver, num):
        self.num      = num
        self.sender   = sender
        self.receiver = receiver

    def __str__(self):
        return self.sender + "->" + self.receiver + " #" + str(self.num)

routSrc = Router("1", delay = 5, buffer_size = 8)
routDst = Router("2", delay = 1, buffer_size = 8)
src = TCPNode("src")
dst = TCPNode("dst")

# src -> dst
src.add_route("dst", routSrc)
routSrc.add_route("dst", routDst)
routDst.add_route("dst", dst)

# dst -> src
dst.add_route("src", routDst)
routDst.add_route("src", routSrc)
routSrc.add_route("src", src)


