import requests
import json
import pandas as pd
import sys
import time
import random

# if len(sys.argv) > 1:
#     try:
#         year = sys.argv[1]
#         start = int(sys.argv[2])
#         end = int(sys.argv[3])

#     except IndexError:
#         print("Please enter the year for which you would like to receive data," 
#                 "and a range therange of sequences you would like to process (a starting number and a finishing number")
#         exit()
# else:
#     print("Please enter the year for which you would like to receive data,"
#             "and a range therange of sequences you would like to process (a starting number and a finishing number")
#     exit()


year = 2019 
start = 0
end = 1
wprdc_zip_codes = ['8600000US15001', '8600000US15003', '8600000US15004', '8600000US15005', '8600000US15006', '8600000US15007', '8600000US15009', '8600000US15010', '8600000US15012', '8600000US15014', '8600000US15015', '8600000US15017', '8600000US15018', '8600000US15019', '8600000US15020', '8600000US15022', '8600000US15024', '8600000US15025', '8600000US15026', '8600000US15027', '8600000US15028', '8600000US15030', '8600000US15031', '8600000US15033', '8600000US15034', '8600000US15035', '8600000US15037', '8600000US15038', '8600000US15042', '8600000US15044', '8600000US15045', '8600000US15046', '8600000US15047', '8600000US15049', '8600000US15050', '8600000US15051', '8600000US15052', '8600000US15053', '8600000US15054', '8600000US15055', '8600000US15056', '8600000US15057', '8600000US15060', '8600000US15061', '8600000US15062', '8600000US15063', '8600000US15064', '8600000US15065', '8600000US15066', '8600000US15067', '8600000US15068', '8600000US15071', '8600000US15072', '8600000US15074', '8600000US15075', '8600000US15076', '8600000US15077', '8600000US15078', '8600000US15081', '8600000US15082', '8600000US15083', '8600000US15084', '8600000US15085', '8600000US15086', '8600000US15087', '8600000US15088', '8600000US15089', '8600000US15090', '8600000US15101', '8600000US15102', '8600000US15104', '8600000US15106', '8600000US15108', '8600000US15110', '8600000US15112', '8600000US15116', '8600000US15120', '8600000US15122', '8600000US15126', '8600000US15129', '8600000US15131', '8600000US15132', '8600000US15133', '8600000US15135', '8600000US15136', '8600000US15137', '8600000US15139', '8600000US15140', '8600000US15142', '8600000US15143', '8600000US15144', '8600000US15145', '8600000US15146', '8600000US15147', '8600000US15148', '8600000US15201', '8600000US15202', '8600000US15203', '8600000US15204', '8600000US15205', '8600000US15206', '8600000US15207', '8600000US15208', '8600000US15209', '8600000US15210', '8600000US15211', '8600000US15212', '8600000US15213', '8600000US15214', '8600000US15215', '8600000US15216', '8600000US15217', '8600000US15218', '8600000US15219', '8600000US15220', '8600000US15221', '8600000US15222', '8600000US15223', '8600000US15224', '8600000US15225', '8600000US15226', '8600000US15227', '8600000US15228', '8600000US15229', '8600000US15232', '8600000US15233', '8600000US15234', '8600000US15235', '8600000US15236', '8600000US15237', '8600000US15238', '8600000US15239', '8600000US15241', '8600000US15243', '8600000US15260', '8600000US15290', '8600000US15301', '8600000US15311', '8600000US15313', '8600000US15314', '8600000US15315', '8600000US15316', '8600000US15317', '8600000US15320', '8600000US15321', '8600000US15322', '8600000US15323', '8600000US15324', '8600000US15325', '8600000US15327', '8600000US15329', '8600000US15330', '8600000US15331', '8600000US15332', '8600000US15333', '8600000US15334', '8600000US15337', '8600000US15338', '8600000US15340', '8600000US15341', '8600000US15342', '8600000US15344', '8600000US15345', '8600000US15346', '8600000US15347', '8600000US15348', '8600000US15350', '8600000US15351', '8600000US15353', '8600000US15357', '8600000US15358', '8600000US15359', '8600000US15360', '8600000US15361', '8600000US15363', '8600000US15364', '8600000US15366', '8600000US15367', '8600000US15368', '8600000US15370', '8600000US15377', '8600000US15378', '8600000US15379', '8600000US15380', '8600000US15401', '8600000US15410', '8600000US15412', '8600000US15413', '8600000US15417', '8600000US15419', '8600000US15420', '8600000US15421', '8600000US15422', '8600000US15423', '8600000US15425', '8600000US15427', '8600000US15428', '8600000US15429', '8600000US15430', '8600000US15431', '8600000US15432', '8600000US15433', '8600000US15434', '8600000US15435', '8600000US15436', '8600000US15438', '8600000US15442', '8600000US15443', '8600000US15444', '8600000US15445', '8600000US15446', '8600000US15447', '8600000US15448', '8600000US15449', '8600000US15450', '8600000US15454', '8600000US15455', '8600000US15456', '8600000US15458', '8600000US15460', '8600000US15461', '8600000US15462', '8600000US15463', '8600000US15466', '8600000US15467', '8600000US15468', '8600000US15470', '8600000US15472', '8600000US15473', '8600000US15474', '8600000US15475', '8600000US15476', '8600000US15477', '8600000US15479', '8600000US15480', '8600000US15482', '8600000US15483', '8600000US15484', '8600000US15486', '8600000US15489', '8600000US15490', '8600000US15492', '8600000US15601', '8600000US15610', '8600000US15611', '8600000US15612', '8600000US15613', '8600000US15615', '8600000US15616', '8600000US15617', '8600000US15618', '8600000US15620', '8600000US15621', '8600000US15623', '8600000US15624', '8600000US15625', '8600000US15626', '8600000US15627', '8600000US15628', '8600000US15629', '8600000US15631', '8600000US15632', '8600000US15633', '8600000US15634', '8600000US15635', '8600000US15636', '8600000US15637', '8600000US15638', '8600000US15639', '8600000US15640', '8600000US15641', '8600000US15642', '8600000US15644', '8600000US15646', '8600000US15647', '8600000US15650', '8600000US15656', '8600000US15660', '8600000US15661', '8600000US15662', '8600000US15663', '8600000US15665', '8600000US15666', '8600000US15668', '8600000US15670', '8600000US15671', '8600000US15672', '8600000US15673', '8600000US15675', '8600000US15676', '8600000US15678', '8600000US15679', '8600000US15680', '8600000US15681', '8600000US15683', '8600000US15684', '8600000US15686', '8600000US15688', '8600000US15689', '8600000US15690', '8600000US15691', '8600000US15692', '8600000US15693', '8600000US15695', '8600000US15696', '8600000US15697', '8600000US15698', '8600000US15701', '8600000US15710', '8600000US15712', '8600000US15713', '8600000US15716', '8600000US15717', '8600000US15723', '8600000US15725', '8600000US15727', '8600000US15728', '8600000US15729', '8600000US15731', '8600000US15732', '8600000US15734', '8600000US15736', '8600000US15739', '8600000US15741', '8600000US15745', '8600000US15746', '8600000US15747', '8600000US15750', '8600000US15752', '8600000US15754', '8600000US15756', '8600000US15759', '8600000US15761', '8600000US15765', '8600000US15771', '8600000US15774', '8600000US15777', '8600000US15779', '8600000US15783', '8600000US15920', '8600000US15923', '8600000US15929', '8600000US15949', '8600000US16001', '8600000US16002', '8600000US16022', '8600000US16023', '8600000US16024', '8600000US16025', '8600000US16027', '8600000US16029', '8600000US16030', '8600000US16033', '8600000US16034', '8600000US16035', '8600000US16037', '8600000US16040', '8600000US16045', '8600000US16046', '8600000US16048', '8600000US16050', '8600000US16051', '8600000US16052', '8600000US16053', '8600000US16055', '8600000US16056', '8600000US16059', '8600000US16061', '8600000US16063', '8600000US16066', '8600000US16101', '8600000US16102', '8600000US16105', '8600000US16117', '8600000US16123', '8600000US16132', '8600000US16136', '8600000US16140', '8600000US16141', '8600000US16157', '8600000US16160', '8600000US16201', '8600000US16210', '8600000US16211', '8600000US16212', '8600000US16226', '8600000US16228', '8600000US16229', '8600000US16236', '8600000US16238', '8600000US16244', '8600000US16246', '8600000US16249', '8600000US16250', '8600000US16253', '8600000US16262', '8600000US16263']
city_of_pgh_codes = ['8600000US15120', '8600000US15106', '8600000US15201', '8600000US15203', '8600000US15204', '8600000US15205',  '8600000US15206', '8600000US15207', '8600000US15208', '8600000US15210', '8600000US15211', '8600000US15212', '8600000US15213', '8600000US15214', '8600000US15215', '8600000US15216', '8600000US15217', '8600000US15218', '8600000US15219', '8600000US15220', '8600000US15221', '8600000US15222', '8600000US15224', '8600000US15226', '8600000US15227', '8600000US15230', '8600000US15232', '8600000US15233', '8600000US15234', '8600000US15235', '8600000US15240', '8600000US15260', '8600000US15290']
annotated_values = ['-666666666', '-999999999', '-888888888', '-222222222', '-333333333', '-555555555', '*']

