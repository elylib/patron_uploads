import argparse
import csv
import re
from collections import namedtuple
import datetime


# OCLC requires these 46 field names in this order to accept a patron upload
OCLCRecord = namedtuple('OCLCRecord', 'prefix givenName middleName familyName suffix nickname canSelfEdit dateOfBirth '
                                      'gender institutionId barcode idAtSource sourceSystem borrowerCategory '
                                      'circRegistrationDate oclcExpirationDate homeBranch primaryStreetAddressLine1 '
                                      'primaryStreetAddressLine2 primaryCityOrLocality primaryStateOrProvince '
                                      'primaryPostalCode primaryCountry primaryPhone secondaryStreetAddressLine1 '
                                      'secondaryStreetAddressLine2 secondaryCityOrLocality secondaryStateOrProvince '
                                      'secondaryPostalCode secondaryCountry secondaryPhone emailAddress mobilePhone '
                                      'notificationEmail notificationTextPhone patronNotes photoURL customdata1 '
                                      'customdata2 customdata3 customdata4 username illId illApprovalStatus '
                                      'illPatronType illPickupLocation')

# Small metaprogramming black magic. Lets us initialize an OCLC Record with the Banner subset, and not worry about
# not immediately (or ever) setting other fields.
OCLCRecord.__new__.__defaults__ = (None,) * len(OCLCRecord._fields)

# The record output by banner. The only difference is oclcExpirationDate is circExpirationDate in the file.
# OCLC changed this field, so we make the change here until Banner is updated.
BannerRecord = namedtuple('BannerRecord', 'givenName familyName dateOfBirth gender institutionId barcode idAtSource '
                                          'sourceSystem borrowerCategory oclcExpirationDate homeBranch '
                                          'primaryStreetAddressLine1 primaryStreetAddressLine2 primaryCityOrLocality '
                                          'primaryStateOrProvince primaryPostalCode primaryCountry primaryPhone '
                                          'secondaryStreetAddressLine1 secondaryStreetAddressLine2 '
                                          'secondaryCityOrLocality secondaryStateOrProvince secondaryPostalCode '
                                          'secondaryCountry secondaryPhone emailAddress mobilePhone patronNotes')

date_regex = re.compile('^\d+-\d+-\d+$')


class Duplicate(Exception):
    def __str__(self):
        return "This student has already been seen."

seen = set()


def banner_to_oclc(csv_row):
    """
    Move data from a Banner tsv row to an OCLCRecord.

    Make the tsv row from Banner by unpacking (*) the list of fields. Then convert that to a dict and unpack it (**)
    into an OCLCRecord namedtuple. This unpacking allows us to map the fields that already exist in the Banner report
    directly to the same-named fields in OCLCRecord. This is why we changed the name of circExpirationDate so this
    would map with errors.

    :param csv_row: Row of fields from the Banner tsv file.
    :return: An OCLCRecord namedtuple with the fields mapped from the Banner fields.
    :raise: Duplicate if we've already seen this one.
    """
    banner = BannerRecord(*csv_row)

    if banner.idAtSource in seen or banner.barcode in seen:
        raise Duplicate

    seen.add(banner.idAtSource)
    seen.add(banner.barcode)
    return OCLCRecord(**banner._asdict())

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file_location', help='Location of the file from Banner')
    args = parser.parse_args()

    today = datetime.datetime.today().strftime('%Y%m%d')
    with open(args.file_location, 'r') as f, open('StudentPatrons_WEX_'+today+'_1.txt', 'w', newline='') as w:
        reader, writer = csv.reader(f, delimiter='\t'), csv.writer(w, delimiter='\t')
        next(reader)  # skip header
        writer.writerow(OCLCRecord._fields)

        for p in reader:
            try:
                patron = banner_to_oclc(p)
            except Duplicate:
                print(p[6])
                continue

            if not date_regex.match(patron.dateOfBirth):
                patron = patron._replace(dateOfBirth='')

            writer.writerow(patron._asdict().values())