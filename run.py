#!/usr/bin/env python3
"""Um JSON de entrada -> um JSON de saída. Logs devem ir a stderr."""
import json
import sys
from src.engine import evaluate_case


def main() -> int:
    for raw in sys.stdin:
        if not raw.strip():
            continue
        case = json.loads(raw)
        result = evaluate_case(case)
        print(json.dumps(result, ensure_ascii=False, separators=(',', ':')))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
