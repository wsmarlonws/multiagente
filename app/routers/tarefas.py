from fastapi import APIRouter, Depends, HTTPException, Query, Response
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import obter_sessao
from app.models.tarefa import Tarefa
from app.schemas.tarefa import (
    TarefaAtualizar,
    TarefaCriar,
    TarefaLista,
    TarefaResposta,
)

router = APIRouter(prefix="/api/v1/tarefas", tags=["tarefas"])


@router.post("", response_model=TarefaResposta, status_code=201)
async def criar_tarefa(
    dados: TarefaCriar,
    sessao: AsyncSession = Depends(obter_sessao),
) -> Tarefa:
    tarefa = Tarefa(titulo=dados.titulo, descricao=dados.descricao)
    sessao.add(tarefa)
    await sessao.flush()
    await sessao.refresh(tarefa)
    return tarefa


@router.get("", response_model=TarefaLista)
async def listar_tarefas(
    limite: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    sessao: AsyncSession = Depends(obter_sessao),
) -> dict:
    resultado = await sessao.execute(
        select(Tarefa).order_by(Tarefa.criado_em.desc()).offset(offset).limit(limite)
    )
    tarefas = resultado.scalars().all()

    contagem = await sessao.execute(select(func.count(Tarefa.id)))
    total = contagem.scalar_one()

    return {
        "itens": tarefas,
        "total": total,
        "limite": limite,
        "offset": offset,
    }


@router.get("/{tarefa_id}", response_model=TarefaResposta)
async def buscar_tarefa(
    tarefa_id: int,
    sessao: AsyncSession = Depends(obter_sessao),
) -> Tarefa:
    resultado = await sessao.execute(
        select(Tarefa).where(Tarefa.id == tarefa_id)
    )
    tarefa = resultado.scalar_one_or_none()
    if tarefa is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefa


@router.put("/{tarefa_id}", response_model=TarefaResposta)
async def atualizar_tarefa(
    tarefa_id: int,
    dados: TarefaAtualizar,
    sessao: AsyncSession = Depends(obter_sessao),
) -> Tarefa:
    resultado = await sessao.execute(
        select(Tarefa).where(Tarefa.id == tarefa_id)
    )
    tarefa = resultado.scalar_one_or_none()
    if tarefa is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    campos_atualizar = dados.model_dump(exclude_unset=True)
    for campo, valor in campos_atualizar.items():
        setattr(tarefa, campo, valor)

    await sessao.flush()
    await sessao.refresh(tarefa)
    return tarefa


@router.delete("/{tarefa_id}", status_code=204)
async def deletar_tarefa(
    tarefa_id: int,
    sessao: AsyncSession = Depends(obter_sessao),
) -> Response:
    resultado = await sessao.execute(
        select(Tarefa).where(Tarefa.id == tarefa_id)
    )
    tarefa = resultado.scalar_one_or_none()
    if tarefa is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    await sessao.delete(tarefa)
    return Response(status_code=204)
