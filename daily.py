import datetime

def main():
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    entry = f"- {now} — Automated daily log\n"

    with open("daily_log.md", "a") as f:
        f.write(entry)

    print("Added log:", entry)

if __name__ == "__main__":
    main()
