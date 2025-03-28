
'''

TO RUN IN PROGRAM AND OBTAIN VISUALZATIONS
STEP 1 DOWNLOAD THE FILE FROM DATA SET FOLDER
STEP 2 CHANGE THE df PATH TO YOUR FILE LOCATION
STEP 3 RUN THE CODE (COLAB,JUPYTER NOTEBOOK OR ANY OTHER ENVIROMENT)

'''


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# Load the dataset (Modify the path if needed)
df = pd.read_csv("laptop_prices.csv")

# 📌 1. Data Cleaning & Summary

# 1️⃣ Missing Values Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cmap="viridis", cbar=False)
plt.title("Missing Values Heatmap")
plt.show()

# 2️⃣ Duplicate Data Check
duplicates = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")

# 3️⃣ Feature Data Types Summary
print(df.info())

# 📌 2. Univariate Analysis

# 4️⃣ Price Distribution (Histogram + KDE Plot)
plt.figure(figsize=(8, 5))
sns.histplot(df["Price_euros"], kde=True, bins=30, color="blue")
plt.title("Price Distribution")
plt.xlabel("Price (Euros)")
plt.ylabel("Frequency")
plt.show()

# 5️⃣ RAM Distribution (Boxplot + Violin Plot)
plt.figure(figsize=(8, 5))
sns.boxplot(x=df["Ram"], color="red")
plt.title("RAM Distribution")
plt.show()

# 6️⃣ Screen Size Analysis (Histogram)
plt.figure(figsize=(8, 5))
sns.histplot(df["Inches"], bins=20, kde=True, color="green")
plt.title("Screen Size Distribution")
plt.show()

# 7️⃣ Weight Distribution (Histogram + Boxplot)
plt.figure(figsize=(8, 5))
sns.histplot(df["Weight"], bins=20, kde=True, color="purple")
plt.title("Weight Distribution")
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(x=df["Weight"], color="purple")
plt.title("Weight Distribution (Boxplot)")
plt.show()

# 📌 3. Categorical Analysis

# 8️⃣ Laptop Brand Distribution (Bar Chart)
plt.figure(figsize=(12, 6))
sns.countplot(y=df["Company"], order=df["Company"].value_counts().index, palette="coolwarm")
plt.title("Laptop Brand Distribution")
plt.show()

# 9️⃣ Average Price by Brand (Boxplot)
plt.figure(figsize=(12, 6))
sns.boxplot(x="Company", y="Price_euros", data=df, palette="coolwarm")
plt.xticks(rotation=45)
plt.title("Average Price by Brand")
plt.show()

# 🔟 Laptop Type Distribution (Pie Chart)
df["TypeName"].value_counts().plot.pie(autopct="%1.1f%%", figsize=(8, 8), colors=sns.color_palette("coolwarm"))
plt.title("Laptop Type Distribution")
plt.ylabel("")
plt.show()

# 1️⃣1️⃣ Operating System Popularity (Bar Chart)
plt.figure(figsize=(10, 5))
sns.countplot(x=df["OS"], order=df["OS"].value_counts().index, palette="magma")
plt.xticks(rotation=45)
plt.title("Operating System Popularity")
plt.show()

# 📌 4. Relationship Between Variables

# 1️⃣2️⃣ Price vs. RAM (Scatter Plot with Regression Line)
plt.figure(figsize=(10, 5))
sns.regplot(x="Ram", y="Price_euros", data=df, scatter_kws={"alpha": 0.5}, line_kws={"color": "red"})
plt.title("Price vs. RAM")
plt.show()

# 1️⃣3️⃣ Price vs. Screen Size (Regression Line)
plt.figure(figsize=(10, 5))
sns.regplot(x="Inches", y="Price_euros", data=df, scatter_kws={"alpha": 0.5}, line_kws={"color": "red"})
plt.title("Price vs. Screen Size")
plt.show()

