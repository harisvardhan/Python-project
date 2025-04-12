import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set visual styles
sns.set(style='darkgrid')
plt.style.use('dark_background')

# Load dataset
df = pd.read_csv(r"C:\Users\haris\Downloads\ICRISAT-District Level Data.csv")

# Drop rows with missing essential values
df.dropna(subset=['TOTAL CONSUMPTION (tons)', 'State Name', 'Year'], inplace=True)

# 1. Line Plot ----------------------
yearly_total = df.groupby('Year')['TOTAL CONSUMPTION (tons)'].sum()
plt.figure(figsize=(10, 5))
plt.plot(yearly_total.index, yearly_total.values, color='cyan', linewidth=2)
plt.title('Total Fertilizer Usage Over Years')
plt.xlabel('Year')
plt.ylabel('Total Fertilizer (tons)')
plt.grid(True)
plt.tight_layout()
plt.show()

#  2. Bar Chart - Top 10 States ----------------------
top_states = df.groupby('State Name')['TOTAL CONSUMPTION (tons)'].sum().nlargest(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_states.values, y=top_states.index, palette='plasma')
plt.title('Top 10 States by Total Fertilizer Usage')
plt.xlabel('Total Fertilizer (tons)')
plt.ylabel('State')
plt.tight_layout()
plt.show()

# 3. Horizontal Bar Chart - Top Districts ----------------------
top_districts = df.groupby('Dist Name')['TOTAL CONSUMPTION (tons)'].sum().nlargest(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_districts.values, y=top_districts.index, palette='inferno')
plt.title('Top 10 Districts by Fertilizer Usage')
plt.xlabel('Total Fertilizer (tons)')
plt.ylabel('District')
plt.tight_layout()
plt.show()

# 4. Donut Chart - GCA vs NCA ----------------------
gca = df['TOTAL PER HA OF GCA (Kg per ha)'].mean()
nca = df['TOTAL PER HA OF NCA (Kg per ha)'].mean()
plt.figure(figsize=(6, 6))
sizes = [gca, nca]
labels = ['GCA (Kg/ha)', 'NCA (Kg/ha)']
colors = ['#00bfc4', '#f8766d']
plt.pie(sizes, labels=labels, colors=colors, wedgeprops=dict(width=0.4), startangle=90, autopct='%1.1f%%')
plt.title('Average Fertilizer per Hectare: GCA vs NCA')
plt.tight_layout()
plt.show()

#  5. Heatmap - Correlation between NPK ----------------------
corr_data = df[['NITROGEN CONSUMPTION (tons)', 'PHOSPHATE CONSUMPTION (tons)', 'POTASH CONSUMPTION (tons)']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr_data, annot=True, cmap='magma', linewidths=0.5)
plt.title('Correlation between N, P, K Usage')
plt.tight_layout()
plt.show()

# 6. Stacked Bar - NPK Usage by Top 5 States ----------------------
top_states_npk = df.groupby('State Name')[[
    'NITROGEN CONSUMPTION (tons)', 
    'PHOSPHATE CONSUMPTION (tons)', 
    'POTASH CONSUMPTION (tons)'
]].sum().nlargest(5, 'NITROGEN CONSUMPTION (tons)')
top_states_npk.plot(kind='bar', stacked=True, colormap='viridis', figsize=(12,6))
plt.title('NPK Usage by Top 5 States')
plt.ylabel('Tons')
plt.xlabel('State')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 7. Histogram - Distribution of Fertilizer Usage ----------------------
plt.figure(figsize=(10, 6))
sns.histplot(df['TOTAL CONSUMPTION (tons)'], bins=30, color='skyblue', kde=True)
plt.title('Distribution of Total Fertilizer Usage')
plt.xlabel('Total Fertilizer (tons)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# 8. Scatter Plot - Nitrogen vs Phosphate (color = Potash) ----------------------
plt.figure(figsize=(10, 6))
scatter = plt.scatter(
    df['NITROGEN CONSUMPTION (tons)'], 
    df['PHOSPHATE CONSUMPTION (tons)'], 
    c=df['POTASH CONSUMPTION (tons)'], 
    cmap='cool', 
    s=30, 
    alpha=0.7
)
plt.colorbar(scatter, label='Potash (tons)')
plt.title('Nitrogen vs Phosphate vs Potash')
plt.xlabel('Nitrogen (tons)')
plt.ylabel('Phosphate (tons)')
plt.tight_layout()
plt.show()

# TABLE 1: Avg NPK per State ----------------------
avg_npk_table = df.groupby('State Name')[[
    'NITROGEN CONSUMPTION (tons)', 
    'PHOSPHATE CONSUMPTION (tons)', 
    'POTASH CONSUMPTION (tons)'
]].mean().round(2).nlargest(5, 'NITROGEN CONSUMPTION (tons)')
print("\n📊 Table 1: Average NPK Consumption (Top 5 States)\n")
print(avg_npk_table.reset_index())

#TABLE 2: Total Fertilizer by Year ----------------------
total_yearly_table = df.groupby('Year')['TOTAL CONSUMPTION (tons)'].sum().reset_index().head()
print("\n📊 Table 2: Total Fertilizer Usage by Year (First 5 Years)\n")
print(total_yearly_table)
#9. Heatmap
# Create figure with larger size
plt.figure(figsize=(20, 12))

# Create heatmap with annotations
ax = sns.heatmap(
    pivot_table,
    cmap=cmap,
    annot=True,  # Show values
    fmt=".0f",
    linewidths=0.5,
    linecolor="#444444",
    annot_kws={"size": 8, "color": "white"},  # Customize annotation text
    cbar_kws={'label': 'Total Consumption (tons)'}
)

# Customize plot
plt.title('Fertilizer Consumption Heatmap by District and Year', 
          fontsize=18, pad=20, color='white')
plt.xlabel('Year', fontsize=14, color='white')
plt.ylabel('District', fontsize=14, color='white')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right', color='white', fontsize=10)
plt.yticks(color='white', fontsize=10)

# Adjust colorbar
cbar = ax.collections[0].colorbar
cbar.ax.yaxis.set_tick_params(color='white')
plt.setp(cbar.ax.get_yticklabels(), color='white', fontsize=10)

# Tight layout to prevent label cutoff
plt.tight_layout()

# Show plot
plt.show()
