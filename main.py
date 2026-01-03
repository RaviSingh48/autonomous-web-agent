import asyncio
from agent.planner import plan
from agent.executor import Executor
from agent.memory import AgentMemory

async def main():
    goal = input("Enter agent goal: ")

    memory = AgentMemory()
    steps = plan(goal)
    memory.add_steps(steps)

    executor = Executor()

    while True:
        step = memory.next_step()
        if not step:
            break

        print("Executing:", step)
        result = await executor.run(step)
        memory.results.append(result)

    print("Task completed")

asyncio.run(main())
