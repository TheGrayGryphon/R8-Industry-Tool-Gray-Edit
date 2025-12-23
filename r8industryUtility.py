import csv
import os
import sys

from r8lib import IndustryFile, Industry

version = '0.01'
last_update = '22-Oct-2024'
fname = 'config.ind'
carfile = 'r8CarTypes.csv'

INTLEN = 4
BYTLEN = 1
SHTLEN = 2
UTFLEN = 2              # Length of UTF-16 char

if __name__ == "__main__":
    file_read = False
    dir_scanned = False
    file_list = []
    locals = []
    curr_dir = os.getcwd()
    cardict = {}

    with open(carfile, mode='r') as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            cardict[lines[0]] = lines[1]

    print(f'+------------------------------------+\n'
          f'| Run 8 Industry Utility             |\n'
          f'|    Version : {version}   {last_update}    |\n'
          f'|                                    |\n'
          f'|   Enter ? for a list of commands   |\n'
          f'+------------------------------------+\n\n'
          f'Current root directory: {curr_dir}')

    while True:
        try:
            cmd = input(f'\nr8 > ').split()
            if len(cmd) < 1:
                cmd = '?'
            if cmd[0] == '?':
                print('List of commands: ')
                print('c            : compare buffer 2 to buffer 1 locals')
                print('l <fn>       : load industry file <fn>.ind')
                print(' l           : load industry file "config.ind"')
                print('m <c> <n>    : Modify <c> field of record <n>:')
                print('                 (n)ame, (l)ocal name, (s)ymbol')
                print('n            : list names of all industry records')
                print('p <n>        : print contents of record n')
                print(' p           : print contents of all industry records')
                print('pl           : print list of all local tags')
                print('pi           : print list of all industry processed-to tags')
                print('ri           : replace all industry processed-to tag <1> with <2> (leave <2> blank to delete)')
                print('rl           : replace local name <1> with <2>')
                print('q            : quit')
                print('r 1          : report ')
                print('t <n>        : Show all track segments associated with record n')
                print('w <fn>       : Write industry file <fn>.ind')
                print(' w           : Write industry file "config.ind"')

            elif cmd[0] == 'l':
                if len(cmd) > 1:
                    input_fname = cmd[1] + '.ind'
                else:
                    input_fname = fname
                ifp = open(input_fname, mode='rb')
                mem_ptr = 0
                fcontent = ifp.read()
                indFile1 = IndustryFile()
                indFile1.unk1 = fcontent[mem_ptr:mem_ptr + INTLEN]
                mem_ptr += INTLEN
                indFile1.num_rec = int.from_bytes(fcontent[mem_ptr:mem_ptr + INTLEN], 'little')
                mem_ptr += INTLEN
                for i in range(0, indFile1.num_rec):
                    indFile1.industries.append(Industry(fcontent, mem_ptr))
                    mem_ptr += len(indFile1.industries[i])
                print(f'File read: {input_fname}\nRecords Found: {indFile1.num_rec}')
                file_read = True

            elif cmd[0] == 'm':
                if not (len(cmd) > 2):
                    print('ERROR : Missing parameter(s)')
                elif not file_read:
                    print('ERROR : Must read in a file first')
                else:
                    rnum = int(cmd[2])
                    if cmd[1] == 'n':       # Name
                        print(f'Current record[{rnum}] name: {indFile1.industries[rnum].name}')
                        new_name = input('Enter new name > ')
                        if new_name != '':
                            indFile1.industries[rnum].replaceName(new_name)
                    elif cmd[1] == 'l':       # Name
                        print(f'Current record[{rnum}] local name: {indFile1.industries[rnum].local_name}')
                        new_name = input('Enter new local name > ')
                        if new_name != '':
                            indFile1.industries[rnum].replaceLocalName(new_name)
                    elif cmd[1] == 's':       # Name
                        print(f'Current record[{rnum}] track symbol: {indFile1.industries[rnum].trk_sym}')
                        new_name = input('Enter new symbol > ')
                        if new_name != '':
                            indFile1.industries[rnum].replaceSymbol(new_name)
                    else:
                        print('ERROR : Unknown modify command')

            elif cmd[0] == 'n':
                if not file_read:
                    print('ERROR : Must read in a file first')
                else:
                    for c, industry in enumerate(indFile1.industries):
                        print(f' Record[{c}] : {industry.name} -> {industry.local_name}')

            elif cmd[0] == 'p':
                if not file_read:
                    print('ERROR : Must read in a file first')
                else:
                    if len(cmd) == 1:
                        for c, industry in enumerate(indFile1.industries):
                            print(f'--- RECORD[{c}] ---')
                            industry.printAttrs(cardict)
                    else:
                        print(f'--- Record[{int(cmd[1])}] ---')
                        indFile1.industries[int(cmd[1])].printAttrs(cardict)

            elif cmd[0] == 't':
                if not file_read:
                    print('ERROR : Must read in a file first')
                elif len(cmd) < 2:
                    print('ERROR : You must supply an industry record number')
                else:
                    recnum = int(cmd[1])
                    print(f'Track segments ({indFile1.industries[recnum].number_of_tracks}) associated with record '
                          f'{recnum} ({indFile1.industries[recnum].name}):')
                    for i in range(int(indFile1.industries[recnum].number_of_tracks)):
                        print(indFile1.industries[recnum].track[i].track_section)

            elif cmd[0] == 'pl':
                if not file_read:
                    print('ERROR : Must read in a file first')
                else:
                    for c, industry in enumerate(indFile1.industries):
                        if industry.local_name not in locals:
                            locals.append(industry.local_name)
                    for lname in locals:
                        print(lname)

            elif cmd[0] == 'rl':
                if not (len(cmd) > 2):
                    print('ERROR : Missing parameter(s)')
                elif not file_read:
                    print('ERROR : Must read in a file first')
                else:
                    name1 = cmd[1]
                    name2 = cmd[2]
                    # Search through existing local names
                    for c, industry in enumerate(indFile1.industries):
                        if industry.local_name == name1:
                            print(f'Replacing local name {name1} in rec[{c}] (ind: {industry.name}) with {name2}')
                            indFile1.industries[c].replaceLocalName(name2)

            elif cmd[0] == 'q':
                input('Press <enter> to close the session...')
                sys.exit(0)

            elif cmd[0] == 'r':
                if not file_read:
                    print('ERROR : Must read in a file first')
                else:
                    if len(cmd) == 1:
                        for c, industry in enumerate(indFile1.industries):
                            print(f'--- RECORD[{c}] ---')
                            for i in range(industry.number_of_tracks):
                                print(f'Track {i}: {industry.track[i].route_prefix}')
                    else:
                        print(f'--- Record[{int(cmd[1])}] ---')
                        indFile1.industries[int(cmd[1])].printAttrs(cardict)

            elif cmd[0] == 'pi':
                if not file_read:
                    print('ERROR : Must read in a file first')
                else:
                    for industry in indFile1.industries:
                        print(f'{industry.name}: ')
                        for producer in industry.producer:
                            if producer.num_tags > 0:
                                print(f'{producer.returnTags()}')
                        print('----------')

            elif cmd[0] == 'ri':
                if not (len(cmd) > 1):
                    print('ERROR : Missing parameter(s)')
                elif not file_read:
                    print('ERROR : Must read in a file first')
                else:
                    name1 = cmd[1]
                    if len(cmd) >2:
                        name2 = cmd[2]
                    else:
                        name2 = ''
                    for industry in indFile1.industries:
                        for producer in industry.producer:
                            if producer.num_tags > 0:
                                producer.replaceTag(name1, name2)

            elif cmd[0] == 'w':
                if not file_read:
                    print('ERROR : Must read in a file first')
                else:
                    if len(cmd) > 1:
                        output_fname = cmd[1] + '.ind'
                    else:
                        resp = input(f'About to overwrite {input_fname} - ok? (y/n) ')
                        if resp == 'y' or resp == 'Y':
                            output_fname = input_fname
                        else:
                            output_fname = ''
                            print('File not written')
                    if len(output_fname) > 0:
                        print(f'Writing to {output_fname}')
                        ofp = open(output_fname, mode='wb')
                        new_content = indFile1.to_bytes()
                        ofp.write(new_content)
                        ofp.close()

        except Exception as e:
            print(f'Fatal exception [{e}] encountered')
            input('Press <enter> to close this window...')
            sys.exit(-1)