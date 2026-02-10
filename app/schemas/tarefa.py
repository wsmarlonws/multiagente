from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class TarefaCriar(BaseModel):
    titulo: str = Field(..., min_length=1, max_length=255)
    descricao: str | None = None


class TarefaAtualizar(BaseModel):
    titulo: str | None = Field(None, min_length=1, max_length=255)
    descricao: str | None = None
    concluida: bool | None = None


class TarefaResposta(BaseModel):
    id: int
    titulo: str
    descricao: str | None
    concluida: bool
    criado_em: datetime
    atualizado_em: datetime

    model_config = ConfigDict(from_attributes=True)


class TarefaLista(BaseModel):
    itens: list[TarefaResposta]
    total: int
    limite: int
    offset: int
