import asyncio
import aiohttp

#Async
'''async def tarefa(nome, tempo):
    print(f'{nome} Começou')
    await asyncio.sleep(tempo)
    print(f'{nome} Terminou')

async def main():
    await asyncio.gather(
    tarefa("Tarefa A", 2),
    tarefa("Tarefa B", 1),
    tarefa("Tarefa C", 3),
    )
asyncio.run(main())'''


async def buscar(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=False) as resposta:
            print(f'{url}: {resposta.status}')
async def main():
    urls = ["https://httpbin.org/delay/1", "https://httpbin.org/delay/2", "https://httpbin.org/delay/3", "https://httpbin.org/delay/4"]
    await asyncio.gather(*(buscar(url) for url in urls))
asyncio.run(main())
