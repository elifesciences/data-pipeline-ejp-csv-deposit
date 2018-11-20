#!/bin/bash
set -e # everything must succeed.
echo "[-] install.sh"

. mkvenv.sh

source venv/bin/activate

pip install -r requirements-frozen.txt --no-cache-dir

echo "[✓] install.sh"
