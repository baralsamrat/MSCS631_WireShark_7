# MSCS631_WireShark_7  
Wireshark Lab 7: Ethernet and ARP Analysis

[Source Code](https://github.com/baralsamrat/MSCS631_WireShark_7)

**Samrat Baral**

University of the Cumberlands  

2025 Spring – Advanced Computer Networks (MSCS-631-M40) – Full Term  

Dr. Yousef Nijim

April 14, 2025

## Lab Overview
This repository provides a Python script using Pyshark to automate the capture and analysis of Ethernet and ARP packets as outlined in Wireshark Lab 7. It includes a Bash-compatible script for easy setup, packet capturing directly from your computer, and automated answering of all lab-related questions.

## Output Screenshots

[https://github.com/baralsamrat/MSCS631_WireShark_7/tree/main/screenshots](/https://github.com/baralsamrat/MSCS631_WireShark_7/tree/main/screenshots)  

## Directory Structure
```
src
├── run.sh                              # Bash script to setup environment and run the analysis
├── wireshark_capture_analyze.py        # Python script for capturing and analyzing packets
├── ethernet-wireshark-trace1.pcapng    # Sample capture file (optional, from Wireshark labs)
└── README.md                           # This documentation file
```

---

## Lab Questions Covered

The Python script (`wireshark_capture_analyze.py`) automatically answers the following questions directly from the terminal output:

Certainly! Below are the answers to the Wireshark Lab 7: Ethernet and ARP Analysis questions, based on standard trace files and common observations. Please note that actual values may vary depending on your specific network configuration and the captured traffic.

---

## Ethernet Frame Analysis (HTTP Request and Response)

1. **What is the 48-bit Ethernet address of your computer?**  
   `00:09:5b:61:8e:6d` citeturn0search7

2. **What is the 48-bit destination address in the Ethernet frame? Is this the Ethernet address of gaia.cs.umass.edu?**  
   `00:0c:41:45:90:a8` — No, this is the address of the router, not gaia.cs.umass.edu. citeturn0search7

3. **Give the hexadecimal value for the two-byte Frame type field. What upper layer protocol does this correspond to?**  
   `0x0800` — This corresponds to the IP protocol. citeturn0search7

4. **How many bytes from the very start of the Ethernet frame does the ASCII “G” in “GET” appear in the Ethernet frame?**  
   52 bytes — Accounting for 14 bytes of Ethernet header, 20 bytes of IP header, and 20 bytes of TCP header. citeturn0search7

5. **What is the value of the Ethernet source address? Is this the address of your computer, or of gaia.cs.umass.edu?**  
   `00:0c:41:45:90:a8` — This is the address of the router, not your computer or gaia.cs.umass.edu. citeturn0search7

6. **What is the destination address in the Ethernet frame? Is this the Ethernet address of your computer?**  
   `00:09:5b:61:8e:6d` — Yes, this is the Ethernet address of your computer. citeturn0search7

7. **Give the hexadecimal value for the two-byte Frame type field. What upper layer protocol does this correspond to?**  
   `0x0800` — This corresponds to the IP protocol. citeturn0search7

8. **How many bytes from the very start of the Ethernet frame does the ASCII “O” in “OK” appear in the Ethernet frame?**  
   52 bytes — Similar to the "GET" request, considering the headers. citeturn0search7

9. **How many Ethernet frames carry data that is part of the complete HTTP “OK 200” reply message?**  
   This can vary; typically, multiple frames are used to carry the full HTTP response.

---

## ARP Protocol Analysis

10. **How many entries are stored in your ARP cache?**  
    This depends on your system's current ARP cache.

11. **What is contained in each displayed entry of the ARP cache?**  
    Each entry contains the IP address, the corresponding MAC address, and the type (dynamic or static).

12. **What is the hexadecimal value of the source address in the Ethernet frame containing the ARP request message sent out by your computer?**  
    `00:d0:59:a9:3d:68` citeturn0search7

13. **What is the hexadecimal value of the destination addresses in the Ethernet frame containing the ARP request message sent out by your computer? And what device (if any) corresponds to that address?**  
    `ff:ff:ff:ff:ff:ff` — This is the broadcast address, targeting all devices on the local network. citeturn0search7

14. **What is the hexadecimal value for the two-byte Ethernet Frame type field? What upper layer protocol does this correspond to?**  
    `0x0806` — This corresponds to the ARP protocol. citeturn0search7

15. **How many bytes from the very beginning of the Ethernet frame does the ARP opcode field begin?**  
    20 bytes from the start of the Ethernet frame. citeturn0search7

16. **What is the value of the opcode field within the ARP request message sent by your computer?**  
    `0x0001` — This indicates an ARP request. citeturn0search7

17. **Does the ARP request message contain the IP address of the sender? If yes, what is that value?**  
    Yes; for example, `192.168.1.105`. citeturn0search7

18. **What is the IP address of the device whose corresponding Ethernet address is being requested in the ARP request message?**  
    This would be the target IP address specified in the ARP request; for example, `192.168.1.1`.

19. **What is the value of the opcode field within the ARP reply message received by your computer?**  
    `0x0002` — This indicates an ARP reply. citeturn0search7

20. **What is the Ethernet address corresponding to the IP address specified in the ARP request?**  
    For example, `00:06:25:da:af:73`. citeturn0search7

21. **Why are there no ARP replies in your trace that are sent in response to other ARP request messages?**  
    Because the ARP requests are not directed to your machine, and thus, your machine does not capture the corresponding replies. citeturn0search7

---

Please replace the example values with those specific to your network environment as observed in your Wireshark captures. 

---

## Prerequisites

- **Python 3.x**
- **Tshark (Wireshark)** [Download Link](https://www.wireshark.org/download.html)
- **Pyshark:** Install via pip:
```bash
pip install pyshark
```

---

## How It Works

The Bash script (`run.sh`) does the following:

- Checks Python and Tshark installation.
- Creates a Python virtual environment.
- Installs required Python libraries (`pyshark`, `wget`).
- Runs the Python script (`wireshark_capture_analyze.py`) to capture packets and perform analysis.
- Outputs clearly formatted answers directly to your terminal.
- Saves a captured packets file (`captured_packets.pcapng`) for future reference.

---

## How to Run

### Step 1: Clone the Repository
```bash
git clone https://github.com/baralsamrat/MSCS631_WireShark_7.git
cd MSCS631_WireShark_7/src
```

### Step 2: Make Bash Script Executable
```bash
chmod +x run.sh
```

### Step 3: Run the Bash Script
```bash
./run.sh
```

When prompted, enter:
- Network interface name (e.g., `eth0` or `Wi-Fi`)
- Capture duration in seconds (recommend: `20`)

---

## Customization & Notes
- Ensure your network interface name is correct for capturing packets.
- You can replace the live capture with a provided PCAP file (such as `ethernet-wireshark-trace1.pcapng`) by modifying the Python script.

---

## References

- [Wireshark Lab 7 Trace Files](http://gaia.cs.umass.edu/wireshark-labs/wireshark-traces-8.1.zip)
- [Pyshark Documentation](https://github.com/KimiNewt/pyshark)
- Kurose, J.F. & Ross, K.W., *Computer Networking: A Top-Down Approach, 8th Edition.*

---

## Output 

```
--- Ethernet Analysis ---
1. Your computer's Ethernet (source) address: xx:xx:xx:xx:xx:xx
2. Destination Ethernet address in GET request: xx:xx:xx:xx:xx:xx
...
--- ARP Analysis ---
10. ARP cache entries count: x
...
```

---
