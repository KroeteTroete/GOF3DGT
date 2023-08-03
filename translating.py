import gof2translate as gt
import langdetect as ld
import sys
import time

data = ld.extractLang("gb.lang")

def translate(lowerBoundary):

    print(len(data))

    for i in data[lowerBoundary:]:
        currentIndex = data.index(i)
        print(currentIndex)
        try:
            translated = gt.breaktranslation(i)

            data[data.index(i)] = translated

            print(f"{i} replaced with {translated}")

        except Exception as e:

            print("Backing up .lang progress")
            ld.writeLang(data, "gb_modded.lang")
            print("Error occured at Index " + str(currentIndex) + " due to timeout. Waiting 1 minute to continue...")

            for remaining in range(60, 0, -1):
                sys.stdout.write("\r")
                sys.stdout.write("{:2d} seconds remaining.".format(remaining)) 
                sys.stdout.flush()
                time.sleep(1)

            translate(currentIndex)
            

    ld.writeLang(data, "gb_modded.lang")

translate(0)