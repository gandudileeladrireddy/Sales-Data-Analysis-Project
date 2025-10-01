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
