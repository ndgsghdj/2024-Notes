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

# OSI Physical Layer
The lowest layer of the OSI Model is concerned with electrically or optically transmitting raw unstructured data bits acrosss the network from the physical layer of the sending device to the phuysical layer of the receiving device. It can include specifications

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


# Transmission Mediums
A **wired network** is a network of devices connected by a physical medium, such as cables.
The Ethernet is the most widely used wired network protocol in LANs and MANs.

<img src="./figure1" />

A **wireless network** is a network of devices in which signals are transmitted without the use of a physical medium. The most common wireless network protocol is Wi-Fi, which uses radio waves to transmit data. A **Wireless Access Point** (WAP) is a network device that provides a connection between wireless devices up to 100 metres away and can connect to wired networks.

:!git init

