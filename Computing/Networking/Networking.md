# Introduction to Networking

# Computer Network

A computer network is a system of two or more computers (or devices) that are connected together by a transmission medium for the exchange of data.

# Advantages

- **Shared Resources**
    - A network allows a group of computers to make use of shared resources such as printers or files
- **Shared Internet Access**
    - Depending on the network’s configuration, every user who logs on to the network may have access to the internet
- **Shared software: Software**
    - Can be stored on the central server of a network and deployed to other computers over a network
- **Shared Storage**
    - Data files can be stored on a central server for ease of access and backup purposes
- **Communication**
    - Computers in the same network are often able to share instant messages and emails for communication

# Disadvantages

- Initial Costs
    - Installing a network could be costly due to the high setup and equipment costs.
- Maintenance Costs
    - There are also subsequent costs associated with administering and maintaining the network
- Security Risks
    - As files are shared through a network, there is the risk of virus or worm attacks spreading throughout the network even with just one infected computer.
- Risk of data loss
    - Data may just become lost due to hardware failures or errors. Using a network means regular data backups are needed.
- Server outage
    - If the server fails, the network will not be able to function, thus affecting work processes.

# Types of Computer Networks

## Geographical Location

- Local Area Network (LAN) - Network of connecting devices connected within a small geographical area, typically within the same building, such as a home, school or office.
- Metropolitan Area Network (MAN) - Network of computing devices typically spanning across two or more buildings within the same

#  Network Protocols
Set of standards and rules that govern how two or more devices communicate over a network. \
OSI stands for **Open Systems Interconnection**. The OSI model is a conceptual model created by the International Organisation for Standardisation which enables diverse communication to communicate using standard protocols. \
The OSI model does not perform any functions in the networking process. It divides network communication into seven layers. The OSI Model can be seen as a universal language for computer networking. It is based on the concept of splitting up a communication system into seven abstract layers, each one stacked upon the last.

**Open Systems Interconnection (OSI)**. In this model, layers 1-4 are considered the lower layers and mostly concern themselves \
> **All People Seem To Need Data Processing**
# OSI Physical Layer
The lowest layer of the OSI Model is concerned with electrically or optically transmitting raw unstructured data bits across the network from the physical layer of the sending device to the physical layer of the receiving device. It can include specifications

# OSI Data Link Layer
**Physical Addressing**\
At the data link layer, directly connected nodes are used to perform node-to-node data transfer where data is packaged into frames. The data link layer also corrects errors that may have occurred at the physical layer.\
The data link layer encompasses two sub-layers of its own. The first media access control (MAC), provides flow control

**Path Determination and Logical Addressing**
The network layer is repsonsible for receiving frames from the data link layer, and delivering them to their intended destinations among based on the addresses contained inside the frame. The network layer finds the destination

# OSI Transport Layer
**End to End Connection and Reliability** \
The transport layer manages the delivery and error checking of data packets. It regulates the size, sequencing, and ultimately the transfer of data \
TCP/IP (Transmission Control Protocol/Internet Protocol; also known as the internet protocol suite) is the set of protocols used over the internet. It organises how data packets are communicated and make sure packets have the following information:
- Source - which computer the message came from.
- Destination - where the message should go
- Packet Seqeuence - The order the message data should be re-assembled
- Data - the data of the message
- Error Check - The check to see that the message has been sent correctly.
# OSI Session Layer
**Interhost Communication**
The session layer controls the conversations betyween different computers. A session or connection between machines is set up, managed and terminated at layer 5. Session layer services also include authentication and reconnections. E.g. Session establishment in TCP, SIP, RTP.

# OSI Presentation Layer
**Data Representation and Communication** \
The presentation layer formats or translates data for the application layer based on the syntax or semantics that the application accepts. Because of this, it is also at times is also called the syntax layer. This layer can also handle the encryption and decryption required by the application layer. E.g. HTML, DOC, JPEG, MP3, M4V, Sockets 

# OSI Application Layer
**Network process to Application** \
At this layer, both the end user and the application layer interact directly with the software application. This layer sees network services provided to end-user applications such as a web browser or Office 365. The application layer identifies communication partners, resources availability and synchronises communication.
E.g. DNS, WWW/HTTP, P2P, EMAIL/POP, SMTO, Telnet FTP.

TCP/IP Protocol includes:
- HTTP - transfers web pages from web servers to the client. All web page addresses start with http. An https address is a secure web address which has been encrypted. An https address is used for sites holding bank details and secure information.
- FTP - used to transfer large files. It is often used for organising files on a web server for a website. You can have private access to download the documents that you have shared.
- UDP - User Datagram Protocol - Similar to TCP, but because messages are sent instead of packets - chunks - it is often faster, allowing for gaming or video calls over the internet.
- SMTP - Simple Mail Transfer Protocol - governs the sending of emails over a network to a mail server.
- IMAP/POP3 - Internet Message Access Protocol - governs retrieving emails from email servers.
- VOIP - is a set of protocols that enables people to have voice conversations over the internet.

