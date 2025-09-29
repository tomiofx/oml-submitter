"""OML submitter — improved script

Features:
- argparse-based CLI
- logging with progress output
- proxy formats with/without auth
- results directory per run
- dry-run mode
- input validation
"""

import argparse
import logging
import os
from typing import List, Dict, Optional

import requests
from tqdm import tqdm

URL = "https://www.oml.wtf/api/submit-application"

HEADERS = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate",  # omit br/zstd
    "content-type": "application/json",
    "origin": "https://www.oml.wtf",
    "referer": "https://www.oml.wtf/",
    "user-agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
    ),
    "x-kl-kfa-ajax-request": "Ajax_Request",
}

logger = logging.getLogger(__name__)


def load_lines(path: str) -> List[str]:
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    with open(path, encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def parse_proxy(line: str) -> Optional[Dict[str, str]]:
    """Supported formats:
    - host:port:user:pass
    - host:port
    """
    parts = line.strip().split(":")
    if len(parts) == 2:
        host, port = parts
        url = f"http://{host}:{port}"
    elif len(parts) == 4:
        host, port, user, pwd = parts
        url = f"http://{user}:{pwd}@{host}:{port}"
    else:
        logger.warning("Unknown proxy format, skipping: %s", line)
        return None
    return {"http": url, "https": url}


def send_request(payload: dict, proxies: Optional[dict], timeout: int) -> str:
    try:
        r = requests.post(URL, headers=HEADERS, json=payload, proxies=proxies, timeout=timeout)
        return f"Status: {r.status_code}\nText: {r.text}"
    except Exception as e:
        return f"Error: {e}"


def main(argv=None):
    parser = argparse.ArgumentParser(description="OML submitter")
    parser.add_argument("--proxies", default="proxies.txt")
    parser.add_argument("--twitter", default="twitter.txt")
    parser.add_argument("--btc", default="btc.txt")
    parser.add_argument("--experience", default="experience.txt")
    parser.add_argument("--contribution", default="contribution.txt")
    parser.add_argument("--why", default="why.txt")
    parser.add_argument("--results", default="results")
    parser.add_argument("--timeout", type=int, default=30)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    proxies_lines = load_lines(args.proxies)
    twitters = load_lines(args.twitter)
    btcs = load_lines(args.btc)
    exps = load_lines(args.experience)
    contribs = load_lines(args.contribution)
    whys = load_lines(args.why)

    n = min(len(proxies_lines), len(twitters), len(btcs), len(exps), len(contribs), len(whys))
    if n == 0:
        logger.error("No data to process. Check that all input files contain at least one line.")
        return

    os.makedirs(args.results, exist_ok=True)

    for i in tqdm(range(n), desc="Submitting"):
        proxy = parse_proxy(proxies_lines[i]) if proxies_lines else None
        payload = {
            "twitterHandle": twitters[i],
            "bitcoinAddress": btcs[i],
            "experience": exps[i],
            "contribution": contribs[i],
            "whyOML": whys[i],
            "occupation": "d",
        }

        if args.dry_run:
            result = f"Dry run — payload for index {i+1}: {payload}"
        else:
            result = send_request(payload, proxy, args.timeout)

        out_path = os.path.join(args.results, f"{i+1}.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(result)

        logger.info("[%d] Done — %s", i+1, out_path)


if __name__ == "__main__":
    main()
