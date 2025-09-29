# OML Submitter

Automates submissions to `https://www.oml.wtf/api/submit-application`.
Use responsibly and in accordance with the target site's rules.

## Quick Start

1. **Create a virtual environment and install dependencies**
```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows
.venv\Scripts\activate

pip install -r requirements.txt
```

2. **Prepare input files** (one value per line; counts across files must match):
- `proxies.txt` — proxies in `host:port:user:pass` **or** `host:port` format.
- `twitter.txt` — Twitter handles (e.g., `@username`).
- `btc.txt` — Bitcoin addresses.
- `experience.txt`, `contribution.txt`, `why.txt` — corresponding free-text fields.

You can use the provided `*.example.txt` files as templates.

3. **Run**
```bash
python -m src.main   --proxies proxies.txt   --twitter twitter.txt   --btc btc.txt   --experience experience.txt   --contribution contribution.txt   --why why.txt   --results results
```

## Command-line Options
- `--proxies` (default: `proxies.txt`)
- `--twitter` (default: `twitter.txt`)
- `--btc` (default: `btc.txt`)
- `--experience` (default: `experience.txt`)
- `--contribution` (default: `contribution.txt`)
- `--why` (default: `why.txt`)
- `--results` (default: `results`)
- `--timeout` (default: `30` seconds)
- `--dry-run` (no real requests; prints payloads and writes them to files)

## Safety Notes
- **Never** commit real proxy credentials or any secrets to a public repository.
- Ensure your usage complies with the target website's Terms of Service.
- Store sensitive data outside of version control and keep `results/` out of Git.

## License
MIT