# 1️⃣4️⃣ Price vs. Weight (Bubble Chart)
plt.figure(figsize=(10, 5))
plt.scatter(df["Weight"], df["Price_euros"], alpha=0.5, c=df["Ram"], cmap="viridis", edgecolors="k")
plt.colorbar(label="RAM Size")
plt.xlabel("Weight (kg)")
plt.ylabel("Price (Euros)")
plt.title("Price vs. Weight (Bubble Chart)")
plt.show()

# 1️⃣5️⃣ Impact of Retina Display on Price (Boxplot)
plt.figure(figsize=(8, 5))
sns.boxplot(x="RetinaDisplay", y="Price_euros", data=df, hue="RetinaDisplay", palette="coolwarm")
plt.title("Impact of Retina Display on Price")
plt.show()

# 1️⃣6️⃣ Price vs. CPU Frequency (Scatter Plot)
plt.figure(figsize=(10, 5))
sns.scatterplot(x="CPU_freq", y="Price_euros", data=df, alpha=0.5, color="red")
plt.title("Price vs. CPU Frequency")
plt.show()

# 📌 5. Feature Engineering & Deep Insights

# 1️⃣7️⃣ Extracting Screen Resolution (Width & Height Analysis)
plt.figure(figsize=(8, 5))
sns.histplot(df["ScreenW"], bins=30, kde=True, color="blue")
plt.title("Screen Width Distribution")
plt.show()

# 1️⃣8️⃣ Storage Type Impact on Price (Stacked Bar Chart)
plt.figure(figsize=(10, 5))
sns.barplot(x="PrimaryStorageType", y="Price_euros", data=df, estimator=np.mean, palette="magma")
plt.title("Storage Type Impact on Price")
plt.show()

# 1️⃣9️⃣ GPU Company vs. Price (Boxplot)
plt.figure(figsize=(12, 6))
sns.boxplot(x="GPU_company", y="Price_euros", data=df, palette="coolwarm")
plt.xticks(rotation=45)
plt.title("GPU Company vs. Price")
plt.show()

# 2️⃣0️⃣ Primary Storage vs. Secondary Storage (Stacked Bar Chart)
plt.figure(figsize=(12, 6))
df.groupby(["PrimaryStorage", "SecondaryStorage"]).size().unstack().plot(kind="bar", stacked=True, figsize=(12, 6), colormap="viridis")
plt.title("Primary Storage vs. Secondary Storage")
plt.show()

# 2️⃣1️⃣ Correlation Heatmap (Fixed)
df_encoded = df.copy()
categorical_cols = df.select_dtypes(include=['object']).columns

for col in categorical_cols:
    df_encoded[col] = LabelEncoder().fit_transform(df[col])

plt.figure(figsize=(12, 8))
sns.heatmap(df_encoded.corr(), cmap="coolwarm", annot=True)
plt.title("Feature Correlation Heatmap (Fixed)")
plt.show()

# 📌 6. Advanced Statistical Analysis

# 2️⃣2️⃣ Outlier Detection (IQR + Boxplots for Price)
plt.figure(figsize=(8, 5))
sns.boxplot(y=df["Price_euros"], color="red")
plt.title("Outlier Detection: Price")
plt.show()

# 2️⃣3️⃣ Top 10 Most Expensive Laptops (Table Visualization)
print(df.nlargest(10, "Price_euros")[["Company", "TypeName", "Price_euros"]])

# 2️⃣4️⃣ CPU Model Price Trend (Bar Chart)
plt.figure(figsize=(22, 6))
sns.barplot(x=df["CPU_model"], y=df["Price_euros"], estimator=np.mean, palette="coolwarm")
plt.xticks(rotation=45)
plt.title("CPU Model Price Trend")
plt.show()

# 2️⃣5️⃣ Multivariate Pairplot (Seaborn Pairplot)
sns.pairplot(df_encoded, vars=["Price_euros", "Ram", "Inches", "Weight", "CPU_freq"], hue="Company", palette="coolwarm")
plt.show()

