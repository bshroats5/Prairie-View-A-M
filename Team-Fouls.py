import matplotlib.pyplot as plt

# Example data for teams
teams = ['Prairie View A&M Panthers', 'Eastern Kentucky Colonels']
fouls = [21, 20]

# Create a bar graph
plt.bar(teams, fouls)

# Define colors for each team
pvam_color = 'Purple'
eastern_kentucky_color = 'Maroon'

# Create a bar graph with custom colors
plt.bar(teams, fouls, color=[pvam_color, eastern_kentucky_color])


# Add title and labels
plt.title('Team Fouls')
plt.xlabel('Teams')
plt.ylabel('Fouls')

# Show the plot
plt.show()
