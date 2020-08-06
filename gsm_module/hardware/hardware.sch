EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A3 16535 11693
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Connector:Screw_Terminal_01x04 J1
U 1 1 5F2608C9
P 850 1475
F 0 "J1" H 768 1050 50  0000 C CNN
F 1 "Screw_Terminal_01x04" H 768 1141 50  0000 C CNN
F 2 "Connector_PinHeader_1.27mm:PinHeader_1x04_P1.27mm_Vertical" H 850 1475 50  0001 C CNN
F 3 "~" H 850 1475 50  0001 C CNN
	1    850  1475
	-1   0    0    1   
$EndComp
$Comp
L Interface_CAN_LIN:MCP2515-xSO U3
U 1 1 5F263E6D
P 2525 4950
F 0 "U3" H 2700 5725 50  0000 C CNN
F 1 "MCP2515-xSO" H 2125 5725 50  0000 C CNN
F 2 "Package_SO:SOIC-18W_7.5x11.6mm_P1.27mm" H 2525 4050 50  0001 C CIN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/21801e.pdf" H 2625 4150 50  0001 C CNN
	1    2525 4950
	1    0    0    -1  
$EndComp
Text GLabel 1050 1575 2    50   Input ~ 0
12-40v
Text GLabel 1050 1475 2    50   Input ~ 0
GND
Text GLabel 1050 1375 2    50   BiDi ~ 0
CAN-LOW
Text GLabel 1050 1275 2    50   BiDi ~ 0
CAN-HIGH
$Comp
L Device:CP1_Small polcap1
U 1 1 5F26D3DB
P 2500 1725
F 0 "polcap1" H 2591 1771 50  0000 L CNN
F 1 "470uF" H 2591 1680 50  0000 L CNN
F 2 "Capacitor_THT:CP_Radial_D8.0mm_P3.50mm" H 2500 1725 50  0001 C CNN
F 3 "~" H 2500 1725 50  0001 C CNN
	1    2500 1725
	1    0    0    -1  
$EndComp
$Comp
L pspice:CAP C3
U 1 1 5F26E0DF
P 2925 1875
F 0 "C3" H 3103 1921 50  0000 L CNN
F 1 "100uF" H 3103 1830 50  0000 L CNN
F 2 "Capacitor_THT:CP_Radial_D8.0mm_P3.50mm" H 2925 1875 50  0001 C CNN
F 3 "~" H 2925 1875 50  0001 C CNN
	1    2925 1875
	1    0    0    -1  
$EndComp
Text GLabel 2425 1625 0    50   Input ~ 0
12-40v
Wire Wire Line
	2425 1625 2500 1625
Connection ~ 2500 1625
Wire Wire Line
	2500 1625 2925 1625
Wire Wire Line
	2925 1625 3400 1625
Connection ~ 2925 1625
Wire Wire Line
	2500 2125 2500 1825
Wire Wire Line
	2925 2125 2500 2125
$Comp
L Diode:1N5820 D1
U 1 1 5F272774
P 4750 1850
F 0 "D1" V 4704 1930 50  0000 L CNN
F 1 "MBR360" V 4795 1930 50  0000 L CNN
F 2 "Diode_THT:D_DO-201AD_P15.24mm_Horizontal" H 4750 1675 50  0001 C CNN
F 3 "https://www.onsemi.com/pub/Collateral/MBR350-D.PDF" H 4750 1850 50  0001 C CNN
	1    4750 1850
	0    1    1    0   
$EndComp
Text GLabel 2300 2125 0    50   UnSpc ~ 0
GND
Wire Wire Line
	2500 2125 2300 2125
Connection ~ 2500 2125
Wire Wire Line
	2925 2125 3575 2125
Wire Wire Line
	3575 2125 3575 2175
Connection ~ 2925 2125
Wire Wire Line
	3850 2175 3850 2125
Connection ~ 3850 2175
Wire Wire Line
	4150 2125 4150 2175
$Comp
L pspice:INDUCTOR L1
U 1 1 5F27D228
P 5000 1625
F 0 "L1" H 5000 1850 50  0000 C CNN
F 1 "68uH" H 5000 1775 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal" H 5000 1625 50  0001 C CNN
F 3 "~" H 5000 1625 50  0001 C CNN
	1    5000 1625
	1    0    0    -1  
$EndComp
Wire Wire Line
	4150 2175 4350 2175
Wire Wire Line
	4350 2175 4350 2000
Wire Wire Line
	4350 2000 4750 2000
Connection ~ 4150 2175
Wire Wire Line
	3575 2175 3700 2175
$Comp
L xl1509:XL1509 U1
U 1 1 5F28150C
P 3900 1725
F 0 "U1" H 3900 2192 50  0000 C CNN
F 1 "XL1509-ADJ" H 3900 2101 50  0000 C CNN
F 2 "Package_SO:SOIC-8-1EP_3.9x4.9mm_P1.27mm_EP2.29x3mm" V 4050 975 50  0001 C CNN
F 3 "https://datasheet.lcsc.com/szlcsc/XLSEMI-XL1509-5-0E1_C61063.pdf" V 4050 975 50  0001 C CNN
	1    3900 1725
	1    0    0    -1  
$EndComp
Connection ~ 3700 2175
Wire Wire Line
	3700 2175 3850 2175
Wire Wire Line
	4050 2175 4150 2175
Wire Wire Line
	4400 1625 4750 1625
Wire Wire Line
	4750 1700 4750 1625
Connection ~ 5625 1625
Wire Wire Line
	5625 1825 5625 2000
