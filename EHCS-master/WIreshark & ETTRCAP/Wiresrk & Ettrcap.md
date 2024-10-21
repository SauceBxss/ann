**Experiment 09** on using **Wireshark** and **Ettercap** 



### Wireshark

#### Aim:
To use Wireshark to capture and analyze network packets, specifically focusing on sniffing HTTP requests.

#### Tools:
- **Wireshark**: A network protocol analyzer used for capturing and analyzing packet data from network connections.

#### Theory:
Wireshark is a widely-used open-source packet sniffer that performs the following functions:

1. **Packet Capture**: Wireshark listens to live network traffic and captures data packets.
2. **Filtering**: It allows users to apply filters to narrow down the displayed packets, focusing on specific data.
3. **Visualization**: Wireshark provides detailed views of packet contents and allows visualization of network conversations.

Uses of Wireshark include troubleshooting network performance issues, analyzing suspect network traffic, and developing new protocols. It was originally named Ethereal and has evolved since its first release in 1998, with the latest version being 3.6.0.

#### Outcome:
Upon completion of this section, students will be able to:
1. Successfully install Wireshark on a Windows system.
2. Sniff HTTP traffic and analyze captured packets to extract relevant information, such as login credentials.

#### Result & Discussion:
In this segment of the experiment, students successfully installed Wireshark and tested its functionality by sniffing HTTP traffic from a login page. They entered login credentials on a test website and observed how Wireshark captured and displayed the data in real time. 

This experiment highlighted the significance of network security and the vulnerabilities associated with unencrypted HTTP traffic. Students discussed the importance of secure communication protocols (like HTTPS) in protecting sensitive data from interception. Overall, this segment provided practical insights into packet analysis and the potential risks involved in network communications.



### Ettercap

#### Aim:
To utilize Ettercap to perform packet sniffing and conduct a man-in-the-middle (MITM) attack using ARP poisoning.

#### Tools:
- **Ettercap**: An open-source tool designed for network traffic analysis and man-in-the-middle attacks.

#### Theory:
Ettercap is a versatile network security tool that enables users to perform various attacks, including:

1. **Packet Sniffing**: Capture and analyze network packets in real time.
2. **ARP Poisoning**: Redirect traffic between devices to intercept and manipulate data.
3. **Active and Passive Dissection**: Inspect and modify packets as they flow through the network.

Ettercap supports both GUI and command line interfaces and is commonly used in penetration testing to identify network vulnerabilities. Its capabilities include capturing sensitive information, performing DNS spoofing, and executing denial-of-service attacks.

#### Outcome:
After completing this section, students will be able to:
1. Launch Ettercap and initiate ARP poisoning to intercept network traffic.
2. Analyze the captured data and understand the implications of MITM attacks.

#### Result & Discussion:
In this portion of the experiment, students effectively launched Ettercap and executed ARP poisoning, positioning themselves between two target systems. They captured network traffic flowing between the targets, allowing them to observe the data being transmitted, including login credentials.

The experiment reinforced the concept of man-in-the-middle attacks and highlighted the critical need for robust security measures in networks. Students discussed the ethical implications of using such tools, emphasizing the importance of responsible usage within legal and ethical boundaries. Overall, the session provided a comprehensive understanding of packet sniffing techniques and their application in cybersecurity.

