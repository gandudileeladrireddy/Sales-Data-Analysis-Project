# Sales-Data-Analysis-Project
Exploratory Data Analysis of sales data using Python, Pandas, and Seaborn.
# Exploratory Data Analysis of Sales Data.

### Project Objective
The goal of this project was to perform a complete Exploratory Data Analysis (EDA) on a raw, unlabeled sales dataset. The process involved a rigorous workflow of data cleaning, feature engineering, and robust outlier treatment to prepare the data for analysis. The final step was to generate a comprehensive dashboard to visualize the data and derive key business insights.

---
### Dataset
The project utilizes a single CSV file (`DSataset.csv`) containing 10,000 anonymized transaction records. The initial data included unnamed numerical features and one categorical column, requiring interpretation and cleaning.

---
### Tools Used
* **Python**
* **Pandas:** For data loading, manipulation, and cleaning.
* **NumPy:** For numerical operations.
* **Matplotlib & Seaborn:** For data visualization, including box plots and the final analysis dashboard.

---
### Analysis Workflow
The project followed a systematic workflow to ensure the integrity and reliability of the final analysis.

**1. Data Cleaning and Preparation:**
* **Column Renaming:** Generic column names (e.g., `Feature_X`) were renamed to meaningful business terms (`Order_Value`, `Unit_Price`, `Gross_Profit`).
* **Handling Missing Values:** Missing values in all numerical columns were imputed using the **median** of each respective column.
* **Duplicate Removal:** Any duplicate rows in the dataset were identified and removed to ensure data accuracy.

**2. Feature Engineering:**
* A unique **`Order_ID`** was created for each transaction to allow for individual record tracking.

**3. Robust Outlier Treatment:**
* A key step in this revised analysis was the robust treatment of outliers. Statistical outliers were identified in both the **`Unit_Price`** and **`Order_Value`** columns.
* These outliers were removed using the **Interquartile Range (IQR) method**, which is a standard and effective technique. This step was critical to ensure that the final analysis and visualizations were based on a realistic and representative range of data.

---
### Key Findings & Conclusion
The analysis of the cleaned and validated data, presented in a comprehensive `2x2` dashboard, yielded several important insights:

* **Category C and B Drive the Business:** The business is heavily dependent on two primary categories. The pie chart shows that **Category C and Category B** together account for a significant majority of all sales transactions.
* **Category C is the Most Profitable:** While sales volume is high for both C and D, the bar chart clearly identifies **Category C** as the most profitable, generating the highest total gross profit.
* **Consistent and Predictable Sales:** The dashboard's key metrics and the histogram show that the `Order_Value` is highly consistent, clustering tightly around the average. This indicates a stable and predictable purchasing behavior from customers.

In conclusion, this EDA provides a more accurate and defensible analysis of the sales data. The key takeaway is that **Category C is the most critical driver of the business's success**, leading in both profitability and sales volume. Future business strategies should prioritize understanding and amplifying the success of Category C, while also maintaining the strong performance of Category B.
* **Below analogy is my assume of the product category so it completly my own analysis**
* **Which helps to understand the raw data i took NAR Mart which is my own assume which is like dmart or reliance mart**
---
# ANALOGY
---

##  The NAR Mart "Shopping Cart" Performance Analysis

Your business is currently driven by a strong, but potentially unbalanced, revenue engine. The key challenge is to maintain the volume and high profit of your staples while strategically activating the low-volume, high-potential categories.

### 1. Performance Overview by Category

We are mapping the specific gross profit percentages to your analogy:

| Category Code | Retail Category | Analogy Role | **Gross Profit %** | Strategic Assessment |
| :--- | :--- | :--- | :--- | :--- |
| **C** | Groceries | **The Staples**  | **40%** | **Powerhouse:** Highest volume and highest profit margin. The absolute foundation of the business. |
| **B** | Pantry Loaders | **The Regulars**  | **30%** | **Strong Contributor:** High frequency and solid profit. A reliable secondary pillar for overall profitability. |
| **A** | Textiles | **The Wants** | **20%** | **Under-leveraged:** Decent margin but likely suffers from low volume compared to C and B. High potential for impulse-driven growth. |
| **D** | Dairy | **The Quick Trip Items**  | **10%** | **Foot-Traffic Driver:** Lowest profit. Essential for bringing customers in, but must be paired with other items to justify the transaction cost. |

