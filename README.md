Problem
-----------------------------------
The purpose of this program is to get get the immigration data trends on H1B(H-1B, H-1B1, E-3) visa application processing over the past years and 
to identify the occupations and states with the most number of approved H1B visas.

This program takes the H1B data as input calculates two metrics: Top 10 Occupations and Top 10 States for certified visa applications.

The program is modular and reusable for future. If the newspaper gets data for the year 2019 (with the assumption that the necessary data to calculate the metrics are available) 
and puts it in the input directory, running the run.sh script should produce the results in the output folder without needing to change the code.


Approach
-----------------------------------
Since each year the input data file can have different columns, we have used file names ColumnStructure.txt which will be placed in the input directory.
This file will contain the column names used to calculate the metrics in ";" separated format. If there is any change in column names in the input data file, user needs to
update this ColumnStructure.txt file. For example, in the 2015 and 2016 col_SOC_CODE and col_SOC_NAME were given by SOC_CODE and SOC_NAME but in year 2014, these two columns were
given by LCA_CASE_SOC_CODE and LCA_CASE_SOC_NAME.

The program will generate two output txt file for two metrics: top_10_occupations.txt and top_10_states.txt. The records in both the files are sorted by NUMBER_CERTIFIED_APPLICATIONS field, 
and in case of a tie, alphabetically by TOP_OCCUPATIONS and TOP_STATES.

Depending on the input, there may be fewer than 10 lines in each file. There, however, should not be more than 10 lines in each file. 
In case of ties, only the top 10 records are listed based on the sorting methods given above.

Percentages are rounded off to 1 decimal place. For instance, 1.05% is rounded to 1.1% and 1.04% is rounded to 1.0%. Also, 1% is represented by 1.0%

Run Instruction
------------------------------------
In Unix system, the user needs to run the run.sh file to run the python source code (h1b_counting.py).
In Windows system, the user needs to run the h1b_counting.py file directly in the src directory.

The program will automatically take the file from input folder generate outputs in the output folder. The input file names should not be changed.
The input files are: h1b_input.csv and ColumnStructure.txt