print("Configuring a single router on Cisco Packet Tracer. Simplified." + "\n"
      + "Basically answer all the questions and the program will prepare a script you have to type in the router to "
        "get desired configuration." + "\n" +
      "Make sure you are typing the data correctly. There's no error-catching as of yet." + "\n"
                                                                                            "Let's start!")

hostname = input("what's the name of the router")
if hostname == "":
    hostname = 'Mr.router'

numberofsubnets = int(input("how many local subnetworks are connected to the router?"))

while numberofsubnets <= 0:
  numberofSubnets = int(input("Type a correct number of local subnetworks."))
print("Number of subnets is " + str(numberofsubnets))

interfacesDictionary = {}
for i in range(numberofsubnets):
  interfaceIP = input("Type IP address of your " + str(i + 1) + " subnet: ")
  interfaceName = input("Type what interface will the subnet be assigned to: ")
  interfacesDictionary[interfaceName] = interfaceIP
  print("The IP address of your " + str(i + 1) + " subnet is: " + interfaceIP)
  print("The assigned interface: " + interfaceName)

defaultGateway = str(input(
  "Do you want the router to have default ip as .254 in the subnets or you prefer custom ones? Type either "
  "'default' or 'custom'."))

while defaultGateway != "Default" and defaultGateway != "custom":
    defaultGateway = input("Wrong answer! Type either 'Default' or 'custom'!")

print(defaultGateway)