### 2. The Core Problem: The **Profit-Volume Disconnect**

The analysis reveals a critical disconnect:

* **Category C (Groceries)** and **Category B (Pantry Loaders)** drive **volume and high profit (40% and 30%)** simultaneously. This is the store's bread-and-butter.
* **Category D (Dairy)** has a **low margin (10%)** and **low volume** (it makes up only 10.1% of sales in your initial scenario). This category is the most resource-intensive per transaction.
* **Category A (Textiles)** has a **mid-range margin (20%)** but is likely not a part of the "main shop," making it an **underperforming asset**.
* **Pantry Loader** is nothing but **Canned & Jarred Goods, Breakfast Cereals, Ready-to-Eat/Cook Mixes, Snacks & Biscuits..etc**

**Conclusion:** Your shopping cart is heavy in high-margin staples (C & B), but transactions are inefficiently low when customers only come for the low-margin necessities (D).

---

## Strategic Improvement Plan: "The Balanced Cart"

The goal is to increase the **Average Transaction Value (ATV)** and **Blended Gross Margin** of every shopping cart by tying low-margin essential purchases (D) to high-margin impulse purchases (A).

### Strategy 1: The **Dairy (D) Multiplier** (Leveraging Foot Traffic)

Instead of accepting Dairy (D) as a standalone, low-profit trip, use its high frequency to drive sales for other categories.

| Action | Categories Involved | Benefit |
| :--- | :--- | :--- |
| **"Quick-Trip Upgrade"** | **D + B (Dairy + Pantry Loaders)** | Use checkout line end-caps to place high-margin impulse items (like premium snacks or sauces) directly near the milk/curd purchase point. When a customer buys Milk (10% GP), they are immediately prompted to grab a 30% GP item (B). |
| **Subscription/Bulk Incentives** | **D + C (Dairy + Groceries)** | Offer a small discount on the next purchase of Groceries (C: 40% GP) only if the customer buys a bundle of Dairy (D) that lasts longer, shifting them from daily small trips to weekly, high-value trips. |

### Strategy 2: The **Textiles (A) Cross-Sell** (Maximizing Impulse Profit)

Textiles (A) has a solid **20% profit margin**—it needs to be integrated into the main shopping path to boost volume.

| Action | Categories Involved | Benefit |
| :--- | :--- | :--- |
| **The "Home Bundle"** | **A + C (Textiles + Groceries)** | During peak festive seasons, place complementary textiles near high-volume Groceries. Example: *Place branded kitchen towels and aprons (A: 20% GP) next to the rice and flour aisle (C: 40% GP).* This converts a staple purchase into a home goods impulse buy. |
| **Loyalty Point Incentives** | **C/B $\rightarrow$ A (High Profit $\rightarrow$ Impulse)** | Structure the loyalty program so that points earned from spending on high-volume, high-margin items (C and B) can only be redeemed for discounts in the Textiles category (A). This forces high-value customers into the mid-margin category, increasing the volume of A sales. |

### Final Conclusion for the Data Analyst

Your primary operational metric should not be the individual profit of Category D, but the **Average Blended Margin per Transaction**.

* A transaction containing only **D** yields **10%** margin.
* A transaction containing **D** (10%), **C** (40%), and **A** (20%) drastically raises the blended margin to over **30%**, while simultaneously justifying the fixed costs of processing the sale.

**Recommendation:** Focus your immediate marketing efforts on **creating mandatory product linkages** between your low-margin traffic driver (D) and your mid-margin impulse profit generator (A), using the high-volume categories (C and B) as the funding mechanism.
