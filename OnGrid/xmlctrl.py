# -*- coding: utf-8 -*-  
f = file("on01.txt")
fout = file("EnergyModel.xml",'w')
fout.write('<?xml version="1.0" encoding="UTF-8" ?>\n')
fout.write("<MEMS>\n")
while True:
	line = f.readline()
	if len(line)==0:
		break
	print line,
	#处理空行
	if line=="\n":
		continue
	#处理<DeviceType行
	if line[0:11]=="<DeviceType":
		t1=line.split(":")
		restr="<DeviceType TypeID='%s'>" % t1[1].split(">")[0]
		fout.write(restr+"\n")
		continue
	#处理<DeviceID行
	if line[0:9]=="<DeviceID":
		d1=line.split(":")
		restr="<Device ID='%s'>" % d1[1].split(">")[0]
		fout.write("\t"+restr+"\n")
		continue
	if line[0:10]=="</DeviceID":
		restr="</Device>"
		fout.write("\t"+restr+"\n")
		continue
	#处理DataType行
	if line[0]=="D":
		s1 = line.split("@@")
		s11 = s1[0].split(":")
		s12 = s1[1].split("##")
		s3 = s12[0].split(":")
		MeaType=0
		if s3[1][0:2]=="YC":
			MeaType=1
		if s3[1][0:2]=="YX":
			MeaType=2
		restr="<MeaPoint DataType='%s' MeaType='%s'>%s</MeaPoint>" %(s11[1],MeaType,s3[1])
		fout.write("\t\t"+restr+"\n")
		continue
	fout.write(line)
fout.write("</MEMS>\n")
f.close()
fout.close()