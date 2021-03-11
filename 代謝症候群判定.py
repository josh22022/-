'''
Case : 代謝症候群判定
ID : 407180221
'''

#要求資料
print("Please input the information below")
question1=("Input 1(Male) or 0(Female): ")
question2=("Waistline (inch) : ")
question3=("Systolic blood pressure : ")
question4=("Diastolic blood pressure : ")
question5=("Are you taking high blood pressure medication ? Input 1(Yes) or 0(No) : ")
question6=("Fasting blood glucose (mg/dL) : ")
question7=("Are you taking diabetes medications ? Input 1(Yes) or 0(No) : ")
question8=("Fasting triglyceride (md/dL) : ")
question9=("Are you taking medication for triglyceride ? Input 1(Yes) or 0(No) : ")
question10=("HDL-C (mg/dL): ")

#輸入變數
sex = eval(input(question1))
waist = eval(input(question2))
systolic = eval(input(question3))
diastolic = eval(input(question4))
highBloodMdc = eval(input(question5))
glucose = eval(input(question6))
diabetesMdc = eval(input(question7))
triglyceride = eval(input(question8))
trigMdc = eval(input(question9))
hdlc = eval(input(question10))

#字串轉換
if sex == 1:
    sexStr = "Male"
if sex == 0:
    sexStr = "Female"
if highBloodMdc == 1:
    highBloodMdcStr = "Yes"
if highBloodMdc == 0:
    highBloodMdcStr = "No"
if diabetesMdc == 1:
    diabetesMdcStr = "Yes"
if diabetesMdc == 0:
    diabetesMdcStr = "No"
if trigMdc == 1:
    trigMdcStr = "Yes"
if trigMdc == 0:
    trigMdcStr = "No"

#使用者確認資料
print("==========\nCheck the data.\nSex :",sexStr,"\nWaistline :",waist,"\nSystolic blood pressure :",systolic,"\nDiastolic blood pressure :",diastolic,"\nTaking high blood medication :",highBloodMdcStr,"\nFasting blood glucose :",glucose,"\nTaking diabetes medications :",diabetesMdcStr,"\nFasting triglyceride : ",triglyceride,"\nTaking medication for triglyceride :",trigMdcStr,"\nHDL-C :",hdlc,"\n==========")
check = eval(input("Input \" 1 \" if Checked : "))

#全域變數
metabolicSyndrome = 0
waistline = 0
error = 0

#確認性別
def sexCheck (sex):
    global error
    if sex == 1 or sex == 0 :
        error += 0
    else:
        print("==========")
        print("Error ! :Sex")
        error += 1
        
#確認用藥
def MdcCheck (highBloodMdc,diabetesMdc,trigMdc):
    global error
    if highBloodMdc == 1 or highBloodMdc == 0 :
        if diabetesMdc == 1 or diabetesMdc == 0 :
            if trigMdc == 1 or trigMdc == 0 :
                error += 0
            else:
                print("==========")
                print("Error ! :Information of medication ")
                error += 1
        else:
            print("==========")
            print("Error ! :Information of medication ")
            error += 1
    else:
        print("==========")
        print("Error ! :Information of medication ")
        error += 1

#單位轉換        
def isCm (waist):
    global waistline , error
    if 10 <= waist <= 50:
        waist *= 2.54
        waistline = int(waist)
    elif waist < 10 :
        print("==========")
        print("Error ! :Waistline ")
        error += 1
    elif waist > 50 :
        print("==========")
        print("Error ! :Waistline ")
        error += 1

#腹部肥胖
def isFat(sex,waistline):
    global metabolicSyndrome
    if sex == 1 and waistline >= 90 :
        metabolicSyndrome += 1
    elif sex == 0 and waist >= 80 :
        metabolicSyndrome += 1

#高血壓        
def isHighPressure(systolic,diastolic,highBloodMdc) :
    global metabolicSyndrome , error
    if systolic <= 50 or systolic >= 300 or diastolic >= 250 or diastolic <= 20 :
        print("==========")
        print("Error ! :Blood Pressure ")
        error += 1
    elif systolic >= 130 or diastolic >= 85 or highBloodMdc == 1 :
        metabolicSyndrome += 1
    

#高血糖        
def isHighGlucose(glucose,diabetesMdc) :
    global metabolicSyndrome , error
    if glucose <= 40 or glucose >= 200 :
        print("==========")
        print("Error ! :Fasting blood glucose ")
        error += 1
    elif glucose >= 100 or diabetesMdc == 1 :
        metabolicSyndrome += 1
    

#三酸甘油脂
def isHighTrig(triglyceride,trigMdc) :
    global metabolicSyndrome , error
    if triglyceride <= 10 or triglyceride >= 300 :
        print("==========")
        print("Error ! :Fasting triglyceride ")
        error += 1
    elif triglyceride >= 150 or trigMdc == 1 :
        metabolicSyndrome += 1

#高密度膽固醇
def isLowHdlc(sex,hdlc) :
    global metabolicSyndrome , error
    if hdlc > 100 or hdlc <= 0:
        print("==========")
        print("Error ! :HDL-C ")
        error += 1
    elif sex == 1 and 0 < hdlc < 40 :
        metabolicSyndrome += 1
    elif sex == 0 and 0 < hdlc < 50 :
        metabolicSyndrome += 1
    
#是否代謝症候群    
def isMS (metabolicSyndrome):
    if metabolicSyndrome >= 3 :
        print("==========")
        print("Result : MetabolicSyndrome")
    elif 0 <= metabolicSyndrome < 3:
        print("==========")
        print("Result : Health")

#錯誤則停        
def isError (error) :
    if error == 0 :
        isMS (metabolicSyndrome)
    elif error >= 1 :
        print("Please restart and check the input value.")

#資料確認
def isCheck(check):
    if check == 1:
        print("==========")
        print("Data checked !")
        sexCheck (sex)
        isCm (waist)
        isFat(sex,waist)
        isHighPressure(systolic,diastolic,highBloodMdc)
        isHighGlucose(glucose,diabetesMdc)
        isHighTrig(triglyceride,trigMdc)
        isLowHdlc(sex,hdlc)
        MdcCheck (highBloodMdc,diabetesMdc,trigMdc)
        isError(error)
    else :
        print("==========\nCheck error !\nPlease restart.\n==========")

#代謝症候群判定
isCheck(check)

'''
預設 :
    腰圍: 10~50 inch
    收縮壓:50~300 mmHg
    舒張壓:20~250 mmHg
    血糖:40~200 mg/dL
    三酸甘油脂：10~300 mg/dL
    高密度膽固醇:0~100 mg/dL
功能：
    使用者確認資料
    數值防呆
    錯誤訊息
'''


        











