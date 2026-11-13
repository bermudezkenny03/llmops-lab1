import sys

from lab1.adapters.csv_reporter import CsvBenchmarkReporter
from lab1.adapters.markdown_reporter import MarkdownBenchmarkReporter
from lab1.adapters.ollama_gateway import OllamaInferenceGateway
from lab1.config import default_config
from lab1.services.benchmark_runner import BenchmarkRunner


def main() -> int:
    config = default_config()
    gateway = OllamaInferenceGateway(config.ollama_generate_url)

    if not gateway.is_ready():
        print("Ollama no responde en :11434. Ejecuta: docker compose up -d", file=sys.stderr)
        return 1

    runner = BenchmarkRunner(
        config=config,
        gateway=gateway,
        report_targets=[
            (CsvBenchmarkReporter(), config.csv_output),
            (MarkdownBenchmarkReporter(), config.markdown_output),
        ],
    )
    runner.run()
    return 0
