
import psutil
import requests
import json
import time
import socket 

def create_doc(uri, doc_data={}):
    """Create new document."""
    query = json.dumps(doc_data)
    response = requests.post(uri, data=query)
    print(response)

uri_create = 'http://192.168.3.152:9200/experimentation/montring/'



i=0

while(1==1):
	node=socket.gethostname()
	date=time.strftime("%d/%m/%Y")
	time1=time.strftime("%H:%M:%S")
	cpu=psutil.cpu_percent(interval=1)
	ram=psutil.virtual_memory().used/(1024*1024)

	disc_r=psutil.disk_io_counters().read_bytes/(1024*1024)
	disc_w=psutil.disk_io_counters().write_bytes/(1024*1024)

	disc_p_r= psutil.net_io_counters().packets_sent
	disc_p_w= psutil.net_io_counters().packets_recv

	bw_o=psutil.net_io_counters().bytes_sent/(1024*1024)
	bw_i=psutil.net_io_counters().bytes_recv/(1024*1024)
	time.sleep(1)
	i=i+1
	print "%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s" % (i,date, time1,cpu,ram,disc_r,disc_w,disc_p_r,disc_p_w,bw_i,bw_o)
	