Wire Wire Line
	5250 1625 5625 1625
Connection ~ 4750 1625
Connection ~ 4750 2000
Wire Wire Line
	5625 1525 5625 1625
Text GLabel 6375 1625 2    50   Output ~ 0
5v
Wire Wire Line
	3850 2175 3950 2175
Connection ~ 4050 2175
Connection ~ 3950 2175
Wire Wire Line
	3950 2175 4050 2175
$Comp
L Device:CP1_Small polcap2
U 1 1 5F283170
P 5625 1725
F 0 "polcap2" H 5850 1600 50  0000 L CNN
F 1 "270uF/10v" H 5716 1680 50  0000 L CNN
F 2 "Capacitor_THT:CP_Radial_D8.0mm_P3.50mm" H 5625 1725 50  0001 C CNN
F 3 "~" H 5625 1725 50  0001 C CNN
	1    5625 1725
	1    0    0    -1  
$EndComp
$Comp
L Device:CP1_Small polcap3
U 1 1 5F2E20E3
P 7025 1600
F 0 "polcap3" H 7116 1646 50  0000 L CNN
F 1 "470uF" H 7116 1555 50  0000 L CNN
F 2 "Capacitor_THT:CP_Radial_D8.0mm_P3.50mm" H 7025 1600 50  0001 C CNN
F 3 "~" H 7025 1600 50  0001 C CNN
	1    7025 1600
	1    0    0    -1  
$EndComp
$Comp
L pspice:CAP C4
U 1 1 5F2E20E9
P 7450 1750
F 0 "C4" H 7628 1796 50  0000 L CNN
F 1 "100uF" H 7628 1705 50  0000 L CNN
F 2 "Capacitor_THT:CP_Radial_D8.0mm_P3.50mm" H 7450 1750 50  0001 C CNN
F 3 "~" H 7450 1750 50  0001 C CNN
	1    7450 1750
	1    0    0    -1  
$EndComp
Text GLabel 6950 1500 0    50   Input ~ 0
12-40v
Wire Wire Line
	6950 1500 7025 1500
Connection ~ 7025 1500
Wire Wire Line
	7025 1500 7450 1500
Wire Wire Line
	7450 1500 7925 1500
Connection ~ 7450 1500
Wire Wire Line
	7025 2000 7025 1700
Wire Wire Line
	7450 2000 7025 2000
$Comp
L Diode:1N5820 D2
U 1 1 5F2E20F7
P 9275 1725
F 0 "D2" V 9229 1805 50  0000 L CNN
F 1 "MBR360" V 9320 1805 50  0000 L CNN
F 2 "Diode_THT:D_DO-201AD_P15.24mm_Horizontal" H 9275 1550 50  0001 C CNN
F 3 "https://www.onsemi.com/pub/Collateral/MBR350-D.PDF" H 9275 1725 50  0001 C CNN
	1    9275 1725
	0    1    1    0   
$EndComp
Text GLabel 6825 2000 0    50   UnSpc ~ 0
GND
Wire Wire Line
	7025 2000 6825 2000
Connection ~ 7025 2000
Wire Wire Line
	7450 2000 8100 2000
Wire Wire Line
	8100 2000 8100 2050
Connection ~ 7450 2000
Wire Wire Line
	8375 2050 8375 2000
Connection ~ 8375 2050
Wire Wire Line
	8675 2000 8675 2050
$Comp
L pspice:INDUCTOR L2
U 1 1 5F2E2106
P 9525 1500
F 0 "L2" H 9525 1725 50  0000 C CNN
F 1 "68uH" H 9525 1650 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal" H 9525 1500 50  0001 C CNN
F 3 "~" H 9525 1500 50  0001 C CNN
	1    9525 1500
	1    0    0    -1  
$EndComp
Wire Wire Line
	8675 2050 8875 2050
Wire Wire Line
	8875 2050 8875 1875
Wire Wire Line
	8875 1875 9275 1875
Connection ~ 8675 2050
Wire Wire Line
	8925 1500 9275 1500
Wire Wire Line
	9275 1575 9275 1500
Connection ~ 10150 1500
Wire Wire Line
	10150 1700 10150 1875
Connection ~ 10150 1875
Wire Wire Line
	10150 1875 10450 1875
Wire Wire Line
	9775 1500 10150 1500
Connection ~ 9275 1500
Wire Wire Line
	9275 1875 10150 1875
Connection ~ 9275 1875
Wire Wire Line
	10150 1400 10150 1500
Text GLabel 10450 1875 2    50   UnSpc ~ 0
GND
$Comp
L Device:CP1_Small polcap4
U 1 1 5F2E212D
P 10150 1600
F 0 "polcap4" H 10241 1646 50  0000 L CNN
F 1 "390uF/6.3v" H 10241 1555 50  0000 L CNN
F 2 "Capacitor_THT:CP_Radial_D8.0mm_P3.50mm" H 10150 1600 50  0001 C CNN
F 3 "~" H 10150 1600 50  0001 C CNN
	1    10150 1600
	1    0    0    -1  
$EndComp
$Comp
L Device:R R4
U 1 1 5F2E5CA7
P 10150 1250
F 0 "R4" H 10220 1296 50  0000 L CNN
F 1 "2.3k" H 10220 1205 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0309_L9.0mm_D3.2mm_P12.70mm_Horizontal" V 10080 1250 50  0001 C CNN
F 3 "~" H 10150 1250 50  0001 C CNN
	1    10150 1250
	-1   0    0    -1  
