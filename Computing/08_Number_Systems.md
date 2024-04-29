# Number Systems

## Denary Number System

### Definition
A number system that is made up of __10 unique digits__.
- Uses place values of powers of 10.

## Binary Number System

### Definition
A number system that is made up of __2 unique digits__.
- Uses place values of powers of 2.

## Notation
To distinguish binary numbers from denary numbers, they can be written in any of the following ways:
- $1101$
- $(1101)_2$
- $0b1101$

Leading zeros are sometimes also shown when using binary numbers in computer systems to show all 8 binary bits in a byte:

e.g. $0000 \space  1101$

## Denary to Binary

### Algorithm 1: Dividing by 2

1. Draw a table with three columns - one column for denary numbers, one column for the quotients and one column for the remainders.
2. Fill in the denary number in the first row.
3. Divide the denary number by 2 and fill in its quotient and remainder in the same row.
4. If the quotient is 0, proceed to step 5. Otherwise, copy the quotient to the denary number column of the next row and repeat step 3.
5. The equivalent binary number is the remainder column read from the bottom up.

#### Example: Converting 135 to binary

| Denary | Quotient | Remainder |
|--------|----------|-----------|
| 135    | 67       | 1         |
| 67     | 33       | 1         |
| 33     | 16       | 1         |
| 16     | 8        | 0         |
| 8      | 4        | 0         |
| 4      | 2        | 0         |
| 2      | 1        | 0         |
| 1      | 0        | 1         |

$\therefore (135)_{10} = (10000111)_2$

### Algorithm 2: Sum of Place Values

E.g. Convert 135 to binary

![figure1](Number_Systems/figure1.png)

## Hexadecimal Number System

### Definition
Number system that is made up of 16 unique digits.

### Denary equivalents of the hexadecimal

| Hexadecimal digit | Denary equivalent |
|-------------------|-------------------|
| 0                 | 0                 |
| 1                 | 1                 |
| 2                 | 2                 |
| 3                 | 3                 |
| 4                 | 4                 |
| 5                 | 5                 |
| 6                 | 6                 |
| 7                 | 7                 |
| 8                 | 8                 |
| 9                 | 9                 |
| A                 | 10                |
| B                 | 11                |
| C                 | 12                |
| D                 | 13                |
| E                 | 14                |
| F                 | 15                |

### Example of Hexadecimal Number

$$ 1C6A $$

$$1C6A_{16} = 1 \times 16^3 + 12 \times 16^2 + 6 \times 16^1 + 10 \times 16^0$$


To distinguish hexadecimal numbers from denary numbers, they can be written in any of the following ways:
- $1C6A_{16}$
- $(1C6A)_{16}$
- $0x1C6A$

### Denary to Hexadecimal

#### Algorithm 1: Divide by 16

1. Draw a table with three columns - one column for denary numbers, one column for the quotients and one column for the remainders.
2. Fill in the denary number in the first row.
3. Divide the denary number by 16  and fill in its quotient and remainder in the same row.
4. If the quotient is 0, proceed to step 5. Otherwise, copy the quotient to the denary number column of the next row and repeat step 3.
5. The equivalent denary number is the remainder column read from the bottom up.

#### Example

Convert 1899 to hexadecimal

| Denary | Quotient | Remainder     |
|--------|----------|---------------|
| 1899   | 118      | $11 = B_{16}$ |
| 118    | 7        | $6 = 6_{16}$  |
| 7      | 0        | $7 = 7_{16}$  |

### Hexadecimal to Binary, or Vice Versa

![figure2](Number_Systems/figure2.png)

## Applications of Number Systems

### RGB Colour Codes

RGB is an abbreviation of red, green, and blue, which are the primary colours of light and can be combined with varying intensities to create other colours.

The intensity of each colour component is stored as a number, and each value is stored in a single byte, corresponding to $00000000_2$ to $11111111_2$, $00_{16}$ to $FF_{16}$, and 0 to 255 in binary, hexadecimal, and decimal respectively.

When all 3 colour intensities are 0, the result is black. If all intensities are at their maximum, the result is white.

RGB colour codes are displayed in the form of #RRGGBB, where RR, GG and BB are 2-digit hexadecimal numbers that represent each component of the colour. These codes are used to represent colours in websites, typically written in HTML and CSS.

### Network Addresses

For computers to communicate/exchange data over a network, they must be able to locate each other so that transmitted data can be directed to the correct destination.

This is done by giving each computer a unique name in the form of a sequence of bytes called a __network address__.

The Internet as an example of a computer network, each computer on the Internet has an __IP Address__, serving as its network address on the internet.

IP (Internet Protocol) is a standard system of rules used by computers on the Internet to communicate with each other. There are 2 versions of IP used today, IPv4 and IPv6

#### IPv4

- An internet protocol that is made up of 4 bytes (32 bits).
    - Usually shown as a sequence of 4 denary numbers, one for each byte of the address, separated by dots.
    - Since the value of a byte can only vary from 0 to 255, none of the 4 denary numbers can fall out of this range.
    - The maximum number of IPv4 addresses is $2^{32}$, or 4.3 billion. With the rapid growth of the Internet in the 80s and 90s, the number of IPv4 addresses is insufficient.

#### IPv6

- Usually shown as a sequence of 8 hexadecimal numbers, each number being 16 bits. Each group uses 4 hexadecimal digits.
- Hexadecimal is used for representation as using decimal would take up a maximum of $3 \times 16 = 48$, which is inconvenient.

## MAC Address

- __Media Access Control (MAC) address__ - A sequence of bytes (usually permanent in nature) that is used to identify a particular network interface controller.
    - It is a permanent way to locate or identify a specific computer or device, as the IP address of a computer may change each time it connects to the Internet.
    - It is made up of 6 bytes (48 bits), and is shown as a sequence of 6 hexadecimal numbers, one for each byte of the address. They are separated either by colons or hyphens.
    - The format for a MAC address is __NN-NN-NN-DD-DD-DD__, where __NN-NN-NN__ is the manufacturer's identity number; and __DD-DD-DD__ is the device's serial number.

## ASCII and Unicode

### ASCII

- Stands for the American Standard Code for Information Interchange
- Defines how numbers are used to represent common characters that can be typed using a keyboard, such as upper-case and lower-case letters.
- Exactly seven bits long, so only 128 (= 27) distinct characters can be represented.

### Unicode

- Similar function to ASCII, but can be used to represent characters in other languages such as Tamil and Mandarin, and even emojis.
- The number of bits used to represent each character can vary from 8 to 32 bits depending on the encoding scheme used.
- Unicode can be used to represent over a million unique characters from many different written languages all over the world.
- For backward compatibility, the first 128 characters of Unicode are the same as ASCII.



