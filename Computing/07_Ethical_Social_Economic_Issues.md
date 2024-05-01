# Ethical, Social and Economic Issues in Computing

* [Data Corruption](#data-corruption)
    * [Effects of Corruption and Data Loss](#effects-of-corruption-and-data-loss)
    * [Causes and Ways to Prevent Data Corruption and Loss](#causes-and-ways-to-prevent-data-corruption-and-loss)
* [Authentication](#authentication)
    * [Passwords](#passwords)
    * [Unauthorised Access](#unauthorised-access)
    * [Biometrics](#biometrics)
* [Authorisation](#authorisation)
    * [File Permissions](#file-permissions)
    * [Firewalls](#firewalls)
* [Encryption](#encryption)
* [Understanding of Privacy Policies](#understanding-of-privacy-policies)
    * [Social Networking Sites](#social-networking-sites)
* [Summary](#summary)
    * [Preventing Unauthorised Access](#preventing-unauthorised-access)
* [Threats to Privacy and Security](#threats-to-privacy-and-security)
    * [Defensive Measures Against Privacy and Security Threats](#defensive-measures-against-privacy-and-security-threats)
        * [Installing anti-virus and anti-spyware programs](#installing-anti-virus-and-anti-spyware-programs)
    * [Operating System](#operating-system)
    * [Update Software Regularly](#update-software-regularly)
    * [Identity Phishing](#identity-phishing)
    * [Identity Pharming](#identity-pharming)
    * [Manage Spam](#manage-spam)
    * [Manage Cookies](#manage-cookies)
* [Intellectual Property](#intellectual-property)
    * [Types of Software Licenses](#types-of-software-licenses)
    * [Software Piracy](#software-piracy)
    * [Plagiarism](#plagiarism)
* [Impact of Technology on Daily Life](#impact-of-technology-on-daily-life)
    * [Communication](#communication)
    * [Finance](#finance)
    * [Healthcare](#healthcare)
    * [Transportation](#transportation)
    * [Entertainment](#entertainment)

## Data Corruption

__Data corruption__ occurs when computer data is made unstable by errors or alterations. This can happen during the reading, writing or transmission of data.

If the corrupted data cannot be recovered / replaced, this results in __data loss__.

### Effects of Corruption and Data Loss

The effects vary depending on the amount of corrupted data and type of data that is represented.

If the corrupted data is not needed to read other data, only that data itself is lost. This is more likely if the amount of corrupted data is small.

However, if the corrupted data is related to other data in the computer, then both itself and its related data may be lost, as it may contain information required to read/interpret the related data. This is more likely if the amount of corrupted data is large.

### Causes and Ways to Prevent Data Corruption and Loss

In all cases, making regular __backups__ (copies of data made in case the original data is damaged or lost) of data will help to prevent the loss of data.

Causes of data corruption and loss include:

- __Human Error__
    - Storage devices may be damaged during transport.
    - Multiple users working on the same file may accidentally overwrite each other.
    - __Preventive Measures__
        - Make regular backups of data
        - Use adequate protection when transporting storage devices.
        - Set up rules when collaborating with multiple users to prevent them from writing to the same file at the same time.
- __Power Failure__
    - If the power supply to a computer fails, data in the process of being written to a storage device may become corrupted and data stored in volatile memory and not yet written to a storage device will become lost.
    - __Preventive Measures__
        - Regular backups
        - Set up a backup power supply, or __uninterruptible power supply (UPS)__ so storage devices can complete any write operations in case of a power failure.
- __Hardware Failure/Damage__
    - All magnetic, optical and solid-state storage devices can fail, either due to overuse, manufacturing defects, or age.
    - __Preventive Measures__
        - Regular backups
        - Check storage device regularly and replace them immediately when signs of failure are detected.

- __Malware/viruses__
    - Some malware may purposely damage and corrupt data as a way of attacking the computer
    - __Preventive Measures__
        - Regular backups
        - Avoid opening emails/attachments or files from unknown sources.
        - Install and configure a firewall to prevent malware from spreading through the network.
        - Install anti-virus and anti-spyware software and perform regular scans and updates

An __uninterruptible power supply__ is a device that provides enough emergency power for a computer to properly shut down in the event of a power failure.

## Authentication

Authentication is the process of verifying the identity of a user. It requires the user to prove their identity by providing evidence from one or more of the following categories:
- Something the user knows (password)
- Something the user owns (mobile phone)
- Something physically unique about the user (thumbprint)

Each category of evidence used for authentication is called an __authentication factor__

### Passwords

Passwords are the most common form of authentication. Some passwords are entered together with a username that identifies who the user claims to be.

They can be a poor form of authentication if they are chosen poorly or not well-kept as a secret. Avoid using birthdates, surnames and other things that can be easily guessed.

Use hard to guess passwords that are a mixture of lowercase, uppercase letters, numbers and symbols.

Avoid re-using passwords or leaving them unchanged for a long time as it makes it easier for an intruder to guess the password. Use unique passwords for each computer and account, and update them at least once every 90 days.

### Unauthorised Access

Some authentication systems require evidence from more than 1 authentication factor. Banks typically issue a device called a security token to users who wish to access their accounts online.

A __security token__ is a device used specifically for authentication purposes, such as mobile phones and one-time passwords (OTPs).

The type of authentication that uses evidence from both something a user knows and owns is called __2-factor authentication__.

2FA is stronger than a singular password as it is more difficult for an intruder to both guess a password and steal the user’s security token. Hence, it is important to keep the security token in a secure location at all times and to report a missing security token as soon as possible.

If an OTP is sent wirelessly to a user’s mobile phone, it may be intercepted and used by an intruder during the transmission process. If the secret algorithm used to generate OTPs is poorly chosen or accidentally revealed, an intruder may find out how to generate OTPs without needing the security token at all.

There is not much a user can do about this type of intrusion attempt.

### Biometrics

__Biometrics__ is a type of authentication that is based on the measurement of
human physical characteristics.

For example, biometrics is used to identify a user by fingerprint or voice. Other characteristics used include the face, iris, retina, and DNA.

The use of biometric identification is more secure as the physical characteristics measured are typically unique to the individual and cannot be easily replicated. Thus, it helps prevent attempts to establish fraudulent identities and __identity theft__.

__Identity theft__ is the impersonation of another person to steal personal details such as name and identity number for fraudulent purposes.

## Authorisation

Once the user is authenticated, the ability of a computer to control the access of data and resources by that user is called __access control/authorisation__.

Computers provide access control through a variety of means.

### File Permissions

Most operating systems have settings to control the ability of users to view or make changes to specific files or folders. These settings are called __permissions__.

An application of file permissions is when a teacher may set a presentation file to be read-only for students, so they do not accidentally (or intentionally) change its contents.

Typically, users can only change the permissions for any file or folder they own. However, most OS's allow for a special user called the __administrator__, who can override the permissions for almost any file or folder.

A normal user may also be given special __administrator rights__ that allow them to override the permissions for certain files or folders, just like an administrator.

Managing permissions and administrative rights can be a complex task, and it is possible to accidentally grant access to a file or administrative rights to an unauthorised user. Such a user can then make use of such mistakes to gain unauthorised access to data and resources.

Authentication for the administrator must be especially strong, as an intruder that successfully claims to be an administrator can bypass file permissions entirely.

File permissions do not prevent an intruder with physical access to a storage device from accessing files or folders directly without going through the operating system. To prevent such access, it is necessary to use encryption.

File permissions can be used as access control for both computers connected to a network and computers that are not connected to a network, but are shared by multiple users.

### Firewalls

Computers connected to a network are naturally more susceptible to intrusion as unauthorised access can occur without the physical presence of an intruder.

Hence, computers connected to a network usually require another layer of access control called a __firewall__

A firewall is a device/network that prevents unauthorised access to or from a private network. It works by monitoring each piece of data transmitted through a network. It then either blocks or allows data to pass based on a set of rules configured by an administrator.

When properly configured, a firewall can protect computers within a network from unauthorised access. They can be configured to block the transmission of data (aka __traffic__) between unauthorised senders and receivers, especially requests for data from anonymous users on the internet. This prevents intruders from gaining access to the computers within a network.

Since firewalls can also block traffic based on the type of application that is transmitting the data, it can also stop certain harmful programs from sending copies of themselves to other computers through the network.

Configuring a firewall correctly can be complex and a misconfigured firewall may have security vulnerabilities that allows intruders to gain unauthorised access.

A properly configured firewall allows for a private network (aka __intranet__) to be set up such that all external traffic is blocked and only authenticated and authorised users are able to access it. Since the users on a private network are generally trusted and expected to keep information on the network confidential, there are usually fewer concerns about unauthorised access when sharing data on a private network.

Conversely, a private network such as the Internet allows anyone to connect to it and share data. Since public networks have little-to-no restrictions, users need to be wary of possible security and privacy risks when accessing it.

## Encryption

__Encryption__ is the process of encoding data so that a secret key is required to read the data. Like passwords, the secret key is usually provided as a sequence of bytes.

Before the encrypted data is decoded using the secret key, it appears as random and meaningless data.

Encryption is often used to protect data from unauthorised access by allowing only authorised users to have the secret key. It can be used in combination with file permissions so an unauthorised user who bypasses file permissions would still be unable to use the accessed data without knowing the secret key.


## Understanding of Privacy Policies

Unauthorised access can occur indirectly due to the actions of 3rd-party users or services.

For example, a user alters file permissions to let a classmate access some private files. That classmate in turn shares those files with others without the original user's knowledge.

- __Privacy__ - The ability to keep specific data or resources from being known by others.
    - In many countries, organisations are required by law to publicise or make available a privacy policy about the rules and practices they follow regarding the collection, protection and use of personal or private data provided by users.
    - __Example__: Organisations in Singapore are required by the Personal Data Protection Act (PDPA) to make their privacy policies available upon request.

An increasing number  of users share personal information such as photos and location data using online services, many of them are unfamiliar with the relevant privacy policies or how such sharing habits may indirectly result in unauthorised access. A poor understanding of the privacy policies of these services can often result in unauthorised access.

### Social Networking Sites
	
Social networking sites such as Twitter, Instagram and TikTok allow users to share photographs and information quickly with their families or friends. They can also be used to promote businesses or raise awareness of campaigns or causes.

However, these sites can pose many privacy concerns because most users do not read or consider the repercussions of the privacy policies used by these sites regarding personal information such as status updates, notes, photographs and location data.

The privacy policies for many social networking sites do not guarantee that personal data collected will never be exposed to unauthorised users and may even require that your personal data be shared with advertisers in order to use their sites. Hence, personal data can potentially be harvested for spam and other threats to privacy that users did not authorise directly.

Remember: Once data is digitised and uploaded to a public network such as the Internet, it can potentially remain there forever, since it can be easily copied and republished in ways no longer under the control of the original uploader.

Oh, and also some privacy policies for some social networking sites don’t guarantee that their personal data will be deleted from the site completely or immediately even after their account is closed, deleted, or has all personal data removed from it.

Personal data is sensitive and should not be shared publicly. Some companies may reject candidates after reviewing the information and photographs posted on their social networking accounts, even if this was posted while they were still at school.

## Summary

### Preventing Unauthorised Access

- Read and fully understand the privacy policy of the social networking site.
- Set sharing settings to "private" so only people you know in real life can read your posts.
- Think twice before posting personal photographs or information that you may feel uncomfortable sharing.
- Accept friend requests wisely. Make sure you know everyone in your friends list.

## Threats to Privacy and Security

![figure1](Ethical_Social_Economic_Issues/figure1.png)
![figure2](Ethical_Social_Economic_Issues/figure2.png)

### Defensive Measures Against Privacy and Security Threats

#### Installing anti-virus and anti-spyware programs

- __Anti-Spyware__ - Software to detect, remove and stop spyware and other malware from running.
- __Anti-virus__ - Software to detect, remove and stop viruses and other malware from running.

Counters viruses, worms, spyware and Trojan horses, since they need to run on a user's computer in order to perform their respective attacks.

These programs can be used to scan a user's storage and email to detect and remove malware. If a program has been infected by a virus, it may also try to restore the original program.

Although powerful, most rely on a list of __signatures__, unique evidence used to detect a known version of some malicious software. This list has to be updated regularly to ensure protection provided continues to be effective against new malware. Most programs update the list automatically through the Internet.

Some especially devious Trojan horses appear to be anti-virus and anti-spyware programs. Only trust programs provided by reputable companies, or as part of the computer's __operating system__.

### Operating System

An __operating system__ is software designed to support a computer's basic functions, such as Windows and MacOS.

### Update Software Regularly

Most malware require human interaction to activate, but worms can run automatically by exploiting bugs in otherwise legitimate programs already running on a computer.

For example, a flawed web browser may have a bug that allows websites to run malicious programs without the user's knowledge.

To prevent this, update software regularly so bugs that were discovered since the last update can be fixed. This is especially important for software used to interact with public networks like the Internet, as data from public networks is more likely to be malicious and designed to take advantage of known bugs.

### Identity Phishing

Phishing emails should be ignored and deleted. There are several telltale signs to identify phishing emails.
- Claims to be from a company/bank asking for confidential information. Most companies and banks never ask for such information via email. If in doubt, call the company or bank to verify.
- Generic greeting such as "Dear User", it is a sign that the email was sent automatically and not by a person.
- Inaccurate logos and grammatical or spelling errors.
- Sender's email address or contact does not match the supposed source of email.
- Email has hyperlinks with destinations that do not match what the hyperlink text says or is otherwise unexpected. Place mouse cursor over the hyperlink and its destination should appear as a popup or on the status bar.
- Excessively urgent or threatening tone, a scare tactic to make victims act before they can think through their actions properly.
- Email promises offers that are too good to be true, tempting victims into revealing personal information.

### Identity Pharming

Pharming is like phishing V2. The attacker attempts to intercept requests sent from a computer to a legitimate website and redirects the user to a fake website to steal personal data.

For example, a victim of pharming may log into their bank account, and are presented with a website that looks like the bank, but isn't. The attacker can now retrieve your account details to access your bank account on the actual website, stealing your money.

For pharming to be successful, the attacker must either have malware running on the victim's computer or has taken control of a network device such as a router or server. This can occur as the software that runs on such devices is also susceptible to bugs.

It is harder to detect as everything seems to be normal while the attack takes place. Measures include:
- Ensure encryption is used when submitting sensitive information via the internet. Check if there's a padlock icon at the address bar.
- Regularly check bank, debit/credit card and other statements to ensure all transactions are legitimate.
- Regularly update web browsers and the software running on the network hardware so that all known bugs are fixed.
- Enable 2FA for all bank transactions. This means even if the attacker is able to access the bank account, no unauthorised transactions can occur as the attacker would not be able to provide the required OTP.

### Manage Spam

- Avoid giving your email to unfamiliar contacts or untrusted websites. If you really need to provide one, use a temporary email generator like 10minutemail. Or, set up a secondary email address dedicated to unimportant emails.
- Read and understand the privacy policy of any website, trusted or untrusted, that requests an email address before providing it. Some websites share email addresses with advertisers who spam.
- Look for options to disable email update or participation in mailing
lists when signing up or changing online account settings.
- Most email services have a filter feature that allow users to block specific senders or to only allow emails from specific senders through.
    - Some filtering systems have advanced spam detection algorithms that can be trained by having the user identify examples of spam the filter is not yet able to detect. This lets the filter become more effective in detecting spam over time.

### Manage Cookies

Cookies are small pieces of data stored by the web browser when a user visits a website. Each time a user visits a website that uses cookies, the browser checks whether it has a relevant cookie and if so, it sends the information contained in that cookie back to the website.

The website is thus aware that that the user has visited before and sometimes customises what appears on the page for the user. If no relevant cookie is found, the website may request for a new cookie to be created.

They are generally not malicious and are needed to keep track of authentication information to identify which user is currently logged in. However, they can be used to keep track of user movements and preferences within the websites, such as which pages are most recently visited. Advertising companies with advertisements on multiple websites can also use cookies to keep track of users as they move from one website to another.

Most browsers have settings that allow users to manually delete or prevent cookies from being created by untrusted websites. These settings can also be configured to disable cookies or allow only selected websites to use cookies. 

## Intellectual Property

- __Intellectual Property__ - Creations of the mind that have value but can exist purely as data with no physical form.
- __Copyright__ - The legal right of owners to control the use and distribution of their intellectual property.
- __License__ - Official description of activities that are authorised or forbidden by the owner of intellectual property.

### Types of Software Licenses

There are several types of software licenses in order to avoid infringing copyright laws.

- __Public Domain Software__ - Software where the legal protections that are typically granted to intellectual property have either expired, surrendered or are simply inapplicable.
    - Not protected by copyright, anybody can legally copy, modify and distribute public domain software. It may not always come with source code, though most do.

- __Free and Open Source Software (FOSS)__ - Software where users are given freedom to change, copy, study and share the software and its source code.
    - The term "free" refers to free to use, not free of charge.
    - Similar to public domain software, but is still protected under copyright and the copyright owners may use this protection to require that the software must always be distributed with source code, attribution to the original authors must be provided or any modifications must use a similar license if distributed.
    - Other types of copyrighted works such as books, photographs and music must be licensed in a similar manner using Creative Commons (CC) licenses. Note that CC licenses grant users freedom to copy, modify and distribute copyrighted works, CC licenses are not designed for software and should not be used for this purpose. It can, however, be used to license content that is delivered using software. Higher education course materials such as videos and notes created by
        universities and distributed for free on the Internet, aka __open courseware__ often use CC licenses.
- __Open Courseware__ - Higher-education course materials such as videos and notes created by universities and distributed for free on the Internet.
- __Proprietary Software__ - Commercial software for which most of the legal protections under copyright are retained.
    - Unlike FOSS, it is usually not legal to copy, modify or distribute proprietary software. The terms and conditions for which the proprietary software may or may not be used under copyright protection law are usually communicated by users through an End User License Agreement (EULA) contract that the user must accept to use the software.
    - The source code for proprietary software is usually kept secret.
    - Although it seems super restrictive compared to FOSS, it is important to remember that software is a form of intellectual property and it is the right of the owner to be compensated for the use of the property. An example of proprietary software is Windows OS, where unauthorised copying is illegal and the majority of source code is kept secret.
- __Freeware__ - Proprietary software that is available for use at no cost.
    - Some freeware are "lite" versions of proprietary software, allowing users to try a limited version of the software while promoting the full version
- __Shareware__ - Demonstration software that is distributed for free but a specific evaluation period only.
    - After the evaluation period, the program expires and the user can no longer access the program unless the user pays a registration fee.
    - The source code for freeware and shareware is usually kept secret and modifying the software is usually kept illegal. However, it may be legal to copy and distribute freeware and shareware. Adobe Reader and Skype are examples of freeware, and Camtasia Studio and WinRAR are examples of shareware.

### Software Piracy

__Software piracy__ is the crime of copying, distributing or using proprietary software illegally. Despite being illegal, it is prevalent and can take place in many forms.

Installing multiple copies of proprietary software without purchasing additional licenses or sharing proprietary software with unlicensed users is considered software piracy and can result in similar legal repercussions.

Software piracy causes significant loss of revenue for the owners of intellectual property, which leads to higher prices for legitimate buyers.

__Cracks__ are programs that modify proprietary software so that the software cannot detect that it is being used illegally. Software piracy is an example of __copyright infringement__, which is the use or distribution of copyrighted work without the permission of the copyright owner. While software piracy is specific to software, copyright infringement can occur for any copyrighted materials, such as pictures on the Internet, which is equivalent to theft.

### Plagiarism

__Plagiarism__ is the act of passing off someone else's original work as your own, aka the act of claiming to be the author of a piece of work without providing proper credit or attribution to the actual author.

Unlike copyright infringement, plagiarism may not always be illegal, but it is nevertheless an act of dishonesty and is usually a punishable offense in academia.

Plagiarism can still occur when the original owner of a piece of work consents to letting someone use it as their own.

To avoid plagiarism, you can use __citations__ to give proper credit to the original authors of any reproduced materials in published books, websites and articles.

## Impact of Technology on Daily Life

### Communication

The Internet has enabled diverse cultures to interact and share ideas with each other. Social networking sites have enabled users to remain connected with friends, family and colleagues over long distances.

Artificial intelligence has made it possible for anyone to automatically transcribe and translate speech into different languages with high speed and accuracy.

Some people on the Internet use the Internet to reinforce their existing opinions, or to spread the rumors, misinformation, or propaganda. This is worsened by the use of AI by some news and social and media sites to promote content the reader is likely to be interested in. Most sites promote content based on engagement and not accuracy.

Smart phones have led to an increased focus on mobile devices and mobile applications in the computing industry.

Social media has led to increased use of social media for marketing purposes and helps businesses to better understand buying habits and consumer needs by analysing social media posts.

Improvements in communications technology have also reduced business costs through the use of cheap and effective video conferencing calls instead of face-to-face meetings by cutting the costs of finding suitable venues as well as suitable timeframes to meet in person.

### Finance

Financial technology has enabled consumers to spend, borrow, invest and save money through low-cost and easy-to-use mobile and web applications. There is no need to perform such transactions in person. Individuals have better education on how to make smart financial decisions using freely available information on the Internet.

Threats to privacy and security of data as well as the ease of obtaining false information on the Internet has made some people more vulnerable to financial scams and other get-rich-quick schemes.

Financial technology is currently an area of growth in the financial industry. Numerous companies have been started to make financial services more efficient for both individuals and businesses. These companies typically use technology and software to reduce the time, cost and effort needed for payments, investments, fundraising, trading, and/or data analysis for both businesses and individuals.

With the evolution of technology, the time needed to perform a financial trade has decreased from seconds down to mere microseconds. This has led to the rise of algorithmic trading, which is the study and refinement of algorithms to make trading decisions at speeds not possible by a human being.

Many banks also use AI to analyse transaction data and automatically identify unusual spending patterns or money transfers. This helps them to automatically detect and prevent instances of financial fraud without the need for manual intervention.

### Healthcare

On the positive side, technology has enabled telemedicine, which is the use of video conferencing and other technologies, for doctors to provide medical consultations and diagnoses over the Internet or applications in mobile devices. This gives patients who are located in remote places or have limited mobility better access to healthcare. By analysing medical data, AI can automatically identify warning signs of possible health problems and provide doctors with more accurate
diagnoses.

On the negative side, some patients find the use of robots and other technology in healthcare impersonal and mistrust the ability of machines to provide proper healthcare. Other patients may misuse information from the internet and make potentially dangerous decisions based on incorrect diagnoses. Patients may also be uncomfortable with the collection of medical data necessary to improve the performance of healthcare-related AI.

Technology has created new areas of growth in the healthcare industry, such as the provision of telemedicine solutions to existing healthcare businesses. In particular, many of these solutions provide a way for patients to securely transfer potentially sensitive medical information over the internet.

There is also an increased focus in automating healthcare processes through the use of robots to dispense medicine and other more menial tasks. This may in turn cause such jobs to disappear from the job market.

The rise of 3D-printing technology has also opened up new opportunities in the building and customisation of prosthetic limbs, hearing aids and dental fixtures.

### Transportation

On the positive side, transport has become less stressful and more predictable for travellers due to the availability of detailed maps as well as real-time information on bus frequencies, traffic congestion levels and street-level photographs of neighbourhoods around the world. All this information is also available at low cost through mobile devices. Location data from such mobile devices may also be collected by AI to improve the accuracy and relevance of any map or
traffic data that is displayed.

On the negative side, some people are uncomfortable with how pictures and information about themselves or their home may be used by mapping companies without their permission in order to build more accurate maps for travellers. This is especially true with regards to the collection of location data from mobile devices as this data can reveal personal details such as home and work addresses that users may wish to keep private.

The rise of self-driving vehicles with the use of AI to recognise and adapt to road conditions is likely to open new areas of growth in the travel industry. Singapore is one of the first countries where self-driving cars are being tested, and if successful, the technology will likely revolutionise the motor industry.

There are also multiple new companies that offer on demand rides via mobile applications. These developments have led to sweeping changes in the taxi service industry as well as employment opportunities for taxi drivers.

Mapping technology is also another area of growth with an increased focus on making 3D maps and geospatial data more accessible and useful to travellers.

### Entertainment

On the positive side, technology has enabled more exciting and engaging forms of entertainment. Many computer games have active online communities and mobile games have even managed to bring participants together in the real world through in-game incentives to meet or team up. AI has also made it possible to provide more accurate recommendations for consumers based on collected data of their previous choices of entertainment.

On the negative side, some people may be addicted to computer games or social networking sites. There is an increasing concern that such technology is causing people to become deficient in real-life social skills or abandon their responsibilities. AI has also made it possible for anyone to create doctored images and videos that appear remarkably convincing to the average viewer. While such images and videos have been used mostly for entertainment, they can also be used to cause public alarm or spread damaging falsehoods.

Games, animation and media are areas of strong growth in the entertainment industry with new opportunities being opened up by the rise of high-quality virtual reality, augmented reality and motion- tracking technology.

Many businesses are also using monitoring technology and strategies from game design to provide rewards and incentives for work- related achievements.


