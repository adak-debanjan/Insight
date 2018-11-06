input_file=open('../input/h1b_input.csv',encoding="utf8")
structure_file=open('../input/ColumnStructure.txt',encoding="utf8")

F_List = []
for line in input_file:
    F_List.append(line.split(';'))

col_List = []
for line in structure_file:
    col_List.append(line.strip().split(';'))

col_idx1 = col_List[0].index('col_SOC_CODE')
col_idx2 = col_List[0].index('col_SOC_NAME')
col_idx3 = col_List[0].index('col_WORKSITE_STATE')
col_idx4 = col_List[0].index('col_CASE_STATUS')

col_code = col_List[1][col_idx1]
col_name = col_List[1][col_idx2]
col_state = col_List[1][col_idx3]
col_status = col_List[1][col_idx4]

idx1 = F_List[0].index(col_code)
idx2 = F_List[0].index(col_name)
idx3 = F_List[0].index(col_state)
idx4 = F_List[0].index(col_status)

##Count of State Start
      
cert_state = []
for n in range(1,len(F_List)):
    if(F_List[n][idx4].strip().upper()=='CERTIFIED'):
        if(F_List[n][idx3] not in cert_state):
            cert_state.append(F_List[n][idx3])

cert_dict = {item:[0,0] for item in cert_state}
for n in range(1,len(F_List)):
    if(F_List[n][idx3] in cert_state):
        key=F_List[n][idx3]
        cert_dict[key][0] += 1

app_total = 0
for n in range(1,len(F_List)):
    if(F_List[n][idx4].strip().upper()=='CERTIFIED'):
        app_total += 1

for n in range(1,len(F_List)):
    key=F_List[n][idx3]
    if(key in cert_state):
        cert_dict[key][1] = (cert_dict[key][0])/app_total

cnt = 0
output_file=open('../output/top_10_states.txt','w')
output_file.write('TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')
for key, value in sorted(cert_dict.items(), key=lambda item: (-item[1][0],item[0])):
    output_file.write("%s;%s;%.1f" % (key, value[0], value[1]*100)+'%\n')
    cnt += 1
    if(cnt==10):
        break
output_file.close()

##Count of Occupation Start
        
cert_occp_code = []
cert_occp_name = []
for n in range(1,len(F_List)):
    if(F_List[n][idx4].strip().upper()=='CERTIFIED'):
        if(F_List[n][idx1] not in cert_occp_code):
            cert_occp_code.append(F_List[n][idx1])
            cert_occp_name.append(F_List[n][idx2].replace('"',''))

cert_dict = {item:['',0,0] for item in cert_occp_code}
for n in range(1,len(F_List)):
    if(F_List[n][idx1] in cert_occp_code):
        key=F_List[n][idx1]
        cert_dict[key][1] += 1
        cert_dict[key][0] = F_List[n][idx2]
        
for n in range(1,len(F_List)):
    key=F_List[n][idx1]
    if(key in cert_occp_code):
        cert_dict[key][2] = (cert_dict[key][1])/app_total

cnt = 0
output_file=open('../output/top_10_occupations.txt','w')
output_file.write('TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')
for key, value in sorted(cert_dict.items(), key=lambda item: (-item[1][1],item[1][0].replace('"',''))):
    output_file.write("%s;%s;%.1f" % (value[0].replace('"',''), value[1], value[2]*100)+'%\n')
    cnt += 1
    if(cnt==10):
        break
output_file.close()
input_file.close()