zcta_labels = []
response_zcta = requests.get(f'https://api.census.gov/data/{year}/acs/acs5/variables.json')
zcta_labels.append(json.loads(response_zcta.content))

set_of_zcta_seqs = set()
full_label = set()
for item in zcta_labels[0]['variables']:
    if(item[0])=='B':
        if 'B02001' in item:
            full_label.add(item)
            cat_label = item.split('_')
            set_of_zcta_seqs.add(cat_label[0])
            
        else:
            pass
        
list_of_zcta_seqs = list(set_of_zcta_seqs)
list_of_zcta_seqs.sort()

full_header_list = {}
for item in full_label:
    full_header_list[item] = zcta_labels[0]['variables'][item]['concept']+': '+zcta_labels[0]['variables'][item]['label']

print(list_of_zcta_seqs)

zcta = []
zcta_reduced = []
zcta_header_list = []
starting_rest = 0.5
one_shot = []
estimate_column_list = []
margin_column_list = []
for x in range(start, end):
    one_shot = []
    column_list = []

    moe_column_list = []
    print(x)
    zcta_staging_list = []
    response = requests.get(f'https://api.census.gov/data/2020/acs/acs5?key=93f87a458e810a7cb0bd7a44edca904e6ba62ddb&get=NAME,group({list_of_zcta_seqs[x]})&for=zip%20code%20tabulation%20area:*')
