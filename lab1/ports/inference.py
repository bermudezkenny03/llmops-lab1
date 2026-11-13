from typing import Protocol

from lab1.config import InferenceOptions
from lab1.domain.entities import InferenceMetrics


class InferenceGateway(Protocol):
    def generate(self, model: str, prompt: str, options: InferenceOptions) -> InferenceMetrics: ...
