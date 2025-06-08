# POS Data Warehouse Project

A portfolio project to practice **ETL pipelines** and **data warehouse modeling** using a local PostgreSQL setup. This project simulates a basic retail Point-of-Sale (POS) analytics workflow, starting from a raw CSV file and ending with a Power BI dashboard connected to a properly modeled star schema.

---

## 🧠 Objective

To reinforce data warehousing concepts by designing a complete **ETL pipeline**, implementing a **star schema**, and visualizing the results using **Power BI**—all without using cloud platforms.

---

## 🛠️ Tools Used

- **Python (Pandas)** – for data cleaning and transformation
- **PostgreSQL** – for storing and modeling the data warehouse
- **pgAdmin** – for schema creation and SQL operations
- **Power BI** – for data visualization and dashboarding

---

## 📁 Project Structure

1. `raw_data.csv` – initial POS data file with transactions
2. `data_cleaning.ipynb` – notebook to transform and generate dimension/fact tables
3. `csv_exports/` – directory containing transformed CSVs: `dim_customer.csv`, `dim_item.csv`, etc.
4. `sql/schema.sql` – SQL script to create the star schema in PostgreSQL
5. `python/insert_data.py` – script to load CSVs into PostgreSQL tables
6. `powerbi_dashboard/` – screenshots of the final Power BI dashboard

---

## 🔄 ETL Flow Summary

- **Extract**: Load raw POS transaction data from a CSV file
- **Transform**: Clean and split data into dimension and fact tables (Python Pandas)
- **Load**: Insert transformed data into PostgreSQL using Python + SQL
- **Visualize**: Build a dashboard in Power BI using the PostgreSQL connection

---

## 🧱 Star Schema Design

![Schema Design](images/star_schema.png)

### Tables:
- `dim_customer`
- `dim_item`
- `dim_payment_method`
- `fact_sales`

---

## 🖼️ Project Workflow Visuals

| Step | Screenshot |
|------|------------|
| Raw CSV Data | ![Raw CSV](images/raw_csv.png) |
| Star Schema Design | ![Schema](images/star_schema.png) |
| Data in PostgreSQL | ![PostgreSQL Tables](images/postgres_ingest.png) |
| PostgreSQL → Power BI | ![Power BI Connection](images/powerbi_connection.png) |
| Final Dashboard | ![Dashboard](images/dashboard.png) |

---

## 📊 Power BI Dashboard Highlights

- Sales by Item Category
- Top Customers by Spending
- Payment Method Distribution
- Daily/Monthly Revenue Trends

---

## 💡 Learning Outcome

This project helped me gain hands-on experience in:
- ETL pipeline design
- Star schema modeling
- PostgreSQL + SQL operations
- Connecting databases to BI tools like Power BI

---
