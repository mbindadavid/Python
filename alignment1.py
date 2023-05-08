#Function 

def machinga(id):
    #our assumption is we have whole printing job table
    pj = [
            {
                'status': -1,
                'job_id': '1234_8900',
            },
            {
                'status': -1,
                'job_id': '1234_1100',
            },
            {
                'status': 0,
                'job_id': '00234_1100',
            },
        ] 
    for i in range(0, len(pj)):
       print(pj[i]["job_id"]);
       if id == pj[i]['job_id']:
            pj[i]['status'] = 0;
            print(pj[i])                   

machinga('1234_1100')