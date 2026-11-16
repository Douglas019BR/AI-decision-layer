"""Implemente aqui o motor de decisão da MAIA. Sem chamadas a sistemas reais."""
from typing import Any


def evaluate_case(case: dict[str, Any]) -> dict[str, Any]:
    """Retorna um objeto de saída definido em docs/CONTRATO.md.

    Requisitos: determinismo no modo offline, auditoria, isolamento de tenant,
    política normativa, deduplicação, consentimento e cálculo de SLA útil.
    """
    raise NotImplementedError("Implemente evaluate_case(case)")
