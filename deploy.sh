#!/usr/bin/env bash
# Runs on the EC2 server after `git pull` (called by .github/workflows/deploy.yml)
set -euo pipefail
cd "$(dirname "$0")"

echo "==> Kutubxonalarni o'rnatish"
.venv/bin/pip install -q -r requirements.txt

echo "==> Migratsiyalarni qo'llash"
# Faqat upgrade! "alembic revision --autogenerate" ni lokalda qiling va commit qiling
.venv/bin/alembic upgrade head

echo "==> Servisni qayta ishga tushirish"
sudo systemctl restart fastapi_blog

echo "==> Health check"
for i in $(seq 1 10); do
    if curl -fs http://127.0.0.1:8000/roothealth; then
        echo
        echo "==> Deploy muvaffaqiyatli: $(git log --oneline -1)"
        exit 0
    fi
    sleep 2
done

echo "==> Ilova ishga tushmadi, oxirgi loglar:"
sudo journalctl -u fastapi_blog --no-pager -n 30
exit 1
