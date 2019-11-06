# -*- coding: utf-8 -*-
# @Author: SyedAli
# @Date:   2019-02-01 02:55:42
# @Last Modified by:   SyedAli
# @Last Modified time: 2019-02-04 07:19:18


s = """cified period of timed under specified operating conditions [5]. The software reliability is used as one of the metri
c to control the testing phase of software development life cycle [6]. Nowadays from an average to large sized hospitals, the different types of medical devices range from 5,000 to more than 10,000. A product that is used to diagnose, treat, or monitor a m
edical condition is called a medical device [7]. ISO defines Medical d
e- safety critica
l system in particular, since a small failure can result in significant loss to human life. Most of the medical devices are software driven (i.e. Software is used to drive the hardware to perform the required and intended function). In other words, we can say most of the medical devices are embedded systems. The software which is used to for t- the Medical software used in Medical devices for easy understanding. Software driven me
d-
ical devices resulted in over 1818 recalls affecting 15,27,345 devices from the year 2010 to 2012. Nearly 25% of all recalls are attributable to software failures [10]
. For an a
d-
verse event free operation of a medical device, the medical embedded software must be designed such that, it must be robust to software faults due to pure software error, and also due to the interaction with other factors like hardware and human beings (user). Maximum reliability of Medical embedded software must be ascertained before deplo
y-
ment. Roughly around 200 models were developed for software reliability prediction and estimation. A few models have proved their efficiency and accuracy in reliability estim
a-
tion and prediction [10]. For embedded software, some researchers developed model considering the effects of software and hardware. Human beings also have an impact on the embedded systems. The effect of human error could also be consider
ed. As the co
m-
plexity of the Medical Embedded systems (medical devices) grew, they become incre
a-
singly dependent on the Human factors. As per FDA (Food and Drug Administration, USA) Report 2016, the human error is considered as the main cause of catastroph
ic events and accidents and should not be neglected in decision making [11]. The medical device is used either by the patient or by the medical practitioners (operators) in the ho
s-
pitals. Since humans directly involved in the use of medical devices, the p
robability of interaction with the devices (both hardware and software) is more. An incorrect data i
n-
put into the system will result in software failures in medical devices. Attempting to use 3 medical device by an unskilled user or operator often result in error that could cause fai
l-
ures, which in turn could lead to severe injury to patients, and at some circumstances result in loss of human lives and property. In this paper, the authors propose a reliability model for medical embedded software considering the effects of pure software error, hardware error, and human error induced software failures. Appropriate models are adopted for the pure software, hardware and user induced failures. The failure rate function, mean value function, and reliability fun
c-
tio
n are given. Finally, the model is validated for accuracy. A case study is presented for the applicability model in real time environment. 2. RELIABILITY MODEL FOR MEDICAL EMBEDDED SOFT
WARE To develop the model, the failure rate function was developed at firs
t. Then the mean value function is derived from the failure rate function. The reliability function is developed from the mean value function. The following section discusses the assumptions of the proposed model. 2.1 Assumptions of the proposed model 1. In Medi
cal embedded software, the following are the three types of failures: i. Pure software failures ii. Hardware induced software failures iii. User induced software failures 2. The Goel
-
Okumoto Non
 """
import re

words = s.split(" ")

start = 0
end = 500
while(start<len(words)):
	print(start,end)
	print(" ".join(words[start:end]))
	start += 500;
	end += 500

count = len(re.findall(r'\w+', s))
print(count,len(words))