$EndComp
$Comp
L Device:R R2
U 1 1 5F2E5E3E
P 10150 950
F 0 "R2" H 10220 996 50  0000 L CNN
F 1 "1k" H 10220 905 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0309_L9.0mm_D3.2mm_P12.70mm_Horizontal" V 10080 950 50  0001 C CNN
F 3 "~" H 10150 950 50  0001 C CNN
	1    10150 950 
	1    0    0    -1  
$EndComp
Text GLabel 10150 800  1    50   Input ~ 0
GND
$Comp
L Device:C C2
U 1 1 5F2FA770
P 10300 1250
F 0 "C2" H 10415 1296 50  0000 L CNN
F 1 "3.3n" H 10415 1205 50  0000 L CNN
F 2 "Capacitor_THT:C_Disc_D4.3mm_W1.9mm_P5.00mm" H 10338 1100 50  0001 C CNN
F 3 "~" H 10300 1250 50  0001 C CNN
	1    10300 1250
	1    0    0    -1  
$EndComp
Wire Wire Line
	8925 1400 9850 1400
Wire Wire Line
	9850 1400 9850 1100
Wire Wire Line
	9850 1100 10150 1100
Connection ~ 10150 1100
Wire Wire Line
	10150 1100 10300 1100
Wire Wire Line
	10300 1400 10300 1500
Wire Wire Line
	10150 1500 10300 1500
Connection ~ 10300 1500
Wire Wire Line
	10300 1500 10525 1500
Text GLabel 10525 1500 2    50   Output ~ 0
4v
Text GLabel 6375 2000 2    50   UnSpc ~ 0
GND
Wire Wire Line
	4750 2000 5625 2000
$Comp
L Device:LED D3
U 1 1 5F441DF2
P 925 2000
F 0 "D3" V 872 2080 50  0000 L CNN
F 1 "LED" V 963 2080 50  0000 L CNN
F 2 "LED_THT:LED_D5.0mm" H 925 2000 50  0001 C CNN
F 3 "~" H 925 2000 50  0001 C CNN
	1    925  2000
	1    0    0    -1  
$EndComp
$Comp
L Device:LED D4
U 1 1 5F44C430
P 925 2275
F 0 "D4" V 872 2355 50  0000 L CNN
F 1 "LED" V 963 2355 50  0000 L CNN
F 2 "LED_THT:LED_D5.0mm" H 925 2275 50  0001 C CNN
F 3 "~" H 925 2275 50  0001 C CNN
	1    925  2275
	1    0    0    -1  
$EndComp
$Comp
L Device:LED D5
U 1 1 5F44FA2D
P 925 2550
F 0 "D5" V 872 2630 50  0000 L CNN
F 1 "LED" V 963 2630 50  0000 L CNN
F 2 "LED_THT:LED_D5.0mm" H 925 2550 50  0001 C CNN
F 3 "~" H 925 2550 50  0001 C CNN
	1    925  2550
	1    0    0    -1  
$EndComp
Wire Wire Line
	775  2000 775  2275
Connection ~ 775  2275
Wire Wire Line
	775  2275 775  2550
Text GLabel 700  2275 0    50   UnSpc ~ 0
GND
Wire Wire Line
	775  2275 700  2275
Text GLabel 1375 2550 2    50   Input ~ 0
NETWORK_ERROR
Text GLabel 1375 2275 2    50   Input ~ 0
SIM_CARD_ERROR
Text GLabel 1375 2000 2    50   Input ~ 0
200OK
$Comp
L Device:R R7
U 1 1 5F44FA27
P 1225 2550
F 0 "R7" H 1050 2600 50  0000 L CNN
F 1 "330" H 1025 2500 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0309_L9.0mm_D3.2mm_P12.70mm_Horizontal" V 1155 2550 50  0001 C CNN
F 3 "~" H 1225 2550 50  0001 C CNN
	1    1225 2550
	0    1    1    0   
$EndComp
$Comp
L Device:R R6
U 1 1 5F44C42A
P 1225 2275
F 0 "R6" H 1050 2325 50  0000 L CNN
F 1 "330" H 1025 2225 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0309_L9.0mm_D3.2mm_P12.70mm_Horizontal" V 1155 2275 50  0001 C CNN
F 3 "~" H 1225 2275 50  0001 C CNN
	1    1225 2275
	0    1    1    0   
$EndComp
$Comp
L Device:R R5
U 1 1 5F44142A
P 1225 2000
F 0 "R5" H 1050 2050 50  0000 L CNN
F 1 "330" H 1025 1950 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0309_L9.0mm_D3.2mm_P12.70mm_Horizontal" V 1155 2000 50  0001 C CNN
F 3 "~" H 1225 2000 50  0001 C CNN
	1    1225 2000
	0    1    1    0   
$EndComp
$Comp
L Device:R R3
U 1 1 5F52D8A2
P 5625 1375
F 0 "R3" H 5695 1421 50  0000 L CNN
F 1 "320" H 5695 1330 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0309_L9.0mm_D3.2mm_P12.70mm_Horizontal" V 5555 1375 50  0001 C CNN
F 3 "~" H 5625 1375 50  0001 C CNN
	1    5625 1375
	-1   0    0    -1  
$EndComp
$Comp
L Device:R R1
U 1 1 5F52D8A8
P 5625 1075
F 0 "R1" H 5695 1121 50  0000 L CNN
F 1 "1k" H 5695 1030 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0309_L9.0mm_D3.2mm_P12.70mm_Horizontal" V 5555 1075 50  0001 C CNN
F 3 "~" H 5625 1075 50  0001 C CNN
	1    5625 1075
	1    0    0    -1  
