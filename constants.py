# OCLC requires these 46 field names in this order to accept a patron upload
OCLC_FIELDS = ('prefix', 'givenName', 'middleName', 'familyName', 'suffix', 'nickname',
               'canSelfEdit', 'dateOfBirth', 'gender', 'institutionId', 'barcode',
               'idAtSource', 'sourceSystem', 'borrowerCategory', 'circRegistrationDate',
               'oclcExpirationDate', 'homeBranch', 'primaryStreetAddressLine1',
               'primaryStreetAddressLine2', 'primaryCityOrLocality', 'primaryStateOrProvince',
               'primaryPostalCode', 'primaryCountry', 'primaryPhone', 'secondaryStreetAddressLine1',
               'secondaryStreetAddressLine2', 'secondaryCityOrLocality', 'secondaryStateOrProvince',
               'secondaryPostalCode', 'secondaryCountry', 'secondaryPhone', 'emailAddress', 'mobilePhone',
               'notificationEmail', 'notificationTextPhone', 'patronNotes', 'photoURL', 'customdata1',
               'customdata2', 'customdata3', 'customdata4', 'username', 'illId', 'illApprovalStatus',
               'illPatronType', 'illPickupLocation')

# The record output by banner. The only difference is oclcExpirationDate is circExpirationDate in the file.
# OCLC changed this field, so we make the change here until Banner is updated.
BANNER_FIELDS = ('givenName', 'familyName', 'dateOfBirth', 'gender', 'institutionId', 'barcode', 'idAtSource',
                 'sourceSystem', 'borrowerCategory', 'oclcExpirationDate', 'homeBranch', 'primaryStreetAddressLine1',
                 'primaryStreetAddressLine2', 'primaryCityOrLocality', 'primaryStateOrProvince', 'primaryPostalCode',
                 'primaryCountry', 'primaryPhone', 'secondaryStreetAddressLine1', 'secondaryStreetAddressLine2',
                 'secondaryCityOrLocality', 'secondaryStateOrProvince', 'secondaryPostalCode', 'secondaryCountry',
                 'secondaryPhone', 'emailAddress', 'mobilePhone', 'patronNotes')

# These fields contain Personally Identifiable Information that we do not actual need
# So there is no reason to send someone's home address to OCLC, or to store it where
# student workers can look it up, etc.
SCRUB_FIELDS = {'dateOfBirth', 'gender', 'primaryStreetAddressLine1', 'primaryStreetAddressLine2',
                'primaryCityOrLocality', 'primaryStateOrProvince', 'primaryPostalCode', 'primaryCountry',
                'primaryPhone', 'secondaryStreetAddressLine1', 'secondaryStreetAddressLine2',
                'secondaryCityOrLocality', 'secondaryStateOrProvince', 'secondaryPostalCode',
                'secondaryCountry', 'secondaryPhone', 'mobilePhone'}
