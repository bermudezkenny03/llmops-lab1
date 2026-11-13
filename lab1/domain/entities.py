from dataclasses import dataclass


@dataclass(frozen=True)
class PromptSpec:
    tipo: str
    texto: str


@dataclass(frozen=True)
class InferenceMetrics:
    ttft_ms: float
    tps: float
    tokens_generados: int
    tiempo_total_s: float
    respuesta_completa: str


@dataclass(frozen=True)
class BenchmarkRecord:
    model: str
    prompt: PromptSpec
    metrics: InferenceMetrics

    @property
    def model_short_name(self) -> str:
        return self.model.split(":")[-1] if ":" in self.model else self.model
