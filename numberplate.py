 #IVE ASSUMED THIS TO BE A TEST DATA. YOU CAN CHECK BY CHANGING IT
#number_plate=str(number_plate) THIS IS THE ORIGINAL DATA THAT WE WILL GET FROM AWS
"""THE BELOW IS CHECKING LENGTH OF NUMBER PLATE"""

def number_plate_verify(number_plate):
    if(len(number_plate)>10):
        print("Its not a genuine number plate")
    else:
        check=0
        states=["AN","AP","AR","AS","BR","CG","CH","DD","DL","DN","GA","GJ","HR","HP","JH","JK","KA","KL","LD","MH","ML","MN","MP","MZ","NL","OD","PB","PY","RJ","SK","TN","TR","TS","UK","UP","WB"]
        state=number_plate[0:2]
        """CHECKS FOR 1ST 2 ALPHA IF ITS ONE OF THE 28 STATES """
        for i in range(0,36,1):
            if (state==states[i]):
                check=1
                break
        no=number_plate[2:4]
        no_list=["01","02","03","04","05","06","07","08","09"]
        """CHECKS IF 3RD AND 4TH DIGITS ARE NOS FROM 01 TO 99"""
        if (check==1):
            for j in range(0,9,1):
                if (no == no_list[j]):
                    check=2
                elif (int(no) >= 10 and int(no) <=99):
                    check=2
        alpha1=number_plate[4]
        alpha2=number_plate[5]
        """CHECKS IF 5TH AND 6TH CHARACTERS ARE BOTH ALPHABETS"""
        if(check==2):
            if(alpha1.isalpha() and alpha2.isalpha()):
                check=3
        no2=number_plate[5:10]
        """CHECKS IF 7,8,9 AND 10TH CHARACTERS ARE NOS BETWEEN 0001 AND 9999"""
        if(check==3):
            if(int(no)>=0 and int(no)<=9999):
                check=4
        if(check==4):
            print("Its a genuine number plate")
            return 1
        if(check!=4):
            print("Its not a genuine number plate")
            return 0
                
    
