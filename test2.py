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
total_sent_packets = 0
total_received_packets = 0

for packet in traceList:
    if packet.type == "tcp" or packet.type == "ack":
        if packet.event == "+":
            total_sent_packets += 1
        elif packet.event == "r":
            total_received_packets += 1
        x.append(packet.time)
        y.append(total_received_packets/total_sent_packets*100)

# plotting the points
plt.plot(x, y)

# naming the x axis
plt.xlabel('Zaman')
# naming the y axis
plt.ylabel('Paket Teslim Oranı (%)')

# giving a title to my graph
plt.title('Paket Teslim Oranı (PDF) Dağılımı')


# function to show the plot
plt.show()
