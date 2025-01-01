import time, os

def send_notification():
    os.system("""
        osascript -e 'display notification "Stay hydrated it will keep your brain working at high pace!" with title "💧 Time to Drink Water!"'
    """)

def water_reminder(interval):
    try:
        while True:
            send_notification()
            time.sleep(interval * 60)
    except KeyboardInterrupt:
        print("Reminder stopped!")

if __name__ == "__main__":
    interval = 1
    print(f"Water reminder is running you will get a notification in every {interval} hours PRESS ctrl + c to STOP")
    water_reminder(interval)