import sys
import json
from client import PNCounterCRDT

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    if method == "inc_dec":
        c = PNCounterCRDT(params.get("node_id", 0))
        c.increment(params.get("inc", 0))
        c.decrement(params.get("dec", 0))
        return c.get_state()
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
