import serial
import matplotlib.pyplot as plt
import csv
from datetime import datetime
import time

port = "COM6"
baud_rate = 9600

times = []
light_levels = []
motions = []
led_states = []
modes = []

filename = f"smart_room_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

print("Opening port...")
ser = serial.Serial(port, baud_rate, timeout=1)

time.sleep(2)  # allow Arduino to reset

print("Using port:", port)
print("Saving data to:", filename)
print("Reading data... Press Ctrl+C to stop.")

with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["time_ms", "time_s", "light_level", "motion", "led_state", "mode"])

    try:
        while True:
            line = ser.readline().decode("utf-8", errors="ignore").strip()

            if not line:
                continue

            parts = line.split(",")

            if len(parts) != 5:
                continue

            try:
                time_ms = int(parts[0])
                light_level = int(parts[1])
                motion = int(parts[2])
                led_state = int(parts[3])
                mode = int(parts[4])
            except:
                continue

            time_s = time_ms / 1000

            times.append(time_s)
            light_levels.append(light_level)
            motions.append(motion)
            led_states.append(led_state)
            modes.append(mode)

            writer.writerow([time_ms, time_s, light_level, motion, led_state, mode])
            file.flush()

            print(time_ms, light_level, motion, led_state, mode)

    except KeyboardInterrupt:
        print("\nStopped logging.")

    finally:
        ser.close()

# Graph + save
if times:
    graph_filename = f"smart_room_graph_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"

    plt.plot(times, light_levels, label="Light Level")
    plt.plot(times, motions, label="Motion")
    plt.plot(times, led_states, label="LED")
    plt.plot(times, modes, label="Mode")

    plt.xlabel("Time (s)")
    plt.ylabel("Value")
    plt.title("Smart Room Data Log")
    plt.legend()

    plt.savefig(graph_filename)
    print("Graph saved as:", graph_filename)

    plt.show()
else:
    print("No data collected.")



    