$EndComp
Text GLabel 5625 925  1    50   Input ~ 0
GND
$Comp
L Device:C C1
U 1 1 5F52D8AF
P 5775 1375
F 0 "C1" H 5890 1421 50  0000 L CNN
F 1 "3.3n" H 5890 1330 50  0000 L CNN
F 2 "Capacitor_THT:C_Disc_D4.3mm_W1.9mm_P5.00mm" H 5813 1225 50  0001 C CNN
F 3 "~" H 5775 1375 50  0001 C CNN
	1    5775 1375
	1    0    0    -1  
$EndComp
Wire Wire Line
	4400 1525 5325 1525
Wire Wire Line
	5325 1525 5325 1225
Wire Wire Line
	5325 1225 5625 1225
Connection ~ 5625 1225
Wire Wire Line
	5625 1225 5775 1225
Wire Wire Line
	5775 1525 5775 1625
Wire Wire Line
	5775 1625 5625 1625
Connection ~ 5625 2000
Text GLabel 2525 5750 3    50   UnSpc ~ 0
GND
Wire Wire Line
	3500 5150 3500 4450
Wire Wire Line
	3500 4450 3125 4450
Wire Wire Line
	3600 5250 3600 4350
Wire Wire Line
	3600 4350 3125 4350
Wire Wire Line
	3975 5850 3975 5750
$Comp
L Device:R R16
U 1 1 5F2F550D
P 3700 5700
F 0 "R16" H 3500 5775 50  0000 L CNN
F 1 "10k" H 3475 5650 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0309_L9.0mm_D3.2mm_P12.70mm_Horizontal" V 3630 5700 50  0001 C CNN
F 3 "~" H 3700 5700 50  0001 C CNN
	1    3700 5700
	1    0    0    -1  
$EndComp
Text GLabel 4200 4650 1    50   Input ~ 0
5v
Text GLabel 4200 5750 3    50   UnSpc ~ 0
GND
$Comp
L Interface_CAN_LIN:MCP2551-I-SN U5
U 1 1 5F2661D2
P 4200 5350
F 0 "U5" H 4000 5775 50  0000 C CNN
F 1 "MCP2551-I-SN" H 4575 5775 50  0000 C CNN
F 2 "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" H 4200 4850 50  0001 C CIN
F 3 "http://ww1.microchip.com/downloads/en/devicedoc/21667d.pdf" H 4200 5350 50  0001 C CNN
	1    4200 5350
	1    0    0    -1  
$EndComp
Wire Wire Line
	3975 5750 4200 5750
Wire Wire Line
	3700 5850 3975 5850
Wire Wire Line
	3125 5550 3275 5550
$Comp
L Device:R R15
U 1 1 5F381376
P 3275 5400
F 0 "R15" H 3350 5475 50  0000 L CNN
F 1 "10k" H 3350 5350 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0309_L9.0mm_D3.2mm_P12.70mm_Horizontal" V 3205 5400 50  0001 C CNN
F 3 "~" H 3275 5400 50  0001 C CNN
	1    3275 5400
	1    0    0    -1  
$EndComp
Text GLabel 3275 5250 1    50   Input ~ 0
5v
$Comp
L Device:Crystal_Small Y1
U 1 1 5F3C8002
P 1775 6175
F 0 "Y1" H 1775 6425 50  0000 C CNN
F 1 "8mhz" H 1775 6325 50  0000 C CNN
F 2 "Crystal:Crystal_HC18-U_Vertical" H 1775 6175 50  0001 C CNN
F 3 "~" H 1775 6175 50  0001 C CNN
	1    1775 6175
	1    0    0    -1  
$EndComp
Wire Wire Line
	1925 5150 1675 5150
Wire Wire Line
	1675 5150 1675 6175
Wire Wire Line
	1925 5250 1875 5250
Wire Wire Line
	1875 5250 1875 6175
Wire Wire Line
	1875 6175 1975 6175
Wire Wire Line
	1975 6175 1975 6450
Connection ~ 1875 6175
Wire Wire Line
	1575 6175 1575 6450
Wire Wire Line
	1675 6175 1575 6175
Connection ~ 1675 6175
$Comp
L Device:C C13
U 1 1 5F42353E
P 1975 6600
F 0 "C13" H 2090 6646 50  0000 L CNN
F 1 "27pF" H 2090 6555 50  0000 L CNN
F 2 "Capacitor_THT:C_Disc_D4.3mm_W1.9mm_P5.00mm" H 2013 6450 50  0001 C CNN
F 3 "~" H 1975 6600 50  0001 C CNN
	1    1975 6600
	1    0    0    -1  
$EndComp
$Comp
L Device:C C12
U 1 1 5F423AE3
P 1575 6600
F 0 "C12" H 1690 6646 50  0000 L CNN
F 1 "27pF" H 1690 6555 50  0000 L CNN
F 2 "Capacitor_THT:C_Disc_D4.3mm_W1.9mm_P5.00mm" H 1613 6450 50  0001 C CNN
F 3 "~" H 1575 6600 50  0001 C CNN
	1    1575 6600
	1    0    0    -1  
$EndComp
Wire Wire Line
	1575 6750 1975 6750
Text GLabel 1775 6750 3    50   UnSpc ~ 0
GND
Wire Wire Line
	3500 5150 3700 5150
