# 📊 KAGGLE DATASET GUIDE & DATABASE SEEDING (OLIST BRAZILIAN E-COMMERCE)

This directory contains the documentation, download automation scripts, and database ETL pipeline for the **Brazilian E-Commerce Public Dataset by Olist**.

---

## 1. DATASET OVERVIEW
- **Source**: [Kaggle: Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
- **Scale**: ~100,000 authentic commercial orders spanning 2016 through 2018.
- **Relational Complexity**: 8 normalized relational tables linking customers, geo-locations, items, sellers, payments, reviews, and categories.

### Key Tables & Files:
| File | Schema / Description |
| :--- | :--- |
| `olist_customers_dataset.csv` | `customer_id`, `customer_unique_id`, `customer_zip_code_prefix`, `customer_city`, `customer_state` |
| `olist_orders_dataset.csv` | `order_id`, `customer_id`, `order_status`, `order_purchase_timestamp`, `order_delivered_customer_date` |
| `olist_order_items_dataset.csv` | `order_id`, `order_item_id`, `product_id`, `seller_id`, `price`, `freight_value` |
| `olist_order_payments_dataset.csv` | `order_id`, `payment_sequential`, `payment_type`, `payment_installments`, `payment_value` |
| `olist_order_reviews_dataset.csv` | `review_id`, `order_id`, `review_score`, `review_comment_title`, `review_comment_message` |
| `olist_products_dataset.csv` | `product_id`, `product_category_name`, `product_weight_g`, `product_length_cm` |

---

## 2. HOW TO DOWNLOAD

### Method A: Automated Download via Kaggle CLI (Recommended)
1. Generate your Kaggle API key: Go to [Kaggle](https://www.kaggle.com) -> Account Settings -> **Create New API Token** (`kaggle.json`).
2. Move it to `~/.kaggle/kaggle.json` and set permissions:
   ```bash
   mkdir -p ~/.kaggle
   mv /path/to/kaggle.json ~/.kaggle/
   chmod 600 ~/.kaggle/kaggle.json
   ```
3. Run the automated download script:
   ```bash
   chmod +x datasets/download_dataset.sh
   ./datasets/download_dataset.sh
   ```

### Method B: Manual Web Download
1. Navigate to [Olist Dataset on Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).
2. Click **Download** (~45 MB zip archive).
3. Extract all CSV files directly into `datasets/data/`.

### Method C: Zero-Download Synthetic Generator (Instant Fallback)
If you do not have a Kaggle account or want to run tests immediately, `seed_data.py` comes with a built-in **Synthetic Data Generator**. If no CSVs are found in `datasets/data/`, the script automatically generates **5,000+ realistic Brazilian e-commerce orders, customers, items, payments, and reviews** with mock vector embeddings.

---

## 3. SEEDING THE DATABASE

Ensure PostgreSQL is running (e.g. via `docker compose up -d postgres`):

```bash
# Install dependencies
pip install -r services/chat-service/requirements.txt

# Run the seeding ETL pipeline
python3 datasets/seed_data.py
```

The script will:
1. Connect to PostgreSQL and enable the `pgvector` extension.
2. Create all relational tables with appropriate primary and foreign keys.
3. Ingest records from CSVs (or generate synthetic data).
4. Populate `order_review_embeddings` with vector embeddings.
5. Create HNSW indexes for sub-millisecond similarity search.
