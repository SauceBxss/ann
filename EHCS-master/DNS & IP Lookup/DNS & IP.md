# Experiment 03

## Aim
To learn about DNS Enumeration and Reverse IP Lookup to extract records and gather information about websites.

## Tools
- MxToolbox
- ViewDNS

## Theory
**What is DNS?**  
The Domain Name System (DNS) acts as the internet's phonebook, translating human-readable domain names (like `nytimes.com`) into machine-friendly IP addresses (like `192.168.1.1`). Each device connected to the internet has a unique IP address, and DNS servers facilitate this translation, enabling web browsers to access resources efficiently.

**How does DNS work?**  
When a user types a domain name into a browser, the DNS resolution process converts that name into an IP address, allowing the browser to locate the requested webpage. 

**What is DNS Enumeration?**  
DNS Enumeration is the process of finding every DNS server and its accompanying entries for an organization, providing insight into the target's infrastructure. This information can include usernames, machine names, and IP addresses.

**What is Reverse IP Lookup?**  
Reverse IP Lookup queries the DNS to determine the domain name associated with a specific IP address. This technique can reveal the organization owning the IP address and provide top-level domain data.

## Outcomes
Students will:
- Understand the concept of DNS records.
- Learn how to perform information gathering about subdomains, mail servers, and network resources.
- Gain practical experience using MxToolbox and ViewDNS for DNS information extraction.

## Results and Discussion
This experiment demonstrated the effectiveness of DNS Enumeration and Reverse IP Lookup in gathering valuable information about target websites. By utilizing tools like MxToolbox and ViewDNS, students successfully extracted DNS records and identified mail servers and subdomains associated with specific IP addresses.

The use of DNS Enumeration provided insights into the target’s infrastructure, revealing potential vulnerabilities that could be exploited in a penetration testing scenario. Meanwhile, Reverse IP Lookup helped identify the organizations linked to specific IP addresses, further enriching the information gathered.

Overall, the experiment highlighted the importance of DNS techniques in cybersecurity, emphasizing how they can be used for both ethical hacking and security assessments.
