class AgentMemory:
    def __init__(self):
        self.steps = []
        self.current_step = 0
        self.results = []

    def add_steps(self, steps):
        self.steps = steps

    def next_step(self):
        if self.current_step < len(self.steps):
            step = self.steps[self.current_step]
            self.current_step += 1
            return step
        return None
