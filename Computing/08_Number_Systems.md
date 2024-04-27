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








