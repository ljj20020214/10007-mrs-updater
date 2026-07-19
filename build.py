import argparse
import ipaddress
from pathlib import Path


SKIP = {"localhost", "localhost.localdomain", "ip6-loopback", "ip6-localhost", "hostname"}


def extract_domains(lines):
    domains = set()
    for line in lines:
        fields = line.split("#", 1)[0].split()
        if len(fields) < 2:
            continue
        try:
            ipaddress.ip_address(fields[0])
        except ValueError:
            continue
        for domain in fields[1:]:
            domain = domain.lower().rstrip(".")
            try:
                ipaddress.ip_address(domain)
                continue
            except ValueError:
                pass
            if domain not in SKIP and "." in domain:
                domains.add(domain)
    return sorted(domains)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("target", type=Path)
    parser.add_argument("--min-count", type=int, default=10_000)
    args = parser.parse_args()

    domains = extract_domains(args.source.read_text(encoding="utf-8-sig").splitlines())
    if len(domains) < args.min_count:
        raise SystemExit(f"refusing to publish only {len(domains)} domains")
    args.target.parent.mkdir(parents=True, exist_ok=True)
    args.target.write_text("\n".join(domains) + "\n", encoding="utf-8")
    print(f"domains={len(domains)}")


if __name__ == "__main__":
    main()
