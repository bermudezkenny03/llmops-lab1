# Lab 1 — Benchmarking local y cuantización

## Ejecutar

```powershell
docker compose up -d
docker exec -it ollama-local-lab ollama pull qwen2.5:1.5b-instruct-q4_K_M
docker exec -it ollama-local-lab ollama pull qwen2.5:1.5b-instruct-q8_0
pip install -r requirements.txt
python benchmark.py
```

Guía: `guia-lab1-benchmarking.html` · Arquitectura: `ARCHITECTURE.md`
