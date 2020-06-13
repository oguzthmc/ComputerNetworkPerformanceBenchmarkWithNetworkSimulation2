import os
import sys

import matplotlib.pyplot as plt


class TraceStringFormat:
    def __init__(self, line):
        self.event = line[0]
        self.time = float(line[1])
        self.fromNode = int(line[2])
        self.toNode = int(line[3])
        self.type = line[4]
        self.size = int(line[5])
        self.flags = FlagsFormat(line[6])
        self.flowID = int(line[7])
        self.source = line[8]
        self.destination = line[9]
        self.sequenceNumber = int(line[10])
        self.packetID = int(line[11])


class FlagsFormat:
    def __init__(self, flags):
        self.flag1 = flags[0]
        self.flag2 = flags[1]
        self.flag3 = flags[2]
        self.flag4 = flags[3]
        self.flag5 = flags[4]
        self.flag6 = flags[5]
        self.flag7 = flags[6]


traceList = []
with open('iz.tr', 'r') as inputFile:  # open file
    while True:
        line = inputFile.readline().strip('\n').split(' ')  # readline and split
        if (line == ['']):  # check end of file
            break
        traceString = TraceStringFormat(line)  # format line
        traceList.append(traceString)  # add formatted line to list

x, y = [], []
start_time, stop_time = [], []
total_duration = 0.0
received_packets = 0

for packet in traceList:
    try:
        if start_time[packet.packetID] == 0:
            start_time[packet.packetID] = packet.time
    except IndexError:
        start_time.insert(packet.packetID, packet.time)
    try:
        if packet.event == "r" and (packet.type == "tcp" or packet.type == "ack"):
            stop_time[packet.packetID] = packet.time
        else:
            stop_time[packet.packetID] = -1
    except IndexError:
        stop_time.insert(packet.packetID, packet.time)

for i in range(0, len(start_time)):
    packet_duration = stop_time[i] - start_time[i]
    if packet_duration > 0:
        total_duration += packet_duration
        received_packets += 1
        x.append(stop_time[i])
        y.append((total_duration/received_packets)*1000)


# plotting the points
plt.plot(x, y)

# naming the x axis
plt.xlabel('Zaman')
# naming the y axis
plt.ylabel('Uçtan Uca Gecikme (ms)')

# giving a title to my graph
plt.title('Uçtan Uca Gecikme Dağılımı (EED)')

# function to show the plot
plt.show()
