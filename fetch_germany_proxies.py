import requests
from datetime import datetime

# List of your subscription URLs (.txt)
SUB_URLS = [
    "https://raw.githubusercontent.com/V2RAYCONFIGSPOOL/V2RAY_SUB/refs/heads/main/v2ray_configs_no1.txt",
    "https://raw.githubusercontent.com/V2RAYCONFIGSPOOL/V2RAY_SUB/refs/heads/main/v2ray_configs_no2.txt",
    "https://raw.githubusercontent.com/V2RAYCONFIGSPOOL/V2RAY_SUB/refs/heads/main/v2ray_configs_no3.txt",
    "https://raw.githubusercontent.com/V2RAYCONFIGSPOOL/V2RAY_SUB/refs/heads/main/v2ray_configs_no4.txt",
    "https://raw.githubusercontent.com/V2RAYCONFIGSPOOL/V2RAY_SUB/refs/heads/main/v2ray_configs_no5.txt",
    "https://raw.githubusercontent.com/V2RAYCONFIGSPOOL/V2RAY_SUB/refs/heads/main/v2ray_configs_no6.txt",
    "https://raw.githubusercontent.com/V2RAYCONFIGSPOOL/V2RAY_SUB/refs/heads/main/v2ray_configs_no7.txt",
    "https://raw.githubusercontent.com/V2RAYCONFIGSPOOL/V2RAY_SUB/refs/heads/main/v2ray_configs_no8.txt",
    "https://raw.githubusercontent.com/V2RAYCONFIGSPOOL/V2RAY_SUB/refs/heads/main/v2ray_configs_no9.txt",
    "https://raw.githubusercontent.com/V2RAYCONFIGSPOOL/V2RAY_SUB/refs/heads/main/v2ray_configs_no10.txt",
    "https://github.com/Epodonios/v2ray-configs/raw/main/All_Configs_Sub.txt",
]

OUTPUT_FILE = "merged_subscription_germany.txt"
TIMEOUT = 15

KEYWORDS = ["germany", "🇩🇪"]  # text OR flag


def fetch(url):
    r = requests.get(url, timeout=TIMEOUT)
    r.raise_for_status()
    return r.text


def is_germany(line: str) -> bool:
    lower = line.lower()
    return any(k in lower for k in KEYWORDS)


def main():
    merged = []

    for url in SUB_URLS:
        try:
            print(f"Fetching: {url}")
            content = fetch(url)

            lines = content.splitlines()
            germany_lines = [line for line in lines if is_germany(line)]

            merged.extend(germany_lines)
            print(f"  ✔ Kept {len(germany_lines)} Germany proxies")

        except Exception as e:
            print(f"❌ Failed: {url} ({e})")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(merged))

    print(f"\n✅ Total Germany proxies: {len(merged)}")
    print(f"📄 Output: {OUTPUT_FILE}")
    print(f"🕒 Updated: {datetime.now()}")


if __name__ == "__main__":
    main()

 
