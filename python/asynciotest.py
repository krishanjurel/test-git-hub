import asyncio
import concurrent.futures
import time
async def nested(saythis, after):
	await asyncio.sleep(after)
	print (saythis)

async def nested1(saythis, after):
	await asyncio.sleep(after)
	print (saythis)


async def test_pool():
	loop = asyncio.get_running_loop()
	print(f"started at {time.strftime('%X')}")
	with concurrent.futures.ThreadPoolExecutor() as pool:
		result = await loop.run_in_executor(pool, nested, "I was first", 5)
	loop1 = asyncio.get_running_loop()
	print(f"started at {time.strftime('%X')}")
	with concurrent.futures.ThreadPoolExecutor() as pool1:
		result1 = await loop1.run_in_executor(pool1, nested1, "I was second", 2)
	#task = asyncio.create_task(nested())
	await nested("hey", 5)
	await nested1("second hey", 2)
	
	
	#task = asyncio.sleep(2)
	#await task

async def test_task():
	#task1 = asyncio.create_task(nested("hello I was first still second", 5))
	#task2 = asyncio.create_task(nested("Hello I was second still first", 2))
	
	#await task1
	#await task2
	await asyncio.gather(nested("hello I was first still second", 5),
						 nested("Hello I was second still first", 2),)
						 
						 
async def main():
	await test_pool()
	
asyncio.run(main())