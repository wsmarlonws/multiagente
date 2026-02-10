from httpx import AsyncClient

BASE_URL = "/api/v1/tarefas"


async def test_criar_tarefa(cliente: AsyncClient):
    resposta = await cliente.post(BASE_URL, json={
        "titulo": "Minha primeira tarefa",
        "descricao": "Descrição de teste",
    })
    assert resposta.status_code == 201
    dados = resposta.json()
    assert dados["titulo"] == "Minha primeira tarefa"
    assert dados["descricao"] == "Descrição de teste"
    assert dados["concluida"] is False
    assert "id" in dados
    assert "criado_em" in dados


async def test_criar_tarefa_sem_descricao(cliente: AsyncClient):
    resposta = await cliente.post(BASE_URL, json={
        "titulo": "Tarefa sem descrição",
    })
    assert resposta.status_code == 201
    assert resposta.json()["descricao"] is None


async def test_criar_tarefa_titulo_vazio(cliente: AsyncClient):
    resposta = await cliente.post(BASE_URL, json={
        "titulo": "",
    })
    assert resposta.status_code == 422


async def test_criar_tarefa_sem_titulo(cliente: AsyncClient):
    resposta = await cliente.post(BASE_URL, json={
        "descricao": "Sem título",
    })
    assert resposta.status_code == 422


async def test_listar_tarefas_vazio(cliente: AsyncClient):
    resposta = await cliente.get(BASE_URL)
    assert resposta.status_code == 200
    dados = resposta.json()
    assert dados["itens"] == []
    assert dados["total"] == 0


async def test_listar_tarefas_com_dados(cliente: AsyncClient):
    await cliente.post(BASE_URL, json={"titulo": "Tarefa 1"})
    await cliente.post(BASE_URL, json={"titulo": "Tarefa 2"})

    resposta = await cliente.get(BASE_URL)
    assert resposta.status_code == 200
    dados = resposta.json()
    assert dados["total"] == 2
    assert len(dados["itens"]) == 2


async def test_listar_tarefas_paginacao(cliente: AsyncClient):
    for i in range(5):
        await cliente.post(BASE_URL, json={"titulo": f"Tarefa {i}"})

    resposta = await cliente.get(f"{BASE_URL}?limite=2&offset=0")
    dados = resposta.json()
    assert len(dados["itens"]) == 2
    assert dados["total"] == 5
    assert dados["limite"] == 2
    assert dados["offset"] == 0


async def test_buscar_tarefa(cliente: AsyncClient):
    criar = await cliente.post(BASE_URL, json={"titulo": "Buscar esta"})
    tarefa_id = criar.json()["id"]

    resposta = await cliente.get(f"{BASE_URL}/{tarefa_id}")
    assert resposta.status_code == 200
    assert resposta.json()["titulo"] == "Buscar esta"


async def test_buscar_tarefa_inexistente(cliente: AsyncClient):
    resposta = await cliente.get(f"{BASE_URL}/9999")
    assert resposta.status_code == 404
    assert "não encontrada" in resposta.json()["detail"].lower()


async def test_atualizar_tarefa(cliente: AsyncClient):
    criar = await cliente.post(BASE_URL, json={"titulo": "Original"})
    tarefa_id = criar.json()["id"]

    resposta = await cliente.put(f"{BASE_URL}/{tarefa_id}", json={
        "titulo": "Atualizado",
        "concluida": True,
    })
    assert resposta.status_code == 200
    dados = resposta.json()
    assert dados["titulo"] == "Atualizado"
    assert dados["concluida"] is True


async def test_atualizar_tarefa_parcial(cliente: AsyncClient):
    criar = await cliente.post(BASE_URL, json={
        "titulo": "Original",
        "descricao": "Descrição original",
    })
    tarefa_id = criar.json()["id"]

    resposta = await cliente.put(f"{BASE_URL}/{tarefa_id}", json={
        "concluida": True,
    })
    assert resposta.status_code == 200
    dados = resposta.json()
    assert dados["titulo"] == "Original"
    assert dados["descricao"] == "Descrição original"
    assert dados["concluida"] is True


async def test_atualizar_tarefa_inexistente(cliente: AsyncClient):
    resposta = await cliente.put(f"{BASE_URL}/9999", json={"titulo": "Nope"})
    assert resposta.status_code == 404


async def test_deletar_tarefa(cliente: AsyncClient):
    criar = await cliente.post(BASE_URL, json={"titulo": "Deletar esta"})
    tarefa_id = criar.json()["id"]

    resposta = await cliente.delete(f"{BASE_URL}/{tarefa_id}")
    assert resposta.status_code == 204

    # Verificar que foi removida
    buscar = await cliente.get(f"{BASE_URL}/{tarefa_id}")
    assert buscar.status_code == 404


async def test_deletar_tarefa_inexistente(cliente: AsyncClient):
    resposta = await cliente.delete(f"{BASE_URL}/9999")
    assert resposta.status_code == 404


async def test_health_check(cliente: AsyncClient):
    resposta = await cliente.get("/health")
    assert resposta.status_code == 200
    assert resposta.json() == {"status": "ok"}
