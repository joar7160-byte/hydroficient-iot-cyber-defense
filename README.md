# Hydroficient IoT Cyber Defense: The Grand Marina

- **Externship:** Hydroficient IoT Cyber Defense Externship (February to April 2026)
- **Role:** Security Intern
- **Client scenario:** The Grand Marina, a luxury hotel with 500 rooms using Hydroficient's HYDROLOGIC water flow monitoring system

## Business problem

The Grand Marina's HYDROLOGIC devices monitor water pressure and flow across the hotel
and allow remote shutoff through a dashboard. The system was deployed with no
encryption, no authentication, and no message verification. Anyone on the hotel network
could read every sensor reading, inject fake data, or replay old commands. Because this
system controls physical infrastructure, a compromise is not just a data breach. It could mean a
potential flood, an ignored leak, or a phantom shutoff order at 2 AM. The threat model
opens with a real precedent: a $4.2M damage incident caused by an ignored leak alert.

## What this repo covers

- `01-baseline-pipeline`: the unsecured MQTT pipeline as originally built, plus the recon and vulnerability assessment run against it
- `02-threat-model`: STRIDE threat model across all four system components, written for a general manager who is not technical
- `03-tls-in-transit`: adds TLS encryption. Experiments prove it stops eavesdropping but not spoofing
- `04-mtls-and-replay-defense`: adds mutual TLS (device identity) plus three replay defenses (timestamp, sequence counter, HMAC signing), tested across 12 controlled experiments
- `05-device-provisioning-policy`: the certificate lifecycle policy governing how HYDROLOGIC devices are provisioned, renewed, and revoked
- `06-live-defended-dashboard`: a live dashboard plus an attack simulator with three phases (eavesdrop, inject, replay) demonstrating all defenses blocking real attacks in real time

## Key result

- Twelve controlled experiments showed that no single defense covers every attack type
- Timestamp validation alone misses fast replays
- Sequence counters alone miss tampered messages
- Only all three defenses together (HMAC plus timestamp plus counter) blocked 100% of attacks across every category
- Adding all three together added under 1ms of latency per reading, which is invisible to hotel operations
- Full writeup: `04-mtls-and-replay-defense/docs/defense-comparison-report.pdf`

## What I would do differently in production

- Add topic based access controls so each device can only publish to its own channel, since testing showed an authenticated device could still publish to topics it should not have access to
- Set up logging from the start, so every rejected message is tracked from the beginning instead of only during the later testing phase
- Automate certificate rotation instead of manually tracking expiry dates, since the provisioning policy currently relies on someone noticing a 60 day renewal window
- Move the CA private key out of local storage and into a real secrets manager, since the provisioning policy calls for AWS Secrets Manager but this lab never actually wires that up
- Run the broker with high availability instead of a single instance, so a broker outage does not take down monitoring for the whole hotel
- Add centralized alerting, such as paging or a ticket, when the system starts rejecting an unusual number of messages, rather than relying on someone watching the dashboard

## Deliverables index

- `01-baseline-pipeline/docs/vulnerability-assessment.pdf`
- `02-threat-model/docs/threat-model-stride.pdf`
- `04-mtls-and-replay-defense/docs/defense-comparison-report.pdf`
- `05-device-provisioning-policy/docs/grand-marina-provisioning-policy.pdf`
- `06-live-defended-dashboard/docs/capstone-presentation.pdf`
