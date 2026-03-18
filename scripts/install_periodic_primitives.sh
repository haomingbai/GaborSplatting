#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
EXT_DIR="$ROOT_DIR/CUDA_modules/PeriodicPrimitivesCUDA"

if [[ ! -d "$EXT_DIR" ]]; then
  echo "[ERROR] Extension directory not found: $EXT_DIR" >&2
  exit 1
fi

# Use the active Python environment whenever possible.
# If no environment is active but uv-managed .venv exists, use uv pip.
if [[ -n "${CONDA_PREFIX:-}" ]]; then
  ENV_KIND="conda"
  INSTALL_CMD=(python -m pip)
elif [[ -n "${VIRTUAL_ENV:-}" ]]; then
  ENV_KIND="venv"
  INSTALL_CMD=(python -m pip)
elif command -v uv >/dev/null 2>&1 && [[ -d "$ROOT_DIR/.venv" ]]; then
  ENV_KIND="uv"
  INSTALL_CMD=(uv pip)
else
  echo "[ERROR] No active Python environment detected." >&2
  echo "Please activate conda/venv first, or create .venv with: uv venv --python 3.10" >&2
  exit 1
fi

echo "[INFO] Installing PeriodicPrimitives in environment: $ENV_KIND"

# Keep build toolchain consistent across conda/uv to avoid known compatibility issues.
"${INSTALL_CMD[@]}" install "numpy<2" "setuptools<70" wheel packaging
"${INSTALL_CMD[@]}" install --no-build-isolation "$EXT_DIR"

echo "[OK] PeriodicPrimitives installation completed."