Wire Wire Line
	3700 5250 3600 5250
Text GLabel 1325 4350 0    50   Input ~ 0
SPI_MOSI
Text GLabel 1325 4450 0    50   Input ~ 0
SPI_MOSI
Text GLabel 1325 4550 0    50   Input ~ 0
SPI_NSS
Text GLabel 1325 4650 0    50   Input ~ 0
SPI_CSK
$Comp
L Device:C C11
U 1 1 5F5351A3
P 4050 4650
F 0 "C11" H 3750 4600 50  0000 L CNN
F 1 "5nF" H 3750 4700 50  0000 L CNN
F 2 "Capacitor_THT:C_Disc_D4.3mm_W1.9mm_P5.00mm" H 4088 4500 50  0001 C CNN
F 3 "~" H 4050 4650 50  0001 C CNN
	1    4050 4650
	0    1    1    0   
$EndComp
Text GLabel 2525 3850 1    50   Input ~ 0
5v
$Comp
L Device:C C5
U 1 1 5F535FAB
P 2375 3850
F 0 "C5" H 2100 3825 50  0000 L CNN
F 1 "5nF" H 2075 3925 50  0000 L CNN
F 2 "Capacitor_THT:C_Disc_D4.3mm_W1.9mm_P5.00mm" H 2413 3700 50  0001 C CNN
F 3 "~" H 2375 3850 50  0001 C CNN
	1    2375 3850
	0    1    1    0   
$EndComp
Wire Wire Line
	4200 4650 4200 4950
Wire Wire Line
	2525 3850 2525 4150
Text GLabel 3900 4650 0    50   UnSpc ~ 0
GND
Text GLabel 2225 3850 0    50   UnSpc ~ 0
GND
$Comp
L Connector:Conn_01x02_Male J6
U 1 1 5F2F1289
P 6225 1425
F 0 "J6" V 6287 1469 50  0001 L CNN
F 1 "Conn_01x02_Male" V 6378 1469 50  0001 L CNN
F 2 "Connector_PinHeader_1.00mm:PinHeader_1x02_P1.00mm_Vertical" H 6225 1425 50  0001 C CNN
F 3 "~" H 6225 1425 50  0001 C CNN
	1    6225 1425
	0    1    1    0   
$EndComp
Wire Wire Line
	6225 1625 6375 1625
Wire Wire Line
	6125 1625 5775 1625
Connection ~ 5775 1625
$Comp
L Connector:Conn_01x02_Male J7
U 1 1 5F3010C0
P 6225 1800
F 0 "J7" V 6287 1844 50  0001 L CNN
F 1 "Conn_01x02_Male" V 6378 1844 50  0001 L CNN
F 2 "Connector_PinHeader_1.00mm:PinHeader_1x02_P1.00mm_Vertical" H 6225 1800 50  0001 C CNN
F 3 "~" H 6225 1800 50  0001 C CNN
	1    6225 1800
	0    1    1    0   
$EndComp
Wire Wire Line
	6225 2000 6375 2000
Wire Wire Line
	5625 2000 6125 2000
$Comp
L Connector:Conn_01x02_Male J8
U 1 1 5F31A9DF
P 1625 4150
F 0 "J8" V 1687 4194 50  0001 L CNN
F 1 "Conn_01x02_Male" V 1778 4194 50  0001 L CNN
F 2 "Connector_PinHeader_1.00mm:PinHeader_1x02_P1.00mm_Vertical" H 1625 4150 50  0001 C CNN
F 3 "~" H 1625 4150 50  0001 C CNN
	1    1625 4150
	0    1    1    0   
$EndComp
$Comp
L Connector:Conn_01x02_Male J9
U 1 1 5F32827E
P 1625 4250
F 0 "J9" V 1687 4294 50  0001 L CNN
F 1 "Conn_01x02_Male" V 1778 4294 50  0001 L CNN
F 2 "Connector_PinHeader_1.00mm:PinHeader_1x02_P1.00mm_Vertical" H 1625 4250 50  0001 C CNN
F 3 "~" H 1625 4250 50  0001 C CNN
	1    1625 4250
	0    1    1    0   
$EndComp
Wire Wire Line
	1525 4350 1325 4350
Wire Wire Line
	1625 4350 1925 4350
Wire Wire Line
	1525 4450 1325 4450
Wire Wire Line
	1625 4450 1925 4450
$Comp
L Connector:Conn_01x02_Male J10
U 1 1 5F349CCE
P 1625 4350
F 0 "J10" V 1687 4394 50  0001 L CNN
F 1 "Conn_01x02_Male" V 1778 4394 50  0001 L CNN
F 2 "Connector_PinHeader_1.00mm:PinHeader_1x02_P1.00mm_Vertical" H 1625 4350 50  0001 C CNN
F 3 "~" H 1625 4350 50  0001 C CNN
	1    1625 4350
	0    1    1    0   
$EndComp
Wire Wire Line
	1925 4550 1625 4550
Wire Wire Line
	1525 4550 1325 4550
$Comp
L Connector:Conn_01x02_Male J11
U 1 1 5F35F3A1
P 1625 4450
F 0 "J11" V 1687 4494 50  0001 L CNN
F 1 "Conn_01x02_Male" V 1778 4494 50  0001 L CNN
F 2 "Connector_PinHeader_1.00mm:PinHeader_1x02_P1.00mm_Vertical" H 1625 4450 50  0001 C CNN
F 3 "~" H 1625 4450 50  0001 C CNN
	1    1625 4450
	0    1    1    0   
