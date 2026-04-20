import time
# from rich import print
import asyncio

async def endpoint(route:str)->str:
    print(f">> handling {route}")
    
    await asyncio.sleep(1)#it has a function like time module
    
    print(f"<< response {route}")
    return route


async def server():
    test = (
        "GET/shipment?id=1",
        "PATCH/shipment?id=4",
        "GET/shipment?id=3",
    )
    # start=time.perf_counter()
    # requests=[
    #     asyncio.create_task(endpoint(route))#Task-Takes a coroutine and creates a task at the same time
    #     for route in test
    # ]
    # done,prending=await asyncio.wait(requests) #wait is a function,processes the iterable of the task,return [task_done,task pending],but returns a coroutine so need to use the await function
    start=time.perf_counter()
    async with asyncio.TaskGroup() as task_grp:
        tasks=[
            task_grp.create_task(endpoint(route))
            for route in test
        ]  
    end=time.perf_counter()
    print(f"end-start: {end-start:.2f}s")
        
asyncio.run(server())