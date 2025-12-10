# Tests - Recogning

Sistema de pruebas para Recogning.

## Estructura

```
tests/
├── unit/           # Tests unitarios
├── integration/    # Tests de integración
└── README.md       # Este archivo
```

## Ejecutar Tests

```bash
# Instalar dependencias de desarrollo
pip install -r requirements-dev.txt

# Ejecutar todos los tests
pytest tests/

# Ejecutar solo tests unitarios
pytest tests/unit/

# Ejecutar con cobertura
pytest --cov=recogning tests/
```

## Convenciones

- Tests unitarios: `test_*.py` en `tests/unit/`
- Tests de integración: `test_*_integration.py` en `tests/integration/`
- Fixtures compartidas en `conftest.py`

## Cobertura

Objetivo: Mantener cobertura > 80%

---

**Estado:** 🚧 Tests se añadirán en PHASE 1+
