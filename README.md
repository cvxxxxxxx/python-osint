# CVX Work OSINT Tool

A terminal-based Open Source Intelligence framework with 37 modules. Built in Python, runs anywhere, zero API keys required.

> **For educational and authorized security research only. Do not use against systems you do not own or have explicit permission to test. Misuse is illegal.**

---

## Features

- 37 investigation modules across 6 categories
- Zero API keys required — all free public endpoints
- Results auto-saved to `.txt` files for easy sharing
- Plain-text copy section printed after every scan
- Works on Windows, Linux, macOS

---

## Installation

```bash
git clone https://github.com/cvxxxxxxx/
cd cvx-osint
pip install -r requirements.txt
python firework_osint.py
```

---

## Modules

### Network Intelligence
| # | Module | Description |
|---|--------|-------------|
| 01 | IP Deep Recon | Geolocation, ASN, ISP, VPN/proxy flags, co-hosted domains |
| 02 | IP Threat Intel | Shodan InternetDB — open ports, CVEs, CPEs |
| 03 | WHOIS + RDAP | Full registration data + RDAP enrichment |
| 04 | DNS Full Recon | All record types + zone transfer attempt |
| 05 | Subdomain Enumerator | DNS brute-force + certificate transparency (crt.sh) |
| 06 | Port & Service Scanner | TCP connect sweep + banner grab |
| 07 | BGP / ASN Recon | ASN owner, prefixes, peers via bgpview.io |
| 08 | Reverse IP Lookup | Domains sharing the same IP via hackertarget |

### Host & Web Intel
| # | Module | Description |
|---|--------|-------------|
| 09 | Website Fingerprint | Stack detection, WAF, security headers, SSL |
| 10 | SSL / TLS Audit | Cert chain, expiry countdown, cipher, SANs |
| 11 | HTTP Header Probe | Full headers, CORS audit, info disclosure |
| 12 | URL Redirect Chaser | Full redirect chain + final domain analysis |
| 13 | Google Dork Builder | 20 templates, auto-encodes, opens in browser |
| 14 | Tech Stack Detector | CMS, framework, CDN, exposed sensitive files |

### Identity & Social OSINT
| # | Module | Description |
|---|--------|-------------|
| 15 | Username OSINT | Check 42 platforms simultaneously |
| 16 | Email Investigator | MX, Gravatar, breach check links |
| 17 | GitHub Recon | Profile, repos, orgs via public API |
| 18 | Phone Recon | Country code, carrier hints, lookup links |

### Discord Intelligence
| # | Module | Description |
|---|--------|-------------|
| 19 | Snowflake Decoder | Convert any Discord ID to exact timestamp |
| 20 | Invite Probe | Server info, member count, features |
| 21 | User Lookup | Avatar, badges, creation date |
| 22 | Server Hunt | Find public servers by keyword |
| 26 | Server ID Lookup | Guild widget API + snowflake analysis |
| 27 | Webhook Probe | Channel and server info from webhook URL |
| 28 | Message Link Decoder | Decode all snowflake IDs from a message link |
| 29 | Bot Lookup | Bot profile and top.gg data |
| 30 | Vanity URL Resolver | Full server intel from custom discord.gg link |
| 31 | Discord Status | Live Discord outage and incident monitor |

### Tracking & Investigation
| # | Module | Description |
|---|--------|-------------|
| 32 | Wayback Machine | Archive snapshots + CDX history |
| 33 | URLScan.io Analysis | Public scans, IPs, server tech |
| 34 | Email Header Analyzer | Hop extraction, originating IP geo, SPF/DKIM |
| 35 | OSINT Aggregator | 30+ tool links auto-tailored to target type |
| 36 | Domain History | WHOIS age, passive DNS, history links |
| 37 | Breach Aggregator | LeakCheck public API + 10 breach databases |

### Threat & Vuln Research
| # | Module | Description |
|---|--------|-------------|
| 23 | CVE Search | Live NVD NIST database query |
| 24 | Hash Identifier | Type detection + common password crack attempt |
| 25 | MAC Vendor Lookup | OUI to manufacturer via macvendors.com |

---

## Usage

Run and select a module number at the prompt:

```
[FSOCIETY][SELECT MODULE]> 01
```

After each scan, results are:
- Printed in a clean bordered card
- Saved automatically to `cvxwork_result_TIMESTAMP.txt`
- Printed as plain text at the bottom for easy copying

---

## Free APIs Used

| Service | Used For |
|---------|----------|
| ip-api.com | IP geolocation, ASN, proxy flags |
| ipinfo.io | IP enrichment, hostname |
| internetdb.shodan.io | Open ports, CVEs (no key) |
| bgpview.io | ASN, prefixes, peers |
| hackertarget.com | Reverse IP, host search, passive DNS |
| crt.sh | Certificate transparency |
| discordlookup.mesalytic.moe | Discord user info (no key) |
| discord.com/api | Invite info, server widget (public) |
| archive.org/wayback | Web archive snapshots |
| urlscan.io | Public URL scan results |
| nvd.nist.gov | CVE database |
| api.macvendors.com | MAC OUI lookup |
| leakcheck.io | Breach check (public endpoint) |
| api.github.com | GitHub profiles (public) |

---

## Requirements

- Python 3.8+
- See `requirements.txt`

```
colorama
requests
dnspython
python-whois
```

---

## Legal

This tool is provided for educational purposes and authorized security research only.

- Only scan and test systems you own or have written permission to test
- Some modules (port scanner, traceroute) require elevated privileges on Linux
- The author takes no responsibility for misuse

---

## Author

[cvxxxxxxx](https://github.com/cvxxxxxxx/)
