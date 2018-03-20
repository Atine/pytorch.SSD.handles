from tqdm import *
import sys
if sys.version_info[0] == 2:
  import xml.etree.cElementTree as ET
else:
  import xml.etree.ElementTree as ET
import glob
import os

def check_xml(target):
  res = []
  for obj in target.iter('object'):
    res += ['annotated']

  if res == []:
    print (target.find('path').text)


rootpath = '/home/mil/chou/STORAGE/dataset/handles'
subsets = ['doors', 'handles', 'knobs']
ids = []

for name in subsets:
  path_name = os.path.join(rootpath,'train','JPEGImages',name)
  for numbers in tqdm(glob.glob(os.path.join(path_name,'*.*'))):
    if os.path.isfile(numbers):
      ids.append((rootpath,name,os.path.basename(os.path.splitext(numbers)[0])))
    else:
      print ("path '%s' is wrong!" % numbers)

annopath = os.path.join('%s','train','Annotations','%s','%s.xml')

for i in range(len(ids)):
  img_id = ids[i]
  target = ET.parse(annopath % img_id).getroot()
  check_xml(target)
