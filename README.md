# ContainerLab Network Automation Playground

Alright — so this repo’s basically me learning how to think and build like a Network Automation Engineer.  
I’ve been messing around with **ContainerLab**, **Python**, and **Jinja2** to figure out how network configs actually come together automatically from topology files.

---

## What’s Going On Here

I’m running a full **Debian (WSL)** setup with **Docker** and **ContainerLab** to emulate routers and PCs — all virtual, all self-contained.

Inside this setup, I:
- Pull topology data straight from the `.clab.yml` file (that’s where all the routers, PCs, and links live).  
- Parse the YAML with Python to grab info like node names, images, kinds, and connections.  
- Use **Jinja2 templates** to generate router configs automatically — no more manual typing.  
- (Eventually) push those configs out to devices using Paramiko or Ansible.

Basically, I’m taking the network map and making Python do the boring parts.

---

## What I’ve Learned So Far

- How to read nested YAML data and make it make sense  
- How Jinja2 templates work to build configs dynamically  
- How to loop through topologies and links to auto-map connections  
- That `print()` outside a loop will make you question your entire life  
- And that automation removes a ton of human error once it’s wired up right

---

## Tech Stack

- **Python 3**
- **ContainerLab + Docker**
- **Jinja2**
- **YAML / JSON parsing**
- **Debian (WSL)**
- (Later on: **Ansible**, **REST APIs**, and **NetBox**)

---

## Current Topology (frr01)

The lab runs three routers and three PCs in a simple triangle:
- Routers 1–3 form a core mesh  
- Each PC connects to one router  
- You can trace all the links automatically in the rendered configs

It’s not redundant (on purpose) — each PC is single-homed to make failures easier to test.

---

## What’s Next

- Auto-assign IPs to each link via Jinja2  
- Push configs with Ansible or Python (Paramiko)  
- Integrate with NetBox as a source of truth  
- Eventually spin up full CI/CD-style automation for network deployment

---

## Final Thoughts

This repo’s just my hands-on lab while I get deeper into network automation.  
If you stumble across it and want to learn too, feel free to clone it, break it, fix it, and see how it all fits together.

