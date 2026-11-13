from dataclasses import dataclass, field

from lab1.domain.entities import PromptSpec


@dataclass(frozen=True)
class InferenceOptions:
    temperature: float = 0.1
    num_ctx: int = 2048


@dataclass(frozen=True)
class LabConfig:
    ollama_generate_url: str = "http://localhost:11434/api/generate"
    models: tuple[str, ...] = (
        "qwen2.5:1.5b-instruct-q4_K_M",
        "qwen2.5:1.5b-instruct-q8_0",
    )
    warmup_prompt: str = "Hola"
    inference_options: InferenceOptions = field(default_factory=InferenceOptions)
    prompts: tuple[PromptSpec, ...] = (
        PromptSpec(
            tipo="Corto (Definición)",
            texto="Explica en exactamente 3 viñetas qué es la cuantización en modelos de lenguaje.",
        ),
        PromptSpec(
            tipo="Medio (Razonamiento)",
            texto=(
                "Tengo un servidor con 16 GB de RAM y sin GPU. Quiero desplegar un asistente "
                "interno para 5 empleados. ¿Qué arquitectura y tamaño de modelo me recomiendas y por qué?"
            ),
        ),
        PromptSpec(
            tipo="Largo (Generación de Código)",
            texto=(
                "Escribe una función en Python bien documentada que implemente búsqueda binaria "
                "sobre una lista ordenada, incluyendo manejo de excepciones y 3 casos de prueba."
            ),
        ),
    )
    csv_output: str = "resultados_benchmark.csv"
    markdown_output: str = "resultados_benchmark.md"


def default_config() -> LabConfig:
    return LabConfig()
