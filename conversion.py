import argparse
import datetime

import students
import fac_staff

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file_location', help='Location of the file from Banner')
    parser.add_argument('fac_staff_or_students',
                        help='Whether we are working with faculty/staff or student files',
                        choices=['faculty', 'students'])
    args = parser.parse_args()

    today = datetime.datetime.today()
    if args.fac_staff_or_students == 'students':
        students.main(args.file_location, today)
    else:
        fac_staff.main(args.file_location, today)
