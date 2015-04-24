__author__ = 'Taikor'


class pipeline:
    def __init__(self, input, jobs):
        self.input = input
        self.jobs = jobs

    def pipelining(self):
        flowin = None
        flowout = None

        size = len(self.jobs)
        flowout = self.jobs[0](self.input)
        for i in range(size-1):
            flowin = self.jobs[i](flowout)
            flowout = flowin

        return flowout
