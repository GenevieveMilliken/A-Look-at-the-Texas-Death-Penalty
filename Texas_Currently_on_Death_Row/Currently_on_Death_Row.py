import urllib.request
from bs4 import BeautifulSoup
import csv
import time


def run():
    #  get the webpage with the prisoner data
    uri = 'https://www.tdcj.state.tx.us/death_row/dr_offenders_on_dr.html'

    f = csv.writer(open("Currently_on_Death_Row" + ".csv", "w", newline=''), dialect='excel')

    #Write column headers as the first line
    f.writerow(["TDCJ Number", "Last Name", "First Name", "Date of Birth", "Race", "Date Received", "County", "Date of Offense"])

    urllines = urllib.request.urlopen(uri)
    pagedat = urllines.read()
    urllines.close()
    soup = BeautifulSoup(pagedat)
    allrows = soup.find_all("tr")
    suburi = uri[:38]
    for row in allrows:
        tds = row.find_all("td")
        try: 
            TDCJ = str(tds[0].get_text())
            LN = str(tds[2].get_text())
            FN = str(tds[3].get_text())
            DOB = str(tds[4].get_text())
            Race = str(tds[6].get_text())
            Received = str(tds[7].get_text())
            County = str(tds[8].get_text())
            Offense = str(tds[9].get_text())
            print("good string")
        except Exception:
            print("bad string")
            time.sleep(.1)
            continue
        f.writerow([TDCJ, LN, FN, DOB, Race, Received, County, Offense])

if __name__ == "__main__":        
    run()
    print("job complete!")

  
