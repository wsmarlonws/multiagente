from pydantic_settings import BaseSettings, SettingsConfigDict


class Configuracoes(BaseSettings):
    # Banco de dados
    POSTGRES_USER: str = "multiagente"
    POSTGRES_PASSWORD: str = "multiagente123"
    POSTGRES_HOST: str = "postgres"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = "multiagente"

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    # Aplicação
    APP_NOME: str = "multiagente"
    DEBUG: bool = False

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


configuracoes = Configuracoes()
