# SEC_Financial_Statement_Scraper-V1


The goal of this project is to create a program to pull financial statements from the SEC website. Ideally, most of the process will be automatic. I am completely new to coding and am using this first project as a way to learn. I have no formal education in coding so I appologize in advance if my coding is sloppy and inefficient. Any and all constructive feedback is welcome. All that being said, I am really only doing this for me, I have no intention of anyone else using this script. Feel free to do so but know you do so at your own risk. 


I would also like to point out that some of the code is taken from Coding Fun's blog here: https://codingandfun.com/python-sec-edgar-scraper/. Although when I took it it was unfinished and did have some bugs that I have fixed. But a huge thank you to him since his code makes up the backbone of this project. 


If you do end up downloading the python file just know it is set up to run natively on a linux computer. If you have a windows computer you will have to change the file paths to reflect the change in operating system. This will not be difficult since I already over-engineered the stupid thing unnecessarily. I am not completely sure all that it will entail but I know it will take some configuration on your part to get that to work properly. Good luck with that. Although I am sure you will not need it.


The only thing it can do at the moment is download the Balance Sheet for any publically traded company. 


It does not save it in any format other than a pandas DataFrame object. If you want it in any other format you will have to give it that functionality yourself. Eventually I will try to make it so that it automatically saves it as a libreoffice .odt file and possible an Excel .XLSX file formats. 


When completed, I want this script (I will never make this a program with a nice UI.) to be able to be able to download and format as many financial statements as a person can need without much user manipulation in a foramt that would allow someone like me doing company valuations to creat DCFs and other foreward looking focasts. This is simply an efficiency project and not monetary or portfolio building so dont have high hopes for this. Despite this, if you have any suggestions please leave them here. I would love to see some suggestions that might lead to features that I did not think of. (I am not that creative). 


Thanks and happy coding!
