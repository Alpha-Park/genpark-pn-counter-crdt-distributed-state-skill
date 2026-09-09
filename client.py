class PNCounterCRDT:
    """State-based Positive-Negative Counter CRDT."""
    def __init__(self, node_id: int, cluster_size: int = 5):
        self.node_id = node_id
        self.size = cluster_size
        self.P = [0] * cluster_size
        self.N = [0] * cluster_size

    def increment(self, amount: int = 1):
        self.P[self.node_id] += amount
        return self.value()

    def decrement(self, amount: int = 1):
        self.N[self.node_id] += amount
        return self.value()

    def value(self) -> int:
        return sum(self.P) - sum(self.N)

    def get_state(self) -> dict:
        return {"node_id": self.node_id, "P": list(self.P), "N": list(self.N), "value": self.value()}

    def merge(self, other_state: dict):
        other_P = other_state.get("P", [])
        other_N = other_state.get("N", [])
        for i in range(min(self.size, len(other_P))):
            self.P[i] = max(self.P[i], other_P[i])
        for i in range(min(self.size, len(other_N))):
            self.N[i] = max(self.N[i], other_N[i])
        return self.value()
