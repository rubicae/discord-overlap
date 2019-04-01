#!/bin/bash
cd "$(dirname "${BASH_SOURCE[0]}")"
if [ ! -d venv ]; then
  virtualenv --python=python3 venv
fi
source venv/bin/activate
pip install -r requirements.txt
grep -l -R 'asyncio.async' venv/lib/python*/site-packages/ |\
 xargs sed -i 's/asyncio.async/asyncio.__dict__["async"]/g'
