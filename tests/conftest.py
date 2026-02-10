import pytest
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.core.database import Base, obter_sessao
from app.main import app

# Banco SQLite em memória para testes
ENGINE_TESTE = create_async_engine("sqlite+aiosqlite://", echo=False)
SessionTeste = async_sessionmaker(
    bind=ENGINE_TESTE,
    class_=AsyncSession,
    expire_on_commit=False,
)


@pytest.fixture(autouse=True)
async def preparar_banco():
    """Cria tabelas antes de cada teste e limpa depois."""
    async with ENGINE_TESTE.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with ENGINE_TESTE.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


async def obter_sessao_teste():
    """Sobrescreve a dependência de sessão para usar banco de teste."""
    async with SessionTeste() as sessao:
        try:
            yield sessao
            await sessao.commit()
        except Exception:
            await sessao.rollback()
            raise


@pytest.fixture
async def cliente():
    """Cliente HTTP para testar a API."""
    app.dependency_overrides[obter_sessao] = obter_sessao_teste
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://teste") as c:
        yield c
    app.dependency_overrides.clear()
