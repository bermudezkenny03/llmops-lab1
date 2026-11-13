import pandas as pd

from lab1.domain.entities import BenchmarkRecord


class CsvBenchmarkReporter:
    def publish(self, records: list[BenchmarkRecord], destination: str) -> None:
        rows = [
            {
                "Modelo": r.model_short_name,
                "Prompt": r.prompt.tipo,
                "TTFT (ms)": r.metrics.ttft_ms,
                "Velocidad (TPS)": r.metrics.tps,
                "Tokens": r.metrics.tokens_generados,
                "Total (s)": r.metrics.tiempo_total_s,
            }
            for r in records
        ]
        pd.DataFrame(rows).to_csv(destination, index=False)
