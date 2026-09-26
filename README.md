# Hydroficient IoT Cyber Defense — The Grand Marina

**Externship:** Hydroficient IoT Cyber Defense Externship (Feb–Apr 2026)
**Role:** Security Intern
**Client scenario:** The Grand Marina, a 500-room luxury hotel using Hydroficient's HYDROLOGIC water flow monitoring system

## Scenario

The Grand Marina's HYDROLOGIC devices monitor water pressure and flow across the hotel
and allow remote shutoff through a dashboard. The system was deployed with no
encryption, no authentication, and no message verification — anyone on the hotel network
could read every sensor reading, inject fake data, or replay old commands. Because this
system controls physical infrastructure, a compromise isn't just a data breach — it's a
potential flood, an ignored leak, or a phantom shutoff order at 2 AM. (The threat model
opens with a real precedent: a $4.2M damage incident caused by an ignored leak alert.)

## What this repo covers

This project moved through a full security engagement, not just a coding exercise:

| # | Folder | What it covers |
|---|--------|-----------------|
| 1 | `01-baseline-pipeline` | The unsecured MQTT pipeline as originally built, plus the recon and vulnerability assessment run against it |
| 2 | `02-threat-model` | STRIDE threat model across all four system components, written for a non-technical GM |
| 3 | `03-tls-in-transit` | Adds TLS encryption; experiments proving it stops eavesdropping but not spoofing |
| 4 | `04-mtls-and-replay-defense` | Adds mutual TLS (device identity) plus three replay defenses (timestamp, sequence counter, HMAC signing), tested across 12 controlled experiments |
| 5 | `05-device-provisioning-policy` | The certificate lifecycle policy governing how HYDROLOGIC devices are provisioned, renewed, and revoked |
| 6 | `06-live-defended-dashboard` | A live dashboard plus a three-phase attack simulator (eavesdrop, inject, replay) demonstrating all defenses blocking real attacks in real time |

## Key result

Twelve controlled experiments showed that **no single defense covers every attack type**:
timestamp validation alone misses fast replays, sequence counters alone miss tampered
messages. Only all three defenses together (HMAC + timestamp + counter) blocked 100%
of attacks across every category, with under 1ms of added latency per reading — invisible
to hotel operations. See `04-mtls-and-replay-defense/docs/defense-comparison-report.pdf`
for the full writeup.

## Security note on this repo

The `certs/` folders in this repo contain a **demo certificate authority created for this
lab** — not real production credentials. Private keys (`*-key.pem`) are excluded from git
via `.gitignore`; only public certificates are committed. To regenerate the full set locally,
run `generate_certs.py` (folder 3) and `generate_client_certs.py` (folder 4).

## Deliverables index

- `01-baseline-pipeline/docs/vulnerability-assessment.pdf`
- `02-threat-model/docs/threat-model-stride.pdf`
- `04-mtls-and-replay-defense/docs/defense-comparison-report.pdf`
- `05-device-provisioning-policy/docs/grand-marina-provisioning-policy.pdf`
- `06-live-defended-dashboard/docs/capstone-presentation.pdf`
