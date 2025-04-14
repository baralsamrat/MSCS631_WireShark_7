import pyshark
import time

CAPTURE_FILE = 'captured_packets.pcapng'

def capture_packets(interface='eth0', duration=20):
    print(f"Starting capture on interface {interface} for {duration} seconds...")
    capture = pyshark.LiveCapture(interface=interface, output_file=CAPTURE_FILE)
    capture.sniff(timeout=duration)
    capture.close()
    print(f"Packet capture saved to {CAPTURE_FILE}.")

def analyze_capture(file_path):
    cap = pyshark.FileCapture(file_path)

    # Ethernet Analysis (HTTP GET and Response)
    http_get, http_response, http_data_frames = None, None, []
    for pkt in cap:
        if 'HTTP' in pkt:
            if hasattr(pkt.http, 'request_method') and pkt.http.request_method == 'GET' and not http_get:
                http_get = pkt
            elif hasattr(pkt.http, 'response_code') and not http_response:
                http_response = pkt
            if 'TCP' in pkt and hasattr(pkt.tcp, 'payload'):
                http_data_frames.append(pkt)

    if http_get:
        print("\n--- Ethernet Analysis ---")
        print(f"1. Your computer's Ethernet (source) address: {http_get.eth.src}")
        print(f"2. Destination Ethernet address in GET request: {http_get.eth.dst}")
        print(f"3. Frame type in GET request (hex): {http_get.eth.type}")
        print(f"4. Bytes to 'G' in 'GET': {int(http_get.tcp.get_field('payload').pos)//2 + 14}")
    else:
        print("HTTP GET request not found.")

    if http_response:
        print(f"\n5. Source Ethernet address in response: {http_response.eth.src}")
        print(f"6. Destination Ethernet address in response: {http_response.eth.dst}")
        print(f"7. Frame type in response (hex): {http_response.eth.type}")
        print(f"8. Bytes to 'O' in 'OK': {int(http_response.tcp.get_field('payload').pos)//2 + 14}")
        print(f"9. Number of Ethernet frames in HTTP response: {len(http_data_frames)}")
    else:
        print("HTTP response not found.")

    # ARP Analysis
    arp_reqs = [p for p in cap if 'ARP' in p and p.arp.opcode == '1']
    arp_reps = [p for p in cap if 'ARP' in p and p.arp.opcode == '2']

    arp_cache_entries = set((p.arp.src_proto_ipv4, p.arp.src_hw_mac) for p in arp_reps)

    print("\n--- ARP Analysis ---")
    print(f"10. ARP cache entries count: {len(arp_cache_entries)}")
    print(f"11. Each entry contains IP and MAC address pairs.")

    if arp_reqs:
        arp_req = arp_reqs[0]
        print(f"12. ARP request source address: {arp_req.eth.src}")
        print(f"13. ARP request destination (broadcast): {arp_req.eth.dst}")
        print(f"14. ARP request Ethernet frame type: {arp_req.eth.type}")
        print(f"15. ARP opcode offset: 20 bytes")
        print(f"16. ARP opcode value: {arp_req.arp.opcode}")
        print(f"17. Sender IP in ARP request: {arp_req.arp.src_proto_ipv4}")
        print(f"18. Target IP in ARP request: {arp_req.arp.dst_proto_ipv4}")

    if arp_reps:
        arp_rep = arp_reps[0]
        print(f"19. ARP reply opcode: {arp_rep.arp.opcode}")
        print(f"20. Ethernet address from ARP reply: {arp_rep.arp.src_hw_mac}")

    other_arp_requests = [p for p in arp_reqs if p.eth.src != arp_reqs[0].eth.src]
    if other_arp_requests:
        print("21. Additional ARP requests detected without replies (different subnet or hosts).")

    cap.close()

if __name__ == "__main__":
    INTERFACE = input("Enter network interface (e.g., eth0, Wi-Fi, en0): ")
    capture_duration = int(input("Enter capture duration in seconds (recommended 20): "))

    capture_packets(INTERFACE, capture_duration)
    analyze_capture(CAPTURE_FILE)