$EndComp
Wire Wire Line
	1925 4650 1625 4650
Wire Wire Line
	1525 4650 1325 4650
$Comp
L xl1509:XL1509 U10
U 1 1 5F57E02E
P 8425 1600
F 0 "U10" H 8425 2067 50  0000 C CNN
F 1 "XL1509-ADJ" H 8425 1976 50  0000 C CNN
F 2 "Package_SO:SOIC-8-1EP_3.9x4.9mm_P1.27mm_EP2.29x3mm" V 8575 850 50  0001 C CNN
F 3 "https://datasheet.lcsc.com/szlcsc/XLSEMI-XL1509-5-0E1_C61063.pdf" V 8575 850 50  0001 C CNN
	1    8425 1600
	1    0    0    -1  
$EndComp
Wire Wire Line
	8375 2050 8475 2050
Wire Wire Line
	8575 2050 8675 2050
Wire Wire Line
	8100 2050 8225 2050
Connection ~ 8225 2050
Wire Wire Line
	8225 2050 8375 2050
Wire Wire Line
	8475 2050 8575 2050
Connection ~ 8475 2050
Connection ~ 8575 2050
Text GLabel 6550 3025 0    50   Input ~ 0
STM-SIM8xx_BridgeTX
Wire Wire Line
	7175 3125 7700 3125
Text GLabel 6650 2725 1    50   UnSpc ~ 0
GND
Wire Wire Line
	6650 3025 6875 3025
Connection ~ 6650 3025
Wire Wire Line
	6550 3025 6650 3025
$Comp
L Device:R R8
U 1 1 5F2B40A9
P 6650 2875
F 0 "R8" H 6720 2921 50  0000 L CNN
F 1 "5.6k" H 6720 2830 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0309_L9.0mm_D3.2mm_P12.70mm_Horizontal" V 6580 2875 50  0001 C CNN
F 3 "~" H 6650 2875 50  0001 C CNN
	1    6650 2875
	1    0    0    -1  
$EndComp
Wire Wire Line
	7700 3025 7175 3025
$Comp
L Device:R R9
U 1 1 5F2A2985
P 7025 3025
F 0 "R9" V 6818 3025 50  0000 C CNN
F 1 "1k" V 6909 3025 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0309_L9.0mm_D3.2mm_P12.70mm_Horizontal" V 6955 3025 50  0001 C CNN
F 3 "~" H 7025 3025 50  0001 C CNN
	1    7025 3025
	0    1    1    0   
$EndComp
Text GLabel 7175 3125 0    50   Output ~ 0
STM-SIM8xx_BridgeRX
Text GLabel 7700 2925 0    50   Input ~ 0
RESET_PIN
Text GLabel 7700 2825 0    50   Input ~ 0
4v
Text GLabel 7700 3225 0    50   UnSpc ~ 0
GND
$Comp
L Connector:Conn_01x02_Male J13
U 1 1 5F2CC3E4
P 8750 5225
F 0 "J13" V 8812 5269 50  0001 L CNN
F 1 "Conn_01x02_Male" V 8903 5269 50  0001 L CNN
F 2 "Connector_PinHeader_1.00mm:PinHeader_1x02_P1.00mm_Vertical" H 8750 5225 50  0001 C CNN
F 3 "~" H 8750 5225 50  0001 C CNN
	1    8750 5225
	0    1    1    0   
$EndComp
Wire Wire Line
	8200 5425 8650 5425
Wire Wire Line
	8975 5425 8750 5425
Wire Wire Line
	8175 5325 8650 5325
Wire Wire Line
	8975 5325 8750 5325
$Comp
L Connector:Conn_01x02_Male J12
U 1 1 5F2BDFEB
P 8750 5125
F 0 "J12" V 8812 5169 50  0001 L CNN
F 1 "Conn_01x02_Male" V 8903 5169 50  0001 L CNN
F 2 "Connector_PinHeader_1.00mm:PinHeader_1x02_P1.00mm_Vertical" H 8750 5125 50  0001 C CNN
F 3 "~" H 8750 5125 50  0001 C CNN
	1    8750 5125
	0    1    1    0   
$EndComp
Text GLabel 5350 3900 0    50   Input ~ 0
5v
Text GLabel 8150 5225 2    50   Output ~ 0
SPI_MOSI
Text GLabel 8150 5125 2    50   Output ~ 0
SPI_MISO
Text GLabel 8150 5025 2    50   Output ~ 0
SPI_CSK
Text GLabel 8150 4925 2    50   Output ~ 0
SPI_NSS
Text GLabel 8150 4625 2    50   Output ~ 0
NETWORK_ERROR
Text GLabel 8150 4725 2    50   Output ~ 0
SIM_CARD_ERROR
$Comp
L Device:R R12
U 1 1 5F4C561A
P 9650 4675
F 0 "R12" H 9450 4600 50  0000 L CNN
F 1 "100k" H 9450 4475 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0309_L9.0mm_D3.2mm_P12.70mm_Horizontal" V 9580 4675 50  0001 C CNN
F 3 "~" H 9650 4675 50  0001 C CNN
	1    9650 4675
	1    0    0    -1  
$EndComp
Text GLabel 7150 5625 0    50   Output ~ 0
200OK
Wire Wire Line
	8150 4525 9650 4525
Text GLabel 5425 4200 0    50   UnSpc ~ 0
GND
Text GLabel 4700 5450 2    50   BiDi ~ 0
CAN-LOW
Text GLabel 4700 5250 2    50   BiDi ~ 0
CAN-HIGH
Connection ~ 9650 4525
Text GLabel 9875 4175 1    50   Input ~ 0
12-40v
Connection ~ 9875 4525
Wire Wire Line
	9875 4475 9875 4525
