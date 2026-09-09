from client import PNCounterCRDT

def main():
    print("=== PN-Counter CRDT State-Based Replication ===")
    node0 = PNCounterCRDT(node_id=0, cluster_size=3)
    node1 = PNCounterCRDT(node_id=1, cluster_size=3)

    node0.increment(10)
    node0.decrement(3) # node0 value: 7
    node1.increment(20) # node1 value: 20

    # Bidirectional synchronization
    node0.merge(node1.get_state())
    node1.merge(node0.get_state())

    print("Node 0 Converged Value:", node0.value())
    print("Node 1 Converged Value:", node1.value())
    assert node0.value() == 27
    assert node1.value() == 27

    print("PN-Counter CRDT verified successfully!")

if __name__ == "__main__":
    main()
