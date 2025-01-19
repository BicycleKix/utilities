import json

def open_stats(filename):
        try:
            with open(filename, 'r') as file:
                stats = json.load(file)
        except FileNotFoundError:
            print("File not found. No stats loaded.")
        except Exception as e:
            print("Error loading stats:", e)
        return stats

def save_stats(stats, filename):
    try:
        with open(filename, 'w') as file:
            json.dump(stats, file)
    except Exception as e:
        print("Error saving stats:", e)