Wire Wire Line
	9650 4525 9875 4525
Text GLabel 9875 4825 3    50   UnSpc ~ 0
GND
Wire Wire Line
	9650 4825 9875 4825
$Comp
L Device:R R13
U 1 1 5F4C1E81
P 9875 4675
F 0 "R13" H 9945 4721 50  0000 L CNN
F 1 "22k" H 9945 4630 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0309_L9.0mm_D3.2mm_P12.70mm_Horizontal" V 9805 4675 50  0001 C CNN
F 3 "~" H 9875 4675 50  0001 C CNN
	1    9875 4675
	1    0    0    -1  
$EndComp
$Comp
L Device:R R10
U 1 1 5F4C15F0
P 9875 4325
F 0 "R10" H 9945 4371 50  0000 L CNN
F 1 "270k" H 9945 4280 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0309_L9.0mm_D3.2mm_P12.70mm_Horizontal" V 9805 4325 50  0001 C CNN
F 3 "~" H 9875 4325 50  0001 C CNN
	1    9875 4325
	1    0    0    -1  
$EndComp
Text GLabel 8975 5325 2    50   Output ~ 0
STM-SIM8xx_BridgeTX
Text GLabel 8150 4825 2    50   Output ~ 0
RESET_PIN
Connection ~ 5650 4200
Wire Wire Line
	5425 4200 5650 4200
Connection ~ 7650 4200
Wire Wire Line
	7650 4200 7650 4325
Connection ~ 5975 3900
Wire Wire Line
	5950 3900 5975 3900
Wire Wire Line
	6900 4200 7325 4200
Wire Wire Line
	6425 4200 6900 4200
Wire Wire Line
	7325 4200 7650 4200
Connection ~ 7325 4200
Connection ~ 6900 4200
Connection ~ 6425 4200
Wire Wire Line
	5975 4200 6425 4200
Connection ~ 5975 4200
Wire Wire Line
	5650 4200 5975 4200
$Comp
L Regulator_Linear:AMS1117-3.3 U2
U 1 1 5F3C655D
P 5650 3900
F 0 "U2" H 5650 4142 50  0000 C CNN
F 1 "AMS1117-3.3" H 5650 4051 50  0000 C CNN
F 2 "Package_TO_SOT_SMD:SOT-223-3_TabPin2" H 5650 4100 50  0001 C CNN
F 3 "http://www.advanced-monolithic.com/pdf/ds1117.pdf" H 5750 3650 50  0001 C CNN
	1    5650 3900
	1    0    0    -1  
$EndComp
Wire Wire Line
	9000 6100 9075 6100
Wire Wire Line
	9000 5625 9000 6100
Wire Wire Line
	8150 5525 9075 5525
Wire Wire Line
	9075 5525 9075 6000
$Comp
L Connector:Conn_01x02_Male J5
U 1 1 5F2DFC4D
P 9275 6100
F 0 "J5" H 9383 6281 50  0000 C CNN
F 1 "SWD Debugging Interface" H 9383 6190 50  0000 C CNN
F 2 "Connector_PinHeader_1.00mm:PinHeader_1x02_P1.00mm_Vertical" H 9275 6100 50  0001 C CNN
F 3 "~" H 9275 6100 50  0001 C CNN
	1    9275 6100
	-1   0    0    1   
$EndComp
Wire Wire Line
	8200 6175 6700 6175
Connection ~ 8200 5425
Wire Wire Line
	8200 5425 8200 6175
Connection ~ 8175 5325
Wire Wire Line
	8175 5325 8175 6100
Wire Wire Line
	6600 6100 8175 6100
Wire Wire Line
	8150 5325 8175 5325
Wire Wire Line
	8150 5425 8200 5425
Text GLabel 8975 5425 2    50   Input ~ 0
STM-SIM8xx_BridgeRX
Wire Wire Line
	7325 3900 7650 3900
$Comp
L Device:C C10
U 1 1 5F2F40E3
P 7650 4050
F 0 "C10" H 7765 4096 50  0000 L CNN
F 1 "10uF" H 7765 4005 50  0000 L CNN
F 2 "Capacitor_THT:C_Disc_D4.3mm_W1.9mm_P5.00mm" H 7688 3900 50  0001 C CNN
F 3 "~" H 7650 4050 50  0001 C CNN
	1    7650 4050
	1    0    0    1   
$EndComp
Connection ~ 7325 3900
$Comp
L Device:C C9
U 1 1 5F2F3561
P 7325 4050
F 0 "C9" H 7440 4096 50  0000 L CNN
F 1 "1uF" H 7440 4005 50  0000 L CNN
F 2 "Capacitor_THT:C_Disc_D4.3mm_W1.9mm_P5.00mm" H 7363 3900 50  0001 C CNN
F 3 "~" H 7325 4050 50  0001 C CNN
	1    7325 4050
	1    0    0    1   
$EndComp
Wire Wire Line
	6900 3900 7325 3900
Wire Wire Line
	8150 5625 9000 5625
Wire Wire Line
	6700 5100 6500 5100
Wire Wire Line
	6700 6175 6700 5100
Wire Wire Line
	6600 5200 6500 5200
Wire Wire Line
	6600 6100 6600 5200
Wire Wire Line
	6850 5000 6850 5825
