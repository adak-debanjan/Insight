#Input file for H1B data
input_file=open('../input/h1b_input.csv',encoding="utf8")

#Input file for the column structure of the H1B data. This file contains only the relevant column names.
structure_file=open('../input/ColumnStructure.txt',encoding="utf8")

#Extract the input ";" separated H1B data and store it in a list
F_List = []
for line in input_file:
    F_List.append(line.split(';'))

#Extract the input ";" separated column structure data and store it in a list
col_List = []
for line in structure_file:
    col_List.append(line.strip().split(';'))

#Get the positions of the relevant column names in the column structure data
col_idx1 = col_List[0].index('col_SOC_CODE')
col_idx2 = col_List[0].index('col_SOC_NAME')
col_idx3 = col_List[0].index('col_WORKSITE_STATE')
col_idx4 = col_List[0].index('col_CASE_STATUS')

#Get the actual column names from the column structure data based on the positions
col_code = col_List[1][col_idx1]
col_name = col_List[1][col_idx2]
col_state = col_List[1][col_idx3]
col_status = col_List[1][col_idx4]

#Get the positions of the relevant column names in the input H1B data
idx1 = F_List[0].index(col_code)
idx2 = F_List[0].index(col_name)
idx3 = F_List[0].index(col_state)
idx4 = F_List[0].index(col_status)

#############################################Counting the top 10 States##################################################

#Get all the states in a list where the applications have been certified      
cert_state = []
for n in range(1,len(F_List)):
    if(F_List[n][idx4].strip().upper()=='CERTIFIED'):
        if(F_List[n][idx3] not in cert_state):
            cert_state.append(F_List[n][idx3])

#Create a dictionary where keys are the states and values are lists containing number of applications and percentage of applications
cert_dict = {item:[0,0] for item in cert_state}
for n in range(1,len(F_List)):
    if(F_List[n][idx3] in cert_state):
        key=F_List[n][idx3]
        cert_dict[key][0] += 1

#Get the total number of certified applications irrespective of the states
app_total = 0
for n in range(1,len(F_List)):
    if(F_List[n][idx4].strip().upper()=='CERTIFIED'):
        app_total += 1

#Update the perecntage of applications for each states in the dictionary
for n in range(1,len(F_List)):
    key=F_List[n][idx3]
    if(key in cert_state):
        cert_dict[key][1] = (cert_dict[key][0])/app_total

#Write the data in output file
cnt = 0
output_file=open('../output/top_10_states.txt','w')
output_file.write('TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')
for key, value in sorted(cert_dict.items(), key=lambda item: (-item[1][0],item[0])):
    output_file.write("%s;%s;%.1f" % (key, value[0], value[1]*100)+'%\n')
    cnt += 1
    if(cnt==10):
        break
output_file.close()

#############################################Counting the top 10 Occupations##################################################

#Get all the SOC Codes and the corresponding names in lists where the applications have been certified         
cert_occp_code = []
cert_occp_name = []
for n in range(1,len(F_List)):
    if(F_List[n][idx4].strip().upper()=='CERTIFIED'):
        if(F_List[n][idx1] not in cert_occp_code):
            cert_occp_code.append(F_List[n][idx1])
            cert_occp_name.append(F_List[n][idx2].replace('"',''))

#Create a dictionary where keys are the SOC codes and values are lists containing SOC names, number of applications and percentage of applications
cert_dict = {item:['',0,0] for item in cert_occp_code}
for n in range(1,len(F_List)):
    if(F_List[n][idx1] in cert_occp_code):
        key=F_List[n][idx1]
        cert_dict[key][1] += 1
        cert_dict[key][0] = F_List[n][idx2]

#Update the perecntage of applications for each SOC code in the dictionary        
for n in range(1,len(F_List)):
    key=F_List[n][idx1]
    if(key in cert_occp_code):
        cert_dict[key][2] = (cert_dict[key][1])/app_total

#Write the data in output file
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
