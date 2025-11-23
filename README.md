# Hydration Reminder

A Python-based hydration reminder that will automatically remind you at regular intervals, tracks how many times you drink water, and generates a visual chart of your hydration performance throughout the day

# Overview

This project will remind the user to drink water at regular intervals between a selected time range.

It asks the user whether they drank water during each reminder, then calculates hydration efficiency and finally generates a hydration performance chart using Matplotlib.

This project can be used for:

* **Students**
* **Office workers**
* **Fitness lovers**
* **Anyone who is trying to build a healthy drinking water habit**

# Features
* **Set custom start and end hours**
* **Choose reminder interval in minutes**
* **Plays sound on every reminder**
* **Counts number of reminders vs the number of times water was drunk**
* **Calculates hydration percentage**
* **Generates a line chart of hydration performance**
* **Clean workflow with input validation**

# Technologies Used

* **Python 3**
* **time module**
* **datetime module**
* **winsound (Windows beep sound)**
* **matplotlib (for graphical chart)**

# How to Install & Run

1. **Install Python**

   Ensure that Python 3 is installed.

3. **Install required libraries**

   Run the following command:

   pip install matplotlib

5. **Execute the script**

   python hydration_reminder.py

# How to Use

1. **Enter start hour (24 hr format)**

2. **Enter end hour (24 hr format)**

3. **Enter reminder interval (in minutes)**

4. **The program initiates the reminders**

5. **Type:**

   Y → if you drank water

   N → if you didn't

7. In the last hour, the system generates a hydration chart.

# Output Statistics Example️

Reminder 3: Drink water!

Did you drink water? (Y/N): y

Stats: Drank 2/3 (66.67%)

# The chart will show

* Time of each reminder
* Hydration percentage over the day
* Provides a visual of how consistent your water intake was.
* Testing Instructions

# Try different combinations

Start at 8, end at 11, interval 30 mins
