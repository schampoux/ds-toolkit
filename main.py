

path = "/Users/spun/Documents/local-development/ds-toolkit/ingestion/data/raw/1d373a90-890d-4420-af40-262afc5dbf7b.xml"

from lxml import etree

def parse_drug_label(path: str):
    with open(path) as p:
        p

    parser = etree.XMLParser(recover=True) # recover = True to ignore errors from parsing invalid characters 
    root = etree.parse(data = p, parser = parser)

    # tree = et.parse(source = path, parser = parser)
    # root.tag
    # et.ElementTree(file=path)
    return print(root.tag)


def main():
    print("Running entry point for ds toolkit")
    parse_drug_label(path = path)

if __name__ == "__main__":
    main()
