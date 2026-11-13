from lab1.config import LabConfig
from lab1.domain.entities import BenchmarkRecord
from lab1.ports.inference import InferenceGateway
from lab1.ports.reporters import BenchmarkReporter


class BenchmarkRunner:
    def __init__(
        self,
        config: LabConfig,
        gateway: InferenceGateway,
        report_targets: list[tuple[BenchmarkReporter, str]],
    ) -> None:
        self._config = config
        self._gateway = gateway
        self._report_targets = report_targets

    def run(self) -> list[BenchmarkRecord]:
        records: list[BenchmarkRecord] = []
        opts = self._config.inference_options

        for model in self._config.models:
            print(f"--- {model} ---")
            self._gateway.generate(model, self._config.warmup_prompt, opts)
            for prompt in self._config.prompts:
                print(f"  {prompt.tipo}...")
                metrics = self._gateway.generate(model, prompt.texto, opts)
                records.append(BenchmarkRecord(model=model, prompt=prompt, metrics=metrics))

        for reporter, path in self._report_targets:
            reporter.publish(records, path)

        print("Listo:", ", ".join(p for _, p in self._report_targets))
        return records
