import time
import asyncio


# Async function that simulates a task and waits for 1 second
async def function1():
    await asyncio.sleep(1)
    print("function1")
    return "return"


# Async function that simulates a task and waits for 1 second
async def function2():
    await asyncio.sleep(1)
    print("function2")
    return "value"


# Async function that simulates a longer task and waits for 2 seconds
async def function3():
    await asyncio.sleep(2)
    print("function3")
    return "of"


# Async function that simulates a task and waits for 1 second
async def function4():
    await asyncio.sleep(1)
    print("function4")
    return "function"


# Async function that simulates a task and waits for 1 second
async def function5():
    await asyncio.sleep(1)
    print("function5")
    return "1, 2, 3, 4, 5"


# Async main function that orchestrates the execution of other functions
async def main():
    # Run function1 in the background while other functions execute
    task = asyncio.create_task(function1())

    # Run the functions sequentially
    await function2()
    await function3()
    await function4()
    await function5()
    print("#\tTask Finished")

    # Run the functions in parallel and gather their results
    results = await asyncio.gather(
        function1(),
        function2(),
        function3(),
        function4(),
        function5()
    )
    print(results)


# Run the main function asynchronously
asyncio.run(main())
