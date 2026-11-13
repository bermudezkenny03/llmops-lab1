from typing import Protocol

from lab1.domain.entities import BenchmarkRecord


class BenchmarkReporter(Protocol):
    def publish(self, records: list[BenchmarkRecord], destination: str) -> None: ...
