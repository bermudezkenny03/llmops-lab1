import json
import time

import requests

from lab1.config import InferenceOptions
from lab1.domain.entities import InferenceMetrics


class OllamaInferenceGateway:
    def __init__(self, generate_url: str) -> None:
        self._url = generate_url

    def generate(self, model: str, prompt: str, options: InferenceOptions) -> InferenceMetrics:
        payload = {
            "model": model,
            "prompt": prompt,
            "stream": True,
            "options": {
                "temperature": options.temperature,
                "num_ctx": options.num_ctx,
            },
        }

        start = time.perf_counter()
        first_token = None
        parts: list[str] = []
        eval_count = 0
        eval_duration_ns = 0

        with requests.post(self._url, json=payload, stream=True, timeout=600) as resp:
            resp.raise_for_status()
            for line in resp.iter_lines():
                if not line:
                    continue
                chunk = json.loads(line.decode("utf-8"))
                if first_token is None and chunk.get("response"):
                    first_token = time.perf_counter()
                parts.append(chunk.get("response", ""))
                if chunk.get("done"):
                    eval_count = chunk.get("eval_count", 0)
                    eval_duration_ns = chunk.get("eval_duration", 1)

        end = time.perf_counter()
        ttft_ms = (first_token - start) * 1000 if first_token else 0.0
        tps = eval_count / (eval_duration_ns / 1e9) if eval_duration_ns else 0.0

        return InferenceMetrics(
            ttft_ms=round(ttft_ms, 2),
            tps=round(tps, 2),
            tokens_generados=eval_count,
            tiempo_total_s=round(end - start, 2),
            respuesta_completa="".join(parts),
        )

    def is_ready(self) -> bool:
        try:
            base = self._url.rsplit("/api/", 1)[0]
            requests.get(f"{base}/api/tags", timeout=3).raise_for_status()
            return True
        except requests.RequestException:
            return False
