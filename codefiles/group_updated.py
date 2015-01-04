import os.path
import csv

def csv_dict_reader(f_obj):
  #reader = [row for row in csv.reader(f_obj.read().splitlines())]
  reader = csv.DictReader(f_obj, delimiter=',')
  rev = {}
  busi = {}
  name = "../csvfiles/yelp_academic_dataset_business.csv"
  bus_obj = open(name,'rU')
  read = csv.DictReader(bus_obj, delimiter=',')
  for bname in read:
    #if bname["type"] == "restaurant"
    if not bname["business_id"] in busi and len(bname["business_id"])<=23: 
      busi[bname["business_id"]] = bname["name"].replace(" ","")

  for line in reader:
    bid = line["business_id"]
    #print bid
    if len(bid) <= 23:
      if not busi[bid] is None :
        gname = busi[line["business_id"]].replace("/","")
    else: gname = "others"
    if not gname in rev:
      rev[gname] = line["text"]
    else:
      str = rev[gname]
      rev[gname] = "%s %s" %(str,line["text"])
  create_file(rev)

def create_file(review):
  count=0
  for business_id in review.keys():
    if count<=8000:
      filename = "../reviewfiles/"+business_id+".txt"
      file_obj = open(filename,'w+')
      file_obj.write(review[business_id])
      count=count+1
    elif count>8000 and count<9600:
      filename = "../testingfiles/"+business_id+".txt"
      file_obj = open(filename,'w+')
      file_obj.write(review[business_id])
      count=count+1




if __name__ == "__main__":
  filename = "../csvfiles/yelp_academic_dataset_review.csv"
  #filename = os.path.join(os.pardir,"/csvfiles/yelp_academic_dataset_review.csv")
  #print filename
  with open(filename,'rU') as obj:
    csv_dict_reader(obj)
