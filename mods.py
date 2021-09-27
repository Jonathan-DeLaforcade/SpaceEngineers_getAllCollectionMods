import requests
import re
url = "https://steamcommunity.com/sharedfiles/filedetails/?id=2001355838"

req = requests.get(url)
text = req.text.split("\n")
file = open("out.txt","w")

nbmods = 0

for line in text:
    
    if line.find("SharedFileBindMouseHover") > 0:
        nbmods += 1
        modID = ""
        modName = ""
        regName = '"title":"(.{0,75})",'
        regID = '"id":"(.{0,10})",'
        matchname = re.findall(regName,line)
        matchID = re.findall(regID,line)
        if len(matchname) > 0:
            modName = matchname[0]

        if len(matchID) > 0:
            modID = matchID[0]

        file.write(f"{modName}\n")
        #file.write(f"    <ModItem FriendlyName=\"{modName}\">\n")
        #file.write(f"      <Name>{modName}.sbm</Name>\n")
        #file.write(f"      <PublishedFileId>{modID}</PublishedFileId>\n")
        #file.write(f"      <PublishedServiceName>Steam</PublishedServiceName>\n")
        #file.write(f"    </ModItem>\n")
        print(f"Mod: {modName}")
print(f"Done => {nbmods}")
