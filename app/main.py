from fastapi import FastAPI

from app.routers import tarefas

app = FastAPI(
    title="multiagente",
    description="API REST de tarefas (todo-list)",
    version="0.1.0",
)

app.include_router(tarefas.router)


@app.get("/health")
async def health_check() -> dict:
    return {"status": "ok"}
