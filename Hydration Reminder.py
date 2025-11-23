import time
import datetime
import winsound
import matplotlib.pyplot as plt

start = int(input("Enter start hour (0-23): "))
end = int(input("Enter end hour (0-23): "))
interval = int(input("Reminder interval in minutes: "))

interval_seconds = interval * 60

reminders = 0
drank_count = 0
percentages = []
times = []

print("\nHydration Reminder Started!")
print("Type 'Y' whenever you drink water and 'N' you don't.\n")


while True:
    now = datetime.datetime.now()
    hour = now.hour

    if start <= hour <= end:
        reminders += 1

        print(f"\n🔔 Reminder {reminders}: Drink water!")
        winsound.Beep(1000,1000)
        
        drank = input("Did you drink water? (Y/N): ").strip().lower()

        while drank not in ["y", "n"]:
            print("Invalid input! Please enter only Y or N.")
            drank = input("Did you drink water? (Y/N): ").strip().lower()
        
        if drank == "y":
            drank_count += 1

        percentage = (drank_count / reminders) * 100
        percentages.append(percentage)
        times.append(now.strftime("%H:%M"))

        print(f"📊 Stats: Drank {drank_count}/{reminders} ({percentage:.2f}%)")
        time.sleep(interval_seconds)


    if hour == end and now.minute == (now.minute):
        
        if reminders > 0:
            print("\nGenerating your hydration chart...")

            plt.figure(figsize=(8,5))
            plt.plot(times, percentages, marker='o')
            plt.title("Hydration Percentage Throughout Your Chosen Time Period")
    
    

