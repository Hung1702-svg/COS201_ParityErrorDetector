# References for the Parity Error Detector Project

This file contains 15 online resources related to my **Parity Error
Detector** project. The project uses Verilog to create a parity bit,
simulate a transmission error, and check whether an error has happened.

> **Note:** These links are for learning and reference. Some websites
> may ask you to sign in. Please open each link and check the
> information before using it in a report.

## A. Verilog Design

1.  **8-bit Parity Generator and Checker in Verilog**\
    https://www.engineersgarage.com/verilog-tutorial-12-how-to-design-8-bit-parity-generator-and-checker-circuits-in-verilog/\
    *What it is about:* How to make a parity generator and checker for
    8-bit data.

2.  **Parity Generator and Checker --- UPC**\
    https://digsys.upc.edu/csd/products/D1_14/D1_14.html\
    *What it is about:* The main parts of a parity system and how data
    can be checked after transmission.

3.  **Parity Generator and Checker Using Verilog --- Project Report**\
    https://www.studocu.com/in/document/konduru-institute-of-technology-and-sciences-akshar-institute-of-technology/electronics-and-comuunication/parity-generator-and-checker-using-verilog-hdl-project-report/143960738\
    *What it is about:* An example of how a student report is organized.
    You may need an account to read it.

4.  **Design and Simulation of an Even Parity Checker**\
    https://cmosedu.com/jbaker/courses/ee421L/f17/students/verdum1/proj/proj.htm\
    *What it is about:* An even-parity circuit, its diagram, and
    simulation results.

5.  **Parity Generator and Checker --- Verilog Project Report**\
    https://www.studocu.com/in/document/geethanjali-college-of-engineering-and-technology/geetanjali-college-of-engineering-snd-technology/project-report-on-parity-generator-checker-design-using-verilog-btech/157960612\
    *What it is about:* An example of a project report about parity
    design. You may need an account to read it.

## B. Error Detection Basics

6.  **Error Detecting and Correcting Codes --- University of Michigan**\
    https://www.eecs.umich.edu/courses/eecs373.w05/lecture/errorcode.html\
    *What it is about:* How error detection works and what parity can
    and cannot detect.

7.  **Web Coding Theory Book --- Parity Code**\
    https://users.math.msu.edu/users/iwenmark/Teaching/MTH810/web-coding-book2.pdf\
    *What it is about:* The basic ideas behind parity codes and error
    checking.

8.  **Error Detection and Correction --- Stanford University**\
    https://web.stanford.edu/class/ee179/lectures/notes18.pdf\
    *What it is about:* Class notes about finding and correcting data
    errors.

9.  **Even Parity --- Error Detection**\
    https://www.ece.unb.ca/tervo/ece4253/ecc.shtml\
    *What it is about:* How even parity works and how XOR is used to
    check data.

10. **Error Detection: Parity Bits and Check Digits --- Longwood
    University**\
    https://cs.longwood.edu/courses/cmsc121/resources/s24/error-detection/\
    *What it is about:* Parity bits and the difference between finding
    an error and fixing it.

11. **The Mathematics of Coding Theory**\
    https://pws.npru.ac.th/sartthong/data/files/\_Mathematics_of_Coding_Theory.pdf\
    *What it is about:* More details about codes and parity checks.

12. **Error Detection and Correction --- NPTEL**\
    https://archive.nptel.ac.in/content/storage2/courses/106105080/pdf/M3L2.pdf\
    *What it is about:* Error checking methods, including parity,
    checksum, and Hamming code.

## C. Extra Learning Resources

13. **Parity Generator and Checker Explained --- YouTube**\
    https://www.youtube.com/watch?v=c8qAti1zBVQ\
    *What it is about:* A video that explains how a parity generator and
    checker work.

14. **Parity Generator --- Paiz Logic**\
    https://docs.paizlogic.com/en/dec-paritygen\
    *What it is about:* A short guide to parity and its truth table.

15. **Parity Bit Tutorial: Single-Bit Error Detection --- DigiSim**\
    https://digisim.io/blog/parity-bit-tutorial-single-bit-error-detection\
    *What it is about:* How parity can find a one-bit error and its
    limits.

## Best Resources for My Project

-   **High-Level and Low-Level diagrams:** Resource 2.
-   **Verilog code:** Resource 1.
-   **Circuit diagrams and simulation:** Resource 4.
-   **Basic theory for the report:** Resources 6, 8, 9, and 10.
-   **Report layout examples:** Resources 3 and 5.

## My Project Modules

The project currently has these Verilog modules:

-   `parity_generator.v`
-   `error_injector.v`
-   `parity_checker.v`
-   `top.v`

The design creates a parity bit from the original data. The error
injector can flip bit 5. Then, the checker uses the received data and
the parity bit to set `error_flag`.

Parity can detect a one-bit error, but it cannot detect every possible
error. Use these resources to learn and explain the design in your own
words. Do not copy text or code without checking it and giving credit to
the source.
