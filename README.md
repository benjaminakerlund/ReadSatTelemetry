# Spacecraft-Engineering-Assignment
Assignment for job application to Spacecraft Engineering Intern July of 2021
I applied for a job titled Spacecraft Engineering Intern, where the assignment was to convert real telemetry data from a real satellite into a more readable form for humans.
The telemetry is recieved in a telemetry.bin file, most of the relevant files should be in the "submission" folder on my computer and the given task reads as follows:

### Task for the Spacecraft Engineering Intern Position
Using Python 3.x, parse all the binary frames in the ‘telemetry.bin’ file attached according to the
structure described in ‘TLM_LIST.csv’.  
Extract time, position and attitude information and export this data to STK format in order to
make the data available to be imported and replayed.  
Deliverables from this practice will be: code + STK files ready to be imported. 

 

Notes: 
- Time information in the binary file is in TAI seconds from January 1st 2000, 00:00:00 
- ECI frame of reference is J2000 
- The size of a data chunk is 2068 bytes 

## ToDo:
* Review assignment, and reupload all necessary stuff
  * The main thing wrong according to what they said in the interview was that I had forgot about the Most Significant Bit - Least Significant Bit principle
  * I think my program might be very fine, 
* What would be interesting to do is also reflect on whether or not this data comes according to the ECSS standard: https://www.esa.int/TEC/Software_engineering_and_standardisation/TECT5CUXBQE_0.html