Connection ~ 6850 5000
Wire Wire Line
	6850 4725 6850 5000
Wire Wire Line
	6850 5000 6500 5000
Connection ~ 6850 5825
Wire Wire Line
	6500 5825 6500 5300
Wire Wire Line
	6850 5825 6500 5825
Wire Wire Line
	6700 4900 6500 4900
Wire Wire Line
	6700 4525 6700 4900
$Comp
L Connector:Conn_01x05_Male J4
U 1 1 5F2D262B
P 6300 5100
F 0 "J4" H 6408 5481 50  0000 C CNN
F 1 "Programming interface" H 6408 5390 50  0000 C CNN
F 2 "Connector_PinHeader_1.00mm:PinHeader_1x05_P1.00mm_Vertical" H 6300 5100 50  0001 C CNN
F 3 "~" H 6300 5100 50  0001 C CNN
	1    6300 5100
	1    0    0    -1  
$EndComp
Wire Wire Line
	6850 5825 7650 5825
Wire Wire Line
	6850 4525 6700 4525
Connection ~ 6850 4525
$Comp
L Device:R R14
U 1 1 5F2C9BE9
P 7000 4725
F 0 "R14" V 6793 4725 50  0000 C CNN
F 1 "6.8k" V 6884 4725 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0309_L9.0mm_D3.2mm_P12.70mm_Horizontal" V 6930 4725 50  0001 C CNN
F 3 "~" H 7000 4725 50  0001 C CNN
	1    7000 4725
	0    1    1    0   
$EndComp
Wire Wire Line
	7650 4375 7650 4325
Wire Wire Line
	6850 4375 7650 4375
Wire Wire Line
	6850 4525 6850 4375
$Comp
L Device:R R11
U 1 1 5F2C4135
P 7000 4525
F 0 "R11" V 6793 4525 50  0000 C CNN
F 1 "6.8k" V 6884 4525 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0309_L9.0mm_D3.2mm_P12.70mm_Horizontal" V 6930 4525 50  0001 C CNN
F 3 "~" H 7000 4525 50  0001 C CNN
	1    7000 4525
	0    1    1    0   
$EndComp
Text GLabel 7650 5825 2    50   UnSpc ~ 0
GND
Wire Wire Line
	7650 4325 7750 4325
Connection ~ 7650 4325
Wire Wire Line
	6425 3900 6900 3900
Connection ~ 6425 3900
$Comp
L MCU_ST_STM32F0:STM32F030F4Px U4
U 1 1 5F25C437
P 7650 5025
F 0 "U4" H 7650 4136 50  0000 C CNN
F 1 "STM32F030F4Px" H 7650 4045 50  0000 C CNN
F 2 "Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm" H 7250 4325 50  0001 R CNN
F 3 "http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00088500.pdf" H 7650 5025 50  0001 C CNN
	1    7650 5025
	1    0    0    -1  
$EndComp
Wire Wire Line
	7625 4325 7650 4325
$Comp
L Device:C C6
U 1 1 5F2AF9BD
P 5975 4050
F 0 "C6" H 6090 4096 50  0000 L CNN
F 1 "100nF" H 6090 4005 50  0000 L CNN
F 2 "Capacitor_THT:C_Disc_D4.3mm_W1.9mm_P5.00mm" H 6013 3900 50  0001 C CNN
F 3 "~" H 5975 4050 50  0001 C CNN
	1    5975 4050
	1    0    0    1   
$EndComp
$Comp
L Device:C C7
U 1 1 5F2B13E0
P 6425 4050
F 0 "C7" H 6540 4096 50  0000 L CNN
F 1 "100nF" H 6540 4005 50  0000 L CNN
F 2 "Capacitor_THT:C_Disc_D4.3mm_W1.9mm_P5.00mm" H 6463 3900 50  0001 C CNN
F 3 "~" H 6425 4050 50  0001 C CNN
	1    6425 4050
	1    0    0    1   
$EndComp
Wire Wire Line
	5975 3900 6425 3900
Connection ~ 6900 3900
$Comp
L Device:C C8
U 1 1 5F2AE9C9
P 6900 4050
F 0 "C8" H 7015 4096 50  0000 L CNN
F 1 "4.7uF" H 7015 4005 50  0000 L CNN
F 2 "Capacitor_THT:C_Disc_D4.3mm_W1.9mm_P5.00mm" H 6938 3900 50  0001 C CNN
F 3 "~" H 6900 4050 50  0001 C CNN
	1    6900 4050
	1    0    0    1   
$EndComp
$Comp
L Connector:Conn_01x06_Female J2
U 1 1 5F296694
P 7900 2925
F 0 "J2" H 7928 2901 50  0000 L CNN
F 1 "SIM800C Module" H 8050 2500 50  0000 L CNN
F 2 "Connector_PinHeader_1.27mm:PinHeader_1x06_P1.27mm_Vertical" H 7900 2925 50  0001 C CNN
F 3 "~" H 7900 2925 50  0001 C CNN
	1    7900 2925
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x06_Female J3
U 1 1 5F29668E
P 8950 2925
F 0 "J3" H 8978 2901 50  0000 L CNN
F 1 "SIM800C Module Side A" H 8978 2810 50  0001 L CNN
F 2 "Connector_PinHeader_1.27mm:PinHeader_1x06_P1.27mm_Vertical" H 8950 2925 50  0001 C CNN
F 3 "~" H 8950 2925 50  0001 C CNN
	1    8950 2925
	1    0    0    -1  
$EndComp
$EndSCHEMATC
