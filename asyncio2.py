import asyncio

async def tarefa(nome, tempo):
    print(f'{nome} Começou')
    await asyncio.sleep(tempo)
    print(f'{nome} Terminou')

async def main():
    await asyncio.gather(
    tarefa("Tarefa A", 2),
    tarefa("Tarefa B", 1),
    tarefa("Tarefa C", 3),
    )
    asyncio.run(main())