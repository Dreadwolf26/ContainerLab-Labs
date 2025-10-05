from jinja2 import Template
import yaml
import json
from pathlib import Path

with open("/home/critter/containerlab/lab-examples/frr01/frr01.clab.yml") as f:
    topo = yaml.safe_load(f)
    #pretty_topo = json.dumps(topo, indent=2)
    #print(pretty_topo)


template = Template(open("router_config.j2").read())

output_dir = Path("./rendered")
output_dir.mkdir(exist_ok=True)

for node_name, node_data in topo["topology"]["nodes"].items():
    kind  = node_data["kind"]
    image = node_data["image"]
    binds = node_data.get("binds", [])
    
    config = template.render(
    name=node_name,
    kind=node_data["kind"],
    image=node_data["image"],
    links=topo["topology"]["links"],
    binds=node_data.get("binds", []))
    stripped_config = "\n".join(line for line in config.splitlines() if line.strip())


    #print(stripped_config)

    outfile = output_dir / f"{node_name}.cfg"
    with outfile.open("w") as f:
        f.write(stripped_config)

    print(f"✅ wrote {outfile}")