#if this is shared widely, edit so that the api key isn't included!!
    print(response.content[:20])
    print(type(response.content))
    content = json.loads(response.content)
    content[0].insert(0, 'ID')
    zcta_header_list.append(content[0])
    for item in content[0]:
        if item in full_header_list:
            column_list.append(f'{item}: {full_header_list[item]}')
        elif item[-1]=='M':
            fill_in = item[:-1]+'E'
            column_list.append(f'{item}: {full_header_list[fill_in]}')
        else:
            column_list.append(item)
#    for item in content[0]:
#         if item.isalpha():
#             estimate_column_list.append(item)
#             margin_column_list.append(item)
#         if "_001EA" in item:
#             pass
#         elif "_001MA" in item:
#             pass
#         elif "_001E" in item:
#             estimate_column_list.append(f'{item}: {full_header_list[item]}')
#         elif "_001M" in item:
#             temp_file_name = item[:-1]+'E'
#             moe_column_list.append(f'{item}: Margin of Error for {full_header_list[temp_file_name]}')
#         else:
#             pass
    for y in range(1, len(content)):
        if content[y][-3] in city_of_pgh_codes:
            content[y].insert(0, list_of_zcta_seqs[x])
            zcta.append(content[y])
            zcta_reduced.append([content[y][1], content[y][2]])
            one_shot.append(content[y])
            file_name = f'{list_of_zcta_seqs[x]}_table.csv'
#             one_shot_df = pd.DataFrame(one_shot)
#             one_shot_df.columns = column_list
#             one_shot_df.to_csv(file_name)

zcta_df = pd.DataFrame(zcta)
# zcta_reduced_df = zcta_df.iloc[:, 0:2]
# zcta_reduced_df.columns = column_list
# zcta_reduced_df.to_csv("19test.csv")
zcta_df.columns = column_list
zcta_df.to_csv("B02001test.csv")

latest_list = []
for x in range(len(zcta)):
    for z in range(len(zcta_header_list)):
        if zcta[x][0] == zcta_header_list[z][2][:len(zcta[x][0])]:
            zcta_row_len = len(zcta_header_list[z])-4
            table_id = zcta_header_list[z]
    for y in range(2, zcta_row_len)[::4]:
        try:
            if zcta[x][y] in annotated_values and zcta[x][y+2] in annotated_values:
                staging_list = [zcta[x][zcta_row_len+1], None, zcta[x][y], None, 
                                zcta[x][y+2], 'acs', int(year), table_id[y][:-1]]
            elif zcta[x][y] in annotated_values:
                staging_list = [zcta[x][zcta_row_len+1], None, zcta[x][y], int(zcta[x][y+2]), 
                                zcta[x][y+2], 'acs', int(year), table_id[y][:-1]]
            elif zcta[x][y+2] in annotated_values:
                staging_list = [zcta[x][zcta_row_len+1], int(zcta[x][y]), zcta[x][y], None, 
                                zcta[x][y+2], 'acs', int(year), table_id[y][:-1]]
            else:
                staging_list = [zcta[x][zcta_row_len+1], int(zcta[x][y]), zcta[x][y], int(zcta[x][y+2]), 
                                zcta[x][y+2], 'acs', int(year), table_id[y][:-1]]
        except (TypeError, ValueError) as e:
            staging_list = [zcta[x][zcta_row_len+1], (zcta[x][y]), "nan", (zcta[x][y+2]), 
                            "nan", 'acs', int(year), table_id[y][:-1]]
        except IndexError: 
            pass
        latest_list.append(staging_list)

file_name_start = list_of_zcta_seqs[start]
file_name_end = list_of_zcta_seqs[int(end)-1]

columns_list = ["geoid", "estimate", "raw_estimate", "margin_of_error", "raw_margin_of_error", "survey", "year", "table_id"]
output_file_name = f'census_data_by_zipcodes_from_{file_name_start}_to_{file_name_end}.csv.gz'
latest_df = pd.DataFrame(latest_list)
latest_df.columns = columns_list
latest_df.to_csv(output_file_name, compression='gzip')