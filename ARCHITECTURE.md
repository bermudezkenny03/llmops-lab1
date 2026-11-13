# Arquitectura (hexagonal + SOLID)

```
lab1/                    # Núcleo del dominio
├── config.py            # Modelos, prompts, rutas de salida
├── domain/entities.py   # PromptSpec, métricas, registros
├── ports/               # Contratos (Protocol)
├── adapters/            # Ollama HTTP, CSV, Markdown
├── services/            # BenchmarkRunner (orquestación)
└── cli.py               # Composición / inyección de dependencias

benchmark.py             # Entrada: python benchmark.py
```

| Principio | Dónde |
|-----------|--------|
| **S** | Cada carpeta una responsabilidad |
| **O** | Nuevo reporte = nueva clase `BenchmarkReporter` |
| **L** | Cualquier `InferenceGateway` válido en el runner |
| **I** | Puertos pequeños: `generate`, `publish` |
| **D** | `BenchmarkRunner` solo usa `ports/`; `cli.py` cablea adaptadores |

Flujo: `cli` → `BenchmarkRunner` → `OllamaInferenceGateway` → reporters.