## TCP
- Slower but more reliable transfers
- Typical Applications:
    - File Transfer Protocol (FTP)
    - Web Browsing
    - Email

## UDP
- Faster but not guaranteed transfers ("best effort")
- Typical Applications:
    - Live streaming
    - Online games
    - VoIP

The reason why FTP uses only TCP (Transmission Control Protocol) is that TCP provides a **reliable**, connection-oriented, byte-stream service, which is 

TCP is slower but more reliable it makes sure the data is safely passed. UDP on the other hand does not care and yeets the data hoping it works.

UDP uses time-sensitive transmissions. It speeds up transmissions by enabling the transfer of data before an agreement is provided by the receiving party. Basically 2fast4u.

## ARP
### What is ARP?
Address Resolution Protocol (ARP) is a protocol or procedure that connects an ever-changing Internet Protocol (IP) address to a fixed physical machine address, also known as a media access control (MAC) address.


# Transmission Mediums
A **wired network** is a network of devices connected by a physical medium, such as cables.
The Ethernet is the most widely used wired network protocol in LANs and MANs.

![figure1](Networking/figure1.png)
A **wireless network** is a network of devices in which signals are transmitted without the use of a physical medium. The most common wireless network protocol is Wi-Fi, which uses radio waves to transmit data. 

A **Wireless Access Point** (WAP) is a network device that provides a connection between wireless devices up to 100 metres away and can connect to wired networks.

![figure2](Networking/figure2.png)

To get 1m, talk about both Wired and Wireless.

# VoIP
### Advantages of VoIP include:
- Lower cost
- Completely portable
- Advanced features
- More scalable

## Organisation (Client - Server Network)
## Client-Server Network
- A **client** is a computer that initiates a connection to a server to request for resources and services to perform operations. E.g. Employees in offices or students in schools would normally use client computers to do their work.

- A **server** is a computer that shares resources and responds to requests from devices and other servers on the network. It usually has a higher capacity and is more powerful than a client as it needs to manage resources and services. E.g. Providing central storage of files, sharing hardware such as printers, controlling logins and network access.

### Advantages
- Centralised control of data and resources
- Easy to schedule backups of all shared files at regular intervals
- Security may be enhanced with the use of specialised software or operating system features that are designed for servers.

### Disadvantages
- Higher initial cost due to the need for a server
- Administrative costs needed for the maintenance of server and clients.

## Peer-To-Peer (P2P) Network
- All computers are considered as equals and the load is distributed among all computers. Each computer in the network is able to act as both a client and a server, communicating directly with other computers
### Advantages
- Cheaper to set up as there is no cost related to dedicated servers 
- Easy to set up as no specialised or operating system features are needed.
### Disadvantages
- More effort is required to access and backup resources as they are stored locally within each computer instead of centrally in a server.
- Security is an issue as access rights are not administered by a central server

![figure3](Networking/figure3.png)
![figure4](Networking/figure4.png)
![figure5](Networking/figure5.png)
![figure6](Networking/figure6.png)
![figure7](Networking/figure7.png)


# Identifiers

## Identifiers

- IPv4 Address
- IPv6 Address
- MAC Address
- Port Number

### IPv4 Addresses

#### Example of an IPv4 address

![figure8](Networking/figure8.png)
#### Example of IPv6 address

![figure9](Networking/figure9.png)

### Public vs Private IP Addresses

- Each network will share the same public IP address. Other networks will be able to see your public IP address.
- When data meant for you is sent from another network to yours, it will be sent to your public IP address (which is your router's IP address)
- Your router keeps track of requests for data from each device by noting the private IP address down in a routing table. When it receives the data, it is able to route it to the correct device which requested for it.

### Network Address Translation

#### Example of a MAC address

![figure10](Networking/figure10.png)


### Why have we not run out of IPv4 Addresses?
- This is largely because of technologies like the __Network Address Translation (NAT)__, which maps many private IP addresses onto one public IP. There are also markets that sell and reallocate old IPv4 addresses for reuse.

### Why are we still using IPv4 when there is a better IPv6?
- IPv4 is still the dominant internet protocol. A key benefit of IPv4 is its __ease of deployment and widespread use__. Because IPv4 is used so broadly, network administrators and other internet developers can assume it is everywhere because everyone is compelled to support it.

### IP Address in Singapore
- Singapore has a total of ±20,297,984 IP address assigned.
- Population of SG in 2024 is 6.03 million.
- In SG, each home network has its own public IP.

### IP Address in USA
- USA has a total of ± 1,528,537,344 IP addresses assigned.
- Population of USA in 2021 is 341.82 million
- In US, shared public IP by area/town/roads (determined by ISP)
- Each street has its own public IP address.

### Port Number
- Used in combination with an IP address to identify a program that is running on a network
- All port numbers are assigned in a range from 0 to 65,535.

#### Did you know?
You can list all the port numbers that are in use on your computer by entering `netstat -na` in the command prompt.

### Service Set Identifier (SSID)

- A string of up to 32 bytes that identifies a wireless access point (WAP) and all the devices connected to it.
- All wireless devices connected to the same WAP must use the same SSID.










