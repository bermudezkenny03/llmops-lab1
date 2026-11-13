from lab1.domain.entities import BenchmarkRecord


class MarkdownBenchmarkReporter:
    def publish(self, records: list[BenchmarkRecord], destination: str) -> None:
        md = "# Reporte de Benchmark y Respuestas: LLMOps Lab 1\n\n---\n\n"
        for idx, r in enumerate(records, 1):
            m = r.metrics
            md += f"## Prueba {idx}: {r.model}\n\n"
            md += f"- **Prompt:** {r.prompt.tipo}\n"
            md += f"- **Métricas:** TTFT {m.ttft_ms} ms | TPS {m.tps} | Tokens {m.tokens_generados}\n\n"
            md += f"> {r.prompt.texto}\n\n```text\n{m.respuesta_completa}\n```\n\n---\n\n"
        with open(destination, "w", encoding="utf-8") as f:
            f.write(md)
