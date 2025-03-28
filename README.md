# UnifiedMentor-Laptop_Data_Analysis

# 💻 Laptop Price Analysis

## 📌 Project Overview  
This project explores factors affecting laptop prices using **Exploratory Data Analysis (EDA)**.  
Key aspects analyzed include:  
- **Brand reputation** and its impact on pricing  
- **Hardware specifications** (RAM, CPU, GPU, storage)  
- **Physical attributes** (screen size, weight)  
- **Operating System preferences**  

By leveraging **visualizations and statistical insights**, the analysis helps identify market trends and optimal laptop configurations based on price.

---

## 🗂️ Dataset Information  
- **Number of Records:** ~1300 laptops  
- **Features Included:**  
  - `Company` – Brand of the laptop (Apple, Dell, HP, etc.)  
  - `TypeName` – Laptop category (Gaming, Ultrabook, Notebook, etc.)  
  - `Price_euros` – Price in Euros  
  - `Ram` – RAM size in GB (4GB, 8GB, 16GB, etc.)  
  - `Inches` – Screen size  
  - `Weight` – Weight in kg  
  - `OS` – Operating system (Windows, MacOS, Linux, etc.)  
  - `Storage` – Primary and secondary storage type (SSD/HDD)  
  - `CPU_freq` – CPU frequency  
  - `GPU_company` – GPU brand (NVIDIA, AMD, Intel)  

---

## 🔍 Analysis & Process  

### 🛠️ **1. Data Cleaning & Summary**  
✅ **Handling Missing Values:**  
- Visualized missing data using a **heatmap**.  
- No significant missing values were found.  

✅ **Duplicate Data Check:**  
- Identified and removed duplicate records.  

✅ **Feature Data Types Check:**  
- Ensured appropriate data types for each column.  

---

### 📊 **2. Univariate Analysis**  
📌 **Price Distribution:**  
- Histogram and KDE plot reveal **skewed price distribution**, indicating more laptops in the lower-mid price range.  

📌 **RAM & Storage Analysis:**  
- Boxplots and violin plots show RAM distribution across brands.  

📌 **Screen Size & Weight:**  
- Histogram analysis of laptop sizes and weights shows a preference for **13–15 inch** models.  

📌 **Operating System Trends:**  
- Bar chart visualizes the most common OS choices.  

---

### 🔄 **3. Categorical Feature Analysis**  
📌 **Laptop Brand Distribution:**  
- Countplot shows dominant brands in the dataset.  

📌 **Average Price by Brand:**  
- Boxplot visualization highlights price variations across manufacturers.  

📌 **Laptop Type Preferences:**  
- Pie chart reveals user preferences for **Ultrabooks, Gaming laptops, Notebooks, etc.**  

📌 **Storage Type Influence on Price:**  
- Stacked bar chart illustrates SSD vs. HDD pricing impact.  

---

### 🔗 **4. Relationships Between Variables**  
📌 **Price vs. RAM (Regression Analysis):**  
- Higher RAM **correlates** with higher prices.  

📌 **Price vs. Screen Size:**  
- Larger screens tend to be more expensive.  

📌 **Price vs. Weight (Bubble Chart):**  
- Weight has **moderate impact** on pricing.  

📌 **Retina Display vs. Price:**  
- Retina displays tend to be in premium-priced models.  

📌 **CPU Frequency vs. Price:**  
- Faster CPUs correspond to higher laptop prices.  

---

### 🏗 **5. Feature Engineering & Deep Insights**  
📌 **Extracting Screen Resolution:**  
- Split resolution into **width & height** to assess display trends.  

📌 **GPU Brand Impact on Pricing:**  
- NVIDIA and AMD GPUs are associated with **higher price ranges**.  

📌 **Primary vs. Secondary Storage:**  
- Stacked bar chart shows laptop configurations.  

📌 **Feature Correlation Heatmap:**  
- Reveals relationships between specifications and price.  

---

### 📉 **6. Advanced Statistical Analysis**  
📌 **Outlier Detection:**  
- Identified outliers in laptop prices using **IQR boxplots**.  

📌 **Top 10 Most Expensive Laptops:**  
- Extracted premium models for analysis.  

📌 **CPU Model Pricing Trends:**  
- Bar chart shows price variation across **different CPU models**.  

📌 **Multivariate Analysis (Pairplots):**  
- Pairwise relationships between **price, RAM, screen size, CPU, weight** were explored.  

---

## 📌 Conclusion  
1️⃣ **Brand & Specs Impact Price:**  
   - **Apple & gaming brands** are pricier than budget options.  

2️⃣ **Storage & RAM Correlation with Price:**  
   - **SSD models** cost significantly more than HDD models.  
   - Laptops with **higher RAM (16GB+) have premium pricing**.  

3️⃣ **Operating System Popularity:**  
   - **Windows laptops dominate** the market, followed by **MacOS**.  

4️⃣ **Screen Size & Weight Preferences:**  
   - **13-15 inch screens** are the most popular.  
   - **Lightweight ultrabooks** are in demand.  

5️⃣ **Feature Engineering Insights:**  
   - **Retina Display, CPU speed, and SSD storage** significantly increase laptop cost.  

---

## 📌 Future Work  
- 📊 **Time-series analysis** on laptop pricing trends.  
- 🔍 **Predictive modeling** to estimate laptop prices.  
- 💡 **Feature selection & Machine Learning** for better price predictions.  

---

## 🛠 Tools & Technologies Used  
- **Python**: Data processing & analysis  
- **Pandas & NumPy**: Data manipulation  
- **Seaborn & Matplotlib**: Data visualization  
- **Scikit-learn**: Feature engineering  

---



