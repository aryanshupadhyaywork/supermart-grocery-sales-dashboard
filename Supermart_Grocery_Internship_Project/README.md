# Supermart Grocery Sales Dashboard — Internship Project

## Overview
An end-to-end retail analytics portfolio project based on the supplied SapphireIQ project brief and CSV dataset. It explores overall performance, product/category performance, discounts and profit, and geographic performance.

## Dataset
- Rows: 9,994
- Fields: 11
- Date coverage after normalization: 2015-01-02 to 2018-12-30
- Source: `Supermart Grocery Sales - Retail Analytics Dataset.csv` (provided)

## Deliverables
- `dashboard.html` — interactive dashboard (Chart.js loads from a CDN, so an internet connection is needed to render charts).
- `Supermart_Grocery_Analysis.xlsx` — cleaned data and analysis sheets.
- `Internship_Project_Report.pdf` — concise project report and findings.
- `analysis.py` — reproducible analysis script.
- `data/retail_sales.csv` — normalized dataset used in the workbook/dashboard.
- `README.md` — this guide.

## Quick start
1. Open `dashboard.html` in Chrome, Safari, or Edge with internet access.
2. Open the Excel workbook to inspect the cleaned dataset and pivot-style summaries.
3. Read the PDF report for project objectives, methodology, findings and limitations.

## Key results
- Total sales: ₹14,956,982.00
- Total profit: ₹3,747,121.20
- Records / order IDs: 9,994
- Average discount rate: 22.68%
- Overall profit margin: 25.05%

## Data-quality note
The source contains mixed date separators. Dates were parsed using a consistent day-first interpretation; all 9,994 records parsed successfully. The `State` field contains only Tamil Nadu, so the source cannot support a meaningful state-to-state comparison. The dashboard reports average discount rather than summing discount rates.

## Suggested internship submission
Submit the ZIP folder or its contents as required by the internship coordinator. If the organization expects a Power BI `.pbix` file, this package does not include one; the HTML dashboard and Excel analysis are working deliverables, but a Power BI version would need to be built in Power BI Desktop.
