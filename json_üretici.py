import os
def json_türet(kalın_metinler,pdf_path):
    try:
        os.mkdir(pdf_path[:-4])
    except:
        for filename in os.listdir(pdf_path[:-4]):
            file_path = os.path.join(pdf_path[:-4], filename)
            os.remove(file_path)
    os.chdir(pdf_path[:-4])
    for girdi in kalın_metinler:
            #print(girdi["line"])
            with open(pdf_path[:-4]+f"{girdi["line"]}.json","a") as f:
                f.write("{\n")
                f.write(f" \"title\": \"{girdi["başlık"]}\",\n \"parent_title\":\"{girdi["üstbaşlık"]}\",\n \"page\": {girdi['page']},\n \"summary\": \"{girdi['summary']}\"")
                #print(girdi["öncülbaşlık"])
                if girdi["öncülbaşlık"]:
                    f.write(",")
                    f.write(f"\n \"owner_title\": \"{girdi["öncülbaşlık"]}\"")
                f.write("\n}")
