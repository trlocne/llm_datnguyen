# Makefile
# =========================================================
# PURPOSE: Developer shortcuts — không cần nhớ lệnh dài.
#
# WHAT TO IMPLEMENT:
#   make setup
#     → cp .env.example .env
#     → pip install -r services/chat-service/requirements.txt
#
#   make seed
#     → docker compose up -d postgres
#     → sleep 5
#     → python3 datasets/seed_data.py
#
#   make up
#     → docker compose up -d --build
#
#   make down
#     → docker compose down -v
#
#   make logs SERVICE=chat-service
#     → docker compose logs -f $(SERVICE)
#
#   make test
#     → pytest tests/ -v --tb=short
#
#   make vault-init
#     → Chạy script security/vault/scripts/init-vault.sh thủ công
#
#   make k8s-dry-run
#     → kubectl apply --dry-run=client -f k8s/
#     → Kiểm tra syntax K8s manifests
#
#   make fmt
#     → black services/ datasets/ security/
#     → prettier --write frontend/src/
#
# =========================================================
