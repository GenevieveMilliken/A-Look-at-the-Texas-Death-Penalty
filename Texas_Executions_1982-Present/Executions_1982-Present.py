import urllib.request
from bs4 import BeautifulSoup
import csv
import time


def run():
    #  get the webpage with the prisoner data
    uri = 'http://www.tdcj.state.tx.us/death_row/dr_executed_offenders.html'

    f = csv.writer(open("Executions_1983-Present" + ".csv", "w", newline=''), dialect='excel')

    # Write column headers as the first line
    f.writerow(["Last Name", "First Name", "TDCJ Num", "Age", "Date", "Race", "County"])
    
    urllines = urllib.request.urlopen(uri)
    pagedat = urllines.read()
    urllines.close()
    soup = BeautifulSoup(pagedat)
    allrows = soup.find_all("tr")
    suburi = uri[:38]
    for row in allrows:
        tds = row.find_all("td")
        try: 
            LN = str(tds[3].get_text())
            FN = str(tds[4].get_text())
            TDCJ = str(tds[5].get_text())
            Age = str(tds[6].get_text())
            Date = str(tds[7].get_text())
            Race = str(tds[8].get_text())
            County = str(tds[9].get_text())
            print("good string")
        except Exception:
            print("bad string")
            time.sleep(.1)
            continue
        f.writerow([LN, FN, TDCJ, Age, Date, Race, County])

if __name__ == "__main__":
    run()
    print("job complete!")
