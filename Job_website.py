from bs4 import BeautifulSoup
import requests
import time

#print("Enter the skills you are familiar with")
familiar_skills="artificialintelligence"
def find_jobs():
    text=requests.get('https://www.timesjobs.com/candidate/parametricSearchResult.html?from=parametricSearch&mCompId=27496').text   #html text prints
    #print(text)
    soup=BeautifulSoup(text,"lxml")
    jobs=soup.find_all("li",class_="clearfix job-bx wht-shd-bx")
    for index,job in enumerate(jobs):
        date=job.find('span',class_="sim-posted").text
        if 'today' in date:
            job_titles=job.find("header",class_="clearfix")
            job_title=job_titles.h2.text.replace(' ','')
            skills=soup.find('span',class_="srp-skills").text.replace(' ','')
            Info=job.header.h2.a['href']
            if familiar_skills in skills:
                with open(f'Job_posts/{index}.txt','w') as f:
                    f.write(f"JOB TITLE      :\t {job_title.strip()}\n")
                    f.write(f"Skills Required:\t{skills.strip()}\n")
                    f.write(f"Date Posted    :\t{date.strip()}\n")
                    f.write(f"For More Info  :\t{Info.strip()}\n")
                    f.write("\n")
                print(f'file saves:{index}')

if __name__=='__main__':
    while True:
        find_jobs()
        time_wait=10
        print(f"Waiting {time_wait} seconds")
        time.sleep(time_wait)


