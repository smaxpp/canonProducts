import requests
from bs4 import BeautifulSoup
from bs4 import element
import pandas as pd
import re
def testConvert(s):
    s2 = re.sub('[$,]', '', s)
    # print(s2)
    f = float(s2)
    # print(f)
    return f

def main():
    # loadAndStoreRawHTML()

    # create soup and analyze
    soup = BeautifulSoup(open('lensList/canonLens.txt'), "html.parser")
    rows = soup.find_all("tr")
    resultDictList = [extractLensDataFromRow(r) for r in rows]
    df = pd.DataFrame(resultDictList)

    # delete header
    df = df[1:]

    # calculate brand
    df['brand'] = df.apply(lambda x: x['lensName'].strip().split(' ')[0], axis=1)

    # calculate price for each lens
    df['price2'] = df.apply(lambda x: testConvert(x['price'].split(' ')[0].rstrip('+')) if x['price'][0] == '$' else 0.0, axis=1)

    # delete extender lens
    df = df[~df['lensName'].str.contains('Extender')]

    # calculate min & max
    df['min'] = df['min'].apply(lambda x: float(x.split(' ')[0]))
    df['max'] = df['max'].apply(lambda x: float(x.split(' ')[0]))

    # calculate prime or zoom
    df['type'] = df.apply(lambda x: 'Prime' if x['min']==x['max'] else 'zoom', axis=1)
    # print(df)
    print(df.info())

    df.to_csv('lensList/lens.csv')



def extractLensDataFromRow(r1):
    columns = r1.contents
    result = {}
    for c in columns:
        if(type(c) == element.Tag):
            if (c['class'][0] == 'column-1'):
                result['lensName'] = c.text
            elif (c['class'][0] == 'column-2'):
                result['min'] = c.text
            elif (c['class'][0] == 'column-3'):
                result['max'] = c.text
            elif (c['class'][0] == 'column-4'):
                result['aperture'] = c.text
            else:
                if(len(c.contents)==1):
                    result['price'] = c.text
                else:
                    result['price'] = str(c.contents[0])
    return result


def loadAndStoreRawHTML():
    lensPageLink = r'http://www.lightandmatter.org/2012/lens-recommendations/canon-lens-recommendations/complete-canon-lens-list/'
    r = requests.get(lensPageLink)
    with open("lensList/canonLens.txt", "a+") as f:
        f.write(r.text)




if __name__ == '__main__':
    main()