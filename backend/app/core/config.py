from pathlib import Path
from typing import Dict, List, Optional
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

# Determinar raíz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent.parent
PROJECT_ROOT = BASE_DIR.parent


class Settings(BaseSettings):
    PROJECT_NAME: str = "OpenNavy - Sovereign Fleet Navigator"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"

    # Database (SQLite by default for local ease, switchable to PostgreSQL)
    DATABASE_URL: str = Field(
        default=f"sqlite:///{BASE_DIR / 'opennavy.db'}",
        description="SQLAlchemy database connection URL"
    )

    # Preferred LLM Provider: "auto", "google", "openai", "ollama"
    LLM_PROVIDER: str = Field(default="ollama", description="LLM provider: ollama, auto, google, or openai")

    # Ollama / llama.cpp Configuration (Local On-Premise Inference - ADR-001 / ADR-003)
    OLLAMA_BASE_URL: str = Field(default="http://localhost:11434", description="Base URL of local Ollama / llama.cpp instance")
    OPENNAVY_TIER: str = Field(default="e2b", description="Hardware profile: e4b (deep reasoning) or e2b (ultra-fast)")
    PRAXIA_LOCAL_TIER: str = Field(default="standard", description="Legacy compatibility alias for local tier")
    OLLAMA_MODEL: str = Field(default="gemma4:e2b", description="Primary Google Gemma 4 navigation model")
    OLLAMA_FALLBACK_MODEL: str = Field(default="gemma4:e4b", description="Secondary contingency model")


    # Google AI Studio / Gemini Configuration
    GOOGLE_API_KEY: Optional[str] = Field(default=None, description="Google AI Studio / Gemini API Key")
    GEMINI_API_KEY: Optional[str] = Field(default=None, description="Alias for Gemini API Key")
    GOOGLE_MODEL: str = Field(default="gemini-1.5-flash", description="Google Gemini model for evaluation and chat")

    # OpenAI Configuration
    OPENAI_API_KEY: Optional[str] = Field(default=None, description="OpenAI API Key")
    OPENAI_MODEL: str = Field(default="gpt-4o-mini", description="OpenAI model for evaluation")
    EMBEDDING_MODEL: str = Field(default="text-embedding-3-large", description="RAG embedding model")

    # Security and Webhooks
    WEBHOOK_SECRET: Optional[str] = Field(default=None, description="Shared HMAC-SHA256 secret for GitHub Webhooks")
    GITLAB_WEBHOOK_TOKEN: Optional[str] = Field(default=None, description="Secret token for GitLab Webhooks")

    # System Paths
    KNOWLEDGE_BASE_PATH: Path = PROJECT_ROOT / "docs" / "knowledge_base"
    CLONE_STORAGE_PATH: Path = BASE_DIR / "temp_repos"

    # Criteria Weights for Global Health Score (Sum = 1.00)
    CRITERIA_WEIGHTS: Dict[str, float] = {
        "maintainability_index": 0.15,
        "cyclomatic_complexity": 0.15,
        "solid_principles": 0.15,
        "code_duplication": 0.10,
        "test_coverage": 0.15,
        "architecture": 0.15,
        "clean_code": 0.05,
        "dependency_version_control": 0.10,
    }

    # Critical Alert Thresholds
    CRITICAL_SCORE_THRESHOLD: float = 60.0
    HIGH_COMPLEXITY_THRESHOLD: int = 15
    LOW_MAINTAINABILITY_THRESHOLD: float = 50.0

    # CORS
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "*"
    ]

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="allow"
    )


settings = Settings()
