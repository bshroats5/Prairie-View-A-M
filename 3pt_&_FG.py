import matplotlib.pyplot as plt

# Initialize figure and axis
fig, ax = plt.subplots()

# Data for Eastern Kentucky
eastern_kentucky_fg = 23
eastern_kentucky_fga = 67
eastern_kentucky_3pt = 10
eastern_kentucky_3pta = 24

# Data for PVAM
pvam_fg = 25
pvam_fga = 65
pvam_3pt = 10
pvam_3pta = 24

# Calculate percentages
eastern_kentucky_fg_percentage = eastern_kentucky_fg / eastern_kentucky_fga * 100
eastern_kentucky_3pt_percentage = eastern_kentucky_3pt / eastern_kentucky_3pta * 100
pvam_fg_percentage = pvam_fg / pvam_fga * 100
pvam_3pt_percentage = pvam_3pt / pvam_3pta * 100

# Set bar width and positions
bar_width = 0.35  # Width of each bar
index = [1, 2, 4, 5]  # X-axis positions for the bars

# Set bar colors
colors = ["#800000", "#000000", "#800080", "#FFD700"]  # Maroon, Black, Purple, Gold

# Create the bars
ax.bar(index[0], eastern_kentucky_fg_percentage, bar_width, label="EKU FG%", color=colors[0])
ax.bar(index[1], eastern_kentucky_3pt_percentage, bar_width, label="EKU 3PT%", color=colors[1])
ax.bar(index[2], pvam_fg_percentage, bar_width, label="PVAM FG%", color=colors[2])
ax.bar(index[3], pvam_3pt_percentage, bar_width, label="PVAM 3PT%", color=colors[3])

# Set x-axis ticks and labels
ax.set_xticks([index[0] + bar_width / 2, index[1] + bar_width / 2, index[2] + bar_width / 2, index[3] + bar_width / 2])
ax.set_xticklabels(["EKU FG%", "EKU 3PT%", "PVAM FG%", "PVAM 3PT%"])

# Show the graph
plt.show()
