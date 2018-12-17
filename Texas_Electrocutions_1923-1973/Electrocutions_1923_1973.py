import urllib.request
from bs4 import BeautifulSoup
import csv
import time


def run():
    #  get the webpage with the prisoner data
    uri = 'https://www.tdcj.state.tx.us/death_row/dr_electrocutions_list_1923-1973.html'

    f = csv.writer(open("Electrocutions, 1923-1973" + ".csv", "w", newline=''), dialect='excel')

    #Write column headers as the first line
    f.writerow(["Last Name", "First Name", "TDCJ Number", "Age at Execution", "Date_Execution", "Race", "County"])

    urllines = urllib.request.urlopen(uri)
    pagedat = urllines.read()
    urllines.close()
    soup = BeautifulSoup(pagedat)
    allrows = soup.find_all("tr")
    suburi = uri[:38]
    for row in allrows:
        tds = row.find_all("td")
        try: 
            LN = str(tds[0].get_text())
            FN = str(tds[1].get_text())
            TDCJ = str(tds[2].get_text())
            Age_Execution = str(tds[3].get_text())
            Date_Execution = str(tds[4].get_text())
            Race = str(tds[5].get_text())
            County = str(tds[6].get_text())
            print("good string")
        except Exception:
            print("bad string")
            time.sleep(.1)
            continue
        f.writerow([LN, FN, TDCJ, Age_Execution, Date_Execution, Race, County])

if __name__ == "__main__":        
    run()
    print("job complete!")
